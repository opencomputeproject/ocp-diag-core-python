"""
This module contains output channel configuration for the OCPTV library.
"""
import threading
from abc import ABC, abstractmethod

from ocptv.api import export_api


class Writer(ABC):
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
    """

    def __init__(self):
        self._lock = threading.Lock()
        self._writer = StdoutWriter()

    @property
    def writer(self) -> Writer:
        with self._lock:
            return self._writer

    @writer.setter
    def writer(self, writer: Writer):
        with self._lock:
            self._writer = writer


# module scoped configuration (similar to python logging)
_config: Config = Config()


@export_api
def config_output(writer: Writer):
    """
    Configure the output channel for this library.
    """
    global _config
    _config.writer = writer


def get_config() -> Config:
    """
    Get the module configuration.
    Internal usage only.
    """
    global _config
    return _config
