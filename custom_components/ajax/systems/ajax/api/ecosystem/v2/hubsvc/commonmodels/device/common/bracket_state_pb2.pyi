from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BracketStatePart(_message.Message):
    __slots__ = ("bracket_state", "capabilities")
    class BracketState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BRACKET_STATE_UNSPECIFIED: _ClassVar[BracketStatePart.BracketState]
        BRACKET_STATE_LOCKED: _ClassVar[BracketStatePart.BracketState]
        BRACKET_STATE_UNLOCKED: _ClassVar[BracketStatePart.BracketState]
    BRACKET_STATE_UNSPECIFIED: BracketStatePart.BracketState
    BRACKET_STATE_LOCKED: BracketStatePart.BracketState
    BRACKET_STATE_UNLOCKED: BracketStatePart.BracketState
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[BracketStatePart.Capability]
        CAPABILITY_BRACKET_STATE_SUPPORTED: _ClassVar[BracketStatePart.Capability]
    CAPABILITY_UNSPECIFIED: BracketStatePart.Capability
    CAPABILITY_BRACKET_STATE_SUPPORTED: BracketStatePart.Capability
    BRACKET_STATE_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    bracket_state: BracketStatePart.BracketState
    capabilities: _containers.RepeatedScalarFieldContainer[BracketStatePart.Capability]
    def __init__(self, bracket_state: _Optional[_Union[BracketStatePart.BracketState, str]] = ..., capabilities: _Optional[_Iterable[_Union[BracketStatePart.Capability, str]]] = ...) -> None: ...
