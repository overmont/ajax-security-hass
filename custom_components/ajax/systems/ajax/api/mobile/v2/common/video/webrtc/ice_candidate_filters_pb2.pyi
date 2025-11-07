from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IceCandidateFilters(_message.Message):
    __slots__ = ("type_filter", "protocol_filter", "force_tcp_for_turn")
    class TypeFilter(_message.Message):
        __slots__ = ("host", "reflexive", "relay")
        HOST_FIELD_NUMBER: _ClassVar[int]
        REFLEXIVE_FIELD_NUMBER: _ClassVar[int]
        RELAY_FIELD_NUMBER: _ClassVar[int]
        host: bool
        reflexive: bool
        relay: bool
        def __init__(self, host: bool = ..., reflexive: bool = ..., relay: bool = ...) -> None: ...
    class ProtocolFilter(_message.Message):
        __slots__ = ("tcp", "udp")
        TCP_FIELD_NUMBER: _ClassVar[int]
        UDP_FIELD_NUMBER: _ClassVar[int]
        tcp: bool
        udp: bool
        def __init__(self, tcp: bool = ..., udp: bool = ...) -> None: ...
    TYPE_FILTER_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FILTER_FIELD_NUMBER: _ClassVar[int]
    FORCE_TCP_FOR_TURN_FIELD_NUMBER: _ClassVar[int]
    type_filter: IceCandidateFilters.TypeFilter
    protocol_filter: IceCandidateFilters.ProtocolFilter
    force_tcp_for_turn: bool
    def __init__(self, type_filter: _Optional[_Union[IceCandidateFilters.TypeFilter, _Mapping]] = ..., protocol_filter: _Optional[_Union[IceCandidateFilters.ProtocolFilter, _Mapping]] = ..., force_tcp_for_turn: bool = ...) -> None: ...
