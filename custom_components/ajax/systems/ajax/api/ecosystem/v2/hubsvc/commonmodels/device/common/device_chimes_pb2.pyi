from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceChimes(_message.Message):
    __slots__ = ("settings", "capabilities", "chimes_trigger_capabilities")
    class Sound(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SOUND_UNSPECIFIED: _ClassVar[DeviceChimes.Sound]
        SOUND_1: _ClassVar[DeviceChimes.Sound]
        SOUND_2: _ClassVar[DeviceChimes.Sound]
        SOUND_3: _ClassVar[DeviceChimes.Sound]
        SOUND_4: _ClassVar[DeviceChimes.Sound]
    SOUND_UNSPECIFIED: DeviceChimes.Sound
    SOUND_1: DeviceChimes.Sound
    SOUND_2: DeviceChimes.Sound
    SOUND_3: DeviceChimes.Sound
    SOUND_4: DeviceChimes.Sound
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[DeviceChimes.Capability]
        CAPABILITY_CHIMES: _ClassVar[DeviceChimes.Capability]
    CAPABILITY_UNSPECIFIED: DeviceChimes.Capability
    CAPABILITY_CHIMES: DeviceChimes.Capability
    class ChimesTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHIMES_TRIGGER_UNSPECIFIED: _ClassVar[DeviceChimes.ChimesTrigger]
        CHIMES_TRIGGER_REED: _ClassVar[DeviceChimes.ChimesTrigger]
        CHIMES_TRIGGER_EXTRA_CONTACT: _ClassVar[DeviceChimes.ChimesTrigger]
    CHIMES_TRIGGER_UNSPECIFIED: DeviceChimes.ChimesTrigger
    CHIMES_TRIGGER_REED: DeviceChimes.ChimesTrigger
    CHIMES_TRIGGER_EXTRA_CONTACT: DeviceChimes.ChimesTrigger
    class ChimesSettings(_message.Message):
        __slots__ = ("enabled_triggers", "chimes_sound")
        ENABLED_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
        CHIMES_SOUND_FIELD_NUMBER: _ClassVar[int]
        enabled_triggers: _containers.RepeatedScalarFieldContainer[DeviceChimes.ChimesTrigger]
        chimes_sound: DeviceChimes.Sound
        def __init__(self, enabled_triggers: _Optional[_Iterable[_Union[DeviceChimes.ChimesTrigger, str]]] = ..., chimes_sound: _Optional[_Union[DeviceChimes.Sound, str]] = ...) -> None: ...
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    CHIMES_TRIGGER_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    settings: DeviceChimes.ChimesSettings
    capabilities: _containers.RepeatedScalarFieldContainer[DeviceChimes.Capability]
    chimes_trigger_capabilities: _containers.RepeatedScalarFieldContainer[DeviceChimes.ChimesTrigger]
    def __init__(self, settings: _Optional[_Union[DeviceChimes.ChimesSettings, _Mapping]] = ..., capabilities: _Optional[_Iterable[_Union[DeviceChimes.Capability, str]]] = ..., chimes_trigger_capabilities: _Optional[_Iterable[_Union[DeviceChimes.ChimesTrigger, str]]] = ...) -> None: ...
