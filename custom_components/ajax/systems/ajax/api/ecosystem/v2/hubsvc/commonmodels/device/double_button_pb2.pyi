from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import common_button_part_pb2 as _common_button_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_battery_pb2 as _device_battery_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import alarm_verification_pb2 as _alarm_verification_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DoubleButton(_message.Message):
    __slots__ = ("common_button_part", "device_battery_without_charging", "alarm_verification", "siren_triggers")
    class SirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SIREN_TRIGGER_UNSPECIFIED: _ClassVar[DoubleButton.SirenTrigger]
        SIREN_TRIGGER_SECURITY_BUTTON: _ClassVar[DoubleButton.SirenTrigger]
    SIREN_TRIGGER_UNSPECIFIED: DoubleButton.SirenTrigger
    SIREN_TRIGGER_SECURITY_BUTTON: DoubleButton.SirenTrigger
    COMMON_BUTTON_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_WITHOUT_CHARGING_FIELD_NUMBER: _ClassVar[int]
    ALARM_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    common_button_part: _common_button_part_pb2.CommonButtonPart
    device_battery_without_charging: _device_battery_pb2.DeviceBatteryWithoutCharging
    alarm_verification: _alarm_verification_pb2.AlarmVerification
    siren_triggers: _containers.RepeatedScalarFieldContainer[DoubleButton.SirenTrigger]
    def __init__(self, common_button_part: _Optional[_Union[_common_button_part_pb2.CommonButtonPart, _Mapping]] = ..., device_battery_without_charging: _Optional[_Union[_device_battery_pb2.DeviceBatteryWithoutCharging, _Mapping]] = ..., alarm_verification: _Optional[_Union[_alarm_verification_pb2.AlarmVerification, _Mapping]] = ..., siren_triggers: _Optional[_Iterable[_Union[DoubleButton.SirenTrigger, str]]] = ...) -> None: ...
