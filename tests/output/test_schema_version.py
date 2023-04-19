import ocptv.output as tv
from ocptv.output import OCPVersion

from .checks import IgnoreAssert, assert_json
from .conftest import MockWriter


def test_schema_version_is_emitted(writer: MockWriter):
    run = tv.TestRun(name="test", version="1.0")
    run.start(dut=tv.Dut(id="test_dut"))

    assert len(writer.lines) == 2
    assert_json(
        writer.lines[0],
        {
            "schemaVersion": {
                "major": OCPVersion.VERSION_2_0.value[0],
                "minor": OCPVersion.VERSION_2_0.value[1],
            },
            "sequenceNumber": 0,
            "timestamp": IgnoreAssert(),
        },
    )
