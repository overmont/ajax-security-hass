from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.onvif import onvif_user_pb2 as _onvif_user_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateVideoEdgeOnvifUserRequest(_message.Message):
    __slots__ = ("space_id", "video_edge_id", "username", "new_username", "role")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    NEW_USERNAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    username: str
    new_username: str
    role: _onvif_user_pb2.OnvifUser.OnvifUserRole
    def __init__(self, space_id: _Optional[str] = ..., video_edge_id: _Optional[str] = ..., username: _Optional[str] = ..., new_username: _Optional[str] = ..., role: _Optional[_Union[_onvif_user_pb2.OnvifUser.OnvifUserRole, str]] = ...) -> None: ...
