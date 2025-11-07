from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LedIndicationPart(_message.Message):
    __slots__ = ("alarm_led_indication", "capabilities", "led_brightness")
    class AlarmLedIndication(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALARM_LED_INDICATION_UNSPECIFIED: _ClassVar[LedIndicationPart.AlarmLedIndication]
        ALARM_LED_INDICATION_DISABLED: _ClassVar[LedIndicationPart.AlarmLedIndication]
        ALARM_LED_INDICATION_ENABLED: _ClassVar[LedIndicationPart.AlarmLedIndication]
    ALARM_LED_INDICATION_UNSPECIFIED: LedIndicationPart.AlarmLedIndication
    ALARM_LED_INDICATION_DISABLED: LedIndicationPart.AlarmLedIndication
    ALARM_LED_INDICATION_ENABLED: LedIndicationPart.AlarmLedIndication
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[LedIndicationPart.Capability]
        CAPABILITY_ALARM_LED_INDICATION: _ClassVar[LedIndicationPart.Capability]
        CAPABILITY_LED_BRIGHTNESS: _ClassVar[LedIndicationPart.Capability]
    CAPABILITY_UNSPECIFIED: LedIndicationPart.Capability
    CAPABILITY_ALARM_LED_INDICATION: LedIndicationPart.Capability
    CAPABILITY_LED_BRIGHTNESS: LedIndicationPart.Capability
    class LedIndicationPartSettings(_message.Message):
        __slots__ = ("alarm_led_indication", "led_brightness")
        ALARM_LED_INDICATION_FIELD_NUMBER: _ClassVar[int]
        LED_BRIGHTNESS_FIELD_NUMBER: _ClassVar[int]
        alarm_led_indication: LedIndicationPart.AlarmLedIndication
        led_brightness: LedIndicationPart.LedBrightness
        def __init__(self, alarm_led_indication: _Optional[_Union[LedIndicationPart.AlarmLedIndication, str]] = ..., led_brightness: _Optional[_Union[LedIndicationPart.LedBrightness, _Mapping]] = ...) -> None: ...
    class LedBrightness(_message.Message):
        __slots__ = ("smooth_level",)
        SMOOTH_LEVEL_FIELD_NUMBER: _ClassVar[int]
        smooth_level: LedIndicationPart.SmoothLevel
        def __init__(self, smooth_level: _Optional[_Union[LedIndicationPart.SmoothLevel, _Mapping]] = ...) -> None: ...
    class SmoothLevel(_message.Message):
        __slots__ = ("current_level", "smooth_limits")
        CURRENT_LEVEL_FIELD_NUMBER: _ClassVar[int]
        SMOOTH_LIMITS_FIELD_NUMBER: _ClassVar[int]
        current_level: int
        smooth_limits: LedIndicationPart.SmoothLimits
        def __init__(self, current_level: _Optional[int] = ..., smooth_limits: _Optional[_Union[LedIndicationPart.SmoothLimits, _Mapping]] = ...) -> None: ...
    class SmoothLimits(_message.Message):
        __slots__ = ("min", "max")
        MIN_FIELD_NUMBER: _ClassVar[int]
        MAX_FIELD_NUMBER: _ClassVar[int]
        min: int
        max: int
        def __init__(self, min: _Optional[int] = ..., max: _Optional[int] = ...) -> None: ...
    ALARM_LED_INDICATION_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    LED_BRIGHTNESS_FIELD_NUMBER: _ClassVar[int]
    alarm_led_indication: LedIndicationPart.AlarmLedIndication
    capabilities: _containers.RepeatedScalarFieldContainer[LedIndicationPart.Capability]
    led_brightness: LedIndicationPart.LedBrightness
    def __init__(self, alarm_led_indication: _Optional[_Union[LedIndicationPart.AlarmLedIndication, str]] = ..., capabilities: _Optional[_Iterable[_Union[LedIndicationPart.Capability, str]]] = ..., led_brightness: _Optional[_Union[LedIndicationPart.LedBrightness, _Mapping]] = ...) -> None: ...
