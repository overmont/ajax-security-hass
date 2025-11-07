from systems.ajax.api.ecosystem.v2.commonmodels.device.common import common_arming_part_pb2 as _common_arming_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_chimes_pb2 as _device_chimes_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import deprecated_device_chimes_pb2 as _deprecated_device_chimes_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_tamper_status_pb2 as _device_tamper_status_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_temperature_pb2 as _device_temperature_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_sensor_settings_pb2 as _device_sensor_settings_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_siren_triggers_pb2 as _device_siren_triggers_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommonDoorProtectPart(_message.Message):
    __slots__ = ("common_arming_part", "device_temperature", "siren_triggers", "device_tamper_status", "device_chimes", "reed_status", "reed_sensor", "extra_contact_status", "extra_contact_sensor", "capabilities", "always_active", "deprecated_device_chimes")
    class ReedStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REED_STATUS_UNSPECIFIED: _ClassVar[CommonDoorProtectPart.ReedStatus]
        REED_STATUS_OPENED: _ClassVar[CommonDoorProtectPart.ReedStatus]
        REED_STATUS_CLOSED: _ClassVar[CommonDoorProtectPart.ReedStatus]
        REED_STATUS_DISABLED: _ClassVar[CommonDoorProtectPart.ReedStatus]
    REED_STATUS_UNSPECIFIED: CommonDoorProtectPart.ReedStatus
    REED_STATUS_OPENED: CommonDoorProtectPart.ReedStatus
    REED_STATUS_CLOSED: CommonDoorProtectPart.ReedStatus
    REED_STATUS_DISABLED: CommonDoorProtectPart.ReedStatus
    class ExtraContactStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXTRA_CONTACT_STATUS_UNSPECIFIED: _ClassVar[CommonDoorProtectPart.ExtraContactStatus]
        EXTRA_CONTACT_STATUS_OPENED: _ClassVar[CommonDoorProtectPart.ExtraContactStatus]
        EXTRA_CONTACT_STATUS_CLOSED: _ClassVar[CommonDoorProtectPart.ExtraContactStatus]
        EXTRA_CONTACT_STATUS_DISABLED: _ClassVar[CommonDoorProtectPart.ExtraContactStatus]
        EXTRA_CONTACT_STATUS_CONNECTED: _ClassVar[CommonDoorProtectPart.ExtraContactStatus]
        EXTRA_CONTACT_STATUS_ALERT: _ClassVar[CommonDoorProtectPart.ExtraContactStatus]
    EXTRA_CONTACT_STATUS_UNSPECIFIED: CommonDoorProtectPart.ExtraContactStatus
    EXTRA_CONTACT_STATUS_OPENED: CommonDoorProtectPart.ExtraContactStatus
    EXTRA_CONTACT_STATUS_CLOSED: CommonDoorProtectPart.ExtraContactStatus
    EXTRA_CONTACT_STATUS_DISABLED: CommonDoorProtectPart.ExtraContactStatus
    EXTRA_CONTACT_STATUS_CONNECTED: CommonDoorProtectPart.ExtraContactStatus
    EXTRA_CONTACT_STATUS_ALERT: CommonDoorProtectPart.ExtraContactStatus
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[CommonDoorProtectPart.Capability]
        CAPABILITY_PRIMARY_DETECTOR: _ClassVar[CommonDoorProtectPart.Capability]
        CAPABILITY_SIREN_ALARM: _ClassVar[CommonDoorProtectPart.Capability]
        CAPABILITY_ROLLER_SHUTTER: _ClassVar[CommonDoorProtectPart.Capability]
    CAPABILITY_UNSPECIFIED: CommonDoorProtectPart.Capability
    CAPABILITY_PRIMARY_DETECTOR: CommonDoorProtectPart.Capability
    CAPABILITY_SIREN_ALARM: CommonDoorProtectPart.Capability
    CAPABILITY_ROLLER_SHUTTER: CommonDoorProtectPart.Capability
    class AlwaysActive(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALWAYS_ACTIVE_UNSPECIFIED: _ClassVar[CommonDoorProtectPart.AlwaysActive]
        ALWAYS_ACTIVE_DISABLED: _ClassVar[CommonDoorProtectPart.AlwaysActive]
        ALWAYS_ACTIVE_ENABLED: _ClassVar[CommonDoorProtectPart.AlwaysActive]
    ALWAYS_ACTIVE_UNSPECIFIED: CommonDoorProtectPart.AlwaysActive
    ALWAYS_ACTIVE_DISABLED: CommonDoorProtectPart.AlwaysActive
    ALWAYS_ACTIVE_ENABLED: CommonDoorProtectPart.AlwaysActive
    COMMON_ARMING_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TAMPER_STATUS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CHIMES_FIELD_NUMBER: _ClassVar[int]
    REED_STATUS_FIELD_NUMBER: _ClassVar[int]
    REED_SENSOR_FIELD_NUMBER: _ClassVar[int]
    EXTRA_CONTACT_STATUS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_CONTACT_SENSOR_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_DEVICE_CHIMES_FIELD_NUMBER: _ClassVar[int]
    common_arming_part: _common_arming_part_pb2.CommonArmingPart
    device_temperature: _device_temperature_pb2.DeviceTemperature
    siren_triggers: _device_siren_triggers_pb2.SirenTriggers
    device_tamper_status: _device_tamper_status_pb2.DeviceTamperStatus
    device_chimes: _device_chimes_pb2.DeviceChimes
    reed_status: CommonDoorProtectPart.ReedStatus
    reed_sensor: _device_sensor_settings_pb2.ReedSensorSettings
    extra_contact_status: CommonDoorProtectPart.ExtraContactStatus
    extra_contact_sensor: _device_sensor_settings_pb2.ExtraContactSensorSettings
    capabilities: _containers.RepeatedScalarFieldContainer[CommonDoorProtectPart.Capability]
    always_active: CommonDoorProtectPart.AlwaysActive
    deprecated_device_chimes: _deprecated_device_chimes_pb2.DeprecatedDeviceChimes
    def __init__(self, common_arming_part: _Optional[_Union[_common_arming_part_pb2.CommonArmingPart, _Mapping]] = ..., device_temperature: _Optional[_Union[_device_temperature_pb2.DeviceTemperature, _Mapping]] = ..., siren_triggers: _Optional[_Union[_device_siren_triggers_pb2.SirenTriggers, _Mapping]] = ..., device_tamper_status: _Optional[_Union[_device_tamper_status_pb2.DeviceTamperStatus, str]] = ..., device_chimes: _Optional[_Union[_device_chimes_pb2.DeviceChimes, _Mapping]] = ..., reed_status: _Optional[_Union[CommonDoorProtectPart.ReedStatus, str]] = ..., reed_sensor: _Optional[_Union[_device_sensor_settings_pb2.ReedSensorSettings, _Mapping]] = ..., extra_contact_status: _Optional[_Union[CommonDoorProtectPart.ExtraContactStatus, str]] = ..., extra_contact_sensor: _Optional[_Union[_device_sensor_settings_pb2.ExtraContactSensorSettings, _Mapping]] = ..., capabilities: _Optional[_Iterable[_Union[CommonDoorProtectPart.Capability, str]]] = ..., always_active: _Optional[_Union[CommonDoorProtectPart.AlwaysActive, str]] = ..., deprecated_device_chimes: _Optional[_Union[_deprecated_device_chimes_pb2.DeprecatedDeviceChimes, _Mapping]] = ...) -> None: ...
