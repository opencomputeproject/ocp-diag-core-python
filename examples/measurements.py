import time

import ocptv.output as tv
from ocptv.output import SoftwareType, SubcomponentType, ValidatorType

from . import demo


@demo
def demo_create_measurement_simple():
    """
    Simple demo with some measurements taken but not referencing DUT hardware.
    """

    run = tv.TestRun(name="test", version="1.0")
    with run.scope(dut=tv.Dut(id="dut0")):
        step = run.add_step("step0")
        with step.scope():
            step.add_measurement(name="fan_speed", value="1200", unit="rpm")
            step.add_measurement(name="temperature", value=42.5)


@demo
def demo_create_measurement_series():
    """
    Show various patterns of time measurement series.

    Step0 has a single series, manually ended.
    Step1 has a single series but using a scope, so series ends automatically.
    Step2 shows multiple measurement interspersed series, they can be concurrent.
    """

    run = tv.TestRun(name="test", version="1.0")
    with run.scope(dut=tv.Dut(id="dut0")):
        step0 = run.add_step("step0")
        with step0.scope():
            fan_speed = step0.start_measurement_series(name="fan_speed", unit="rpm")
            fan_speed.add_measurement(value=1000)
            fan_speed.add_measurement(value=1200)
            fan_speed.add_measurement(value=1500)
            fan_speed.end()

        step1 = run.add_step("step1")
        with step1.scope():
            temp0 = step1.start_measurement_series(name="temp0", unit="C")
            with temp0.scope():
                temp0.add_measurement(value=42, timestamp=time.time() - 2)
                temp0.add_measurement(value=43)

        step2 = run.add_step("step2")
        with step2.scope():
            s0 = step2.start_measurement_series(name="freq0", unit="ghz")
            s1 = step2.start_measurement_series(name="freq1", unit="ghz")

            s0.add_measurement(value=1.0)
            s1.add_measurement(value=2.0)
            s0.add_measurement(value=1.2)
            s0.end()
            s1.end()


@demo
def demo_create_measurements_with_validators():
    """
    Showcase a measurement item and series, both using validators to document
    what the diagnostic package actually validated.
    """

    run = tv.TestRun(name="test", version="1.0")
    with run.scope(dut=tv.Dut(id="dut0")):
        step = run.add_step("step0")
        with step.scope():
            step.add_measurement(
                name="temp",
                value=40,
                validators=[
                    tv.Validator(
                        type=ValidatorType.GREATER_THAN,
                        value=30,
                        name="gt_30",
                    )
                ],
            )

            fan_speed = step.start_measurement_series(
                name="fan_speed",
                unit="rpm",
                validators=[
                    tv.Validator(
                        type=ValidatorType.LESS_THAN_OR_EQUAL,
                        value=3000,
                    )
                ],
            )
            with fan_speed.scope():
                fan_speed.add_measurement(value=1000)


@demo
def demo_create_measurements_with_subcomponent():
    """
    This is a more comprehensive example with a DUT having both hardware and software
    components specified. The measurements reference the hardware items.
    """

    dut = tv.Dut(id="dut0", name="dut0.server.net")
    dut.add_platform_info("memory-optimized")
    dut.add_software_info(
        name="bmc0",
        type=SoftwareType.FIRMWARE,
        version="10",
        revision="11",
        computer_system="primary_node",
    )
    ram0_hardware = dut.add_hardware_info(
        name="ram0",
        version="1",
        revision="2",
        location="MB/DIMM_A1",
        serial_no="HMA2022029281901",
        part_no="P03052-091",
        manufacturer="hynix",
        manufacturer_part_no="HMA84GR7AFR4N-VK",
        odata_id="/redfish/v1/Systems/System.Embedded.1/Memory/DIMMSLOTA1",
        computer_system="primary_node",
        manager="bmc0",
    )

    run = tv.TestRun(name="test", version="1.0")
    with run.scope(dut=dut):
        step = run.add_step("step0")
        with step.scope():
            step.add_measurement(
                name="temp0",
                value=100.5,
                unit="F",
                hardware_info=ram0_hardware,
                subcomponent=tv.Subcomponent(name="chip0"),
            )

            chip1_temp = step.start_measurement_series(
                name="temp1",
                unit="C",
                hardware_info=ram0_hardware,
                subcomponent=tv.Subcomponent(
                    name="chip1",
                    location="U11",
                    version="1",
                    revision="1",
                    type=SubcomponentType.UNSPECIFIED,
                ),
            )
            with chip1_temp.scope():
                chip1_temp.add_measurement(value=79)
