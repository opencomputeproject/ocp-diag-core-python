# ocptv.output.measurement module


### _class_ ocptv.output.measurement.Validator(\*, type, value, name=None, metadata=None)
The `Validator` object represents a named validation that is relevant to a measurement or
measurement series.

Specification reference:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#validator](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#validator)

This type can be instantiated by user code directly.


#### \__init__(\*, type, value, name=None, metadata=None)
Initialize a new validator object.


* **Parameters**

    
    * **type** ([`ValidatorType`](output.objects.md#ocptv.output.objects.ValidatorType)) – classification for this validator.
    See: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#validatortype](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#validatortype)


    * **value** (`Union`[`List`[`float`], `List`[`int`], `List`[`bool`], `List`[`str`], `float`, `int`, `bool`, `str`]) – reference value for this validator. Can be a primitive type (int, float, str, bool)
    or a homogenous list of the same primitives. The list is only valid for the set-type validations.


    * **name** (`Optional`[`str`]) – identification for this validator item.


    * **metadata** (`Optional`[[`Metadata`](output.objects.md#ocptv.output.objects.Metadata)]) – dictionary with unspecified metadata for this validator.


For additional details on parameters, see:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#validator](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#validator)


### _class_ ocptv.output.measurement.MeasurementSeries(emitter, series_id, \*, name, unit=None, validators=None, hardware_info=None, subcomponent=None, metadata=None)
The `MeasurementSeries` instances model a specific time-based list of values relevant to the diagnostic.
A series is started by default on instantiation and must be ended with the `.end()` method or
by using a `.scope()` context manager.

Instances of this type must only be created by calls to `TestStep.start_measurement_series()`.

All the methods in this class are threadsafe.

Specification reference:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#measurementseriesstart](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#measurementseriesstart)


#### add_measurement(\*, value, timestamp=None, metadata=None)
Emit a new measurement item for this series.


* **Parameters**

    
    * **value** (`Union`[`float`, `int`, `bool`, `str`]) – value of the taken measurement.


    * **timestamp** (`Optional`[`float`]) – wallclock time when this measurement was taken. If unspecified,
    it will be computed based on the current wallclock time on the system running the diagnostic.


    * **metadata** (`Optional`[[`Metadata`](output.objects.md#ocptv.output.objects.Metadata)]) – dictionary with unspecified metadata for this measurement item.



#### end()
Emit a measurement series end artifact.

Specification reference:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#measurementseriesend](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#measurementseriesend)


#### scope()
Wrap the measurement series into a scope that guarantees exception safety.
When this scope ends, whether normally or from as exception, the end artifact is emitted.

Usage:

```python
fan_speeds = step.start_measurement_series(name="fan0", ...)
with fan_speeds.scope():
    fan_speeds.add_measurement(value=4200)
```
