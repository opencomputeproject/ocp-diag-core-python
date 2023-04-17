import json
import typing as ty
from abc import ABC, abstractmethod

from ocptv.output.emit import JSON, Primitive


class MatcherAssert(ABC):  # pragma: no cover
    @abstractmethod
    def eval(self, value: JSON):
        pass


class LambdaAssert(MatcherAssert):
    def __init__(self, func: ty.Callable[[JSON], bool]):
        self._func = func

    def eval(self, value: JSON):
        assert self._func(value)


Number = ty.Union[int, float]


class RangeAssert(MatcherAssert):
    def __init__(self, *, low: ty.Optional[Number] = None, high: ty.Optional[Number] = None):
        self._low = low
        self._high = high

    def eval(self, value: JSON):
        assert isinstance(value, (int, float)), "Unexpected type for RangeAssert"

        if self._low is not None:
            assert self._low <= value

        if self._high is not None:
            assert value <= self._high


class IgnoreAssert(MatcherAssert):
    def __init__(self) -> None:
        super().__init__()

    def eval(self, value: JSON):
        pass


JSON_MATCHER = ty.Union[
    ty.Dict[str, "JSON_MATCHER"], ty.List["JSON_MATCHER"], LambdaAssert, RangeAssert, IgnoreAssert, Primitive
]


def assert_json(line: str, matcher: JSON_MATCHER):
    """
    Assert that a matcher, as JSON-type structure of exact values or matchers,
    fits the given input JSON `line`.
    """

    def recurse(value: JSON, matcher: JSON_MATCHER):
        if isinstance(matcher, dict):
            assert isinstance(value, dict), "Unexpected type for dict matcher"
            assert value.keys() == matcher.keys(), "Dict keys unequal to matcher"
            for k, v in matcher.items():
                recurse(value[k], v)
        elif isinstance(matcher, list):
            assert isinstance(value, list), "Unexpected type"
            assert len(value) == len(matcher), "List length unequal to matcher"
            for i, v in enumerate(matcher):
                recurse(value[i], v)
        elif isinstance(matcher, MatcherAssert):
            matcher.eval(value)
        else:
            # anything else should be a primitive
            assert value == matcher, "Primitive values not equal"

    recurse(json.loads(line), matcher)
