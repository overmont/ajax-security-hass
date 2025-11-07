from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.localuser import local_user_permissions_pb2 as _local_user_permissions_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateVideoEdgeLocalUserRequest(_message.Message):
    __slots__ = ("space_id", "video_edge_id", "name", "new_name", "permissions")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    name: str
    new_name: str
    permissions: _local_user_permissions_pb2.LocalUserPermissions
    def __init__(self, space_id: _Optional[str] = ..., video_edge_id: _Optional[str] = ..., name: _Optional[str] = ..., new_name: _Optional[str] = ..., permissions: _Optional[_Union[_local_user_permissions_pb2.LocalUserPermissions, _Mapping]] = ...) -> None: ...
