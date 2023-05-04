import ocptv.output as tv
from ocptv.output import (
    DiagnosisType,
    LogSeverity,
    SoftwareType,
    TestResult,
    TestStatus,
)

from . import demo


@demo
def demo_no_contexts():
    """
    Show that a run/step can be manually started and ended.

    The scope version should be preferred, as it makes it safer not to miss the end
    artifacts in case of unhandled exceptions or code misuse.
    """

    run = tv.TestRun(name="no with", version="1.0", parameters={"param": "test"})
    run.start(dut=tv.Dut(id="dut0"))

    step = run.add_step("step0")
    step.start()
    step.add_log(LogSeverity.DEBUG, "Some interesting message.")
    step.end(status=TestStatus.COMPLETE)

    run.end(status=TestStatus.COMPLETE, result=TestResult.PASS)


@demo
def demo_context_run_skip():
    """
    Show a context-scoped run that automatically exits the whole func
    because of the marker exception that triggers SKIP outcome.
    """

    run = tv.TestRun(name="run_skip", version="1.0", parameters={"param": "test"})
    with run.scope(dut=tv.Dut(id="dut0")):
        raise tv.TestRunError(status=TestStatus.SKIP, result=TestResult.NOT_APPLICABLE)


@demo
def demo_context_step_fail():
    """
    Show a scoped run with scoped steps, everything starts at "with" time and
    ends automatically when the block ends (regardless of unhandled exceptions).
    """

    run = tv.TestRun(name="step_fail", version="1.0")
    with run.scope(dut=tv.Dut(id="dut0")):
        step = run.add_step("step0")
        with step.scope():
            step.add_log(LogSeverity.INFO, "info log")

        step = run.add_step("step1")
        with step.scope():
            # TODO: maybe this should fail the whole run?
            raise tv.TestStepError(status=TestStatus.ERROR)


@demo
def demo_diagnosis():
    """
    Show outputting a diagnosis message for the given step.
    Normally the diagnosis is one of the later messages in an output, likely
    right before exiting the test step scope.

    In this case, the diagnosis does not reference any particular hardware component.
    """

    class Verdict:
        # str consts for error classifier
        PASS = "pass-default"

    run = tv.TestRun(name="run_with_diagnosis", version="1.0")
    with run.scope(dut=tv.Dut(id="dut0")):
        step = run.add_step("step0")
        with step.scope():
            step.add_diagnosis(DiagnosisType.PASS, verdict=Verdict.PASS)


@demo
def demo_error_while_gathering_duts():
    """
    In case of failure to discover DUT hardware before needing to present it at test run
    start, we can error out right at the beginning.
    """

    class Symptom:
        # str consts for error classifier
        NO_DUT = "no-dut"

    run = tv.TestRun(name="test", version="1.0")
    run.add_error(
        symptom=Symptom.NO_DUT,
        message="could not find any valid DUTs",
    )


@demo
def demo_run_error_with_dut():
    """
    Show outputting an error message, triggered by a specific software component of the DUT.
    """

    dut = tv.Dut(id="dut0", name="dut0.server.net")
    bmc_software = dut.add_software_info(
        name="bmc",
        type=SoftwareType.FIRMWARE,
        version="2.5",
    )

    run = tv.TestRun(name="test", version="1.0")
    with run.scope(dut=dut):
        run.add_error(
            symptom="power-fail",
            software_infos=[bmc_software],
        )
