from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BypassPart(_message.Message):
    __slots__ = ("bypass_mode", "capabilities")
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[BypassPart.Capability]
        CAPABILITY_BYPASS: _ClassVar[BypassPart.Capability]
        CAPABILITY_TAMPER_BYPASS: _ClassVar[BypassPart.Capability]
        CAPABILITY_ONE_TIME_BYPASS: _ClassVar[BypassPart.Capability]
    CAPABILITY_UNSPECIFIED: BypassPart.Capability
    CAPABILITY_BYPASS: BypassPart.Capability
    CAPABILITY_TAMPER_BYPASS: BypassPart.Capability
    CAPABILITY_ONE_TIME_BYPASS: BypassPart.Capability
    class BypassMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BYPASS_MODE_UNSPECIFIED: _ClassVar[BypassPart.BypassMode]
        BYPASS_MODE_DISABLED: _ClassVar[BypassPart.BypassMode]
        BYPASS_MODE_ENABLED_ENGINEER_BYPASS: _ClassVar[BypassPart.BypassMode]
        BYPASS_MODE_ENABLED_TAMPER_BYPASS: _ClassVar[BypassPart.BypassMode]
        BYPASS_MODE_AUTO_BYPASS_BY_COUNT: _ClassVar[BypassPart.BypassMode]
        BYPASS_MODE_AUTO_BYPASS_BY_ACTIVE: _ClassVar[BypassPart.BypassMode]
        BYPASS_MODE_ONETIME_FULL_ENABLED: _ClassVar[BypassPart.BypassMode]
        BYPASS_MODE_ONETIME_TAMPER_ENABLED: _ClassVar[BypassPart.BypassMode]
    BYPASS_MODE_UNSPECIFIED: BypassPart.BypassMode
    BYPASS_MODE_DISABLED: BypassPart.BypassMode
    BYPASS_MODE_ENABLED_ENGINEER_BYPASS: BypassPart.BypassMode
    BYPASS_MODE_ENABLED_TAMPER_BYPASS: BypassPart.BypassMode
    BYPASS_MODE_AUTO_BYPASS_BY_COUNT: BypassPart.BypassMode
    BYPASS_MODE_AUTO_BYPASS_BY_ACTIVE: BypassPart.BypassMode
    BYPASS_MODE_ONETIME_FULL_ENABLED: BypassPart.BypassMode
    BYPASS_MODE_ONETIME_TAMPER_ENABLED: BypassPart.BypassMode
    BYPASS_MODE_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    bypass_mode: _containers.RepeatedScalarFieldContainer[BypassPart.BypassMode]
    capabilities: _containers.RepeatedScalarFieldContainer[BypassPart.Capability]
    def __init__(self, bypass_mode: _Optional[_Iterable[_Union[BypassPart.BypassMode, str]]] = ..., capabilities: _Optional[_Iterable[_Union[BypassPart.Capability, str]]] = ...) -> None: ...
