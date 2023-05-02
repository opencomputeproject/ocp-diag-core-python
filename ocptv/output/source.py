import traceback
import typing as ty

from ocptv.api import export_api

from .objects import SourceLocation as SourceLocationSpec


@export_api
class SourceLocation:
    """
    The ``SourceLocation`` instances are coordinates in user diagnostic code, used
    for documenting where an ``Error``, ``Log`` or ``Diagnosis`` artifacts were emitted from.

    For functions taking a ``source_location`` parameter, eg. the ones making error messages,
    the default value is ``SourceLocation.CALLER``. Thi special instance is used to tell the
    library to try to guess the location in user code based on the call stack.

    However, the ``source_location`` can also be manually specified if needed.

    Usage:

    .. code-block:: python

        import ocptv.output as tv
        run = tv.TestRun(name="test", version="1.0")
        # default source_location=SourceLocation.CALLER on the following line
        # will result in the fields identifying the next line itself
        run.add_log(LogSeverity.DEBUG, "Some interesting message.")

    Specification reference:
    - https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#sourcelocation
    """

    CALLER: "SourceLocation"
    """ Special instance. See ``SourceLocation`` docstring for details. """

    def __init__(self, filename: str, line_number: int):
        """
        :param filename: diagnostic package source filename being referenced.
        :param line_number: line number inside the diagnostic package source file.
        """
        self._file = filename
        self._line = line_number

    def to_spec(self) -> ty.Optional[SourceLocationSpec]:
        """
        Internal usage. Convert to low-level model.

        :meta private:
        """
        return SourceLocationSpec(file=self._file, line=self._line)


# note: the field values here dont matter. This is used as a guard value.
# Equality comparison should be done by instance.
SourceLocation.CALLER = SourceLocation("", 0)


class NullSourceLocation(SourceLocation):
    """
    This is an internal specialization of ``SourceLocation`` that will result in the
    ``source_location`` message fields not to be emitted by virtue of translating into a None.
    """

    def __init__(self):
        super().__init__("", 0)

    def to_spec(self) -> ty.Optional[SourceLocationSpec]:
        return None


def get_caller_source(offset: int = 1) -> SourceLocation:
    """
    Get the caller site coordinates as a SourceLocation instance.
    This will try to guess the callsite in user code by going down the stack.

    :param offset: expected number of stack frames to user code from the
        context of the code calling this function. Default value is 1, as it's
        expected that this function is called from lib code that is exactly one
        level from the user code.
    :returns: if the user code coordinates could be identified, this returns
        a valid SourceLocation object; otherwise it returns a null-value specialization that
        results in the JSON output to not be emitted.
    """
    assert offset > 0

    # TODO: this may be refactored later on to look at frame data, rather than use an index
    frames = traceback.extract_stack()[::-1]
    try:
        # the +1 is this function frame
        caller = frames[offset + 1]

        lineno = 0
        if caller.lineno is not None:
            lineno = caller.lineno

        return SourceLocation(
            filename=caller.filename,
            line_number=lineno,
        )
    except IndexError:
        # unlikely: error trying to get the user code frame, so return an
        # instance that will translate to None in the spec
        return NullSourceLocation()
