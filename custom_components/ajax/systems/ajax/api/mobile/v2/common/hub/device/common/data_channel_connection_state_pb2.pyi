from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DataChannelConnectionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATA_CHANNEL_CONNECTION_STATE_UNSPECIFIED: _ClassVar[DataChannelConnectionState]
    DATA_CHANNEL_CONNECTION_STATE_OFFLINE: _ClassVar[DataChannelConnectionState]
    DATA_CHANNEL_CONNECTION_STATE_ONLINE: _ClassVar[DataChannelConnectionState]
DATA_CHANNEL_CONNECTION_STATE_UNSPECIFIED: DataChannelConnectionState
DATA_CHANNEL_CONNECTION_STATE_OFFLINE: DataChannelConnectionState
DATA_CHANNEL_CONNECTION_STATE_ONLINE: DataChannelConnectionState
