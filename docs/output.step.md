# ocptv.output.step module

This module describes the test steps inside the test run.


### _class_ ocptv.output.step.TestStepError(\*, status)
The `TestStepError` can be raised within a context scope started by `TestStep.scope()`.
Any instance will be caught and handled by the context and will result in ending the
step with an error.

This type can be instantiated by user code directly.


#### \__init__(\*, status)

* **Parameters**

    **status** ([`TestStatus`](output.objects.md#ocptv.output.objects.TestStatus)) – outcome status for this step.



### _class_ ocptv.output.step.TestStep(name, \*, step_id, emitter)
The `TestStep` instances are the stateful interface to diagnostic steps inside a run.
They present methods to interact with the steps themselves or to make child artifacts.

Should not be used directly by user code, but created through `TestRun.add_step()`.

Usage:

```python
step0 = run.add_step("step0") # run: TestRun
with step0.scope():
    pass
```

For other usages, see the the `examples` folder in the root of the project.

All the methods in this class are threadsafe.

Specification reference:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#test-step-artifacts](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#test-step-artifacts)


#### add_diagnosis(diagnosis_type, \*, verdict, message=None, hardware_info=None, subcomponent=None, source_location=<ocptv.output.source.SourceLocation object>)
Emit a new diagnosis artifact as determined by this test step.


* **Parameters**

    
    * **diagnosis_type** ([`DiagnosisType`](output.objects.md#ocptv.output.objects.DiagnosisType)) – outcome type, eg. pass/fail/unknown
    see [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#diagnosistype](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#diagnosistype)


    * **verdict** (`str`) – free-form specification of diagnosis outcome


    * **message** (`Optional`[`str`]) – message associated with this diagnosis


    * **hardware_info** (`Optional`[[`HardwareInfo`](output.dut.md#ocptv.output.dut.HardwareInfo)]) – reference to a part of the DUT that was diagnosed


    * **subcomponent** (`Optional`[[`Subcomponent`](output.dut.md#ocptv.output.dut.Subcomponent)]) – reference to a subcomponent of the DUT hardware


    * **source_location** (`Optional`[[`SourceLocation`](output.source.md#ocptv.output.source.SourceLocation)]) – source coordinates inside the diagnostic package
    where this artifact was produced. Default value `SourceLocation.CALLER` means that this
    function will automatically populate the spec field based on the caller frame.


For additional details on parameters, see:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#diagnosis](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#diagnosis)


#### add_error(\*, symptom, message=None, software_infos=None, source_location=<ocptv.output.source.SourceLocation object>)
Emit an error artifact relevant for this test step.


* **Parameters**

    
    * **symptom** (`str`) – free-form description of the error symptom.


    * **message** (`Optional`[`str`]) – free-form message associated with this error.


    * **software_infos** (`Optional`[`List`[[`SoftwareInfo`](output.dut.md#ocptv.output.dut.SoftwareInfo)]]) – a list of SoftwareInfo references (as created
    in the DUT discovery process), that are relevant for this error. This can be used to specify
    a causal relationship between a software component and this error.


    * **source_location** (`Optional`[[`SourceLocation`](output.source.md#ocptv.output.source.SourceLocation)]) – source coordinates inside the diagnostic package
    where this artifact was produced. Default value `SourceLocation.CALLER` means that this
    function will automatically populate the spec field based on the caller frame.


For additional details on parameters, see:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#error](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#error)


#### add_extension(\*, name, content)
Emits a step extension artifact.
Extensions are meant to accommodate any aspects that are not standardized and may be vendor specific.


* **Parameters**

    
    * **name** (`str`) – identification of this specific extension artifact


    * **content** (`Any`) – any vendor specific content that can be serialized to JSON


For additional details on parameters, see:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#extension](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#extension)


#### add_file(\*, name, uri, is_snapshot=True, description=None, content_type=None, metadata=None)
Emit an artifact specifying a file resource produced in the diagnosis process.


* **Parameters**

    
    * **name** (`str`) – identifying name for this file.


    * **uri** (`str`) – a local/remote location specification for this file.


    * **bool** – specifies whether this file is a complete production or if it is a
    temporary snapshot as seen in the diagnosis process.


    * **description** (`Optional`[`str`]) – free-form description for this file resource.


    * **content_type** (`Optional`[`str`]) – MIME-type specification for this file contents.


    * **metadata** (`Optional`[[`Metadata`](output.objects.md#ocptv.output.objects.Metadata)]) – dictionary with unspecified metadata for this file.


For additional details on parameters, see:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#file](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#file)


#### add_log(severity, message, source_location=<ocptv.output.source.SourceLocation object>)
Emit a log entry artifact relevant for this test step.


* **Parameters**

    
    * **severity** ([`LogSeverity`](output.objects.md#ocptv.output.objects.LogSeverity)) – level of this log entry.
    See: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#severity](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#severity)


    * **message** (`str`) – free-form message for this log entry.


    * **source_location** (`Optional`[[`SourceLocation`](output.source.md#ocptv.output.source.SourceLocation)]) – source coordinates inside the diagnostic package
    where this artifact was produced. Default value `SourceLocation.CALLER` means that this
    function will automatically populate the spec field based on the caller frame.


For additional details on parameters, see:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#log](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#log)


#### add_measurement(\*, name, value, unit=None, validators=None, hardware_info=None, subcomponent=None, metadata=None)
Emit a single measurement artifact as taken by the test step.


* **Parameters**

    
    * **name** (`str`) – identification for this measurement item.


    * **value** (`Union`[`float`, `int`, `bool`, `str`]) – value of the taken measurement.


    * **unit** (`Optional`[`str`]) – free-form unit specification for this measurement.


    * **validator** – specifies how this measurement was validated in the
    test step by the diagnostic package.


    * **hardware_info** (`Optional`[[`HardwareInfo`](output.dut.md#ocptv.output.dut.HardwareInfo)]) – reference to the hardware component that this
    measurement was taken from or is relative to.


    * **subcomponent** (`Optional`[[`Subcomponent`](output.dut.md#ocptv.output.dut.Subcomponent)]) – reference to the hardware subcomponent (lower than FRU
    level) that this measurement was taken from or is relative to.


    * **metadata** (`Optional`[[`Metadata`](output.objects.md#ocptv.output.objects.Metadata)]) – dictionary with unspecified metadata for this measurement item.


For additional details on parameters, see:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#measurement](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#measurement)


#### end(\*, status)
Emit a test step end artifact.


* **Parameters**

    **status** ([`TestStatus`](output.objects.md#ocptv.output.objects.TestStatus)) – outcome status for this step.


For additional details on parameters, see:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#teststepend](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#teststepend)


#### scope()
Start a scoped test step.
Emits the test step start artifact and, at the end of the scope, emits the step end artifact.

The scope can also be exited sooner by raising the `TestStepError` error type.
If no such exception was raised, the test step will end with status COMPLETE.
Any other exceptions are not handled and will pass through.

Usage:

```python
step0 = run.add_step(name="step0")
with step0.scope():
    pass

step0 = run.add_step(name="step0")
with step0.scope():
    raise TestStepError(status=TestStatus.SKIP)
```


#### start()
Emit a test step start artifact.

Specification reference:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#teststepstart](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#teststepstart)


#### start_measurement_series(\*, name, unit=None, validators=None, hardware_info=None, subcomponent=None, metadata=None)
Start a new series of measurement and emit the series start artifact.


* **Parameters**

    
    * **name** (`str`) – identification for this measurement series.


    * **unit** (`Optional`[`str`]) – free-form unit specification for this measurement series.


    * **validator** – specifies how the measurement elements in this series
    will be validated in this test step by the diagnostic package.


    * **hardware_info** (`Optional`[[`HardwareInfo`](output.dut.md#ocptv.output.dut.HardwareInfo)]) – reference to the hardware component that this
    measurement series elements will be taken from or will be relative to.


    * **subcomponent** (`Optional`[[`Subcomponent`](output.dut.md#ocptv.output.dut.Subcomponent)]) – reference to the hardware subcomponent (lower than FRU
    level) that this measurement series elements will be taken from or will be relative to.


    * **metadata** (`Optional`[[`Metadata`](output.objects.md#ocptv.output.objects.Metadata)]) – dictionary with unspecified metadata for this measurement series.



* **Return type**

    [`MeasurementSeries`](output.measurement.md#ocptv.output.measurement.MeasurementSeries)


For additional details on parameters, see:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#measurementseriesstart](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#measurementseriesstart)
