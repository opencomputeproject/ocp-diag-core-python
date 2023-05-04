import sys
import threading
import time
import typing as ty
from datetime import timedelta, timezone

import ocptv.output as tv
from ocptv.output import LogSeverity, StdoutWriter, Writer

from . import demo


@demo
def demo_different_timezone():
    """
    Demo showing how we can manually control the timezone used in the output
    of timestamp fields. This may be useful if reporting and running the diagnostic
    are in different geographical zones.
    """

    tz = timezone(offset=timedelta(hours=-2))
    try:
        tv.config(timezone=tz)

        run = tv.TestRun(name="test", version="1.0")
        with run.scope(dut=tv.Dut(id="dut0")):
            pass
    finally:
        tv.config(timezone=None)


@demo
def demo_custom_writer():
    """
    Showcase parallel running steps outputting to a threadsafe writer on top of
    stdout. The start/end messages get correctly scoped.
    """

    class FileSyncWriter(Writer):
        def __init__(self, file: ty.TextIO):
            self.__file = file
            self.__lock = threading.Lock()

        def write(self, buffer: str):
            with self.__lock:
                print(buffer, file=self.__file)

    tv.config(writer=FileSyncWriter(sys.stdout))

    def parallel_step(step: tv.TestStep):
        with step.scope():
            for _ in range(5):
                step.add_log(
                    LogSeverity.INFO,
                    f"log from: {step.name}, ts: {time.time()}",
                )
                time.sleep(0.001)

    try:
        run = tv.TestRun(name="custom writer", version="1.0")
        with run.scope(dut=tv.Dut(id="dut0")):
            threads: ty.List[threading.Thread] = []
            for id in range(4):
                step = run.add_step(f"parallel_step_{id}")
                threads.append(threading.Thread(target=parallel_step, args=(step,)))

            for t in threads:
                t.start()

            for t in threads:
                t.join()
    finally:
        tv.config(writer=StdoutWriter())
