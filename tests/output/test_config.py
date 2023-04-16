import pytest

from ocptv.output import StdoutWriter


def test_stdout_writer(capsys: pytest.CaptureFixture):
    ref = "test output"

    w = StdoutWriter()
    w.write(ref)

    value: str = capsys.readouterr().out
    assert value.strip() == ref
