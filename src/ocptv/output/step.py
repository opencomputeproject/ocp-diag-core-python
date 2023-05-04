"""
This module describes the test steps inside the test run.
"""
import threading
import typing as ty
from contextlib import contextmanager

from ocptv.api import export_api

from .dut import HardwareInfo, SoftwareInfo, Subcomponent
from .emit import ArtifactEmitter
from .measurement import MeasurementSeries, MeasurementSeriesEmitter, Validator
from .objects import (
    Diagnosis,
    DiagnosisType,
    Error,
    Extension,
    ExtensionContentType,
    File,
    Log,
    LogSeverity,
    Measurement,
    MeasurementValueType,
    Metadata,
    StepArtifact,
    StepEnd,
    StepStart,
    TestStatus,
)
from .source import SourceLocation, get_caller_source


@export_api
class TestStepError(RuntimeError):
    """
    The ``TestStepError`` can be raised within a context scope started by ``TestStep.scope()``.
    Any instance will be caught and handled by the context and will result in ending the
    step with an error.
    """

    __slots__ = "status"

    def __init__(self, *, status: TestStatus):
        """
        :param status: outcome status for this step.
        """
        self.status = status


class TestStep:
    """
    The ``TestStep`` instances are the stateful interface to diagnostic steps inside a run.
    They present methods to interact with the steps themselves or to make child artifacts.

    Should not be used directly by user code, but created through ``TestRun.add_step()``.

    Usage:

    .. code-block:: python

        step0 = run.add_step("step0") # run: TestRun
        with step0.scope():
            pass

    For other usages, see the the ``examples`` folder in the root of the project.

    All the methods in this class are threadsafe.

    Specification reference:
    - https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#test-step-artifacts
    """

    def __init__(self, name: str, *, step_id: int, emitter: ArtifactEmitter):
        self._name = name
        self._id = step_id
        self._idstr = "{}".format(step_id)
        self._emitter = emitter

        # TODO: do we want manually controlled values for the series id?
        self._series_lock = threading.Lock()
        self._measurement_series_id: int = 0

    def start(self):
        """
        Emit a test step start artifact.

        Specification reference:
        - https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#teststepstart
        """

        start = StepStart(name=self._name)
        self._emitter.emit(StepArtifact(id=self._idstr, impl=start))

    def end(self, *, status: TestStatus):
        """
        Emit a test step end artifact.

        :param status: outcome status for this step.

        For additional details on parameters, see:
        - https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#teststepend
        """

        end = StepEnd(status=status)
        self._emitter.emit(StepArtifact(id=self._idstr, impl=end))

    @contextmanager
    def scope(self):
        """
        Start a scoped test step.
        Emits the test step start artifact and, at the end of the scope, emits the step end artifact.

        The scope can also be exited sooner by raising the ``TestStepError`` error type.
        If no such exception was raised, the test step will end with status COMPLETE.
        Any other exceptions are not handled and will pass through.

        Usage:

        .. code-block:: python

            step0 = run.add_step(name="step0")
            with step0.scope():
                pass

            step0 = run.add_step(name="step0")
            with step0.scope():
                raise TestStepError(status=TestStatus.SKIP)
        """

        try:
            yield self.start()
        except TestStepError as e:
            self.end(status=e.status)
        else:
            self.end(status=TestStatus.COMPLETE)

    def add_measurement(
        self,
        *,
        name: str,
        value: MeasurementValueType,
        unit: ty.Optional[str] = None,
        validators: ty.Optional[ty.List[Validator]] = None,
        hardware_info: ty.Optional[HardwareInfo] = None,
        subcomponent: ty.Optional[Subcomponent] = None,
        metadata: ty.Optional[Metadata] = None,
    ):
        """
        Emit a single measurement artifact as taken by the test step.

        :param name: identification for this measurement item.
        :param value: value of the taken measurement.
        :param unit: free-form unit specification for this measurement.
        :param validator: specifies how this measurement was validated in the
            test step by the diagnostic package.
        :param hardware_info: reference to the hardware component that this
            measurement was taken from or is relative to.
        :param subcomponent: reference to the hardware subcomponent (lower than FRU
            level) that this measurement was taken from or is relative to.
        :param metadata: dictionary with unspecified metadata for this measurement item.

        For additional details on parameters, see:
        - https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#measurement
        """

        if validators is None:
            validators = []

        measurement = Measurement(
            name=name,
            value=value,
            unit=unit,
            validators=[v.to_spec() for v in validators],
            hardware_info=hardware_info.to_spec() if hardware_info else None,
            subcomponent=subcomponent.to_spec() if subcomponent else None,
            metadata=metadata,
        )
        self._emitter.emit(StepArtifact(id=self._idstr, impl=measurement))

    # TODO: we start a measurement series implicitly but not test steps
    def start_measurement_series(
        self,
        *,
        name: str,
        unit: ty.Optional[str] = None,
        validators: ty.Optional[ty.List[Validator]] = None,
        hardware_info: ty.Optional[HardwareInfo] = None,
        subcomponent: ty.Optional[Subcomponent] = None,
        metadata: ty.Optional[Metadata] = None,
    ) -> MeasurementSeries:
        """
        Start a new series of measurement and emit the series start artifact.

        :param name: identification for this measurement series.
        :param unit: free-form unit specification for this measurement series.
        :param validator: specifies how the measurement elements in this series
            will be validated in this test step by the diagnostic package.
        :param hardware_info: reference to the hardware component that this
            measurement series elements will be taken from or will be relative to.
        :param subcomponent: reference to the hardware subcomponent (lower than FRU
            level) that this measurement series elements will be taken from or will be relative to.
        :param metadata: dictionary with unspecified metadata for this measurement series.

        For additional details on parameters, see:
        - https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#measurementseriesstart
        """

        with self._series_lock:
            series_id = self._measurement_series_id
            self._measurement_series_id += 1

        # TODO: arbitrary derivation for measurement id here, but unique for run scope;
        # may be a fea request that this follows a template
        series = MeasurementSeries(
            MeasurementSeriesEmitter(self._idstr, self._emitter),
            "{}_{}".format(self._id, series_id),
            name=name,
            unit=unit,
            validators=validators,
            hardware_info=hardware_info,
            subcomponent=subcomponent,
            metadata=metadata,
        )

        return series

    def add_diagnosis(
        self,
        diagnosis_type: DiagnosisType,
        *,
        verdict: str,
        message: ty.Optional[str] = None,
        hardware_info: ty.Optional[HardwareInfo] = None,
        subcomponent: ty.Optional[Subcomponent] = None,
        source_location: ty.Optional[SourceLocation] = SourceLocation.CALLER,
    ):
        """
        Emit a new diagnosis artifact as determined by this test step.

        :param diagnosis_type: outcome type, eg. pass/fail/unknown
            see https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#diagnosistype
        :param verdict: free-form specification of diagnosis outcome
        :param message: message associated with this diagnosis
        :param hardware_info: reference to a part of the DUT that was diagnosed
        :param subcomponent: reference to a subcomponent of the DUT hardware
        :param source_location: source coordinates inside the diagnostic package
            where this artifact was produced. Default value ``SourceLocation.CALLER`` means that this
            function will automatically populate the spec field based on the caller frame.

        For additional details on parameters, see:
        - https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#diagnosis
        """
        if source_location is SourceLocation.CALLER:
            source_location = get_caller_source()

        diag = Diagnosis(
            verdict=verdict,
            type=diagnosis_type,
            message=message,
            hardware_info=hardware_info.to_spec() if hardware_info else None,
            subcomponent=subcomponent.to_spec() if subcomponent else None,
            source_location=source_location.to_spec() if source_location else None,
        )
        self._emitter.emit(StepArtifact(id=self._idstr, impl=diag))

    def add_log(
        self,
        severity: LogSeverity,
        message: str,
        source_location: ty.Optional[SourceLocation] = SourceLocation.CALLER,
    ):
        """
        Emit a log entry artifact relevant for this test step.

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
        self._emitter.emit(StepArtifact(id=self._idstr, impl=log))

    def add_error(
        self,
        *,
        symptom: str,
        message: ty.Optional[str] = None,
        software_infos: ty.Optional[ty.List[SoftwareInfo]] = None,
        source_location: ty.Optional[SourceLocation] = SourceLocation.CALLER,
    ):
        """
        Emit an error artifact relevant for this test step.

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
        self._emitter.emit(StepArtifact(id=self._idstr, impl=error))

    def add_file(
        self,
        *,
        name: str,
        uri: str,
        is_snapshot: bool = True,
        description: ty.Optional[str] = None,
        content_type: ty.Optional[str] = None,
        metadata: ty.Optional[Metadata] = None,
    ):
        """
        Emit an artifact specifying a file resource produced in the diagnosis process.

        :param name: identifying name for this file.
        :param uri: a local/remote location specification for this file.
        :param bool: specifies whether this file is a complete production or if it is a
            temporary snapshot as seen in the diagnosis process.
        :param description: free-form description for this file resource.
        :param content_type: MIME-type specification for this file contents.
        :param metadata: dictionary with unspecified metadata for this file.

        For additional details on parameters, see:
        - https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#file
        """

        file = File(
            name=name,
            uri=uri,
            is_snapshot=is_snapshot,
            description=description,
            content_type=content_type,
            metadata=metadata,
        )
        self._emitter.emit(StepArtifact(id=self._idstr, impl=file))

    def add_extension(
        self,
        *,
        name: str,
        content: ExtensionContentType,
    ):
        """
        Emits a step extension artifact.
        Extensions are meant to accommodate any aspects that are not standardized and may be vendor specific.

        :param name: identification of this specific extension artifact
        :param content: any vendor specific content that can be serialized to JSON

        For additional details on parameters, see:
        - https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#extension
        """

        ext = Extension(name=name, content=content)
        self._emitter.emit(StepArtifact(id=self._idstr, impl=ext))

    @property
    def name(self) -> str:
        return self._name

    @property
    def id(self) -> int:
        return self._id
