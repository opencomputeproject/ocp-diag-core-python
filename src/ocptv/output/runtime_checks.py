import dataclasses as dc
import sys
import typing as ty

if ty.TYPE_CHECKING:  # pragma: no cover
    # mypy extension for py37
    from typing_extensions import Protocol
else:
    Protocol = object

if sys.version_info >= (3, 8):  # pragma: no cover
    from typing import get_args, get_origin
else:  # pragma: no cover
    # following are very simple substitutes for their py3.8+ equivalents, but
    # they are sufficient for the usage here in `check_field_types`
    def get_origin(typ: ty.Type):
        if not hasattr(typ, "__origin__"):
            return None
        return typ.__origin__

    def get_args(typ: ty.Type):
        if not hasattr(typ, "__args__"):
            return None
        # note: in py37, the __args__ will contain typevar instances if the generic
        # type was not parametrized in the first place. Remove them because they
        # serve no purpose in the type checking here.
        return tuple(x for x in typ.__args__ if not isinstance(x, ty.TypeVar))


from .config import get_config


class Dataclass(Protocol):
    """
    Protocol type to describe all low level serializable objects in this file.
    """

    __dataclass_fields__: ty.ClassVar[dict]


Primitive = ty.Union[float, int, bool, str, None]
CheckedValue = ty.Union[ty.Dict[str, "CheckedValue"], ty.List["CheckedValue"], Dataclass, Primitive]


def ellipsis(value: ty.Any, max_length: int = 64) -> str:
    s = str(value)
    if len(s) > max_length:
        return s[:max_length] + "..."
    return s


class TypeCheckError(TypeError):
    def __init__(
        self,
        value: CheckedValue,
        expected: str,
        *,
        trace: ty.List[str],
    ):
        self._value = value
        self._expected = expected
        self._trace = trace

        parts = [
            "Cannot use type '{}'".format(type(value).__name__),
            "  Expected type '{}'".format(expected),
            "  Path to offending field is '{}'".format(" -> ".join(trace)),
        ]
        self._msg = "\n".join(parts)

    def __str__(self):
        return self._msg

    @property
    def value(self):
        return self._value

    @property
    def expected(self):
        return self._expected

    @property
    def trace(self):
        return self._trace


class UnionCheckError(TypeCheckError):
    def __init__(
        self,
        value: CheckedValue,
        expected: str,
        *,
        trace: ty.List[str],
        tries: ty.List[ty.Union[TypeCheckError, "UnionCheckError"]],
    ):
        super().__init__(value, expected, trace=trace)
        self._tries = tries

        parts = [
            "Cannot use type '{}' for field value".format(type(value).__name__),
            "  Expected type '{}'".format(expected),
            "  Path to offending field is '{}'".format(" -> ".join(trace)),
        ]
        parts.append("  Tried checks:")

        def format_tries(tries, indent=1):
            for t in tries:
                pre = "  " * indent
                parts.append("{}Value '{}' did not match expected type '{}'".format(pre, ellipsis(t.value), t.expected))
                parts.append("{}Path to field is '{}'".format(pre, " -> ".join(t.trace)))
                if type(t) is UnionCheckError:
                    format_tries(t._tries, indent + 1)

        format_tries(tries)
        self._msg = "\n".join(parts)

    def __str__(self):
        return self._msg


def _check_type_any(obj: CheckedValue, hint: ty.Type, trace: ty.List[str]):
    type_origin = get_origin(hint)
    type_args = get_args(hint)

    if type_origin is list:
        # generic type: typ == ty.List[...]
        if len(type_args) != 1:
            # for non-parametric generics, args is () so we can't actually
            # check for the list item types; short return
            return

        # for list, alias nparams=1
        item_type = type_args[0]

        if not isinstance(obj, list):
            raise TypeCheckError(obj, expected=f"List [{item_type}]", trace=trace)

        # unpack generic type to list item
        for i, v in enumerate(obj):
            subtrace = trace + [f"List[{i}]"]
            _check_type_any(v, item_type, subtrace)

    elif type_origin is dict:
        # generic type: typ == ty.Dict[...]
        if len(type_args) != 2:
            # for non-parametric generics, args is () so we can't actually
            # check for the dict keys or values types; short return
            return

        # for dict, alias nparams=2
        key_type, value_type = type_args

        if not isinstance(obj, dict):
            raise TypeCheckError(obj, expected=f"Dict [{key_type}, {value_type}]", trace=trace)

        # unpack generic type to kv tuple
        for k, v in obj.items():
            subtrace = trace + [f"Dict[{k}]"]
            _check_type_any(k, key_type, subtrace)
            _check_type_any(v, value_type, subtrace)

    elif type_origin is ty.Union:
        # for other generic types, get the covered types
        # note: ty.Optional is ty.Union[x, type(None)] so it still fits here

        any_passed = False
        errors = []
        for hint_item in type_args:
            try:
                _check_type_any(obj, hint_item, trace)
                any_passed = True
                break
            except TypeCheckError as e:
                errors.append(e)

        if not any_passed:
            raise UnionCheckError(obj, expected=f"Union[{type_args}]", trace=trace, tries=errors)

    elif type_origin is not None:
        raise ValueError(f"unsupported type origin value '{type_origin}'")

    elif hint is ty.Any:
        # we can't check anything if type is any, so just return
        return

    elif dc.is_dataclass(obj):
        for field in dc.fields(obj):
            subtrace = trace + [f"{obj.__class__.__name__}.{field.name}"]
            _check_type_any(getattr(obj, field.name), field.type, subtrace)

    elif not isinstance(obj, hint):
        raise TypeCheckError(obj, expected=hint.__name__, trace=trace)


def check_field_types(obj: Dataclass):
    """
    Check that the values inside the given dataclass' fields are of the correct
    type at runtime.
    This currently covers needed field types used in this lib, but is not generic
    enough to cover all typing configurations. See tests for more details.

    Can be disabled in lib config. See `ocptv.output.config()`.

    :throws TypeError on failures.
    """
    if not get_config().enable_runtime_checks:
        return

    _check_type_any(obj, type(obj), trace=[])
