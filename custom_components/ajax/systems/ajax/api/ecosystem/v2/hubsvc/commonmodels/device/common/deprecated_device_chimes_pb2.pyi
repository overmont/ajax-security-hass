from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeprecatedDeviceChimes(_message.Message):
    __slots__ = ("sound", "capabilities")
    class Sound(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SOUND_UNSPECIFIED: _ClassVar[DeprecatedDeviceChimes.Sound]
        SOUND_1: _ClassVar[DeprecatedDeviceChimes.Sound]
        SOUND_2: _ClassVar[DeprecatedDeviceChimes.Sound]
        SOUND_3: _ClassVar[DeprecatedDeviceChimes.Sound]
        SOUND_4: _ClassVar[DeprecatedDeviceChimes.Sound]
    SOUND_UNSPECIFIED: DeprecatedDeviceChimes.Sound
    SOUND_1: DeprecatedDeviceChimes.Sound
    SOUND_2: DeprecatedDeviceChimes.Sound
    SOUND_3: DeprecatedDeviceChimes.Sound
    SOUND_4: DeprecatedDeviceChimes.Sound
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[DeprecatedDeviceChimes.Capability]
        CAPABILITY_CHIMES: _ClassVar[DeprecatedDeviceChimes.Capability]
    CAPABILITY_UNSPECIFIED: DeprecatedDeviceChimes.Capability
    CAPABILITY_CHIMES: DeprecatedDeviceChimes.Capability
    SOUND_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    sound: DeprecatedDeviceChimes.Sound
    capabilities: _containers.RepeatedScalarFieldContainer[DeprecatedDeviceChimes.Capability]
    def __init__(self, sound: _Optional[_Union[DeprecatedDeviceChimes.Sound, str]] = ..., capabilities: _Optional[_Iterable[_Union[DeprecatedDeviceChimes.Capability, str]]] = ...) -> None: ...
