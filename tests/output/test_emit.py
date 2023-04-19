import dataclasses as dc
import typing as ty

import pytest

from ocptv.output import StdoutWriter
from ocptv.output.emit import ArtifactEmitter

from .conftest import MockWriter, disable_runtime_checks


def test_stdout_writer(capsys: pytest.CaptureFixture):
    ref = "test output"

    w = StdoutWriter()
    w.write(ref)

    value: str = capsys.readouterr().out
    assert value.strip() == ref


def test_emit_ok_with_none_optional(writer: MockWriter):
    @dc.dataclass
    class TestObject:
        SPEC_OBJECT: ty.ClassVar[str] = "test"
        optional: ty.Optional[str]

    e = ArtifactEmitter(writer)
    e.emit(TestObject(optional=None))  # type: ignore[arg-type]


def test_emit_fails_none_in_nonoptional(writer: MockWriter):
    """
    Try to emit a dataclass type with a non-optional field that contains a None value.
    Expect failure.
    Type errors are ignored.
    """

    @dc.dataclass
    class TestObject:
        SPEC_OBJECT: ty.ClassVar[str] = "test"
        nonoptional: str

    with disable_runtime_checks():
        e = ArtifactEmitter(writer)
        with pytest.raises(RuntimeError):
            e.emit(TestObject(nonoptional=None))  # type: ignore[arg-type]


def test_emit_fails_missing_spec_object(writer: MockWriter):
    """
    Try to emit an artifact with no reference to spec.
    Expect failure.
    Type errors are ignored.
    """

    @dc.dataclass
    class TestObject:
        field: int

    e = ArtifactEmitter(writer)
    with pytest.raises(RuntimeError):
        e.emit(TestObject(field=42))  # type: ignore[arg-type]


def test_emil_fails_unserializable_type(writer: MockWriter):
    """
    Try to emit an artifact with a field of a type that cannot be serialized.
    Expect failure.
    Type errors are ignored.
    """

    class Unserializable:
        SPEC_OBJECT: ty.ClassVar[str] = "test"

    with disable_runtime_checks():
        e = ArtifactEmitter(writer)
        with pytest.raises(RuntimeError):
            e.emit(Unserializable())  # type: ignore[arg-type]
