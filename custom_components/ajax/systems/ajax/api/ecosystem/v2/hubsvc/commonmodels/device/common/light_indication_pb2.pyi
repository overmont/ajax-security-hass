from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LightIndication(_message.Message):
    __slots__ = ("light_indication_settings", "capabilities")
    class Indication(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INDICATION_UNSPECIFIED: _ClassVar[LightIndication.Indication]
        INDICATION_OFF: _ClassVar[LightIndication.Indication]
        INDICATION_ARMED: _ClassVar[LightIndication.Indication]
        INDICATION_ALWAYS: _ClassVar[LightIndication.Indication]
    INDICATION_UNSPECIFIED: LightIndication.Indication
    INDICATION_OFF: LightIndication.Indication
    INDICATION_ARMED: LightIndication.Indication
    INDICATION_ALWAYS: LightIndication.Indication
    class ExternalLedMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXTERNAL_LED_MODE_UNSPECIFIED: _ClassVar[LightIndication.ExternalLedMode]
        EXTERNAL_LED_MODE_BLINK: _ClassVar[LightIndication.ExternalLedMode]
        EXTERNAL_LED_MODE_SHINE_CONSTANTLY: _ClassVar[LightIndication.ExternalLedMode]
    EXTERNAL_LED_MODE_UNSPECIFIED: LightIndication.ExternalLedMode
    EXTERNAL_LED_MODE_BLINK: LightIndication.ExternalLedMode
    EXTERNAL_LED_MODE_SHINE_CONSTANTLY: LightIndication.ExternalLedMode
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[LightIndication.Capability]
        CAPABILITY_NEW_ARM_MODE_INDICATION: _ClassVar[LightIndication.Capability]
        CAPABILITY_EXTERNAL_LED_INDICATION_TYPE: _ClassVar[LightIndication.Capability]
    CAPABILITY_UNSPECIFIED: LightIndication.Capability
    CAPABILITY_NEW_ARM_MODE_INDICATION: LightIndication.Capability
    CAPABILITY_EXTERNAL_LED_INDICATION_TYPE: LightIndication.Capability
    class LightIndicationSettings(_message.Message):
        __slots__ = ("light_indication", "external_led_mode")
        LIGHT_INDICATION_FIELD_NUMBER: _ClassVar[int]
        EXTERNAL_LED_MODE_FIELD_NUMBER: _ClassVar[int]
        light_indication: LightIndication.Indication
        external_led_mode: LightIndication.ExternalLedMode
        def __init__(self, light_indication: _Optional[_Union[LightIndication.Indication, str]] = ..., external_led_mode: _Optional[_Union[LightIndication.ExternalLedMode, str]] = ...) -> None: ...
    LIGHT_INDICATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    light_indication_settings: LightIndication.LightIndicationSettings
    capabilities: _containers.RepeatedScalarFieldContainer[LightIndication.Capability]
    def __init__(self, light_indication_settings: _Optional[_Union[LightIndication.LightIndicationSettings, _Mapping]] = ..., capabilities: _Optional[_Iterable[_Union[LightIndication.Capability, str]]] = ...) -> None: ...
