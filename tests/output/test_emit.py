import dataclasses as dc
import typing as ty

import pytest

from ocptv.output import config_output
from ocptv.output.emit import ArtifactEmitter
from ocptv.output.objects import SchemaVersion

from .conftest import MockWriter


@pytest.fixture(autouse=True)
def setup_writer(writer: MockWriter):
    config_output(writer)


def test_emit_ok_with_none_optional():
    @dc.dataclass
    class TestObject:
        SPEC_OBJECT: ty.ClassVar[str] = "test"
        optional: ty.Optional[str]

    e = ArtifactEmitter()
    e.emit(TestObject(optional=None))  # type: ignore[arg-type]


def test_emit_fails_none_in_nonoptional():
    """
    Try to emit a dataclass type with a non-optional field that contains a None value.
    Expect failure.
    Type errors are ignored.
    """

    @dc.dataclass
    class TestObject:
        SPEC_OBJECT: ty.ClassVar[str] = "test"
        nonoptional: str

    e = ArtifactEmitter()
    with pytest.raises(RuntimeError):
        e.emit(TestObject(nonoptional=None))  # type: ignore[arg-type]


def test_emit_fails_missing_spec_object():
    """
    Try to emit an artifact with no reference to spec.
    Expect failure.
    Type errors are ignored.
    """

    @dc.dataclass
    class TestObject:
        field: int

    e = ArtifactEmitter()
    with pytest.raises(RuntimeError):
        e.emit(TestObject(field=42))  # type: ignore[arg-type]


def test_emil_fails_unserializable_type():
    """
    Try to emit an artifact with a field of a type that cannot be serialized.
    Expect failure.
    Type errors are ignored.
    """

    class Unserializable:
        SPEC_OBJECT: ty.ClassVar[str] = "test"

    e = ArtifactEmitter()
    with pytest.raises(RuntimeError):
        e.emit(Unserializable())  # type: ignore[arg-type]
