from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ConnectionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONNECTION_STATUS_UNSPECIFIED: _ClassVar[ConnectionStatus]
    CONNECTION_STATUS_ONLINE: _ClassVar[ConnectionStatus]
    CONNECTION_STATUS_OFFLINE: _ClassVar[ConnectionStatus]
CONNECTION_STATUS_UNSPECIFIED: ConnectionStatus
CONNECTION_STATUS_ONLINE: ConnectionStatus
CONNECTION_STATUS_OFFLINE: ConnectionStatus
