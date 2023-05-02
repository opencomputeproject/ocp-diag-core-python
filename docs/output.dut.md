# ocptv.output.dut module


### _class_ ocptv.output.dut.Dut(id, name=None, metadata=None)
The Dut instances model the specific devices under test used in this diagnostic package.

All the methods in this class are threadsafe.

Specification reference:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#dutinfo](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#dutinfo)

This type can be instantiated by user code directly.


#### \__init__(id, name=None, metadata=None)
Initialize a new Dut instance.


* **Parameters**

    
    * **id** (`str`) – unique identifier for this device under test.


    * **name** (`Optional`[`str`]) – any domain specific naming for the device.


    * **metadata** (`Optional`[[`Metadata`](output.objects.md#ocptv.output.objects.Metadata)]) – dictionary with unspecified metadata for the device.


For additional details on parameters, see:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#dutinfo](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#dutinfo)


#### add_hardware_info(name, version=None, revision=None, location=None, serial_no=None, part_no=None, manufacturer=None, manufacturer_part_no=None, odata_id=None, computer_system=None, manager=None)
Add a new information item describing a hardware component of the DUT.


* **Parameters**

    
    * **name** (`str`) – hardware component name.


    * **version** (`Optional`[`str`]) – version of the hardware component.


    * **revision** (`Optional`[`str`]) – revision of the hardware component.


    * **location** (`Optional`[`str`]) – unspecified representation of the hardware location.


    * **serial_no** (`Optional`[`str`]) – hardware component serial number.


    * **part_no** (`Optional`[`str`]) – hardware component part number.


    * **manufacturer** (`Optional`[`str`]) – manufacturer name of the hardware component.


    * **manufacturer_part_no** (`Optional`[`str`]) – hardware component part number as provided by manufacturer.


    * **odata_id** (`Optional`[`str`]) – Redfish-type identification for this hardware component.


    * **computer_system** (`Optional`[`str`]) – Redfish-type name of the computer system to which this
    hardware component is visible.


    * **manager** (`Optional`[`str`]) – Redfish-type name of the manager of this hardware component. Typically
    this is an out-of-band device/system.



* **Return type**

    `HardwareInfo`



* **Returns**

    model reference to the new hardware component.


For additional details on parameters, see:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#hardwareinfo](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#hardwareinfo)


#### add_platform_info(info_tag)
Add a new platform information item to this DUT.


* **Parameters**

    **info_tag** (`str`) – free-form information about the platform.



* **Return type**

    `PlatformInfo`



* **Returns**

    model reference to the new platform info item.


For additional details on parameters, see:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#platforminfo](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#platforminfo)


#### add_software_info(name, type=None, version=None, revision=None, computer_system=None)
Add a new information item describing a software component for this DUT.


* **Parameters**

    
    * **name** (`str`) – software component name.


    * **type** (`Optional`[[`SoftwareType`](output.objects.md#ocptv.output.objects.SoftwareType)]) – classification of the software component type.
    see: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#softwaretype](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#softwaretype)


    * **version** (`Optional`[`str`]) – version information for the software.


    * **str** – revision information for the software.


    * **computer_system** (`Optional`[`str`]) – Redfish-type name of the computer system where
    this software component is executing.



* **Return type**

    `SoftwareInfo`



* **Returns**

    model reference to the new software component.


For additional details on parameters, see:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#softwareinfo](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#softwareinfo)


### _class_ ocptv.output.dut.HardwareInfo(id, name, version=None, revision=None, location=None, serial_no=None, part_no=None, manufacturer=None, manufacturer_part_no=None, odata_id=None, computer_system=None, manager=None)
Hardware information for a component of the DUT.

This object should not be instantiated directly by user code.

Specification reference:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#hardwareinfo](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#hardwareinfo)


#### \__init__(id, name, version=None, revision=None, location=None, serial_no=None, part_no=None, manufacturer=None, manufacturer_part_no=None, odata_id=None, computer_system=None, manager=None)

### _class_ ocptv.output.dut.PlatformInfo(info_tag)
Platform information for the DUT.

This object should not be instantiated directly by user code.

Specification reference:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#platforminfo](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#platforminfo)


#### \__init__(info_tag)

### _class_ ocptv.output.dut.SoftwareInfo(id, name, type=None, version=None, revision=None, computer_system=None)
Software information for a component of the DUT.

This object should not be instantiated directly by user code.

Specification reference:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#softwareinfo](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#softwareinfo)


#### \__init__(id, name, type=None, version=None, revision=None, computer_system=None)

### _class_ ocptv.output.dut.Subcomponent(\*, name, type=None, location=None, version=None, revision=None)
A lower-than-FRU (field replaceable unit) hardware item inside the DUT.

For additional details on parameters, see:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#subcomponent](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#subcomponent)

This type can be instantiated by user code directly.


#### \__init__(\*, name, type=None, location=None, version=None, revision=None)
Initialize a hardware subcomponent.


* **Parameters**

    
    * **name** (`str`) – hardware subcomponent name.


    * **type** (`Optional`[[`SubcomponentType`](output.objects.md#ocptv.output.objects.SubcomponentType)]) – classification of the subcomponent type.
    See: [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#subcomponenttype](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#subcomponenttype)


    * **location** (`Optional`[`str`]) – unspecified representation of the subcomponent location.


    * **version** (`Optional`[`str`]) – version of the hardware subcomponent.


    * **revision** (`Optional`[`str`]) – revision of the hardware subcomponent.
