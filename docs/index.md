# Welcome to ocp-diag-python’s documentation!

# Contents:


* [ocptv.output package](output.md)


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


            * [`DiagnosisType`](output.objects.md#ocptv.output.objects.DiagnosisType)


            * [`DutInfo`](output.objects.md#ocptv.output.objects.DutInfo)


            * [`Error`](output.objects.md#ocptv.output.objects.Error)


            * [`Extension`](output.objects.md#ocptv.output.objects.Extension)


            * [`File`](output.objects.md#ocptv.output.objects.File)


            * [`HardwareInfo`](output.objects.md#ocptv.output.objects.HardwareInfo)


            * [`Log`](output.objects.md#ocptv.output.objects.Log)


            * [`LogSeverity`](output.objects.md#ocptv.output.objects.LogSeverity)


            * [`Measurement`](output.objects.md#ocptv.output.objects.Measurement)


            * [`MeasurementSeriesElement`](output.objects.md#ocptv.output.objects.MeasurementSeriesElement)


            * [`MeasurementSeriesEnd`](output.objects.md#ocptv.output.objects.MeasurementSeriesEnd)


            * [`MeasurementSeriesStart`](output.objects.md#ocptv.output.objects.MeasurementSeriesStart)


            * [`Metadata`](output.objects.md#ocptv.output.objects.Metadata)


            * [`OCPVersion`](output.objects.md#ocptv.output.objects.OCPVersion)


            * [`PlatformInfo`](output.objects.md#ocptv.output.objects.PlatformInfo)


            * [`Root`](output.objects.md#ocptv.output.objects.Root)


            * [`RunArtifact`](output.objects.md#ocptv.output.objects.RunArtifact)


            * [`RunEnd`](output.objects.md#ocptv.output.objects.RunEnd)


            * [`RunStart`](output.objects.md#ocptv.output.objects.RunStart)


            * [`SchemaVersion`](output.objects.md#ocptv.output.objects.SchemaVersion)


            * [`SoftwareInfo`](output.objects.md#ocptv.output.objects.SoftwareInfo)


            * [`SoftwareType`](output.objects.md#ocptv.output.objects.SoftwareType)


            * [`SourceLocation`](output.objects.md#ocptv.output.objects.SourceLocation)


            * [`StepArtifact`](output.objects.md#ocptv.output.objects.StepArtifact)


            * [`StepEnd`](output.objects.md#ocptv.output.objects.StepEnd)


            * [`StepStart`](output.objects.md#ocptv.output.objects.StepStart)


            * [`Subcomponent`](output.objects.md#ocptv.output.objects.Subcomponent)


            * [`SubcomponentType`](output.objects.md#ocptv.output.objects.SubcomponentType)


            * [`TestResult`](output.objects.md#ocptv.output.objects.TestResult)


            * [`TestStatus`](output.objects.md#ocptv.output.objects.TestStatus)


            * [`Validator`](output.objects.md#ocptv.output.objects.Validator)


            * [`ValidatorType`](output.objects.md#ocptv.output.objects.ValidatorType)


            * [`format_hardware_info()`](output.objects.md#ocptv.output.objects.format_hardware_info)


            * [`format_timestamp_with_tzinfo()`](output.objects.md#ocptv.output.objects.format_timestamp_with_tzinfo)
