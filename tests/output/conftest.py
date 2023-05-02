import json
import typing as ty
from contextlib import contextmanager
from datetime import timedelta, timezone

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
    tv.config(writer=w)
    return w


@contextmanager
def disable_runtime_checks():
    from ocptv.output.config import get_config

    try:
        prev = get_config().enable_runtime_checks
        tv.config(enable_runtime_checks=False)

        yield
    finally:
        tv.config(enable_runtime_checks=prev)


@contextmanager
def offset_timezone(utc_offset_hours: float):
    from ocptv.output.config import get_config

    try:
        prev = get_config().timezone
        tz = timezone(offset=timedelta(hours=utc_offset_hours))
        tv.config(timezone=tz)

        yield
    finally:
        tv.config(timezone=prev)
