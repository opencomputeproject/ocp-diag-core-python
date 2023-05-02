import typing as ty
from datetime import datetime, timezone, tzinfo
from enum import Enum


def format_enum(variant: Enum) -> str:
    """Format an enum by variant value"""
    return "{}".format(variant.value)


def format_timestamp(ts: float, tz: ty.Optional[tzinfo] = timezone.utc) -> str:
    """
    Format an unix timestamp in local tz.
    If the timezone coincides with UTC, returns zulu time format.
    """
    dt = datetime.fromtimestamp(ts)
    isostr = dt.astimezone(tz).isoformat()

    utcsuffix = "+00:00"
    if isostr.endswith(utcsuffix):
        return isostr[: -len(utcsuffix)] + "Z"
    return isostr
