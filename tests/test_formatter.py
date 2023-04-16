from datetime import datetime, timedelta, timezone
from enum import Enum

from ocptv.formatter import format_enum, format_timestamp


def test_format_enum_simple():
    class TestEnum(Enum):
        V42 = 42

    assert format_enum(TestEnum.V42) == "42"


def test_format_timestamp_simple():
    tz = timezone(offset=timedelta(hours=1), name="plus1")
    value = datetime(
        year=2020,
        month=1,
        day=2,
        hour=3,
        minute=4,
        second=5,
        microsecond=100,
        tzinfo=tz,
    )
    assert format_timestamp(value.timestamp(), tz=tz) == "2020-01-02T03:04:05.000100+01:00"


def test_format_timestamp_zulu():
    assert format_timestamp(0, tz=timezone.utc) == "1970-01-01T00:00:00Z"
