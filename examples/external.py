import ocptv.output as tv

from . import demo


@demo
def demo_create_file_during_step():
    """
    Showcase that we can create long duration artifacts such as files from
    a diagnostic package, and how we reference them later on.
    """

    run = tv.TestRun(name="test", version="1.0")
    with run.scope(dut=tv.Dut(id="dut0")):
        step = run.add_step("step0")
        with step.scope():
            step.add_file(
                name="device_info.csv",
                uri="file:///root/device_info.csv",
            )

            meta = tv.Metadata()
            meta["k"] = "v"
            step.add_file(
                name="file_with_meta.txt",
                uri="ftp://file",
                metadata=meta,
            )
