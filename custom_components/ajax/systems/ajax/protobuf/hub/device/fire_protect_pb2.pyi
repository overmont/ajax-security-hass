from google.protobuf import wrappers_pb2 as _wrappers_pb2
from systems.ajax.protobuf.hub.device import common_device_pb2 as _common_device_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FireProtect(_message.Message):
    __slots__ = ("common_part", "siren_triggers", "smoke_alarm_detected", "temperature_alarm_detected", "backup_battery_inserted", "backup_battery_charge_ok", "always_active", "temperature_diff_detection_enabled", "camera_malfunction", "smoke_camera_dusty", "high_temperature_alarms_enabled", "high_temperature_diff_detected", "buzzer_state", "subtype")
    class BuzzerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OFF: _ClassVar[FireProtect.BuzzerState]
        ON: _ClassVar[FireProtect.BuzzerState]
    OFF: FireProtect.BuzzerState
    ON: FireProtect.BuzzerState
    class SirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_TRIGGER_INFO: _ClassVar[FireProtect.SirenTrigger]
        TEMPERATURE: _ClassVar[FireProtect.SirenTrigger]
        TEMPERATURE_DIFF: _ClassVar[FireProtect.SirenTrigger]
        SMOKE: _ClassVar[FireProtect.SirenTrigger]
    NO_SIREN_TRIGGER_INFO: FireProtect.SirenTrigger
    TEMPERATURE: FireProtect.SirenTrigger
    TEMPERATURE_DIFF: FireProtect.SirenTrigger
    SMOKE: FireProtect.SirenTrigger
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[FireProtect.Subtype]
    NO_SUBTYPE: FireProtect.Subtype
    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    SMOKE_ALARM_DETECTED_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_ALARM_DETECTED_FIELD_NUMBER: _ClassVar[int]
    BACKUP_BATTERY_INSERTED_FIELD_NUMBER: _ClassVar[int]
    BACKUP_BATTERY_CHARGE_OK_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_DIFF_DETECTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CAMERA_MALFUNCTION_FIELD_NUMBER: _ClassVar[int]
    SMOKE_CAMERA_DUSTY_FIELD_NUMBER: _ClassVar[int]
    HIGH_TEMPERATURE_ALARMS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    HIGH_TEMPERATURE_DIFF_DETECTED_FIELD_NUMBER: _ClassVar[int]
    BUZZER_STATE_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    siren_triggers: _containers.RepeatedScalarFieldContainer[FireProtect.SirenTrigger]
    smoke_alarm_detected: _wrappers_pb2.BoolValue
    temperature_alarm_detected: _wrappers_pb2.BoolValue
    backup_battery_inserted: _wrappers_pb2.BoolValue
    backup_battery_charge_ok: _wrappers_pb2.BoolValue
    always_active: bool
    temperature_diff_detection_enabled: bool
    camera_malfunction: _wrappers_pb2.BoolValue
    smoke_camera_dusty: _wrappers_pb2.BoolValue
    high_temperature_alarms_enabled: bool
    high_temperature_diff_detected: _wrappers_pb2.BoolValue
    buzzer_state: FireProtect.BuzzerState
    subtype: FireProtect.Subtype
    def __init__(self, common_part: _Optional[_Union[_common_device_pb2.CommonDevicePart, _Mapping]] = ..., siren_triggers: _Optional[_Iterable[_Union[FireProtect.SirenTrigger, str]]] = ..., smoke_alarm_detected: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., temperature_alarm_detected: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., backup_battery_inserted: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., backup_battery_charge_ok: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., always_active: bool = ..., temperature_diff_detection_enabled: bool = ..., camera_malfunction: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., smoke_camera_dusty: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., high_temperature_alarms_enabled: bool = ..., high_temperature_diff_detected: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., buzzer_state: _Optional[_Union[FireProtect.BuzzerState, str]] = ..., subtype: _Optional[_Union[FireProtect.Subtype, str]] = ...) -> None: ...
