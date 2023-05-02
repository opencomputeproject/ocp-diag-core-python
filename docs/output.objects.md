# ocptv.output.objects module

**WARNING**: The following document is not necessary for general usage of the library.

However, it may be of interest to users in order to get a better understanding of how the specification maps onto the code.

## Contents

Low level object models that are to be serialized as JSON.

NOT PUBLIC API, these are not intended to be used by client code
unless explicitly exported as public in `__init__.py`.

Developer notes:
A field can either have `metadata.spec_field` set or `field.SPEC_OBJECT` set, not both.
If `SPEC_OBJECT` is set, this field is an union type and serialization should take the
value in `SPEC_OBJECT` as the serialized field name. Otherwise, the `metadata.spec_field`
says what the serializer should use for field name.
In general, `metadata.spec_field` should only be present for primitive types.


### _class_ ocptv.output.objects.ArtifactType()
Bases: `object`

Protocol type to describe all low level serializable objects in this file.


### _class_ ocptv.output.objects.Diagnosis(verdict, type, message, hardware_info, subcomponent, source_location)
Bases: `object`

Low-level model for the diagnosis spec object.
Contains the verdict given by the diagnostic regarding the DUT that was inspected.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#diagnosis](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#diagnosis)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/diagnosis.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/diagnosis.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/diagnosis](https://github.com/opencomputeproject/ocp-diag-core/diagnosis)


#### SPEC_OBJECT(_: `ClassVar`[`str`_ _ = 'diagnosis_ )

#### hardware_info(_: `Optional`[`HardwareInfo`_ )

#### message(_: `Optional`[`str`_ )

#### source_location(_: `Optional`[`SourceLocation`_ )

#### subcomponent(_: `Optional`[`Subcomponent`_ )

#### type(_: `DiagnosisType_ )

#### verdict(_: `str_ )

### _class_ ocptv.output.objects.DiagnosisType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)
Bases: `Enum`

Outcome of a diagnosis operation.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#diagnosistype](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#diagnosistype)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/diagnosis.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/diagnosis.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/diagnosis/$defs/type](https://github.com/opencomputeproject/ocp-diag-core/diagnosis/$defs/type)


#### FAIL(_ = 'FAIL_ )

#### PASS(_ = 'PASS_ )

#### UNKNOWN(_ = 'UNKNOWN_ )

### _class_ ocptv.output.objects.DutInfo(id, name, platform_infos, software_infos, hardware_infos, metadata)
Bases: `object`

Low-level model for the dutInfo spec object.
Contains all relevant information describing the DUT.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#dutinfo](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#dutinfo)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/dut_info.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/dut_info.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/dutInfo](https://github.com/opencomputeproject/ocp-diag-core/dutInfo)


#### SPEC_OBJECT(_: `ClassVar`[`str`_ _ = 'dutInfo_ )

#### hardware_infos(_: `List`[`HardwareInfo`_ )

#### id(_: `str_ )

#### metadata(_: `Optional`[`Metadata`_ )

#### name(_: `Optional`[`str`_ )

#### platform_infos(_: `List`[`PlatformInfo`_ )

#### software_infos(_: `List`[`SoftwareInfo`_ )

### _class_ ocptv.output.objects.Error(symptom, message, software_infos, source_location)
Bases: `object`

Low-level model for the error spec object.
Represents an error encountered by the diagnostic software. It may refer to a DUT
component or the diagnostic itself.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#error](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#error)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/error.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/error.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/error](https://github.com/opencomputeproject/ocp-diag-core/error)


#### SPEC_OBJECT(_: `ClassVar`[`str`_ _ = 'error_ )

#### message(_: `Optional`[`str`_ )

#### software_infos(_: `List`[`SoftwareInfo`_ )

#### source_location(_: `Optional`[`SourceLocation`_ )

#### symptom(_: `str_ )

### _class_ ocptv.output.objects.Extension(name, content)
Bases: `object`

Low-level model for the extension spec object.
Left as an implementation detail, the Extension just has a name and arbitrary data.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#extension](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#extension)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/test_step_artifact.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/test_step_artifact.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/testStepArtifact/$defs/extension](https://github.com/opencomputeproject/ocp-diag-core/testStepArtifact/$defs/extension)


#### SPEC_OBJECT(_: `ClassVar`[`str`_ _ = 'extension_ )

#### content(_: `Any_ )

#### name(_: `str_ )

### _class_ ocptv.output.objects.File(name, uri, is_snapshot, description, content_type, metadata)
Bases: `object`

Low-level model for the file spec object.
Represents a file artifact that was generated by running the diagnostic.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#file](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#file)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/file.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/file.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/file](https://github.com/opencomputeproject/ocp-diag-core/file)


#### SPEC_OBJECT(_: `ClassVar`[`str`_ _ = 'file_ )

#### content_type(_: `Optional`[`str`_ )

#### description(_: `Optional`[`str`_ )

#### is_snapshot(_: `bool_ )

#### metadata(_: `Optional`[`Metadata`_ )

#### name(_: `str_ )

#### uri(_: `str_ )

### _class_ ocptv.output.objects.HardwareInfo(id, name, version, revision, location, serial_no, part_no, manufacturer, manufacturer_part_no, odata_id, computer_system, manager)
Bases: `object`

Low-level model for the hardwareInfo spec object.
Represents information of an enumerated or exercised hardware component of the DUT.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#hardwareinfo](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#hardwareinfo)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/dut_info.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/dut_info.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/dutInfo/$defs/hardwareInfo](https://github.com/opencomputeproject/ocp-diag-core/dutInfo/$defs/hardwareInfo)


#### SPEC_OBJECT(_: `ClassVar`[`str`_ _ = 'hardwareInfo_ )

#### computer_system(_: `Optional`[`str`_ )

#### id(_: `str_ )

#### location(_: `Optional`[`str`_ )

#### manager(_: `Optional`[`str`_ )

#### manufacturer(_: `Optional`[`str`_ )

#### manufacturer_part_no(_: `Optional`[`str`_ )

#### name(_: `str_ )

#### odata_id(_: `Optional`[`str`_ )

#### part_no(_: `Optional`[`str`_ )

#### revision(_: `Optional`[`str`_ )

#### serial_no(_: `Optional`[`str`_ )

#### version(_: `Optional`[`str`_ )

### _class_ ocptv.output.objects.Log(severity, message, source_location)
Bases: `object`

Low-level model for log spec object.
Is currently relevant for test run and test step artifact types.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#log](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#log)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/log.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/log.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/log](https://github.com/opencomputeproject/ocp-diag-core/log)


#### SPEC_OBJECT(_: `ClassVar`[`str`_ _ = 'log_ )

#### message(_: `str_ )

#### severity(_: `LogSeverity_ )

#### source_location(_: `Optional`[`SourceLocation`_ )

### _class_ ocptv.output.objects.LogSeverity(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)
Bases: `Enum`

Known log severity variants.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#severity](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#severity)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/log.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/log.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/log/$defs/severity](https://github.com/opencomputeproject/ocp-diag-core/log/$defs/severity)


#### DEBUG(_ = 'DEBUG_ )

#### ERROR(_ = 'ERROR_ )

#### FATAL(_ = 'FATAL_ )

#### INFO(_ = 'INFO_ )

#### WARNING(_ = 'WARNING_ )

### _class_ ocptv.output.objects.Measurement(name, value, unit, validators, hardware_info, subcomponent, metadata)
Bases: `object`

Low-level model for the measurement spec object.
Represents an individual measurement taken by the diagnostic regarding the DUT.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#measurement](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#measurement)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/measurement.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/measurement.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/measurement](https://github.com/opencomputeproject/ocp-diag-core/measurement)


#### SPEC_OBJECT(_: `ClassVar`[`str`_ _ = 'measurement_ )

#### hardware_info(_: `Optional`[`HardwareInfo`_ )

#### metadata(_: `Optional`[`Metadata`_ )

#### name(_: `str_ )

#### subcomponent(_: `Optional`[`Subcomponent`_ )

#### unit(_: `Optional`[`str`_ )

#### validators(_: `List`[`Validator`_ )

#### value(_: `Union`[`float`, `int`, `bool`, `str`_ )

### _class_ ocptv.output.objects.MeasurementSeriesElement(index, value, timestamp, series_id, metadata)
Bases: `object`

Low-level model for the measurementSeriesElement spec object.
Equivalent to the Measurement model but inside a time based series.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#measurementserieselement](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#measurementserieselement)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/measurement_series_element.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/measurement_series_element.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/measurementSeriesElement](https://github.com/opencomputeproject/ocp-diag-core/measurementSeriesElement)


#### SPEC_OBJECT(_: `ClassVar`[`str`_ _ = 'measurementSeriesElement_ )

#### index(_: `int_ )

#### metadata(_: `Optional`[`Metadata`_ )

#### series_id(_: `str_ )

#### timestamp(_: `float_ )

#### value(_: `Union`[`float`, `int`, `bool`, `str`_ )

### _class_ ocptv.output.objects.MeasurementSeriesEnd(series_id, total_count)
Bases: `object`

Low-level model for the measurementSeriesEnd spec object.
End marker for a time based series of measurements.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#measurementseriesend](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#measurementseriesend)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/measurement_series_end.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/measurement_series_end.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/measurementSeriesEnd](https://github.com/opencomputeproject/ocp-diag-core/measurementSeriesEnd)


#### SPEC_OBJECT(_: `ClassVar`[`str`_ _ = 'measurementSeriesEnd_ )

#### series_id(_: `str_ )

#### total_count(_: `int_ )

### _class_ ocptv.output.objects.MeasurementSeriesStart(name, unit, series_id, validators, hardware_info, subcomponent, metadata)
Bases: `object`

Low-level model for the measurementSeriesStart spec object.
Start marker for a time based series of measurements.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#measurementseriesstart](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#measurementseriesstart)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/measurement_series_start.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/measurement_series_start.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/measurementSeriesStart](https://github.com/opencomputeproject/ocp-diag-core/measurementSeriesStart)


#### SPEC_OBJECT(_: `ClassVar`[`str`_ _ = 'measurementSeriesStart_ )

#### hardware_info(_: `Optional`[`HardwareInfo`_ )

#### metadata(_: `Optional`[`Metadata`_ )

#### name(_: `str_ )

#### series_id(_: `str_ )

#### subcomponent(_: `Optional`[`Subcomponent`_ )

#### unit(_: `Optional`[`str`_ )

#### validators(_: `List`[`Validator`_ )

### _class_ ocptv.output.objects.Metadata()
Bases: `dict`

Metadata container to accomodate any arbitrary keyed data put into it.
For JSON output to work best, keys should be valid strings.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#metadata](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#metadata)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/metadata.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/metadata.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/metadata](https://github.com/opencomputeproject/ocp-diag-core/metadata)

This type can be instantiated by user code directly.


#### SPEC_OBJECT(_: `ClassVar`[`str`_ _ = 'metadata_ )

### _class_ ocptv.output.objects.OCPVersion(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)
Bases: `Enum`

OCP Test & Validation spec version consts.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#schemaversion](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#schemaversion)
schema: [https://github.com/opencomputeproject/ocp-diag-core/output/$defs/schemaVersion](https://github.com/opencomputeproject/ocp-diag-core/output/$defs/schemaVersion)


#### VERSION_2_0(_ = (2, 0_ )

### _class_ ocptv.output.objects.PlatformInfo(info)
Bases: `object`

Low-level model for the platformInfo spec object.
Describe platform specific attributes of the DUT.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#platforminfo](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#platforminfo)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/dut_info.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/dut_info.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/dutInfo/$defs/platformInfo](https://github.com/opencomputeproject/ocp-diag-core/dutInfo/$defs/platformInfo)


#### SPEC_OBJECT(_: `ClassVar`[`str`_ _ = 'platformInfo_ )

#### info(_: `str_ )

### _class_ ocptv.output.objects.Root(impl, sequence_number, timestamp)
Bases: `object`

Low-level model for the root json node.
Container for the root level artifacts.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#outputartifacts](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#outputartifacts)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/root.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/root.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/output](https://github.com/opencomputeproject/ocp-diag-core/output)


#### impl(_: `Union`[`SchemaVersion`, `RunArtifact`, `StepArtifact`_ )

#### sequence_number(_: `int_ )

#### timestamp(_: `float_ )

### _class_ ocptv.output.objects.RunArtifact(impl)
Bases: `object`

Low-level model for the testRunArtifact spec object.
Container for the run level artifacts.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#test-run-artifacts](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#test-run-artifacts)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/test_run_artifact.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/test_run_artifact.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/testRunArtifact](https://github.com/opencomputeproject/ocp-diag-core/testRunArtifact)


#### SPEC_OBJECT(_: `ClassVar`[`str`_ _ = 'testRunArtifact_ )

#### impl(_: `Union`[`RunStart`, `RunEnd`, `Log`, `Error`_ )

### _class_ ocptv.output.objects.RunEnd(status, result)
Bases: `object`

Low-level model for the testRunEnd spec object.
End marker signaling the finality of a diagnostic test.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#testrunend](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#testrunend)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/test_run_end.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/test_run_end.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/testRunEnd](https://github.com/opencomputeproject/ocp-diag-core/testRunEnd)


#### SPEC_OBJECT(_: `ClassVar`[`str`_ _ = 'testRunEnd_ )

#### result(_: `TestResult_ )

#### status(_: `TestStatus_ )

### _class_ ocptv.output.objects.RunStart(name, version, command_line, parameters, dut_info)
Bases: `object`

Low-level model for the testRunStart spec object.
Start marker for the beginning of a diagnostic test.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#testrunstart](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#testrunstart)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/test_run_start.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/test_run_start.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/testRunStart](https://github.com/opencomputeproject/ocp-diag-core/testRunStart)


#### SPEC_OBJECT(_: `ClassVar`[`str`_ _ = 'testRunStart_ )

#### command_line(_: `str_ )

#### dut_info(_: `DutInfo_ )

#### name(_: `str_ )

#### parameters(_: `Dict`[`str`, `Any`_ )

#### version(_: `str_ )

### _class_ ocptv.output.objects.SchemaVersion(major=2, minor=0)
Bases: `object`

Low-level model for the schemaVersion spec object.
Specifies the version that should be used to interpret following json outputs.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#schemaversion](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#schemaversion)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/root.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/root.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/output/$defs/schemaVersion](https://github.com/opencomputeproject/ocp-diag-core/output/$defs/schemaVersion)


#### SPEC_OBJECT(_: `ClassVar`[`str`_ _ = 'schemaVersion_ )

#### major(_: `int_ _ = _ )

#### minor(_: `int_ _ = _ )

### _class_ ocptv.output.objects.SoftwareInfo(id, name, version, revision, type, computer_system)
Bases: `object`

Low-level model for the softwareInfo spec object.
Represents information of a discovered or exercised software component of the DUT.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#softwareinfo](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#softwareinfo)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/dut_info.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/dut_info.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/dutInfo/$defs/softwareInfo](https://github.com/opencomputeproject/ocp-diag-core/dutInfo/$defs/softwareInfo)


#### SPEC_OBJECT(_: `ClassVar`[`str`_ _ = 'softwareInfo_ )

#### computer_system(_: `Optional`[`str`_ )

#### id(_: `str_ )

#### name(_: `str_ )

#### revision(_: `Optional`[`str`_ )

#### type(_: `Optional`[`SoftwareType`_ )

#### version(_: `Optional`[`str`_ )

### _class_ ocptv.output.objects.SoftwareType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)
Bases: `Enum`

Type specification for a software component of the DUT.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#softwaretype](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#softwaretype)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/dut_info.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/dut_info.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/dutInfo/$defs/softwareInfo/properties/softwareType](https://github.com/opencomputeproject/ocp-diag-core/dutInfo/$defs/softwareInfo/properties/softwareType)


#### APPLICATION(_ = 'APPLICATION_ )

#### FIRMWARE(_ = 'FIRMWARE_ )

#### SYSTEM(_ = 'SYSTEM_ )

#### UNSPECIFIED(_ = 'UNSPECIFIED_ )

### _class_ ocptv.output.objects.SourceLocation(file, line)
Bases: `object`

Provides information about which file/line of the source code in
the diagnostic package generated the output.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#sourcelocation](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#sourcelocation)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/source_location.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/source_location.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/sourceLocation](https://github.com/opencomputeproject/ocp-diag-core/sourceLocation)


#### SPEC_OBJECT(_: `ClassVar`[`str`_ _ = 'sourceLocation_ )

#### file(_: `str_ )

#### line(_: `int_ )

### _class_ ocptv.output.objects.StepArtifact(id, impl)
Bases: `object`

Low-level model for the testStepArtifact spec object.
Container for the step level artifacts.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#test-step-artifacts](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#test-step-artifacts)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/test_step_artifact.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/test_step_artifact.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/testStepArtifact](https://github.com/opencomputeproject/ocp-diag-core/testStepArtifact)


#### SPEC_OBJECT(_: `ClassVar`[`str`_ _ = 'testStepArtifact_ )

#### id(_: `str_ )

#### impl(_: `Union`[`StepStart`, `StepEnd`, `Measurement`, `MeasurementSeriesStart`, `MeasurementSeriesEnd`, `MeasurementSeriesElement`, `Diagnosis`, `Log`, `Error`, `File`, `Extension`_ )

### _class_ ocptv.output.objects.StepEnd(status)
Bases: `object`

Low-level model for the testStepEnd spec object.
End marker for a test step inside a diagnosis run.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#teststepend](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#teststepend)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/test_step_end.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/test_step_end.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/testStepEnd](https://github.com/opencomputeproject/ocp-diag-core/testStepEnd)


#### SPEC_OBJECT(_: `ClassVar`[`str`_ _ = 'testStepEnd_ )

#### status(_: `TestStatus_ )

### _class_ ocptv.output.objects.StepStart(name)
Bases: `object`

Low-level model for the testStepStart spec object.
Start marker for a test step inside a diagnosis run.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#teststepstart](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#teststepstart)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/test_step_start.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/test_step_start.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/testStepStart](https://github.com/opencomputeproject/ocp-diag-core/testStepStart)


#### SPEC_OBJECT(_: `ClassVar`[`str`_ _ = 'testStepStart_ )

#### name(_: `str_ )

### _class_ ocptv.output.objects.Subcomponent(type, name, location, version, revision)
Bases: `object`

Low-level model for the subcomponent spec object.
Represents a physical subcomponent of a DUT hardware element.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#subcomponent](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#subcomponent)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/subcomponent.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/subcomponent.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/subcomponent](https://github.com/opencomputeproject/ocp-diag-core/subcomponent)


#### SPEC_OBJECT(_: `ClassVar`[`str`_ _ = 'subcomponent_ )

#### location(_: `Optional`[`str`_ )

#### name(_: `str_ )

#### revision(_: `Optional`[`str`_ )

#### type(_: `Optional`[`SubcomponentType`_ )

#### version(_: `Optional`[`str`_ )

### _class_ ocptv.output.objects.SubcomponentType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)
Bases: `Enum`

Type specification variants for DUT physical subcomponents.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#subcomponenttype](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#subcomponenttype)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/subcomponent.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/subcomponent.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/subcomponent/$defs/type](https://github.com/opencomputeproject/ocp-diag-core/subcomponent/$defs/type)


#### ASIC(_ = 'ASIC_ )

#### ASIC_SUBSYSTEM(_ = 'ASIC-SUBSYSTEM_ )

#### BUS(_ = 'BUS_ )

#### CONNECTOR(_ = 'CONNECTOR_ )

#### FUNCTION(_ = 'FUNCTION_ )

#### UNSPECIFIED(_ = 'UNSPECIFIED_ )

### _class_ ocptv.output.objects.TestResult(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)
Bases: `Enum`

Represents the final outcome of a test execution.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#testresult](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#testresult)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/test_run_end.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/test_run_end.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/testRunEnd/$defs/testResult](https://github.com/opencomputeproject/ocp-diag-core/testRunEnd/$defs/testResult)


#### FAIL(_ = 'FAIL_ )

#### NOT_APPLICABLE(_ = 'NOT_APPLICABLE_ )

#### PASS(_ = 'PASS_ )

### _class_ ocptv.output.objects.TestStatus(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)
Bases: `Enum`

Represents the final execution status of a test.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#teststatus](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#teststatus)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/test_status.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/test_status.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/testStatus](https://github.com/opencomputeproject/ocp-diag-core/testStatus)


#### COMPLETE(_ = 'COMPLETE_ )

#### ERROR(_ = 'ERROR_ )

#### SKIP(_ = 'SKIP_ )

### _class_ ocptv.output.objects.Validator(name, type, value, metadata)
Bases: `object`

Low-level model for the validator spec object.
Contains the validation logic that the diagnostic applied for a specific measurement.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#validator](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#validator)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/validator.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/validator.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/validator](https://github.com/opencomputeproject/ocp-diag-core/validator)


#### SPEC_OBJECT(_: `ClassVar`[`str`_ _ = 'validator_ )

#### metadata(_: `Optional`[`Metadata`_ )

#### name(_: `Optional`[`str`_ )

#### type(_: `ValidatorType_ )

#### value(_: `Union`[`List`[`float`], `List`[`int`], `List`[`bool`], `List`[`str`], `float`, `int`, `bool`, `str`_ )

### _class_ ocptv.output.objects.ValidatorType(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)
Bases: `Enum`

Type specification for a measurement or series element validator logic.

ref: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#validator](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#validator)
schema url: [https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/validator.json](https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/validator.json)
schema ref: [https://github.com/opencomputeproject/ocp-diag-core/validator/$defs/type](https://github.com/opencomputeproject/ocp-diag-core/validator/$defs/type)


#### EQUAL(_ = 'EQUAL_ )

#### GREATER_THAN(_ = 'GREATER_THAN_ )

#### GREATER_THAN_OR_EQUAL(_ = 'GREATER_THAN_OR_EQUAL_ )

#### IN_SET(_ = 'IN_SET_ )

#### LESS_THAN(_ = 'LESS_THAN_ )

#### LESS_THAN_OR_EQUAL(_ = 'LESS_THAN_OR_EQUAL_ )

#### NOT_EQUAL(_ = 'NOT_EQUAL_ )

#### NOT_IN_SET(_ = 'NOT_IN_SET_ )

#### REGEX_MATCH(_ = 'REGEX_MATCH_ )

#### REGEX_NO_MATCH(_ = 'REGEX_NO_MATCH_ )

### ocptv.output.objects.format_hardware_info(obj)

* **Return type**

    `str`



### ocptv.output.objects.format_timestamp_with_tzinfo(ts)
Curry form with timezone from config


* **Return type**

    `str`
