import json
import typing as ty

import pytest

import ocptv.output as tv
from ocptv.output import Writer
from ocptv.output.emit import JSON


class MockWriter(Writer):
    def __init__(self):
        self.lines: ty.List[str] = []

    def write(self, buffer: str):
        self.lines.append(buffer)

    def decoded_obj(self, index: int) -> ty.Dict[str, JSON]:
        """Decode an expected object from given output index"""
        return json.loads(self.lines[index])


@pytest.fixture
def writer() -> MockWriter:
    w = MockWriter()
    tv.config_output(w)
    return w


def assert_json(line: str, expected: JSON):
    actual = json.loads(line)

    # remove timestamps, cant easily compare
    if isinstance(actual, dict) and "timestamp" in actual:
        del actual["timestamp"]

    if isinstance(expected, dict) and "timestamp" in expected:
        del expected["timestamp"]

    assert actual == expected
