"""
This module contains output channel configuration for the OCPTV library.
"""
import threading
import typing as ty
from abc import ABC, abstractmethod

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

    Note: once a test run has started, configuration is saved and will continue to be used
    until a new test run is instantiated. Normally, there should just be one `TestRun`
    object per execution, hence this behavior is unlikely to be encountered.
    """

    def __init__(self):
        self._lock = threading.Lock()
        self._writer: Writer = StdoutWriter()
        self._enable_runtime_checks = True

    @property
    def writer(self) -> Writer:
        with self._lock:
            return self._writer

    @writer.setter
    def writer(self, writer: Writer):
        with self._lock:
            self._writer = writer

    @property
    def enable_runtime_checks(self):
        with self._lock:
            return self._enable_runtime_checks

    @enable_runtime_checks.setter
    def enable_runtime_checks(self, enable: bool):
        with self._lock:
            self._enable_runtime_checks = enable


# module scoped configuration (similar to python logging)
_config: Config = Config()


@export_api
def config(
    *,
    writer: ty.Optional[Writer] = None,
    enable_runtime_checks: ty.Optional[bool] = None,
):
    """
    Configure how the ocptv.output lib behaves.

    :param Writer writer: if provided, set the output channel writer.
    :param bool enable_runtime_checks: if provided, enables or disables runtime type checks.
    """
    global _config

    if writer is not None:
        _config.writer = writer

    if enable_runtime_checks is not None:
        _config.enable_runtime_checks = enable_runtime_checks


def get_config() -> Config:
    """
    Get the module configuration.
    Internal usage only.
    """
    global _config
    return _config
