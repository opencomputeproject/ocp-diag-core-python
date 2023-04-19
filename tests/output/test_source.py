import sys

from ocptv.output.source import NullSourceLocation, get_caller_source


def test_get_caller_source_with_bad_index():
    value = get_caller_source(offset=sys.maxsize)

    assert isinstance(value, NullSourceLocation)
    assert value.to_spec() is None
