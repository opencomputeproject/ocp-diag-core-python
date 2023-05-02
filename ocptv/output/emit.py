"""
This module covers the raw output semantics of the OCPTV library.
"""
import dataclasses as dc
import json
import threading
import time
import typing as ty
from enum import Enum

from .config import Writer
from .objects import ArtifactType, Root, RootArtifactType, SchemaVersion

Primitive = ty.Union[float, int, bool, str, None]
JSON = ty.Union[ty.Dict[str, "JSON"], ty.List["JSON"], Primitive]


def _is_optional(field: ty.Type):
    # type hackery incoming
    # ty.Optional[T] == ty.Union[T, None]
    # since ty.Union[ty.Union[T,U]] = ty.Union[T,U] we can the
    # following transitiveness to check that type is optional
    return field == ty.Optional[field]


class ArtifactEmitter:
    """
    Serializes and emits the data on the configured output channel for the lib.
    Uses the low level dataclass models for the spec, but should not be used in user code.
    """

    def __init__(self, writer: Writer):
        self._seq_lock = threading.Lock()
        self._seq = 0

        self._writer = writer

        # use this event to ensure that the schema version message is the first to be
        # emitted, even when the initial writer was preempted
        self._version_emitted = threading.Event()

    @staticmethod
    def _serialize(artifact: ArtifactType):
        def visit(
            value: ty.Union[ArtifactType, ty.Dict, ty.List, Primitive],
            formatter: ty.Optional[ty.Callable[[ty.Any], str]] = None,
        ) -> JSON:
            # if present, formatter takes precedence over serialization
            if formatter is not None:
                return formatter(value)

            if dc.is_dataclass(value):
                obj: ty.Dict[str, JSON] = {}
                for field in dc.fields(value):
                    val = getattr(value, field.name)

                    if val is None:
                        if not _is_optional(field.type):
                            # TODO: fix exception text/type
                            raise RuntimeError("unacceptable none where not optional")

                        # for some reason, py3.7-3.10 fail to count the "continue" below as being covered
                        # by tests; this next line is a noop which avoids that behavior
                        val
                        continue

                    # spec_field takes precedence over spec_object
                    spec_field: ty.Optional[str] = field.metadata.get("spec_field", None)
                    spec_object: ty.Optional[str] = getattr(val, "SPEC_OBJECT", None)

                    if spec_field is None and spec_object is None:
                        # TODO: fix error type
                        raise RuntimeError(
                            "internal error, bad object decl: neither spec_field nor spec_object present for {}".format(
                                field.name
                            )
                        )

                    # safety: at least one is not None
                    name: str = ty.cast(str, spec_field or spec_object)
                    formatter = field.metadata.get("formatter", None)
                    obj[name] = visit(val, formatter)
                return obj
            elif isinstance(value, list) or isinstance(value, tuple):
                return [visit(k) for k in value]
            elif isinstance(value, dict):
                return {k: visit(v) for k, v in value.items()}
            elif isinstance(value, (str, float, int, bool, Enum)):
                return value

            raise RuntimeError("dont know how to serialize {}", value)

        return json.dumps(visit(artifact))

    def emit(self, artifact: RootArtifactType):
        """
        Emit the given artifact after serialization to JSON.
        This method is threadsafe.
        """
        seq = self._next_seq_no()
        if seq == 0:
            self._emit_version()
            seq = self._next_seq_no()

        # wait to make sure that version schema was written first
        self._version_emitted.wait()

        root = Root(
            impl=artifact,
            sequence_number=seq,
            timestamp=time.time(),
        )
        self._writer.write(self._serialize(root))

    def _emit_version(self):
        # use defaults for schema version here, should be set to latest
        root = Root(
            impl=SchemaVersion(),
            # seq number is always 0 for the spec version artifact
            sequence_number=0,
            timestamp=time.time(),
        )
        self._writer.write(self._serialize(root))

        # awake all threads that may have been waiting on version first write
        self._version_emitted.set()

    def _next_seq_no(self) -> int:
        with self._seq_lock:
            seq = self._seq
            self._seq += 1

        return seq
