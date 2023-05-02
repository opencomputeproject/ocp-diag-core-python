"""
This module contains output channel configuration for the OCPTV library.
"""
import threading
import typing as ty
from abc import ABC, abstractmethod
from datetime import timezone, tzinfo

from ocptv.api import export_api


class Writer(ABC):  # pragma: no cover
    """
    Abstract writer interface for the lib. Should be used as a base for
    any output writer implementation (for typing purposes).
    NOTE: Writer impls must ensure thread safety.
    """

    @abstractmethod
    def write(self, buffer: str):
        pass


@export_api
class StdoutWriter(Writer):
    """
    A simple writer that prints the json to stdout.
    """

    def __init__(self):
        self._lock = threading.Lock()

    def write(self, buffer: str):
        with self._lock:
            print(buffer)


class Config:
    """
    Thread safe storage for module configuration.

    Note: once a test run has started, configuration is considered committed and will
    continue to be used until a new test run is instantiated. Normally, there should
    just be one `TestRun` object per execution, hence this behavior is unlikely to be
    encountered.
    """

    def __init__(self):
        self._lock = threading.Lock()
        self._writer: Writer = StdoutWriter()
        self._enable_runtime_checks = True
        self._tzinfo: ty.Union[tzinfo, None] = timezone.utc

    @property
    def writer(self) -> Writer:
        with self._lock:
            return self._writer

    @writer.setter
    def writer(self, writer: Writer):
        with self._lock:
            self._writer = writer

    @property
    def enable_runtime_checks(self) -> bool:
        with self._lock:
            return self._enable_runtime_checks

    @enable_runtime_checks.setter
    def enable_runtime_checks(self, enable: bool):
        with self._lock:
            self._enable_runtime_checks = enable

    @property
    def timezone(self) -> ty.Union[tzinfo, None]:
        with self._lock:
            return self._tzinfo

    @timezone.setter
    def timezone(self, tzinfo: ty.Union[tzinfo, None]):
        with self._lock:
            self._tzinfo = tzinfo


# module scoped configuration (similar to python logging)
_config: Config = Config()

if ty.TYPE_CHECKING:  # pragma: no cover
    # We use a sentinel object that looks like a None for the static type checker.
    # At runtime, we check against the specific instance of `object()` to make a decision
    # on whether this parameter was passed in or not.
    # This is useful for types where NoneType is actually a valid instance of the type.
    _NOT_SET = None
else:
    _NOT_SET = object()


@export_api
def config(
    *,
    writer: ty.Optional[Writer] = None,
    enable_runtime_checks: ty.Optional[bool] = None,
    timezone: ty.Union[tzinfo, None] = _NOT_SET,
):
    """
    Configure how the ocptv.output lib behaves.

    :param writer: if provided, set the output channel writer.
    :param enable_runtime_checks: if provided, enables or disables runtime type checks.
    :param timezone: if provided, sets the timezone for the output formatted datetime fields.
        Use `None` to automatically determine the local system timezone.
        The library default, if never configured, is UTC.
    """
    global _config

    if writer is not None:
        _config.writer = writer

    if enable_runtime_checks is not None:
        _config.enable_runtime_checks = enable_runtime_checks

    if timezone is not _NOT_SET:
        _config.timezone = timezone


def get_config() -> Config:
    """
    Get the module configuration.
    Internal usage only.
    """
    global _config
    return _config
