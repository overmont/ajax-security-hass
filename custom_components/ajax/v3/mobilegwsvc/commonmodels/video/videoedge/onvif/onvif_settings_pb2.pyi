from v3.mobilegwsvc.commonmodels.video.videoedge.onvif import onvif_user_pb2 as _onvif_user_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OnvifSettings(_message.Message):
    __slots__ = ("user_auth_enabled", "users", "http_port", "max_users_number")
    USER_AUTH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    HTTP_PORT_FIELD_NUMBER: _ClassVar[int]
    MAX_USERS_NUMBER_FIELD_NUMBER: _ClassVar[int]
    user_auth_enabled: bool
    users: _containers.RepeatedCompositeFieldContainer[_onvif_user_pb2.OnvifUser]
    http_port: int
    max_users_number: int
    def __init__(self, user_auth_enabled: bool = ..., users: _Optional[_Iterable[_Union[_onvif_user_pb2.OnvifUser, _Mapping]]] = ..., http_port: _Optional[int] = ..., max_users_number: _Optional[int] = ...) -> None: ...
