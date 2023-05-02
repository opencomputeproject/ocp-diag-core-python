# ocptv.output package

# Contents:


* [ocptv.output.config module](output.config.md)


    * [`StdoutWriter`](output.config.md#ocptv.output.config.StdoutWriter)


    * [`Writer`](output.config.md#ocptv.output.config.Writer)


    * [`config()`](output.config.md#ocptv.output.config.config)


* [ocptv.output.run module](output.run.md)


    * [`TestRun`](output.run.md#ocptv.output.run.TestRun)


        * [`TestRun.__init__()`](output.run.md#ocptv.output.run.TestRun.__init__)


        * [`TestRun.add_error()`](output.run.md#ocptv.output.run.TestRun.add_error)


        * [`TestRun.add_log()`](output.run.md#ocptv.output.run.TestRun.add_log)


        * [`TestRun.add_step()`](output.run.md#ocptv.output.run.TestRun.add_step)


        * [`TestRun.end()`](output.run.md#ocptv.output.run.TestRun.end)


        * [`TestRun.scope()`](output.run.md#ocptv.output.run.TestRun.scope)


        * [`TestRun.start()`](output.run.md#ocptv.output.run.TestRun.start)


    * [`TestRunError`](output.run.md#ocptv.output.run.TestRunError)


        * [`TestRunError.__init__()`](output.run.md#ocptv.output.run.TestRunError.__init__)


* [ocptv.output.step module](output.step.md)


    * [`TestStepError`](output.step.md#ocptv.output.step.TestStepError)


        * [`TestStepError.__init__()`](output.step.md#ocptv.output.step.TestStepError.__init__)


    * [`TestStep`](output.step.md#ocptv.output.step.TestStep)


        * [`TestStep.add_diagnosis()`](output.step.md#ocptv.output.step.TestStep.add_diagnosis)


        * [`TestStep.add_error()`](output.step.md#ocptv.output.step.TestStep.add_error)


        * [`TestStep.add_extension()`](output.step.md#ocptv.output.step.TestStep.add_extension)


        * [`TestStep.add_file()`](output.step.md#ocptv.output.step.TestStep.add_file)


        * [`TestStep.add_log()`](output.step.md#ocptv.output.step.TestStep.add_log)


        * [`TestStep.add_measurement()`](output.step.md#ocptv.output.step.TestStep.add_measurement)


        * [`TestStep.end()`](output.step.md#ocptv.output.step.TestStep.end)


        * [`TestStep.scope()`](output.step.md#ocptv.output.step.TestStep.scope)


        * [`TestStep.start()`](output.step.md#ocptv.output.step.TestStep.start)


        * [`TestStep.start_measurement_series()`](output.step.md#ocptv.output.step.TestStep.start_measurement_series)


* [ocptv.output.dut module](output.dut.md)


    * [`Dut`](output.dut.md#ocptv.output.dut.Dut)


        * [`Dut.__init__()`](output.dut.md#ocptv.output.dut.Dut.__init__)


        * [`Dut.add_hardware_info()`](output.dut.md#ocptv.output.dut.Dut.add_hardware_info)


        * [`Dut.add_platform_info()`](output.dut.md#ocptv.output.dut.Dut.add_platform_info)


        * [`Dut.add_software_info()`](output.dut.md#ocptv.output.dut.Dut.add_software_info)


    * [`HardwareInfo`](output.dut.md#ocptv.output.dut.HardwareInfo)


        * [`HardwareInfo.__init__()`](output.dut.md#ocptv.output.dut.HardwareInfo.__init__)


    * [`PlatformInfo`](output.dut.md#ocptv.output.dut.PlatformInfo)


        * [`PlatformInfo.__init__()`](output.dut.md#ocptv.output.dut.PlatformInfo.__init__)


    * [`SoftwareInfo`](output.dut.md#ocptv.output.dut.SoftwareInfo)


        * [`SoftwareInfo.__init__()`](output.dut.md#ocptv.output.dut.SoftwareInfo.__init__)


    * [`Subcomponent`](output.dut.md#ocptv.output.dut.Subcomponent)


        * [`Subcomponent.__init__()`](output.dut.md#ocptv.output.dut.Subcomponent.__init__)


* [ocptv.output.measurement module](output.measurement.md)


    * [`Validator`](output.measurement.md#ocptv.output.measurement.Validator)


        * [`Validator.__init__()`](output.measurement.md#ocptv.output.measurement.Validator.__init__)


    * [`MeasurementSeries`](output.measurement.md#ocptv.output.measurement.MeasurementSeries)


        * [`MeasurementSeries.add_measurement()`](output.measurement.md#ocptv.output.measurement.MeasurementSeries.add_measurement)


        * [`MeasurementSeries.end()`](output.measurement.md#ocptv.output.measurement.MeasurementSeries.end)


        * [`MeasurementSeries.scope()`](output.measurement.md#ocptv.output.measurement.MeasurementSeries.scope)


* [ocptv.output.source module](output.source.md)


    * [`SourceLocation`](output.source.md#ocptv.output.source.SourceLocation)


        * [`SourceLocation.__init__()`](output.source.md#ocptv.output.source.SourceLocation.__init__)


    * [`NullSourceLocation`](output.source.md#ocptv.output.source.NullSourceLocation)


* [ocptv.output.objects module](output.objects.md)


    * [Contents](output.objects.md#module-ocptv.output.objects)


        * [`ArtifactType`](output.objects.md#ocptv.output.objects.ArtifactType)


        * [`Diagnosis`](output.objects.md#ocptv.output.objects.Diagnosis)


            * [`Diagnosis.SPEC_OBJECT`](output.objects.md#ocptv.output.objects.Diagnosis.SPEC_OBJECT)


            * [`Diagnosis.hardware_info`](output.objects.md#ocptv.output.objects.Diagnosis.hardware_info)


            * [`Diagnosis.message`](output.objects.md#ocptv.output.objects.Diagnosis.message)


            * [`Diagnosis.source_location`](output.objects.md#ocptv.output.objects.Diagnosis.source_location)


            * [`Diagnosis.subcomponent`](output.objects.md#ocptv.output.objects.Diagnosis.subcomponent)


            * [`Diagnosis.type`](output.objects.md#ocptv.output.objects.Diagnosis.type)


            * [`Diagnosis.verdict`](output.objects.md#ocptv.output.objects.Diagnosis.verdict)


        * [`DiagnosisType`](output.objects.md#ocptv.output.objects.DiagnosisType)


            * [`DiagnosisType.FAIL`](output.objects.md#ocptv.output.objects.DiagnosisType.FAIL)


            * [`DiagnosisType.PASS`](output.objects.md#ocptv.output.objects.DiagnosisType.PASS)


            * [`DiagnosisType.UNKNOWN`](output.objects.md#ocptv.output.objects.DiagnosisType.UNKNOWN)


        * [`DutInfo`](output.objects.md#ocptv.output.objects.DutInfo)


            * [`DutInfo.SPEC_OBJECT`](output.objects.md#ocptv.output.objects.DutInfo.SPEC_OBJECT)


            * [`DutInfo.hardware_infos`](output.objects.md#ocptv.output.objects.DutInfo.hardware_infos)


            * [`DutInfo.id`](output.objects.md#ocptv.output.objects.DutInfo.id)


            * [`DutInfo.metadata`](output.objects.md#ocptv.output.objects.DutInfo.metadata)


            * [`DutInfo.name`](output.objects.md#ocptv.output.objects.DutInfo.name)


            * [`DutInfo.platform_infos`](output.objects.md#ocptv.output.objects.DutInfo.platform_infos)


            * [`DutInfo.software_infos`](output.objects.md#ocptv.output.objects.DutInfo.software_infos)


        * [`Error`](output.objects.md#ocptv.output.objects.Error)


            * [`Error.SPEC_OBJECT`](output.objects.md#ocptv.output.objects.Error.SPEC_OBJECT)


            * [`Error.message`](output.objects.md#ocptv.output.objects.Error.message)


            * [`Error.software_infos`](output.objects.md#ocptv.output.objects.Error.software_infos)


            * [`Error.source_location`](output.objects.md#ocptv.output.objects.Error.source_location)


            * [`Error.symptom`](output.objects.md#ocptv.output.objects.Error.symptom)


        * [`Extension`](output.objects.md#ocptv.output.objects.Extension)


            * [`Extension.SPEC_OBJECT`](output.objects.md#ocptv.output.objects.Extension.SPEC_OBJECT)


            * [`Extension.content`](output.objects.md#ocptv.output.objects.Extension.content)


            * [`Extension.name`](output.objects.md#ocptv.output.objects.Extension.name)


        * [`File`](output.objects.md#ocptv.output.objects.File)


            * [`File.SPEC_OBJECT`](output.objects.md#ocptv.output.objects.File.SPEC_OBJECT)


            * [`File.content_type`](output.objects.md#ocptv.output.objects.File.content_type)


            * [`File.description`](output.objects.md#ocptv.output.objects.File.description)


            * [`File.is_snapshot`](output.objects.md#ocptv.output.objects.File.is_snapshot)


            * [`File.metadata`](output.objects.md#ocptv.output.objects.File.metadata)


            * [`File.name`](output.objects.md#ocptv.output.objects.File.name)


            * [`File.uri`](output.objects.md#ocptv.output.objects.File.uri)


        * [`HardwareInfo`](output.objects.md#ocptv.output.objects.HardwareInfo)


            * [`HardwareInfo.SPEC_OBJECT`](output.objects.md#ocptv.output.objects.HardwareInfo.SPEC_OBJECT)


            * [`HardwareInfo.computer_system`](output.objects.md#ocptv.output.objects.HardwareInfo.computer_system)


            * [`HardwareInfo.id`](output.objects.md#ocptv.output.objects.HardwareInfo.id)


            * [`HardwareInfo.location`](output.objects.md#ocptv.output.objects.HardwareInfo.location)


            * [`HardwareInfo.manager`](output.objects.md#ocptv.output.objects.HardwareInfo.manager)


            * [`HardwareInfo.manufacturer`](output.objects.md#ocptv.output.objects.HardwareInfo.manufacturer)


            * [`HardwareInfo.manufacturer_part_no`](output.objects.md#ocptv.output.objects.HardwareInfo.manufacturer_part_no)


            * [`HardwareInfo.name`](output.objects.md#ocptv.output.objects.HardwareInfo.name)


            * [`HardwareInfo.odata_id`](output.objects.md#ocptv.output.objects.HardwareInfo.odata_id)


            * [`HardwareInfo.part_no`](output.objects.md#ocptv.output.objects.HardwareInfo.part_no)


            * [`HardwareInfo.revision`](output.objects.md#ocptv.output.objects.HardwareInfo.revision)


            * [`HardwareInfo.serial_no`](output.objects.md#ocptv.output.objects.HardwareInfo.serial_no)


            * [`HardwareInfo.version`](output.objects.md#ocptv.output.objects.HardwareInfo.version)


        * [`Log`](output.objects.md#ocptv.output.objects.Log)


            * [`Log.SPEC_OBJECT`](output.objects.md#ocptv.output.objects.Log.SPEC_OBJECT)


            * [`Log.message`](output.objects.md#ocptv.output.objects.Log.message)


            * [`Log.severity`](output.objects.md#ocptv.output.objects.Log.severity)


            * [`Log.source_location`](output.objects.md#ocptv.output.objects.Log.source_location)


        * [`LogSeverity`](output.objects.md#ocptv.output.objects.LogSeverity)


            * [`LogSeverity.DEBUG`](output.objects.md#ocptv.output.objects.LogSeverity.DEBUG)


            * [`LogSeverity.ERROR`](output.objects.md#ocptv.output.objects.LogSeverity.ERROR)


            * [`LogSeverity.FATAL`](output.objects.md#ocptv.output.objects.LogSeverity.FATAL)


            * [`LogSeverity.INFO`](output.objects.md#ocptv.output.objects.LogSeverity.INFO)


            * [`LogSeverity.WARNING`](output.objects.md#ocptv.output.objects.LogSeverity.WARNING)


        * [`Measurement`](output.objects.md#ocptv.output.objects.Measurement)


            * [`Measurement.SPEC_OBJECT`](output.objects.md#ocptv.output.objects.Measurement.SPEC_OBJECT)


            * [`Measurement.hardware_info`](output.objects.md#ocptv.output.objects.Measurement.hardware_info)


            * [`Measurement.metadata`](output.objects.md#ocptv.output.objects.Measurement.metadata)


            * [`Measurement.name`](output.objects.md#ocptv.output.objects.Measurement.name)


            * [`Measurement.subcomponent`](output.objects.md#ocptv.output.objects.Measurement.subcomponent)


            * [`Measurement.unit`](output.objects.md#ocptv.output.objects.Measurement.unit)


            * [`Measurement.validators`](output.objects.md#ocptv.output.objects.Measurement.validators)


            * [`Measurement.value`](output.objects.md#ocptv.output.objects.Measurement.value)


        * [`MeasurementSeriesElement`](output.objects.md#ocptv.output.objects.MeasurementSeriesElement)


            * [`MeasurementSeriesElement.SPEC_OBJECT`](output.objects.md#ocptv.output.objects.MeasurementSeriesElement.SPEC_OBJECT)


            * [`MeasurementSeriesElement.index`](output.objects.md#ocptv.output.objects.MeasurementSeriesElement.index)


            * [`MeasurementSeriesElement.metadata`](output.objects.md#ocptv.output.objects.MeasurementSeriesElement.metadata)


            * [`MeasurementSeriesElement.series_id`](output.objects.md#ocptv.output.objects.MeasurementSeriesElement.series_id)


            * [`MeasurementSeriesElement.timestamp`](output.objects.md#ocptv.output.objects.MeasurementSeriesElement.timestamp)


            * [`MeasurementSeriesElement.value`](output.objects.md#ocptv.output.objects.MeasurementSeriesElement.value)


        * [`MeasurementSeriesEnd`](output.objects.md#ocptv.output.objects.MeasurementSeriesEnd)


            * [`MeasurementSeriesEnd.SPEC_OBJECT`](output.objects.md#ocptv.output.objects.MeasurementSeriesEnd.SPEC_OBJECT)


            * [`MeasurementSeriesEnd.series_id`](output.objects.md#ocptv.output.objects.MeasurementSeriesEnd.series_id)


            * [`MeasurementSeriesEnd.total_count`](output.objects.md#ocptv.output.objects.MeasurementSeriesEnd.total_count)


        * [`MeasurementSeriesStart`](output.objects.md#ocptv.output.objects.MeasurementSeriesStart)


            * [`MeasurementSeriesStart.SPEC_OBJECT`](output.objects.md#ocptv.output.objects.MeasurementSeriesStart.SPEC_OBJECT)


            * [`MeasurementSeriesStart.hardware_info`](output.objects.md#ocptv.output.objects.MeasurementSeriesStart.hardware_info)


            * [`MeasurementSeriesStart.metadata`](output.objects.md#ocptv.output.objects.MeasurementSeriesStart.metadata)


            * [`MeasurementSeriesStart.name`](output.objects.md#ocptv.output.objects.MeasurementSeriesStart.name)


            * [`MeasurementSeriesStart.series_id`](output.objects.md#ocptv.output.objects.MeasurementSeriesStart.series_id)


            * [`MeasurementSeriesStart.subcomponent`](output.objects.md#ocptv.output.objects.MeasurementSeriesStart.subcomponent)


            * [`MeasurementSeriesStart.unit`](output.objects.md#ocptv.output.objects.MeasurementSeriesStart.unit)


            * [`MeasurementSeriesStart.validators`](output.objects.md#ocptv.output.objects.MeasurementSeriesStart.validators)


        * [`Metadata`](output.objects.md#ocptv.output.objects.Metadata)


            * [`Metadata.SPEC_OBJECT`](output.objects.md#ocptv.output.objects.Metadata.SPEC_OBJECT)


        * [`OCPVersion`](output.objects.md#ocptv.output.objects.OCPVersion)


            * [`OCPVersion.VERSION_2_0`](output.objects.md#ocptv.output.objects.OCPVersion.VERSION_2_0)


        * [`PlatformInfo`](output.objects.md#ocptv.output.objects.PlatformInfo)


            * [`PlatformInfo.SPEC_OBJECT`](output.objects.md#ocptv.output.objects.PlatformInfo.SPEC_OBJECT)


            * [`PlatformInfo.info`](output.objects.md#ocptv.output.objects.PlatformInfo.info)


        * [`Root`](output.objects.md#ocptv.output.objects.Root)


            * [`Root.impl`](output.objects.md#ocptv.output.objects.Root.impl)


            * [`Root.sequence_number`](output.objects.md#ocptv.output.objects.Root.sequence_number)


            * [`Root.timestamp`](output.objects.md#ocptv.output.objects.Root.timestamp)


        * [`RunArtifact`](output.objects.md#ocptv.output.objects.RunArtifact)


            * [`RunArtifact.SPEC_OBJECT`](output.objects.md#ocptv.output.objects.RunArtifact.SPEC_OBJECT)


            * [`RunArtifact.impl`](output.objects.md#ocptv.output.objects.RunArtifact.impl)


        * [`RunEnd`](output.objects.md#ocptv.output.objects.RunEnd)


            * [`RunEnd.SPEC_OBJECT`](output.objects.md#ocptv.output.objects.RunEnd.SPEC_OBJECT)


            * [`RunEnd.result`](output.objects.md#ocptv.output.objects.RunEnd.result)


            * [`RunEnd.status`](output.objects.md#ocptv.output.objects.RunEnd.status)


        * [`RunStart`](output.objects.md#ocptv.output.objects.RunStart)


            * [`RunStart.SPEC_OBJECT`](output.objects.md#ocptv.output.objects.RunStart.SPEC_OBJECT)


            * [`RunStart.command_line`](output.objects.md#ocptv.output.objects.RunStart.command_line)


            * [`RunStart.dut_info`](output.objects.md#ocptv.output.objects.RunStart.dut_info)


            * [`RunStart.name`](output.objects.md#ocptv.output.objects.RunStart.name)


            * [`RunStart.parameters`](output.objects.md#ocptv.output.objects.RunStart.parameters)


            * [`RunStart.version`](output.objects.md#ocptv.output.objects.RunStart.version)


        * [`SchemaVersion`](output.objects.md#ocptv.output.objects.SchemaVersion)


            * [`SchemaVersion.SPEC_OBJECT`](output.objects.md#ocptv.output.objects.SchemaVersion.SPEC_OBJECT)


            * [`SchemaVersion.major`](output.objects.md#ocptv.output.objects.SchemaVersion.major)


            * [`SchemaVersion.minor`](output.objects.md#ocptv.output.objects.SchemaVersion.minor)


        * [`SoftwareInfo`](output.objects.md#ocptv.output.objects.SoftwareInfo)


            * [`SoftwareInfo.SPEC_OBJECT`](output.objects.md#ocptv.output.objects.SoftwareInfo.SPEC_OBJECT)


            * [`SoftwareInfo.computer_system`](output.objects.md#ocptv.output.objects.SoftwareInfo.computer_system)


            * [`SoftwareInfo.id`](output.objects.md#ocptv.output.objects.SoftwareInfo.id)


            * [`SoftwareInfo.name`](output.objects.md#ocptv.output.objects.SoftwareInfo.name)


            * [`SoftwareInfo.revision`](output.objects.md#ocptv.output.objects.SoftwareInfo.revision)


            * [`SoftwareInfo.type`](output.objects.md#ocptv.output.objects.SoftwareInfo.type)


            * [`SoftwareInfo.version`](output.objects.md#ocptv.output.objects.SoftwareInfo.version)


        * [`SoftwareType`](output.objects.md#ocptv.output.objects.SoftwareType)


            * [`SoftwareType.APPLICATION`](output.objects.md#ocptv.output.objects.SoftwareType.APPLICATION)


            * [`SoftwareType.FIRMWARE`](output.objects.md#ocptv.output.objects.SoftwareType.FIRMWARE)


            * [`SoftwareType.SYSTEM`](output.objects.md#ocptv.output.objects.SoftwareType.SYSTEM)


            * [`SoftwareType.UNSPECIFIED`](output.objects.md#ocptv.output.objects.SoftwareType.UNSPECIFIED)


        * [`SourceLocation`](output.objects.md#ocptv.output.objects.SourceLocation)


            * [`SourceLocation.SPEC_OBJECT`](output.objects.md#ocptv.output.objects.SourceLocation.SPEC_OBJECT)


            * [`SourceLocation.file`](output.objects.md#ocptv.output.objects.SourceLocation.file)


            * [`SourceLocation.line`](output.objects.md#ocptv.output.objects.SourceLocation.line)


        * [`StepArtifact`](output.objects.md#ocptv.output.objects.StepArtifact)


            * [`StepArtifact.SPEC_OBJECT`](output.objects.md#ocptv.output.objects.StepArtifact.SPEC_OBJECT)


            * [`StepArtifact.id`](output.objects.md#ocptv.output.objects.StepArtifact.id)


            * [`StepArtifact.impl`](output.objects.md#ocptv.output.objects.StepArtifact.impl)


        * [`StepEnd`](output.objects.md#ocptv.output.objects.StepEnd)


            * [`StepEnd.SPEC_OBJECT`](output.objects.md#ocptv.output.objects.StepEnd.SPEC_OBJECT)


            * [`StepEnd.status`](output.objects.md#ocptv.output.objects.StepEnd.status)


        * [`StepStart`](output.objects.md#ocptv.output.objects.StepStart)


            * [`StepStart.SPEC_OBJECT`](output.objects.md#ocptv.output.objects.StepStart.SPEC_OBJECT)


            * [`StepStart.name`](output.objects.md#ocptv.output.objects.StepStart.name)


        * [`Subcomponent`](output.objects.md#ocptv.output.objects.Subcomponent)


            * [`Subcomponent.SPEC_OBJECT`](output.objects.md#ocptv.output.objects.Subcomponent.SPEC_OBJECT)


            * [`Subcomponent.location`](output.objects.md#ocptv.output.objects.Subcomponent.location)


            * [`Subcomponent.name`](output.objects.md#ocptv.output.objects.Subcomponent.name)


            * [`Subcomponent.revision`](output.objects.md#ocptv.output.objects.Subcomponent.revision)


            * [`Subcomponent.type`](output.objects.md#ocptv.output.objects.Subcomponent.type)


            * [`Subcomponent.version`](output.objects.md#ocptv.output.objects.Subcomponent.version)


        * [`SubcomponentType`](output.objects.md#ocptv.output.objects.SubcomponentType)


            * [`SubcomponentType.ASIC`](output.objects.md#ocptv.output.objects.SubcomponentType.ASIC)


            * [`SubcomponentType.ASIC_SUBSYSTEM`](output.objects.md#ocptv.output.objects.SubcomponentType.ASIC_SUBSYSTEM)


            * [`SubcomponentType.BUS`](output.objects.md#ocptv.output.objects.SubcomponentType.BUS)


            * [`SubcomponentType.CONNECTOR`](output.objects.md#ocptv.output.objects.SubcomponentType.CONNECTOR)


            * [`SubcomponentType.FUNCTION`](output.objects.md#ocptv.output.objects.SubcomponentType.FUNCTION)


            * [`SubcomponentType.UNSPECIFIED`](output.objects.md#ocptv.output.objects.SubcomponentType.UNSPECIFIED)


        * [`TestResult`](output.objects.md#ocptv.output.objects.TestResult)


            * [`TestResult.FAIL`](output.objects.md#ocptv.output.objects.TestResult.FAIL)


            * [`TestResult.NOT_APPLICABLE`](output.objects.md#ocptv.output.objects.TestResult.NOT_APPLICABLE)


            * [`TestResult.PASS`](output.objects.md#ocptv.output.objects.TestResult.PASS)


        * [`TestStatus`](output.objects.md#ocptv.output.objects.TestStatus)


            * [`TestStatus.COMPLETE`](output.objects.md#ocptv.output.objects.TestStatus.COMPLETE)


            * [`TestStatus.ERROR`](output.objects.md#ocptv.output.objects.TestStatus.ERROR)


            * [`TestStatus.SKIP`](output.objects.md#ocptv.output.objects.TestStatus.SKIP)


        * [`Validator`](output.objects.md#ocptv.output.objects.Validator)


            * [`Validator.SPEC_OBJECT`](output.objects.md#ocptv.output.objects.Validator.SPEC_OBJECT)


            * [`Validator.metadata`](output.objects.md#ocptv.output.objects.Validator.metadata)


            * [`Validator.name`](output.objects.md#ocptv.output.objects.Validator.name)


            * [`Validator.type`](output.objects.md#ocptv.output.objects.Validator.type)


            * [`Validator.value`](output.objects.md#ocptv.output.objects.Validator.value)


        * [`ValidatorType`](output.objects.md#ocptv.output.objects.ValidatorType)


            * [`ValidatorType.EQUAL`](output.objects.md#ocptv.output.objects.ValidatorType.EQUAL)


            * [`ValidatorType.GREATER_THAN`](output.objects.md#ocptv.output.objects.ValidatorType.GREATER_THAN)


            * [`ValidatorType.GREATER_THAN_OR_EQUAL`](output.objects.md#ocptv.output.objects.ValidatorType.GREATER_THAN_OR_EQUAL)


            * [`ValidatorType.IN_SET`](output.objects.md#ocptv.output.objects.ValidatorType.IN_SET)


            * [`ValidatorType.LESS_THAN`](output.objects.md#ocptv.output.objects.ValidatorType.LESS_THAN)


            * [`ValidatorType.LESS_THAN_OR_EQUAL`](output.objects.md#ocptv.output.objects.ValidatorType.LESS_THAN_OR_EQUAL)


            * [`ValidatorType.NOT_EQUAL`](output.objects.md#ocptv.output.objects.ValidatorType.NOT_EQUAL)


            * [`ValidatorType.NOT_IN_SET`](output.objects.md#ocptv.output.objects.ValidatorType.NOT_IN_SET)


            * [`ValidatorType.REGEX_MATCH`](output.objects.md#ocptv.output.objects.ValidatorType.REGEX_MATCH)


            * [`ValidatorType.REGEX_NO_MATCH`](output.objects.md#ocptv.output.objects.ValidatorType.REGEX_NO_MATCH)


        * [`format_hardware_info()`](output.objects.md#ocptv.output.objects.format_hardware_info)


        * [`format_timestamp_with_tzinfo()`](output.objects.md#ocptv.output.objects.format_timestamp_with_tzinfo)
