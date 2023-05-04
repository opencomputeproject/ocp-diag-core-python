import logging
import sys

import ocptv.output as tv
from ocptv.output import LogSeverity, StdoutWriter, Writer

from . import demo


@demo
def demo_python_logging_io():
    """
    Show that we can output to a python logger backed writer (note the pylog prefix)
    and that we can route the standard python logger as input for the ocp output (mapped to run logs).

    This demo is shown as a migration path for code using standard python logging, until
    we have some on-parity functionality (eg. rolling/archiving output writer).
    """

    class LoggingWriter(Writer):
        def __init__(self):
            logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="[pylog] %(message)s")

        def write(self, buffer: str):
            logging.info(buffer)

    tv.config(writer=LoggingWriter())

    class Handler(logging.StreamHandler):
        def __init__(self, run: tv.TestRun):
            super().__init__(None)
            self._run = run

        def emit(self, record: logging.LogRecord):
            self._run.add_log(self._map_level(record.levelno), record.msg)

        @staticmethod
        def _map_level(level: int) -> LogSeverity:
            if level == logging.DEBUG:
                return LogSeverity.DEBUG
            if level == logging.WARN:
                return LogSeverity.WARNING
            if level == logging.ERROR:
                return LogSeverity.ERROR
            if level == logging.FATAL:
                return LogSeverity.FATAL
            return LogSeverity.INFO

    run = tv.TestRun(name="run_with_diagnosis", version="1.0")

    log = logging.getLogger("ocptv")
    log.addHandler(Handler(run))
    log.setLevel(logging.DEBUG)
    log.propagate = False

    try:
        with run.scope(dut=tv.Dut(id="dut0")):
            log.info("ocp log thru python logger")
            log.debug("debug log sample")
            log.warning("warn level here")
    finally:
        tv.config(writer=StdoutWriter())
        log.removeHandler(log.handlers[-1])
