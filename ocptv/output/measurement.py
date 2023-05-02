import threading
import time
import typing as ty
from contextlib import contextmanager

from ocptv.api import export_api

from .dut import HardwareInfo, Subcomponent
from .emit import ArtifactEmitter
from .objects import (
    MeasurementSeriesElement,
    MeasurementSeriesEnd,
    MeasurementSeriesStart,
    MeasurementSeriesType,
    MeasurementValueType,
    Metadata,
    StepArtifact,
)
from .objects import Validator as ValidatorSpec
from .objects import ValidatorType, ValidatorValueType


class MeasurementSeriesEmitter(ArtifactEmitter):
    def __init__(self, step_id: str, emitter: ArtifactEmitter):
        self._step_id = step_id
        self._emitter = emitter

    def emit_impl(self, impl: MeasurementSeriesType):
        self._emitter.emit(StepArtifact(id=self._step_id, impl=impl))


# Following object is a proxy type so we get future flexibility, avoiding the usage
# of the low-level models.
@export_api
class Validator:
    """
    The ``Validator`` object represents a named validation that is relevant to a measurement or
    measurement series.

    Specification reference:
    - https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#validator
    """

    def __init__(
        self,
        *,
        type: ValidatorType,
        value: ValidatorValueType,
        name: ty.Optional[str] = None,
        metadata: ty.Optional[Metadata] = None,
    ):
        """
        Initialize a new validator object.

        :param type: classification for this validator.
            See: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#validatortype
        :param value: reference value for this validator. Can be a primitive type (int, float, str, bool)
            or a homogenous list of the same primitives. The list is only valid for the set-type validations.
        :param name: identification for this validator item.
        :param metadata: dictionary with unspecified metadata for this validator.

        For additional details on parameters, see:
        - https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#validator
        """

        self._spec_object = ValidatorSpec(
            name=name,
            type=type,
            value=value,
            metadata=metadata,
        )

    def to_spec(self) -> ValidatorSpec:
        """
        Internal usage. Convert to low-level model.

        :meta private:
        """
        return self._spec_object


class MeasurementSeries:
    """
    The ``MeasurementSeries`` instances model a specific time-based list of values relevant to the diagnostic.
    A series is started by default on instantiation and must be ended with the ``.end()`` method or
    by using a ``.scope()`` context manager.

    Instances of this type must only be created by calls to ``TestStep.start_measurement_series()``.

    All the methods in this class are threadsafe.

    Specification reference:
    - https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#measurementseriesstart
    """

    def __init__(
        self,
        emitter: MeasurementSeriesEmitter,
        series_id: str,
        *,
        name: str,
        unit: ty.Optional[str] = None,
        validators: ty.Optional[ty.List[Validator]] = None,
        hardware_info: ty.Optional[HardwareInfo] = None,
        subcomponent: ty.Optional[Subcomponent] = None,
        metadata: ty.Optional[Metadata] = None,
    ):
        self._emitter = emitter
        self._id = series_id

        self._index_lock = threading.Lock()
        self._index: int = 0

        self._start(name, unit, validators, hardware_info, subcomponent, metadata)

    def add_measurement(
        self,
        *,
        value: MeasurementValueType,
        timestamp: ty.Optional[float] = None,
        metadata: ty.Optional[Metadata] = None,
    ):
        """
        Emit a new measurement item for this series.

        :param value: value of the taken measurement.
        :param timestamp: wallclock time when this measurement was taken. If unspecified,
            it will be computed based on the current wallclock time on the system running the diagnostic.
        :param metadata: dictionary with unspecified metadata for this measurement item.
        """

        if timestamp is None:
            # use local time if not specified
            timestamp = time.time()

        with self._index_lock:
            index = self._index
            self._index += 1

        measurement = MeasurementSeriesElement(
            index=index,
            value=value,
            timestamp=timestamp,
            series_id=self._id,
            metadata=metadata,
        )
        self._emitter.emit_impl(measurement)

    def _start(
        self,
        name: str,
        unit: ty.Optional[str] = None,
        validators: ty.Optional[ty.List[Validator]] = None,
        hardware_info: ty.Optional[HardwareInfo] = None,
        subcomponent: ty.Optional[Subcomponent] = None,
        metadata: ty.Optional[Metadata] = None,
    ):
        if validators is None:
            validators = []

        start = MeasurementSeriesStart(
            name=name,
            unit=unit,
            series_id=self._id,
            validators=[v.to_spec() for v in validators],
            hardware_info=hardware_info.to_spec() if hardware_info else None,
            subcomponent=subcomponent.to_spec() if subcomponent else None,
            metadata=metadata,
        )
        self._emitter.emit_impl(start)

    def end(self):
        """
        Emit a measurement series end artifact.

        Specification reference:
        - https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#measurementseriesend
        """

        end = MeasurementSeriesEnd(
            series_id=self._id,
            total_count=self._index,
        )
        self._emitter.emit_impl(end)

    @contextmanager
    def scope(self):
        """
        Wrap the measurement series into a scope that guarantees exception safety.
        When this scope ends, whether normally or from as exception, the end artifact is emitted.

        Usage:

        .. code-block:: python

            fan_speeds = step.start_measurement_series(name="fan0", ...)
            with fan_speeds.scope():
                fan_speeds.add_measurement(value=4200)
        """

        try:
            yield
        finally:
            self.end()
