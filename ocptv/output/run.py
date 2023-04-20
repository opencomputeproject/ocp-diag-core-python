"""
This module describes the high level test run and related objects.
"""
import sys
import threading
import typing as ty
from contextlib import contextmanager

from ocptv.api import export_api

from .config import get_config
from .dut import Dut, SoftwareInfo
from .emit import ArtifactEmitter
from .objects import (
    Error,
    Log,
    LogSeverity,
    RunArtifact,
    RunEnd,
    RunStart,
    TestResult,
    TestStatus,
)
from .source import SourceLocation, get_caller_source
from .step import TestStep


@export_api
class TestRunError(RuntimeError):
    """
    The ``TestRunError`` can be raised with a context scope started by ``TestRun.scope()``.
    Any instance will be caught and handled by the context and will result in ending the
    whole run with an error outcome.
    """

    __slots__ = ("status", "result")

    # this may be further restricted re. params
    def __init__(self, *, status: TestStatus, result: TestResult):
        """
        :param status: outcome status for the diagnostic package as a whole.
        :param result: determine whether the validation passed for this test run.
        """
        self.status = status
        self.result = result


@export_api
class TestRun:
    """
    The ``TestRun`` object is a stateful interface for the diagnostic run.
    It presents various methods to interact with the run itself or to make child artifacts.

    Usage:

    .. code-block:: python

        import ocptv.output as tv
        run = tv.TestRun(name="test", version="1.0")
        with run.scope(dut=ocptv.Dut(id="dut0")):
            pass

    For other usages, see the the ``examples`` folder in the root of the project.

    All the methods in this class are threadsafe.

    Specification reference:
    - https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#test-run-artifacts
    """

    def __init__(
        self,
        name: str,
        version: str,
        *,
        command_line: ty.Optional[str] = None,
        parameters: ty.Optional[ty.Dict[str, ty.Union[str, int]]] = None,
    ):
        """
        Make a new stateful test run model object.

        :param name: name of this test run/diagnostic package.
        :param version: version string for the test run/diagnostic package.
        :param command_line: process command line that the diagnostic was started with.
        :param parameters: a flat dictionary of unspecified input parameters
            used in the diagnostic package.

        Parameters that have a discovery process are left to be specified in
        the ``start()`` or ``scope()`` calls.

        For additional details on parameters, see:
        - https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#testrunstart
        """
        self._name = name
        self._version = version

        if command_line is not None:
            self._cmdline = command_line
        else:
            self._cmdline = self._get_cmdline()

        self._params = parameters or {}

        # once a test run has started, all semantically descendant artifacts
        # must use the same emitter without interruption
        self._emitter = ArtifactEmitter(writer=get_config().writer)

        self._step_lock = threading.Lock()
        self._step_id: int = 0

    def start(self, *, dut: Dut):
        """
        Emit the test run start artifact.

        :param dut: device-under-test information. The DUT info is considered to have
            finished discovery at the point of starting a test run.

        For additional details on parameters, see:
        - https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#testrunstart
        """
        start = RunStart(
            name=self.name,
            version=self._version,
            command_line=self.command_line,
            parameters=self._params,
            dut_info=dut.to_spec(),
        )
        self._emitter.emit(RunArtifact(impl=start))

    def end(self, *, status: TestStatus, result: TestResult):
        """
        Emit the test run end artifact.

        :param status: outcome status for the diagnostic package as a whole.
        :param result: determine whether the validation passed for this test run.

        For additional details on parameters, see:
        - https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#testrunend
        """
        end = RunEnd(
            status=status,
            result=result,
        )
        self._emitter.emit(RunArtifact(impl=end))

    @contextmanager
    def scope(self, *, dut: Dut):
        """
        Start a scoped test run.
        Emits the test run start artifact and, at the end of the scope, emits the run end artifact.

        The scope can also be exited sooner by raising the ``TestRunError`` error type.
        If no such exception was raised, the test run will end with status COMPLETE and result PASS.
        Any other exceptions are not handled and will pass through.

        Usage:

        .. code-block:: python

            import ocptv.output as tv
            run = tv.TestRun(...)
            with run.scope(dut=dut):
                pass

            run = tv.TestRun(...)
            with run.scope(dut=dut):
                raise TestRunError(status=TestStatus.SKIP, result=TestResult.NOT_APPLICABLE)

        :param dut: device-under-test information. See ``start`` method.
        """
        try:
            yield self.start(dut=dut)
        except TestRunError as re:
            self.end(status=re.status, result=re.result)
        else:
            self.end(status=TestStatus.COMPLETE, result=TestResult.PASS)

    def add_step(self, name: str) -> TestStep:
        """
        Create a new test step for this test run.
        The step is not started immediately, and should be used with the ``start()`` or ``scope()`` methods.

        :param name: name of the step to create
        :returns: reference to a model of the test step

        For additional details on parameters and step start, see:
        - https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#teststepstart
        """

        with self._step_lock:
            step_id = self._step_id
            self._step_id += 1

        step = TestStep(name, step_id=step_id, emitter=self._emitter)
        return step

    def add_log(
        self,
        severity: LogSeverity,
        message: str,
        source_location: ty.Optional[SourceLocation] = SourceLocation.CALLER,
    ):
        """
        Emit a log entry artifact relevant for this test run.

        :param severity: level of this log entry.
            See: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#severity
        :param message: free-form message for this log entry.
        :param source_location: source coordinates inside the diagnostic package
            where this artifact was produced. Default value ``SourceLocation.CALLER`` means that this
            function will automatically populate the spec field based on the caller frame.

        For additional details on parameters, see:
        - https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#log
        """

        if source_location is SourceLocation.CALLER:
            source_location = get_caller_source()

        log = Log(
            severity=severity,
            message=message,
            source_location=source_location.to_spec() if source_location else None,
        )
        self._emitter.emit(RunArtifact(impl=log))

    def add_error(
        self,
        *,
        symptom: str,
        message: ty.Optional[str] = None,
        software_infos: ty.Optional[ty.List[SoftwareInfo]] = None,
        source_location: ty.Optional[SourceLocation] = SourceLocation.CALLER,
    ):
        """
        Emit an error artifact relevant for this test run.

        :param symptom: free-form description of the error symptom.
        :param message: free-form message associated with this error.
        :param software_infos: a list of `SoftwareInfo` references (as created
            in the DUT discovery process), that are relevant for this error. This can be used to specify
            a causal relationship between a software component and this error.
        :param source_location: source coordinates inside the diagnostic package
            where this artifact was produced. Default value ``SourceLocation.CALLER`` means that this
            function will automatically populate the spec field based on the caller frame.

        For additional details on parameters, see:
        - https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#error
        """

        if software_infos is None:
            software_infos = []

        if source_location is SourceLocation.CALLER:
            source_location = get_caller_source()

        error = Error(
            symptom=symptom,
            message=message,
            software_infos=[o.to_spec() for o in software_infos],
            source_location=source_location.to_spec() if source_location else None,
        )
        self._emitter.emit(RunArtifact(impl=error))

    def _get_cmdline(self):
        return " ".join(sys.argv[1:])

    @property
    def name(self) -> str:
        return self._name

    @property
    def version(self) -> str:
        return self._version

    @property
    def command_line(self) -> str:
        return self._cmdline

    @property
    def parameters(self) -> ty.Optional[ty.Dict[str, ty.Union[str, int]]]:
        return self._params
