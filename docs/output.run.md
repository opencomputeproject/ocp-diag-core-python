# ocptv.output.run module

This module describes the high level test run and related objects.


### _class_ ocptv.output.run.TestRun(name, version, \*, command_line=None, parameters=None)
The `TestRun` object is a stateful interface for the diagnostic run.
It presents various methods to interact with the run itself or to make child artifacts.

Usage:

```python
import ocptv.output as tv
run = tv.TestRun(name="test", version="1.0")
with run.scope(dut=ocptv.Dut(id="dut0")):
    pass
```

For other usages, see the the `examples` folder in the root of the project.

All the methods in this class are threadsafe.

Specification reference:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#test-run-artifacts](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#test-run-artifacts)

This type can be instantiated by user code directly.


#### \__init__(name, version, \*, command_line=None, parameters=None)
Make a new stateful test run model object.


* **Parameters**

    
    * **name** (`str`) – name of this test run/diagnostic package.


    * **version** (`str`) – version string for the test run/diagnostic package.


    * **command_line** (`Optional`[`str`]) – process command line that the diagnostic was started with.


    * **parameters** (`Optional`[`Dict`[`str`, `Union`[`str`, `int`]]]) – a flat dictionary of unspecified input parameters
    used in the diagnostic package.


Parameters that have a discovery process are left to be specified in
the `start()` or `scope()` calls.

For additional details on parameters, see:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#testrunstart](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#testrunstart)


#### add_error(\*, symptom, message=None, software_infos=None, source_location=<ocptv.output.source.SourceLocation object>)
Emit an error artifact relevant for this test run.


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


#### add_log(severity, message, source_location=<ocptv.output.source.SourceLocation object>)
Emit a log entry artifact relevant for this test run.


* **Parameters**

    
    * **severity** ([`LogSeverity`](output.objects.md#ocptv.output.objects.LogSeverity)) – level of this log entry.
    See: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#severity](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#severity)


    * **message** (`str`) – free-form message for this log entry.


    * **source_location** (`Optional`[[`SourceLocation`](output.source.md#ocptv.output.source.SourceLocation)]) – source coordinates inside the diagnostic package
    where this artifact was produced. Default value `SourceLocation.CALLER` means that this
    function will automatically populate the spec field based on the caller frame.


For additional details on parameters, see:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#log](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#log)


#### add_step(name)
Create a new test step for this test run.
The step is not started immediately, and should be used with the `start()` or `scope()` methods.


* **Parameters**

    **name** (`str`) – name of the step to create



* **Return type**

    [`TestStep`](output.step.md#ocptv.output.step.TestStep)



* **Returns**

    reference to a model of the test step


For additional details on parameters and step start, see:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#teststepstart](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#teststepstart)


#### end(\*, status, result)
Emit the test run end artifact.


* **Parameters**

    
    * **status** ([`TestStatus`](output.objects.md#ocptv.output.objects.TestStatus)) – outcome status for the diagnostic package as a whole.


    * **result** ([`TestResult`](output.objects.md#ocptv.output.objects.TestResult)) – determine whether the validation passed for this test run.


For additional details on parameters, see:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#testrunend](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#testrunend)


#### scope(\*, dut)
Start a scoped test run.
Emits the test run start artifact and, at the end of the scope, emits the run end artifact.

The scope can also be exited sooner by raising the `TestRunError` error type.
If no such exception was raised, the test run will end with status COMPLETE and result PASS.
Any other exceptions are not handled and will pass through.

Usage:

```python
import ocptv.output as tv
run = tv.TestRun(...)
with run.scope(dut=dut):
    pass

run = tv.TestRun(...)
with run.scope(dut=dut):
    raise TestRunError(status=TestStatus.SKIP, result=TestResult.NOT_APPLICABLE)
```


* **Parameters**

    **dut** ([`Dut`](output.dut.md#ocptv.output.dut.Dut)) – device-under-test information. See `start` method.



#### start(\*, dut)
Emit the test run start artifact.


* **Parameters**

    **dut** ([`Dut`](output.dut.md#ocptv.output.dut.Dut)) – device-under-test information. The DUT info is considered to have
    finished discovery at the point of starting a test run.


For additional details on parameters, see:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#testrunstart](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#testrunstart)


### _exception_ ocptv.output.run.TestRunError(\*, status, result)
The `TestRunError` can be raised with a context scope started by `TestRun.scope()`.
Any instance will be caught and handled by the context and will result in ending the
whole run with an error outcome.

This type can be instantiated by user code directly.


#### \__init__(\*, status, result)

* **Parameters**

    
    * **status** ([`TestStatus`](output.objects.md#ocptv.output.objects.TestStatus)) – outcome status for the diagnostic package as a whole.


    * **result** ([`TestResult`](output.objects.md#ocptv.output.objects.TestResult)) – determine whether the validation passed for this test run.
