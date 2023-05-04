"""
Low level object models that are to be serialized as JSON.

NOT PUBLIC API, these are not intended to be used by client code
unless explicitly exported as public in ``__init__.py``.

Developer notes:
A field can either have ``metadata.spec_field`` set or ``field.SPEC_OBJECT`` set, not both.
If ``SPEC_OBJECT`` is set, this field is an union type and serialization should take the
value in ``SPEC_OBJECT`` as the serialized field name. Otherwise, the ``metadata.spec_field``
says what the serializer should use for field name.
In general, ``metadata.spec_field`` should only be present for primitive types.
"""
import dataclasses as dc
import typing as ty
from enum import Enum

from ocptv.api import export_api
from ocptv.formatter import format_enum, format_timestamp

if ty.TYPE_CHECKING:  # pragma: no cover
    # mypy extension for py37
    from typing_extensions import Protocol
else:
    Protocol = object

from .config import get_config
from .runtime_checks import check_field_types


def format_timestamp_with_tzinfo(ts: float) -> str:
    """Curry form with timezone from config"""
    return format_timestamp(ts, tz=get_config().timezone)


class ArtifactType(Protocol):
    """
    Protocol type to describe all low level serializable objects in this file.
    """

    __dataclass_fields__: ty.ClassVar[dict]


class OCPVersion(Enum):
    """
    OCP Test & Validation spec version consts.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#schemaversion
    schema: https://github.com/opencomputeproject/ocp-diag-core/output/$defs/schemaVersion
    """

    VERSION_2_0 = (2, 0)


@dc.dataclass
class SchemaVersion:
    """
    Low-level model for the `schemaVersion` spec object.
    Specifies the version that should be used to interpret following json outputs.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#schemaversion
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/root.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/output/$defs/schemaVersion
    """

    SPEC_OBJECT: ty.ClassVar[str] = "schemaVersion"

    major: int = dc.field(
        default=OCPVersion.VERSION_2_0.value[0],
        metadata={"spec_field": "major"},
    )

    minor: int = dc.field(
        default=OCPVersion.VERSION_2_0.value[1],
        metadata={"spec_field": "minor"},
    )

    def __post_init__(self):
        check_field_types(self)


# NOTE: This is intentionally not a dataclass. It is exported as public api
# because it does not have any inherent structure, other than a dict collection.
@export_api
class Metadata(dict):
    """
    Metadata container to accomodate any arbitrary keyed data put into it.
    For JSON output to work best, keys should be valid strings.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#metadata
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/metadata.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/metadata
    """

    SPEC_OBJECT: ty.ClassVar[str] = "metadata"


@dc.dataclass
class SourceLocation:
    """
    Provides information about which file/line of the source code in
    the diagnostic package generated the output.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#sourcelocation
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/source_location.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/sourceLocation
    """

    SPEC_OBJECT: ty.ClassVar[str] = "sourceLocation"

    file: str = dc.field(
        metadata={"spec_field": "file"},
    )

    line: int = dc.field(
        metadata={"spec_field": "line"},
    )


class LogSeverity(Enum):
    """
    Known log severity variants.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#severity
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/log.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/log/$defs/severity
    """

    INFO = "INFO"
    DEBUG = "DEBUG"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


@dc.dataclass
class Log:
    """
    Low-level model for `log` spec object.
    Is currently relevant for test run and test step artifact types.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#log
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/log.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/log
    """

    SPEC_OBJECT: ty.ClassVar[str] = "log"

    severity: LogSeverity = dc.field(
        metadata={
            "spec_field": "severity",
            "formatter": format_enum,
        },
    )

    message: str = dc.field(
        metadata={"spec_field": "message"},
    )

    source_location: ty.Optional[SourceLocation] = dc.field(
        metadata={"spec_field": "sourceLocation"},
    )

    def __post_init__(self):
        check_field_types(self)


@dc.dataclass
class File:
    """
    Low-level model for the `file` spec object.
    Represents a file artifact that was generated by running the diagnostic.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#file
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/file.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/file
    """

    SPEC_OBJECT: ty.ClassVar[str] = "file"

    name: str = dc.field(
        metadata={"spec_field": "displayName"},
    )

    uri: str = dc.field(
        metadata={"spec_field": "uri"},
    )

    is_snapshot: bool = dc.field(
        metadata={"spec_field": "isSnapshot"},
    )

    description: ty.Optional[str] = dc.field(
        metadata={"spec_field": "description"},
    )

    content_type: ty.Optional[str] = dc.field(
        metadata={"spec_field": "contentType"},
    )

    metadata: ty.Optional[Metadata]

    def __post_init__(self):
        check_field_types(self)


class SubcomponentType(Enum):
    """
    Type specification variants for DUT physical subcomponents.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#subcomponenttype
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/subcomponent.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/subcomponent/$defs/type
    """

    UNSPECIFIED = "UNSPECIFIED"
    ASIC = "ASIC"
    ASIC_SUBSYSTEM = "ASIC-SUBSYSTEM"
    BUS = "BUS"
    FUNCTION = "FUNCTION"
    CONNECTOR = "CONNECTOR"


@dc.dataclass
class Subcomponent:
    """
    Low-level model for the `subcomponent` spec object.
    Represents a physical subcomponent of a DUT hardware element.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#subcomponent
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/subcomponent.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/subcomponent
    """

    SPEC_OBJECT: ty.ClassVar[str] = "subcomponent"

    type: ty.Optional[SubcomponentType] = dc.field(
        metadata={
            "spec_field": "type",
            "formatter": format_enum,
        },
    )

    name: str = dc.field(
        metadata={"spec_field": "name"},
    )

    location: ty.Optional[str] = dc.field(
        metadata={"spec_field": "location"},
    )

    version: ty.Optional[str] = dc.field(
        metadata={"spec_field": "version"},
    )

    revision: ty.Optional[str] = dc.field(
        metadata={"spec_field": "revision"},
    )

    def __post_init__(self):
        check_field_types(self)


class DiagnosisType(Enum):
    """
    Outcome of a diagnosis operation.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#diagnosistype
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/diagnosis.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/diagnosis/$defs/type
    """

    PASS = "PASS"
    FAIL = "FAIL"
    UNKNOWN = "UNKNOWN"


@dc.dataclass
class PlatformInfo:
    """
    Low-level model for the `platformInfo` spec object.
    Describe platform specific attributes of the DUT.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#platforminfo
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/dut_info.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/dutInfo/$defs/platformInfo
    """

    SPEC_OBJECT: ty.ClassVar[str] = "platformInfo"

    info: str = dc.field(
        metadata={"spec_field": "info"},
    )

    def __post_init__(self):
        check_field_types(self)


class SoftwareType(Enum):
    """
    Type specification for a software component of the DUT.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#softwaretype
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/dut_info.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/dutInfo/$defs/softwareInfo/properties/softwareType
    """

    UNSPECIFIED = "UNSPECIFIED"
    FIRMWARE = "FIRMWARE"
    SYSTEM = "SYSTEM"
    APPLICATION = "APPLICATION"


@dc.dataclass
class SoftwareInfo:
    """
    Low-level model for the `softwareInfo` spec object.
    Represents information of a discovered or exercised software component of the DUT.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#softwareinfo
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/dut_info.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/dutInfo/$defs/softwareInfo
    """

    SPEC_OBJECT: ty.ClassVar[str] = "softwareInfo"

    id: str = dc.field(
        metadata={"spec_field": "softwareInfoId"},
    )

    name: str = dc.field(
        metadata={"spec_field": "name"},
    )

    version: ty.Optional[str] = dc.field(
        metadata={"spec_field": "version"},
    )

    revision: ty.Optional[str] = dc.field(
        metadata={"spec_field": "revision"},
    )

    type: ty.Optional[SoftwareType] = dc.field(
        metadata={
            "spec_field": "softwareType",
            "formatter": format_enum,
        },
    )

    computer_system: ty.Optional[str] = dc.field(
        metadata={"spec_field": "computerSystem"},
    )

    def __post_init__(self):
        check_field_types(self)


@dc.dataclass
class HardwareInfo:
    """
    Low-level model for the `hardwareInfo` spec object.
    Represents information of an enumerated or exercised hardware component of the DUT.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#hardwareinfo
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/dut_info.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/dutInfo/$defs/hardwareInfo
    """

    SPEC_OBJECT: ty.ClassVar[str] = "hardwareInfo"

    id: str = dc.field(
        metadata={"spec_field": "hardwareInfoId"},
    )

    name: str = dc.field(
        metadata={"spec_field": "name"},
    )

    version: ty.Optional[str] = dc.field(
        metadata={"spec_field": "version"},
    )

    revision: ty.Optional[str] = dc.field(
        metadata={"spec_field": "revision"},
    )

    location: ty.Optional[str] = dc.field(
        metadata={"spec_field": "location"},
    )

    serial_no: ty.Optional[str] = dc.field(
        metadata={"spec_field": "serialNumber"},
    )

    part_no: ty.Optional[str] = dc.field(
        metadata={"spec_field": "partNumber"},
    )

    manufacturer: ty.Optional[str] = dc.field(
        metadata={"spec_field": "manufacturer"},
    )

    manufacturer_part_no: ty.Optional[str] = dc.field(
        metadata={"spec_field": "manufacturerPartNumber"},
    )

    odata_id: ty.Optional[str] = dc.field(
        metadata={"spec_field": "odataId"},
    )

    computer_system: ty.Optional[str] = dc.field(
        metadata={"spec_field": "computerSystem"},
    )

    manager: ty.Optional[str] = dc.field(
        metadata={"spec_field": "manager"},
    )

    def __post_init__(self):
        check_field_types(self)


def format_hardware_info(obj: HardwareInfo) -> str:
    return obj.id


@dc.dataclass
class DutInfo:
    """
    Low-level model for the `dutInfo` spec object.
    Contains all relevant information describing the DUT.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#dutinfo
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/dut_info.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/dutInfo
    """

    SPEC_OBJECT: ty.ClassVar[str] = "dutInfo"

    id: str = dc.field(
        metadata={"spec_field": "dutInfoId"},
    )

    name: ty.Optional[str] = dc.field(
        metadata={"spec_field": "name"},
    )

    platform_infos: ty.List[PlatformInfo] = dc.field(
        metadata={"spec_field": "platformInfos"},
    )

    software_infos: ty.List[SoftwareInfo] = dc.field(
        metadata={"spec_field": "softwareInfos"},
    )

    hardware_infos: ty.List[HardwareInfo] = dc.field(
        metadata={"spec_field": "hardwareInfos"},
    )

    metadata: ty.Optional[Metadata]

    def __post_init__(self):
        check_field_types(self)


@dc.dataclass
class Diagnosis:
    """
    Low-level model for the `diagnosis` spec object.
    Contains the verdict given by the diagnostic regarding the DUT that was inspected.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#diagnosis
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/diagnosis.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/diagnosis
    """

    SPEC_OBJECT: ty.ClassVar[str] = "diagnosis"

    verdict: str = dc.field(
        metadata={"spec_field": "verdict"},
    )

    type: DiagnosisType = dc.field(
        metadata={
            "spec_field": "type",
            "formatter": format_enum,
        },
    )

    message: ty.Optional[str] = dc.field(
        metadata={"spec_field": "message"},
    )

    hardware_info: ty.Optional[HardwareInfo] = dc.field(
        metadata={
            "spec_field": "hardwareInfoId",
            "formatter": format_hardware_info,
        }
    )

    subcomponent: ty.Optional[Subcomponent]

    source_location: ty.Optional[SourceLocation] = dc.field(
        metadata={"spec_field": "sourceLocation"},
    )

    def __post_init__(self):
        check_field_types(self)


@dc.dataclass
class Error:
    """
    Low-level model for the `error` spec object.
    Represents an error encountered by the diagnostic software. It may refer to a DUT
    component or the diagnostic itself.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#error
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/error.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/error
    """

    SPEC_OBJECT: ty.ClassVar[str] = "error"

    symptom: str = dc.field(
        metadata={"spec_field": "symptom"},
    )

    message: ty.Optional[str] = dc.field(
        metadata={"spec_field": "message"},
    )

    software_infos: ty.List[SoftwareInfo] = dc.field(
        metadata={
            "spec_field": "softwareInfoIds",
            "formatter": lambda objs: [o.id for o in objs],
        },
    )

    source_location: ty.Optional[SourceLocation] = dc.field(
        metadata={"spec_field": "sourceLocation"},
    )

    def __post_init__(self):
        check_field_types(self)


MeasurementValueType = ty.Union[float, int, bool, str]

ValidatorValueType = ty.Union[
    ty.List[float],
    ty.List[int],
    ty.List[bool],
    ty.List[str],
    MeasurementValueType,
]


class ValidatorType(Enum):
    """
    Type specification for a measurement or series element validator logic.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#validator
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/validator.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/validator/$defs/type
    """

    EQUAL = "EQUAL"
    NOT_EQUAL = "NOT_EQUAL"
    LESS_THAN = "LESS_THAN"
    LESS_THAN_OR_EQUAL = "LESS_THAN_OR_EQUAL"
    GREATER_THAN = "GREATER_THAN"
    GREATER_THAN_OR_EQUAL = "GREATER_THAN_OR_EQUAL"
    REGEX_MATCH = "REGEX_MATCH"
    REGEX_NO_MATCH = "REGEX_NO_MATCH"
    IN_SET = "IN_SET"
    NOT_IN_SET = "NOT_IN_SET"


@dc.dataclass
class Validator:
    """
    Low-level model for the `validator` spec object.
    Contains the validation logic that the diagnostic applied for a specific measurement.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#validator
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/validator.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/validator
    """

    SPEC_OBJECT: ty.ClassVar[str] = "validator"

    name: ty.Optional[str] = dc.field(
        metadata={"spec_field": "name"},
    )

    type: ValidatorType = dc.field(
        metadata={
            "spec_field": "type",
            "formatter": format_enum,
        },
    )

    value: ValidatorValueType = dc.field(
        metadata={"spec_field": "value"},
    )

    metadata: ty.Optional[Metadata]

    def __post_init__(self):
        check_field_types(self)


@dc.dataclass
class Measurement:
    """
    Low-level model for the `measurement` spec object.
    Represents an individual measurement taken by the diagnostic regarding the DUT.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#measurement
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/measurement.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/measurement
    """

    SPEC_OBJECT: ty.ClassVar[str] = "measurement"

    name: str = dc.field(
        metadata={"spec_field": "name"},
    )

    value: MeasurementValueType = dc.field(
        metadata={"spec_field": "value"},
    )

    unit: ty.Optional[str] = dc.field(
        metadata={"spec_field": "unit"},
    )

    validators: ty.List[Validator] = dc.field(
        metadata={"spec_field": "validators"},
    )

    hardware_info: ty.Optional[HardwareInfo] = dc.field(
        metadata={
            "spec_field": "hardwareInfoId",
            "formatter": format_hardware_info,
        }
    )

    subcomponent: ty.Optional[Subcomponent]
    metadata: ty.Optional[Metadata]

    def __post_init__(self):
        check_field_types(self)


@dc.dataclass
class MeasurementSeriesStart:
    """
    Low-level model for the `measurementSeriesStart` spec object.
    Start marker for a time based series of measurements.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#measurementseriesstart
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/measurement_series_start.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/measurementSeriesStart
    """

    SPEC_OBJECT: ty.ClassVar[str] = "measurementSeriesStart"

    name: str = dc.field(
        metadata={"spec_field": "name"},
    )

    unit: ty.Optional[str] = dc.field(
        metadata={"spec_field": "unit"},
    )

    series_id: str = dc.field(
        metadata={"spec_field": "measurementSeriesId"},
    )

    validators: ty.List[Validator] = dc.field(
        metadata={"spec_field": "validators"},
    )

    hardware_info: ty.Optional[HardwareInfo] = dc.field(
        metadata={
            "spec_field": "hardwareInfoId",
            "formatter": format_hardware_info,
        }
    )

    subcomponent: ty.Optional[Subcomponent]
    metadata: ty.Optional[Metadata]

    def __post_init__(self):
        check_field_types(self)


@dc.dataclass
class MeasurementSeriesEnd:
    """
    Low-level model for the `measurementSeriesEnd` spec object.
    End marker for a time based series of measurements.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#measurementseriesend
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/measurement_series_end.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/measurementSeriesEnd
    """

    SPEC_OBJECT: ty.ClassVar[str] = "measurementSeriesEnd"

    series_id: str = dc.field(
        metadata={"spec_field": "measurementSeriesId"},
    )

    total_count: int = dc.field(
        metadata={"spec_field": "totalCount"},
    )

    def __post_init__(self):
        check_field_types(self)


@dc.dataclass
class MeasurementSeriesElement:
    """
    Low-level model for the `measurementSeriesElement` spec object.
    Equivalent to the `Measurement` model but inside a time based series.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#measurementserieselement
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/measurement_series_element.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/measurementSeriesElement
    """

    SPEC_OBJECT: ty.ClassVar[str] = "measurementSeriesElement"

    index: int = dc.field(
        metadata={"spec_field": "index"},
    )

    value: MeasurementValueType = dc.field(
        metadata={"spec_field": "value"},
    )

    timestamp: float = dc.field(
        metadata={
            "spec_field": "timestamp",
            "formatter": format_timestamp_with_tzinfo,
        },
    )

    series_id: str = dc.field(
        metadata={"spec_field": "measurementSeriesId"},
    )

    metadata: ty.Optional[Metadata]

    def __post_init__(self):
        check_field_types(self)


MeasurementSeriesType = ty.Union[MeasurementSeriesStart, MeasurementSeriesEnd, MeasurementSeriesElement]

if ty.TYPE_CHECKING:
    # note: these must specify some bounds for the extension content in python, despite
    # the spec saying that it can be anything. This is necessary for the json serializer
    # to actually know how to output the data.
    ExtensionContentType = ty.Union[  # pragma: no cover
        ty.Dict[str, "ExtensionContentType"],
        ty.List["ExtensionContentType"],
        ty.Union[float, int, bool, str, None],
    ]
else:
    # the runtime checker cannot deal with recursive types, and this is meant to be any
    ExtensionContentType = ty.Any


@dc.dataclass
class Extension:
    """
    Low-level model for the `extension` spec object.
    Left as an implementation detail, the `Extension` just has a name and arbitrary data.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#extension
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/test_step_artifact.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/testStepArtifact/$defs/extension
    """

    SPEC_OBJECT: ty.ClassVar[str] = "extension"

    name: str = dc.field(
        metadata={"spec_field": "name"},
    )

    content: ExtensionContentType = dc.field(
        metadata={"spec_field": "content"},
    )

    def __post_init__(self):
        check_field_types(self)


@dc.dataclass
class RunStart:
    """
    Low-level model for the `testRunStart` spec object.
    Start marker for the beginning of a diagnostic test.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#testrunstart
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/test_run_start.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/testRunStart
    """

    SPEC_OBJECT: ty.ClassVar[str] = "testRunStart"

    name: str = dc.field(
        metadata={"spec_field": "name"},
    )

    version: str = dc.field(
        metadata={"spec_field": "version"},
    )

    command_line: str = dc.field(
        metadata={"spec_field": "commandLine"},
    )

    parameters: ty.Dict[str, ty.Any] = dc.field(
        metadata={"spec_field": "parameters"},
    )

    dut_info: DutInfo

    def __post_init__(self):
        check_field_types(self)


class TestStatus(Enum):
    """
    Represents the final execution status of a test.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#teststatus
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/test_status.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/testStatus
    """

    # pytest incorrectly identifies this as a test
    __test__ = False  # type: ignore

    COMPLETE = "COMPLETE"
    ERROR = "ERROR"
    SKIP = "SKIP"


class TestResult(Enum):
    """
    Represents the final outcome of a test execution.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#testresult
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/test_run_end.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/testRunEnd/$defs/testResult
    """

    # pytest incorrectly identifies this as a test
    __test__ = False  # type: ignore

    PASS = "PASS"
    FAIL = "FAIL"
    NOT_APPLICABLE = "NOT_APPLICABLE"


@dc.dataclass
class RunEnd:
    """
    Low-level model for the `testRunEnd` spec object.
    End marker signaling the finality of a diagnostic test.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#testrunend
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/test_run_end.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/testRunEnd
    """

    SPEC_OBJECT: ty.ClassVar[str] = "testRunEnd"

    status: TestStatus = dc.field(
        metadata={
            "spec_field": "status",
            "formatter": format_enum,
        },
    )

    result: TestResult = dc.field(
        metadata={
            "spec_field": "result",
            "formatter": format_enum,
        },
    )

    def __post_init__(self):
        check_field_types(self)


@dc.dataclass
class RunArtifact:
    """
    Low-level model for the `testRunArtifact` spec object.
    Container for the run level artifacts.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#test-run-artifacts
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/test_run_artifact.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/testRunArtifact
    """

    SPEC_OBJECT: ty.ClassVar[str] = "testRunArtifact"

    impl: ty.Union[RunStart, RunEnd, Log, Error]


@dc.dataclass
class StepStart:
    """
    Low-level model for the `testStepStart` spec object.
    Start marker for a test step inside a diagnosis run.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#teststepstart
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/test_step_start.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/testStepStart
    """

    SPEC_OBJECT: ty.ClassVar[str] = "testStepStart"

    name: str = dc.field(
        metadata={"spec_field": "name"},
    )

    def __post_init__(self):
        check_field_types(self)


@dc.dataclass
class StepEnd:
    """
    Low-level model for the `testStepEnd` spec object.
    End marker for a test step inside a diagnosis run.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#teststepend
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/test_step_end.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/testStepEnd
    """

    SPEC_OBJECT: ty.ClassVar[str] = "testStepEnd"

    status: TestStatus = dc.field(
        metadata={
            "spec_field": "status",
            "formatter": format_enum,
        },
    )

    def __post_init__(self):
        check_field_types(self)


@dc.dataclass
class StepArtifact:
    """
    Low-level model for the `testStepArtifact` spec object.
    Container for the step level artifacts.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#test-step-artifacts
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/test_step_artifact.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/testStepArtifact
    """

    SPEC_OBJECT: ty.ClassVar[str] = "testStepArtifact"

    id: str = dc.field(
        metadata={"spec_field": "testStepId"},
    )

    impl: ty.Union[
        StepStart,
        StepEnd,
        Measurement,
        MeasurementSeriesType,
        Diagnosis,
        Log,
        Error,
        File,
        Extension,
    ]

    def __post_init__(self):
        check_field_types(self)


RootArtifactType = ty.Union[SchemaVersion, RunArtifact, StepArtifact]


@dc.dataclass
class Root:
    """
    Low-level model for the root json node.
    Container for the root level artifacts.

    ref: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#outputartifacts
    schema url: https://github.com/opencomputeproject/ocp-diag-core/blob/main/json_spec/output/root.json
    schema ref: https://github.com/opencomputeproject/ocp-diag-core/output
    """

    impl: RootArtifactType

    sequence_number: int = dc.field(
        metadata={"spec_field": "sequenceNumber"},
    )

    timestamp: float = dc.field(
        metadata={
            "spec_field": "timestamp",
            "formatter": format_timestamp_with_tzinfo,
        },
    )

    def __post_init__(self):
        check_field_types(self)
