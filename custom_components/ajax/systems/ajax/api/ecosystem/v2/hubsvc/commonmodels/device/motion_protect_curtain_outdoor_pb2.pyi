from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import common_jeweller_part_pb2 as _common_jeweller_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import common_wings_part_pb2 as _common_wings_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import common_masking_part_pb2 as _common_masking_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import gyroscope_pb2 as _gyroscope_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import common_device_notifications_part_pb2 as _common_device_notifications_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import led_indication_part_pb2 as _led_indication_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import detection_mode_part_pb2 as _detection_mode_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_battery_pb2 as _device_battery_pb2
from systems.ajax.api.ecosystem.v2.commonmodels.device.common import common_arming_part_pb2 as _common_arming_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_tamper_status_pb2 as _device_tamper_status_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_temperature_pb2 as _device_temperature_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_siren_triggers_pb2 as _device_siren_triggers_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import motion_detection_part_pb2 as _motion_detection_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_warnings_pb2 as _device_warnings_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MotionProtectCurtainOutdoorMini(_message.Message):
    __slots__ = ("common_arming_part", "device_temperature", "motion_detection_part", "device_tamper_status", "siren_triggers", "common_jeweller_part", "common_wings_part", "common_masking_part", "gyroscope", "device_notifications_part", "led_indication_part", "detection_mode_part", "device_battery_without_charging_part", "device_warnings")
    COMMON_ARMING_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTION_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TAMPER_STATUS_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    COMMON_JEWELLER_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_WINGS_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_MASKING_PART_FIELD_NUMBER: _ClassVar[int]
    GYROSCOPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NOTIFICATIONS_PART_FIELD_NUMBER: _ClassVar[int]
    LED_INDICATION_PART_FIELD_NUMBER: _ClassVar[int]
    DETECTION_MODE_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_WITHOUT_CHARGING_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_WARNINGS_FIELD_NUMBER: _ClassVar[int]
    common_arming_part: _common_arming_part_pb2.CommonArmingPart
    device_temperature: _device_temperature_pb2.DeviceTemperature
    motion_detection_part: _motion_detection_part_pb2.MotionDetectionPart
    device_tamper_status: _device_tamper_status_pb2.DeviceTamperStatus
    siren_triggers: _device_siren_triggers_pb2.SirenTriggers
    common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
    common_wings_part: _common_wings_part_pb2.CommonWingsPart
    common_masking_part: _common_masking_part_pb2.CommonMaskingPart
    gyroscope: _gyroscope_pb2.Gyroscope
    device_notifications_part: _common_device_notifications_part_pb2.CommonDeviceNotificationsPart
    led_indication_part: _led_indication_part_pb2.LedIndicationPart
    detection_mode_part: _detection_mode_part_pb2.DetectionModePart
    device_battery_without_charging_part: _device_battery_pb2.DeviceBatteryWithoutCharging
    device_warnings: _device_warnings_pb2.DeviceWarnings
    def __init__(self, common_arming_part: _Optional[_Union[_common_arming_part_pb2.CommonArmingPart, _Mapping]] = ..., device_temperature: _Optional[_Union[_device_temperature_pb2.DeviceTemperature, _Mapping]] = ..., motion_detection_part: _Optional[_Union[_motion_detection_part_pb2.MotionDetectionPart, _Mapping]] = ..., device_tamper_status: _Optional[_Union[_device_tamper_status_pb2.DeviceTamperStatus, str]] = ..., siren_triggers: _Optional[_Union[_device_siren_triggers_pb2.SirenTriggers, _Mapping]] = ..., common_jeweller_part: _Optional[_Union[_common_jeweller_part_pb2.CommonJewellerPart, _Mapping]] = ..., common_wings_part: _Optional[_Union[_common_wings_part_pb2.CommonWingsPart, _Mapping]] = ..., common_masking_part: _Optional[_Union[_common_masking_part_pb2.CommonMaskingPart, _Mapping]] = ..., gyroscope: _Optional[_Union[_gyroscope_pb2.Gyroscope, _Mapping]] = ..., device_notifications_part: _Optional[_Union[_common_device_notifications_part_pb2.CommonDeviceNotificationsPart, _Mapping]] = ..., led_indication_part: _Optional[_Union[_led_indication_part_pb2.LedIndicationPart, _Mapping]] = ..., detection_mode_part: _Optional[_Union[_detection_mode_part_pb2.DetectionModePart, _Mapping]] = ..., device_battery_without_charging_part: _Optional[_Union[_device_battery_pb2.DeviceBatteryWithoutCharging, _Mapping]] = ..., device_warnings: _Optional[_Union[_device_warnings_pb2.DeviceWarnings, _Mapping]] = ...) -> None: ...
