from v3.mobilegwsvc.commonmodels.video.videoedge.localuser import local_user_permissions_pb2 as _local_user_permissions_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LocalUser(_message.Message):
    __slots__ = ("name", "permissions")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    permissions: _local_user_permissions_pb2.LocalUserPermissions
    def __init__(self, name: _Optional[str] = ..., permissions: _Optional[_Union[_local_user_permissions_pb2.LocalUserPermissions, _Mapping]] = ...) -> None: ...
