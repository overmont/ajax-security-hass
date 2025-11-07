from systems.ajax.protobuf.hub.device import common_device_pb2 as _common_device_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Button(_message.Message):
    __slots__ = ("common_part", "siren_triggers", "button_mode", "associated_user_id", "brightness", "false_press_filter", "custom_alarm_type", "subtype")
    class SirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_TRIGGER_INFO: _ClassVar[Button.SirenTrigger]
        SECURITY_BUTTON: _ClassVar[Button.SirenTrigger]
    NO_SIREN_TRIGGER_INFO: Button.SirenTrigger
    SECURITY_BUTTON: Button.SirenTrigger
    class ButtonMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_BUTTON_MODE_INFO: _ClassVar[Button.ButtonMode]
        PANIC_BUTTON: _ClassVar[Button.ButtonMode]
        SMART_BUTTON: _ClassVar[Button.ButtonMode]
        INTERCONNECT_DELAY: _ClassVar[Button.ButtonMode]
    NO_BUTTON_MODE_INFO: Button.ButtonMode
    PANIC_BUTTON: Button.ButtonMode
    SMART_BUTTON: Button.ButtonMode
    INTERCONNECT_DELAY: Button.ButtonMode
    class Brightness(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_BRIGHTNESS_INFO: _ClassVar[Button.Brightness]
        OFF: _ClassVar[Button.Brightness]
        LOW: _ClassVar[Button.Brightness]
        HIGH: _ClassVar[Button.Brightness]
    NO_BRIGHTNESS_INFO: Button.Brightness
    OFF: Button.Brightness
    LOW: Button.Brightness
    HIGH: Button.Brightness
    class FalsePressFilter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_FALSE_PRESS_FILTER_INFO: _ClassVar[Button.FalsePressFilter]
        DISABLED: _ClassVar[Button.FalsePressFilter]
        LONG_PUSH: _ClassVar[Button.FalsePressFilter]
        DOUBLE_CLICK: _ClassVar[Button.FalsePressFilter]
    NO_FALSE_PRESS_FILTER_INFO: Button.FalsePressFilter
    DISABLED: Button.FalsePressFilter
    LONG_PUSH: Button.FalsePressFilter
    DOUBLE_CLICK: Button.FalsePressFilter
    class CustomAlarmType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_CUSTOM_ALARM_TYPE: _ClassVar[Button.CustomAlarmType]
        BURGLARY: _ClassVar[Button.CustomAlarmType]
        FIRE: _ClassVar[Button.CustomAlarmType]
        MEDICAL: _ClassVar[Button.CustomAlarmType]
        PANIC: _ClassVar[Button.CustomAlarmType]
        GAS: _ClassVar[Button.CustomAlarmType]
    NO_CUSTOM_ALARM_TYPE: Button.CustomAlarmType
    BURGLARY: Button.CustomAlarmType
    FIRE: Button.CustomAlarmType
    MEDICAL: Button.CustomAlarmType
    PANIC: Button.CustomAlarmType
    GAS: Button.CustomAlarmType
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[Button.Subtype]
    NO_SUBTYPE: Button.Subtype
    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    BUTTON_MODE_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_USER_ID_FIELD_NUMBER: _ClassVar[int]
    BRIGHTNESS_FIELD_NUMBER: _ClassVar[int]
    FALSE_PRESS_FILTER_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ALARM_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    siren_triggers: _containers.RepeatedScalarFieldContainer[Button.SirenTrigger]
    button_mode: Button.ButtonMode
    associated_user_id: str
    brightness: Button.Brightness
    false_press_filter: Button.FalsePressFilter
    custom_alarm_type: Button.CustomAlarmType
    subtype: Button.Subtype
    def __init__(self, common_part: _Optional[_Union[_common_device_pb2.CommonDevicePart, _Mapping]] = ..., siren_triggers: _Optional[_Iterable[_Union[Button.SirenTrigger, str]]] = ..., button_mode: _Optional[_Union[Button.ButtonMode, str]] = ..., associated_user_id: _Optional[str] = ..., brightness: _Optional[_Union[Button.Brightness, str]] = ..., false_press_filter: _Optional[_Union[Button.FalsePressFilter, str]] = ..., custom_alarm_type: _Optional[_Union[Button.CustomAlarmType, str]] = ..., subtype: _Optional[_Union[Button.Subtype, str]] = ...) -> None: ...
