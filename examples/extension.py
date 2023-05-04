import ocptv.output as tv

from . import demo


@demo
def demo_step_extension():
    """
    Showcase how to output a vendor specific test step extension.
    """

    run = tv.TestRun(name="test", version="1.0")
    with run.scope(dut=tv.Dut(id="dut0")):
        step = run.add_step("step0")
        with step.scope():
            step.add_extension(
                name="simple",
                content="extension_identifier",
            )

            step.add_extension(
                name="complex",
                content={
                    "@type": "DemoExtension",
                    "field": "demo",
                    "subtypes": [1, 42],
                },
            )
