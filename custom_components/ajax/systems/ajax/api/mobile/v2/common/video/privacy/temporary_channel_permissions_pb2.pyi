from systems.ajax.api.mobile.v2.common.video.privacy import channel_permission_pb2 as _channel_permission_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TemporaryChannelPermissions(_message.Message):
    __slots__ = ("permissions", "expire_at")
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_AT_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedScalarFieldContainer[_channel_permission_pb2.ChannelPermission]
    expire_at: _timestamp_pb2.Timestamp
    def __init__(self, permissions: _Optional[_Iterable[_Union[_channel_permission_pb2.ChannelPermission, str]]] = ..., expire_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
