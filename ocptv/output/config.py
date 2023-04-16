"""
This module contains output channel configuration for the OCPTV library.
"""
import threading

from ocptv.api import export_api

from .emit import StdoutWriter, Writer


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
