from systems.ajax.api.mobile.v2.common.space.member import space_permission_pb2 as _space_permission_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpacePermissions(_message.Message):
    __slots__ = ("permissions", "has_system_settings_permissions", "expiredAt")
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    HAS_SYSTEM_SETTINGS_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    EXPIREDAT_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedScalarFieldContainer[_space_permission_pb2.SpacePermission]
    has_system_settings_permissions: bool
    expiredAt: _timestamp_pb2.Timestamp
    def __init__(self, permissions: _Optional[_Iterable[_Union[_space_permission_pb2.SpacePermission, str]]] = ..., has_system_settings_permissions: bool = ..., expiredAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
