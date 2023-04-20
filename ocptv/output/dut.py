import threading
import typing as ty

from ocptv.api import export_api

from .objects import DutInfo
from .objects import HardwareInfo as HardwareInfoSpec
from .objects import Metadata
from .objects import PlatformInfo as PlatformInfoSpec
from .objects import SoftwareInfo as SoftwareInfoSpec
from .objects import SoftwareType
from .objects import Subcomponent as SubcomponentSpec
from .objects import SubcomponentType


class PlatformInfo:
    """
    Platform information for the DUT.

    This object should not be instantiated directly by user code.

    Specification reference:
    - https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#platforminfo
    """

    def __init__(self, info_tag: str):
        self._spec_object = PlatformInfoSpec(info=info_tag)

    def to_spec(self) -> PlatformInfoSpec:
        """
        Internal usage. Convert to low-level model.

        :meta private:
        """
        return self._spec_object


class SoftwareInfo:
    """
    Software information for a component of the DUT.

    This object should not be instantiated directly by user code.

    Specification reference:
    - https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#softwareinfo
    """

    def __init__(
        self,
        id: str,
        name: str,
        type: ty.Optional[SoftwareType] = None,
        version: ty.Optional[str] = None,
        revision: ty.Optional[str] = None,
        computer_system: ty.Optional[str] = None,
    ):
        self._spec_object = SoftwareInfoSpec(
            id=id,
            name=name,
            version=version,
            revision=revision,
            type=type,
            computer_system=computer_system,
        )

    def to_spec(self) -> SoftwareInfoSpec:
        """
        Internal usage. Convert to low-level model.

        :meta private:
        """
        return self._spec_object


class HardwareInfo:
    """
    Hardware information for a component of the DUT.

    This object should not be instantiated directly by user code.

    Specification reference:
    - https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#hardwareinfo
    """

    def __init__(
        self,
        id: str,
        name: str,
        version: ty.Optional[str] = None,
        revision: ty.Optional[str] = None,
        location: ty.Optional[str] = None,
        serial_no: ty.Optional[str] = None,
        part_no: ty.Optional[str] = None,
        manufacturer: ty.Optional[str] = None,
        manufacturer_part_no: ty.Optional[str] = None,
        odata_id: ty.Optional[str] = None,
        computer_system: ty.Optional[str] = None,
        manager: ty.Optional[str] = None,
    ):
        self._spec_object = HardwareInfoSpec(
            id=id,
            name=name,
            version=version,
            revision=revision,
            location=location,
            serial_no=serial_no,
            part_no=part_no,
            manufacturer=manufacturer,
            manufacturer_part_no=manufacturer_part_no,
            odata_id=odata_id,
            computer_system=computer_system,
            manager=manager,
        )

    def to_spec(self) -> HardwareInfoSpec:
        """
        Internal usage. Convert to low-level model.

        :meta private:
        """
        return self._spec_object


@export_api
class Dut:
    """
    The `Dut` instances model the specific devices under test used in this diagnostic package.

    All the methods in this class are threadsafe.

    Specification reference:
    - https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#dutinfo
    """

    def __init__(
        self,
        id: str,
        name: ty.Optional[str] = None,
        metadata: ty.Optional[Metadata] = None,
    ):
        """
        Initialize a new Dut instance.

        :param id: unique identifier for this device under test.
        :param name: any domain specific naming for the device.
        :param metadata: dictionary with unspecified metadata for the device.

        For additional details on parameters, see:
        - https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#dutinfo
        """

        self._id = id
        self._name = name
        self._metadata = metadata

        self._info_lock = threading.Lock()
        self._platform_infos: ty.List[PlatformInfo] = []
        self._software_infos: ty.List[SoftwareInfo] = []
        self._hardware_infos: ty.List[HardwareInfo] = []

    def add_platform_info(self, info_tag: str) -> PlatformInfo:
        """
        Add a new platform information item to this DUT.

        :param info_tag: free-form information about the platform.
        :returns: model reference to the new platform info item.

        For additional details on parameters, see:
        - https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#platforminfo
        """

        info = PlatformInfo(info_tag=info_tag)
        with self._info_lock:
            self._platform_infos.append(info)
        return info

    def add_software_info(
        self,
        name: str,
        type: ty.Optional[SoftwareType] = None,
        version: ty.Optional[str] = None,
        revision: ty.Optional[str] = None,
        computer_system: ty.Optional[str] = None,
    ) -> SoftwareInfo:
        """
        Add a new information item describing a software component for this DUT.

        :param name: software component name.
        :param type: classification of the software component type.
            see: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#softwaretype
        :param version: version information for the software.
        :param str: revision information for the software.
        :param computer_system: Redfish-type name of the computer system where
            this software component is executing.
        :returns: model reference to the new software component.

        For additional details on parameters, see:
        - https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#softwareinfo
        """

        with self._info_lock:
            # reserve an index
            software_id = "{}_{}".format(self._id, len(self._software_infos))

            # TODO(mimir-d): arbitrary id derivation; does this need to be more readable?
            info = SoftwareInfo(
                id=software_id,
                name=name,
                type=type,
                version=version,
                revision=revision,
                computer_system=computer_system,
            )
            self._software_infos.append(info)
            return info

    def add_hardware_info(
        self,
        name: str,
        version: ty.Optional[str] = None,
        revision: ty.Optional[str] = None,
        location: ty.Optional[str] = None,
        serial_no: ty.Optional[str] = None,
        part_no: ty.Optional[str] = None,
        manufacturer: ty.Optional[str] = None,
        manufacturer_part_no: ty.Optional[str] = None,
        odata_id: ty.Optional[str] = None,
        computer_system: ty.Optional[str] = None,
        manager: ty.Optional[str] = None,
    ) -> HardwareInfo:
        """
        Add a new information item describing a hardware component of the DUT.

        :param name: hardware component name.
        :param version: version of the hardware component.
        :param revision: revision of the hardware component.
        :param location: unspecified representation of the hardware location.
        :param serial_no: hardware component serial number.
        :param part_no: hardware component part number.
        :param manufacturer: manufacturer name of the hardware component.
        :param manufacturer_part_no: hardware component part number as provided by manufacturer.
        :param odata_id: Redfish-type identification for this hardware component.
        :param computer_system: Redfish-type name of the computer system to which this
            hardware component is visible.
        :param manager: Redfish-type name of the manager of this hardware component. Typically
            this is an out-of-band device/system.
        :returns: model reference to the new hardware component.

        For additional details on parameters, see:
        - https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#hardwareinfo
        """

        with self._info_lock:
            # reserve an index
            hardware_id = "{}_{}".format(self._id, len(self._hardware_infos))

            info = HardwareInfo(
                id=hardware_id,
                name=name,
                version=version,
                revision=revision,
                location=location,
                serial_no=serial_no,
                part_no=part_no,
                manufacturer=manufacturer,
                manufacturer_part_no=manufacturer_part_no,
                odata_id=odata_id,
                computer_system=computer_system,
                manager=manager,
            )

            self._hardware_infos.append(info)
            return info

    def to_spec(self) -> DutInfo:
        """
        Internal usage. Convert to low-level model.

        :meta private:
        """
        with self._info_lock:
            platforms = [x.to_spec() for x in self._platform_infos]
            software = [x.to_spec() for x in self._software_infos]
            hardware = [x.to_spec() for x in self._hardware_infos]

        return DutInfo(
            id=self._id,
            name=self._name,
            platform_infos=platforms,
            software_infos=software,
            hardware_infos=hardware,
            metadata=self._metadata,
        )


# Following object is a proxy type so we get future flexibility, avoiding the usage
# of the low-level models.
@export_api
class Subcomponent:
    """
    A lower-than-FRU (field replaceable unit) hardware item inside the DUT.

    For additional details on parameters, see:
    - https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#subcomponent
    """

    def __init__(
        self,
        *,
        name: str,
        type: ty.Optional[SubcomponentType] = None,
        location: ty.Optional[str] = None,
        version: ty.Optional[str] = None,
        revision: ty.Optional[str] = None,
    ):
        """
        Initialize a hardware subcomponent.

        :param name: hardware subcomponent name.
        :param type: classification of the subcomponent type.
            See: https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#subcomponenttype
        :param location: unspecified representation of the subcomponent location.
        :param version: version of the hardware subcomponent.
        :param revision: revision of the hardware subcomponent.
        """

        self._spec_object = SubcomponentSpec(
            type=type,
            name=name,
            location=location,
            version=version,
            revision=revision,
        )

    def to_spec(self) -> SubcomponentSpec:
        """
        Internal usage. Convert to low-level model.

        :meta private:
        """
        return self._spec_object
