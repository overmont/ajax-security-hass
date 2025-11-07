from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import common_jeweller_part_pb2 as _common_jeweller_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_battery_pb2 as _device_battery_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import common_en54_part_pb2 as _common_en54_part_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class En54A(_message.Message):
    __slots__ = ("common_jeweller_part", "device_battery", "common_en54_part", "common_en54_sounder_part", "common_en54_annunciation_test_part")
    COMMON_JEWELLER_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_SOUNDER_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_ANNUNCIATION_TEST_PART_FIELD_NUMBER: _ClassVar[int]
    common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
    device_battery: _device_battery_pb2.DeviceBatteryWithoutCharging
    common_en54_part: _common_en54_part_pb2.CommonEn54Part
    common_en54_sounder_part: _common_en54_part_pb2.CommonEn54SounderPart
    common_en54_annunciation_test_part: _common_en54_part_pb2.CommonEn54AnnunciationTestPart
    def __init__(self, common_jeweller_part: _Optional[_Union[_common_jeweller_part_pb2.CommonJewellerPart, _Mapping]] = ..., device_battery: _Optional[_Union[_device_battery_pb2.DeviceBatteryWithoutCharging, _Mapping]] = ..., common_en54_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54Part, _Mapping]] = ..., common_en54_sounder_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54SounderPart, _Mapping]] = ..., common_en54_annunciation_test_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54AnnunciationTestPart, _Mapping]] = ...) -> None: ...

class En54Va(_message.Message):
    __slots__ = ("common_jeweller_part", "device_battery", "common_en54_part", "common_en54_vad_part", "common_en54_sounder_part", "common_en54_annunciation_test_part")
    COMMON_JEWELLER_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_VAD_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_SOUNDER_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_ANNUNCIATION_TEST_PART_FIELD_NUMBER: _ClassVar[int]
    common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
    device_battery: _device_battery_pb2.DeviceBatteryWithoutCharging
    common_en54_part: _common_en54_part_pb2.CommonEn54Part
    common_en54_vad_part: _common_en54_part_pb2.CommonEn54VadPart
    common_en54_sounder_part: _common_en54_part_pb2.CommonEn54SounderPart
    common_en54_annunciation_test_part: _common_en54_part_pb2.CommonEn54AnnunciationTestPart
    def __init__(self, common_jeweller_part: _Optional[_Union[_common_jeweller_part_pb2.CommonJewellerPart, _Mapping]] = ..., device_battery: _Optional[_Union[_device_battery_pb2.DeviceBatteryWithoutCharging, _Mapping]] = ..., common_en54_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54Part, _Mapping]] = ..., common_en54_vad_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54VadPart, _Mapping]] = ..., common_en54_sounder_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54SounderPart, _Mapping]] = ..., common_en54_annunciation_test_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54AnnunciationTestPart, _Mapping]] = ...) -> None: ...

class En54V(_message.Message):
    __slots__ = ("common_jeweller_part", "device_battery", "common_en54_part", "common_en54_vad_part", "common_en54_annunciation_test_part")
    COMMON_JEWELLER_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_VAD_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_ANNUNCIATION_TEST_PART_FIELD_NUMBER: _ClassVar[int]
    common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
    device_battery: _device_battery_pb2.DeviceBatteryWithoutCharging
    common_en54_part: _common_en54_part_pb2.CommonEn54Part
    common_en54_vad_part: _common_en54_part_pb2.CommonEn54VadPart
    common_en54_annunciation_test_part: _common_en54_part_pb2.CommonEn54AnnunciationTestPart
    def __init__(self, common_jeweller_part: _Optional[_Union[_common_jeweller_part_pb2.CommonJewellerPart, _Mapping]] = ..., device_battery: _Optional[_Union[_device_battery_pb2.DeviceBatteryWithoutCharging, _Mapping]] = ..., common_en54_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54Part, _Mapping]] = ..., common_en54_vad_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54VadPart, _Mapping]] = ..., common_en54_annunciation_test_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54AnnunciationTestPart, _Mapping]] = ...) -> None: ...

class En54HVa(_message.Message):
    __slots__ = ("common_jeweller_part", "device_battery", "common_en54_part", "common_en54_heat_part", "common_en54_vad_part", "common_en54_sounder_part", "common_en54_annunciation_test_part")
    COMMON_JEWELLER_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_HEAT_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_VAD_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_SOUNDER_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_ANNUNCIATION_TEST_PART_FIELD_NUMBER: _ClassVar[int]
    common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
    device_battery: _device_battery_pb2.DeviceBatteryWithoutCharging
    common_en54_part: _common_en54_part_pb2.CommonEn54Part
    common_en54_heat_part: _common_en54_part_pb2.CommonEn54HeatPart
    common_en54_vad_part: _common_en54_part_pb2.CommonEn54VadPart
    common_en54_sounder_part: _common_en54_part_pb2.CommonEn54SounderPart
    common_en54_annunciation_test_part: _common_en54_part_pb2.CommonEn54AnnunciationTestPart
    def __init__(self, common_jeweller_part: _Optional[_Union[_common_jeweller_part_pb2.CommonJewellerPart, _Mapping]] = ..., device_battery: _Optional[_Union[_device_battery_pb2.DeviceBatteryWithoutCharging, _Mapping]] = ..., common_en54_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54Part, _Mapping]] = ..., common_en54_heat_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54HeatPart, _Mapping]] = ..., common_en54_vad_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54VadPart, _Mapping]] = ..., common_en54_sounder_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54SounderPart, _Mapping]] = ..., common_en54_annunciation_test_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54AnnunciationTestPart, _Mapping]] = ...) -> None: ...

class En54HsVa(_message.Message):
    __slots__ = ("common_jeweller_part", "device_battery", "common_en54_part", "common_en54_heat_part", "common_en54_smoke_part", "common_en54_vad_part", "common_en54_sounder_part", "common_en54_annunciation_test_part")
    COMMON_JEWELLER_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_HEAT_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_SMOKE_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_VAD_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_SOUNDER_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_ANNUNCIATION_TEST_PART_FIELD_NUMBER: _ClassVar[int]
    common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
    device_battery: _device_battery_pb2.DeviceBatteryWithoutCharging
    common_en54_part: _common_en54_part_pb2.CommonEn54Part
    common_en54_heat_part: _common_en54_part_pb2.CommonEn54HeatPart
    common_en54_smoke_part: _common_en54_part_pb2.CommonEn54SmokePart
    common_en54_vad_part: _common_en54_part_pb2.CommonEn54VadPart
    common_en54_sounder_part: _common_en54_part_pb2.CommonEn54SounderPart
    common_en54_annunciation_test_part: _common_en54_part_pb2.CommonEn54AnnunciationTestPart
    def __init__(self, common_jeweller_part: _Optional[_Union[_common_jeweller_part_pb2.CommonJewellerPart, _Mapping]] = ..., device_battery: _Optional[_Union[_device_battery_pb2.DeviceBatteryWithoutCharging, _Mapping]] = ..., common_en54_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54Part, _Mapping]] = ..., common_en54_heat_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54HeatPart, _Mapping]] = ..., common_en54_smoke_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54SmokePart, _Mapping]] = ..., common_en54_vad_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54VadPart, _Mapping]] = ..., common_en54_sounder_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54SounderPart, _Mapping]] = ..., common_en54_annunciation_test_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54AnnunciationTestPart, _Mapping]] = ...) -> None: ...

class En54H(_message.Message):
    __slots__ = ("common_jeweller_part", "device_battery", "common_en54_part", "common_en54_heat_part")
    COMMON_JEWELLER_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_HEAT_PART_FIELD_NUMBER: _ClassVar[int]
    common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
    device_battery: _device_battery_pb2.DeviceBatteryWithoutCharging
    common_en54_part: _common_en54_part_pb2.CommonEn54Part
    common_en54_heat_part: _common_en54_part_pb2.CommonEn54HeatPart
    def __init__(self, common_jeweller_part: _Optional[_Union[_common_jeweller_part_pb2.CommonJewellerPart, _Mapping]] = ..., device_battery: _Optional[_Union[_device_battery_pb2.DeviceBatteryWithoutCharging, _Mapping]] = ..., common_en54_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54Part, _Mapping]] = ..., common_en54_heat_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54HeatPart, _Mapping]] = ...) -> None: ...

class En54S(_message.Message):
    __slots__ = ("common_jeweller_part", "device_battery", "common_en54_part", "common_en54_smoke_part")
    COMMON_JEWELLER_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_SMOKE_PART_FIELD_NUMBER: _ClassVar[int]
    common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
    device_battery: _device_battery_pb2.DeviceBatteryWithoutCharging
    common_en54_part: _common_en54_part_pb2.CommonEn54Part
    common_en54_smoke_part: _common_en54_part_pb2.CommonEn54SmokePart
    def __init__(self, common_jeweller_part: _Optional[_Union[_common_jeweller_part_pb2.CommonJewellerPart, _Mapping]] = ..., device_battery: _Optional[_Union[_device_battery_pb2.DeviceBatteryWithoutCharging, _Mapping]] = ..., common_en54_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54Part, _Mapping]] = ..., common_en54_smoke_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54SmokePart, _Mapping]] = ...) -> None: ...

class En54SV(_message.Message):
    __slots__ = ("common_jeweller_part", "device_battery", "common_en54_part", "common_en54_smoke_part", "common_en54_vad_part", "common_en54_annunciation_test_part")
    COMMON_JEWELLER_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_SMOKE_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_VAD_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_ANNUNCIATION_TEST_PART_FIELD_NUMBER: _ClassVar[int]
    common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
    device_battery: _device_battery_pb2.DeviceBatteryWithoutCharging
    common_en54_part: _common_en54_part_pb2.CommonEn54Part
    common_en54_smoke_part: _common_en54_part_pb2.CommonEn54SmokePart
    common_en54_vad_part: _common_en54_part_pb2.CommonEn54VadPart
    common_en54_annunciation_test_part: _common_en54_part_pb2.CommonEn54AnnunciationTestPart
    def __init__(self, common_jeweller_part: _Optional[_Union[_common_jeweller_part_pb2.CommonJewellerPart, _Mapping]] = ..., device_battery: _Optional[_Union[_device_battery_pb2.DeviceBatteryWithoutCharging, _Mapping]] = ..., common_en54_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54Part, _Mapping]] = ..., common_en54_smoke_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54SmokePart, _Mapping]] = ..., common_en54_vad_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54VadPart, _Mapping]] = ..., common_en54_annunciation_test_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54AnnunciationTestPart, _Mapping]] = ...) -> None: ...

class En54SA(_message.Message):
    __slots__ = ("common_jeweller_part", "device_battery", "common_en54_part", "common_en54_smoke_part", "common_en54_sounder_part", "common_en54_annunciation_test_part")
    COMMON_JEWELLER_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_SMOKE_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_SOUNDER_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_ANNUNCIATION_TEST_PART_FIELD_NUMBER: _ClassVar[int]
    common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
    device_battery: _device_battery_pb2.DeviceBatteryWithoutCharging
    common_en54_part: _common_en54_part_pb2.CommonEn54Part
    common_en54_smoke_part: _common_en54_part_pb2.CommonEn54SmokePart
    common_en54_sounder_part: _common_en54_part_pb2.CommonEn54SounderPart
    common_en54_annunciation_test_part: _common_en54_part_pb2.CommonEn54AnnunciationTestPart
    def __init__(self, common_jeweller_part: _Optional[_Union[_common_jeweller_part_pb2.CommonJewellerPart, _Mapping]] = ..., device_battery: _Optional[_Union[_device_battery_pb2.DeviceBatteryWithoutCharging, _Mapping]] = ..., common_en54_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54Part, _Mapping]] = ..., common_en54_smoke_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54SmokePart, _Mapping]] = ..., common_en54_sounder_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54SounderPart, _Mapping]] = ..., common_en54_annunciation_test_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54AnnunciationTestPart, _Mapping]] = ...) -> None: ...

class En54HV(_message.Message):
    __slots__ = ("common_jeweller_part", "device_battery", "common_en54_part", "common_en54_heat_part", "common_en54_vad_part", "common_en54_annunciation_test_part")
    COMMON_JEWELLER_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_HEAT_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_VAD_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_ANNUNCIATION_TEST_PART_FIELD_NUMBER: _ClassVar[int]
    common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
    device_battery: _device_battery_pb2.DeviceBatteryWithoutCharging
    common_en54_part: _common_en54_part_pb2.CommonEn54Part
    common_en54_heat_part: _common_en54_part_pb2.CommonEn54HeatPart
    common_en54_vad_part: _common_en54_part_pb2.CommonEn54VadPart
    common_en54_annunciation_test_part: _common_en54_part_pb2.CommonEn54AnnunciationTestPart
    def __init__(self, common_jeweller_part: _Optional[_Union[_common_jeweller_part_pb2.CommonJewellerPart, _Mapping]] = ..., device_battery: _Optional[_Union[_device_battery_pb2.DeviceBatteryWithoutCharging, _Mapping]] = ..., common_en54_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54Part, _Mapping]] = ..., common_en54_heat_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54HeatPart, _Mapping]] = ..., common_en54_vad_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54VadPart, _Mapping]] = ..., common_en54_annunciation_test_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54AnnunciationTestPart, _Mapping]] = ...) -> None: ...

class En54Ha(_message.Message):
    __slots__ = ("common_jeweller_part", "device_battery", "common_en54_part", "common_en54_heat_part", "common_en54_sounder_part", "common_en54_annunciation_test_part")
    COMMON_JEWELLER_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_HEAT_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_SOUNDER_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_EN54_ANNUNCIATION_TEST_PART_FIELD_NUMBER: _ClassVar[int]
    common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
    device_battery: _device_battery_pb2.DeviceBatteryWithoutCharging
    common_en54_part: _common_en54_part_pb2.CommonEn54Part
    common_en54_heat_part: _common_en54_part_pb2.CommonEn54HeatPart
    common_en54_sounder_part: _common_en54_part_pb2.CommonEn54SounderPart
    common_en54_annunciation_test_part: _common_en54_part_pb2.CommonEn54AnnunciationTestPart
    def __init__(self, common_jeweller_part: _Optional[_Union[_common_jeweller_part_pb2.CommonJewellerPart, _Mapping]] = ..., device_battery: _Optional[_Union[_device_battery_pb2.DeviceBatteryWithoutCharging, _Mapping]] = ..., common_en54_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54Part, _Mapping]] = ..., common_en54_heat_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54HeatPart, _Mapping]] = ..., common_en54_sounder_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54SounderPart, _Mapping]] = ..., common_en54_annunciation_test_part: _Optional[_Union[_common_en54_part_pb2.CommonEn54AnnunciationTestPart, _Mapping]] = ...) -> None: ...
