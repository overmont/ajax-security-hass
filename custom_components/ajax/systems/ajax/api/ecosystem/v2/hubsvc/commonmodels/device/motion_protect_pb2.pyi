from systems.ajax.api.ecosystem.v2.commonmodels.device.common import common_arming_part_pb2 as _common_arming_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import bracket_state_pb2 as _bracket_state_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import common_jeweller_part_pb2 as _common_jeweller_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import common_masking_part_pb2 as _common_masking_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import common_motion_protect_part_pb2 as _common_motion_protect_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import common_wings_part_pb2 as _common_wings_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_battery_pb2 as _device_battery_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_siren_triggers_pb2 as _device_siren_triggers_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_tamper_status_pb2 as _device_tamper_status_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_temperature_pb2 as _device_temperature_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_warnings_pb2 as _device_warnings_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import fast_tamper_part_pb2 as _fast_tamper_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import led_indication_part_pb2 as _led_indication_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import motion_detection_part_pb2 as _motion_detection_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MotionProtect(_message.Message):
    __slots__ = ("common_jeweller_part", "common_motion_protect_part", "device_battery")
    COMMON_JEWELLER_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_MOTION_PROTECT_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_FIELD_NUMBER: _ClassVar[int]
    common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
    common_motion_protect_part: _common_motion_protect_part_pb2.CommonMotionProtectPart
    device_battery: _device_battery_pb2.DeviceBattery
    def __init__(self, common_jeweller_part: _Optional[_Union[_common_jeweller_part_pb2.CommonJewellerPart, _Mapping]] = ..., common_motion_protect_part: _Optional[_Union[_common_motion_protect_part_pb2.CommonMotionProtectPart, _Mapping]] = ..., device_battery: _Optional[_Union[_device_battery_pb2.DeviceBattery, _Mapping]] = ...) -> None: ...

class MotionProtectS(_message.Message):
    __slots__ = ("common_jeweller_part", "common_motion_protect_part", "device_battery", "fast_tamper_part")
    COMMON_JEWELLER_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_MOTION_PROTECT_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_FIELD_NUMBER: _ClassVar[int]
    FAST_TAMPER_PART_FIELD_NUMBER: _ClassVar[int]
    common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
    common_motion_protect_part: _common_motion_protect_part_pb2.CommonMotionProtectPart
    device_battery: _device_battery_pb2.DeviceBattery
    fast_tamper_part: _fast_tamper_part_pb2.FastTamperPart
    def __init__(self, common_jeweller_part: _Optional[_Union[_common_jeweller_part_pb2.CommonJewellerPart, _Mapping]] = ..., common_motion_protect_part: _Optional[_Union[_common_motion_protect_part_pb2.CommonMotionProtectPart, _Mapping]] = ..., device_battery: _Optional[_Union[_device_battery_pb2.DeviceBattery, _Mapping]] = ..., fast_tamper_part: _Optional[_Union[_fast_tamper_part_pb2.FastTamperPart, _Mapping]] = ...) -> None: ...

class MotionProtectG3(_message.Message):
    __slots__ = ("common_jeweller_part", "common_arming_part", "device_temperature", "device_tamper_status", "siren_triggers", "motion_detection_part", "device_battery", "common_wings_part", "common_masking_part", "bracket_state_part", "led_indication_part", "device_warnings")
    COMMON_JEWELLER_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_ARMING_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TAMPER_STATUS_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTION_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_FIELD_NUMBER: _ClassVar[int]
    COMMON_WINGS_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_MASKING_PART_FIELD_NUMBER: _ClassVar[int]
    BRACKET_STATE_PART_FIELD_NUMBER: _ClassVar[int]
    LED_INDICATION_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_WARNINGS_FIELD_NUMBER: _ClassVar[int]
    common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
    common_arming_part: _common_arming_part_pb2.CommonArmingPart
    device_temperature: _device_temperature_pb2.DeviceTemperature
    device_tamper_status: _device_tamper_status_pb2.DeviceTamperStatus
    siren_triggers: _device_siren_triggers_pb2.SirenTriggers
    motion_detection_part: _motion_detection_part_pb2.MotionDetectionPart
    device_battery: _device_battery_pb2.DeviceBattery
    common_wings_part: _common_wings_part_pb2.CommonWingsPart
    common_masking_part: _common_masking_part_pb2.CommonMaskingPart
    bracket_state_part: _bracket_state_pb2.BracketStatePart
    led_indication_part: _led_indication_part_pb2.LedIndicationPart
    device_warnings: _device_warnings_pb2.DeviceWarnings
    def __init__(self, common_jeweller_part: _Optional[_Union[_common_jeweller_part_pb2.CommonJewellerPart, _Mapping]] = ..., common_arming_part: _Optional[_Union[_common_arming_part_pb2.CommonArmingPart, _Mapping]] = ..., device_temperature: _Optional[_Union[_device_temperature_pb2.DeviceTemperature, _Mapping]] = ..., device_tamper_status: _Optional[_Union[_device_tamper_status_pb2.DeviceTamperStatus, str]] = ..., siren_triggers: _Optional[_Union[_device_siren_triggers_pb2.SirenTriggers, _Mapping]] = ..., motion_detection_part: _Optional[_Union[_motion_detection_part_pb2.MotionDetectionPart, _Mapping]] = ..., device_battery: _Optional[_Union[_device_battery_pb2.DeviceBattery, _Mapping]] = ..., common_wings_part: _Optional[_Union[_common_wings_part_pb2.CommonWingsPart, _Mapping]] = ..., common_masking_part: _Optional[_Union[_common_masking_part_pb2.CommonMaskingPart, _Mapping]] = ..., bracket_state_part: _Optional[_Union[_bracket_state_pb2.BracketStatePart, _Mapping]] = ..., led_indication_part: _Optional[_Union[_led_indication_part_pb2.LedIndicationPart, _Mapping]] = ..., device_warnings: _Optional[_Union[_device_warnings_pb2.DeviceWarnings, _Mapping]] = ...) -> None: ...

class MotionProtectPlusG3(_message.Message):
    __slots__ = ("common_jeweller_part", "common_arming_part", "device_temperature", "device_tamper_status", "siren_triggers", "motion_detection_part", "device_battery", "common_wings_part", "common_masking_part", "bracket_state_part", "led_indication_part", "device_warnings")
    COMMON_JEWELLER_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_ARMING_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TAMPER_STATUS_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTION_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_FIELD_NUMBER: _ClassVar[int]
    COMMON_WINGS_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_MASKING_PART_FIELD_NUMBER: _ClassVar[int]
    BRACKET_STATE_PART_FIELD_NUMBER: _ClassVar[int]
    LED_INDICATION_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_WARNINGS_FIELD_NUMBER: _ClassVar[int]
    common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
    common_arming_part: _common_arming_part_pb2.CommonArmingPart
    device_temperature: _device_temperature_pb2.DeviceTemperature
    device_tamper_status: _device_tamper_status_pb2.DeviceTamperStatus
    siren_triggers: _device_siren_triggers_pb2.SirenTriggers
    motion_detection_part: _motion_detection_part_pb2.MotionDetectionPart
    device_battery: _device_battery_pb2.DeviceBattery
    common_wings_part: _common_wings_part_pb2.CommonWingsPart
    common_masking_part: _common_masking_part_pb2.CommonMaskingPart
    bracket_state_part: _bracket_state_pb2.BracketStatePart
    led_indication_part: _led_indication_part_pb2.LedIndicationPart
    device_warnings: _device_warnings_pb2.DeviceWarnings
    def __init__(self, common_jeweller_part: _Optional[_Union[_common_jeweller_part_pb2.CommonJewellerPart, _Mapping]] = ..., common_arming_part: _Optional[_Union[_common_arming_part_pb2.CommonArmingPart, _Mapping]] = ..., device_temperature: _Optional[_Union[_device_temperature_pb2.DeviceTemperature, _Mapping]] = ..., device_tamper_status: _Optional[_Union[_device_tamper_status_pb2.DeviceTamperStatus, str]] = ..., siren_triggers: _Optional[_Union[_device_siren_triggers_pb2.SirenTriggers, _Mapping]] = ..., motion_detection_part: _Optional[_Union[_motion_detection_part_pb2.MotionDetectionPart, _Mapping]] = ..., device_battery: _Optional[_Union[_device_battery_pb2.DeviceBattery, _Mapping]] = ..., common_wings_part: _Optional[_Union[_common_wings_part_pb2.CommonWingsPart, _Mapping]] = ..., common_masking_part: _Optional[_Union[_common_masking_part_pb2.CommonMaskingPart, _Mapping]] = ..., bracket_state_part: _Optional[_Union[_bracket_state_pb2.BracketStatePart, _Mapping]] = ..., led_indication_part: _Optional[_Union[_led_indication_part_pb2.LedIndicationPart, _Mapping]] = ..., device_warnings: _Optional[_Union[_device_warnings_pb2.DeviceWarnings, _Mapping]] = ...) -> None: ...
