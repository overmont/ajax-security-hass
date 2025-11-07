from systems.ajax.api.mobile.v2.common.hub.user import hub_user_type_pb2 as _hub_user_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HubUser(_message.Message):
    __slots__ = ("id", "role")
    ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    id: str
    role: _hub_user_type_pb2.HubUserType
    def __init__(self, id: _Optional[str] = ..., role: _Optional[_Union[_hub_user_type_pb2.HubUserType, str]] = ...) -> None: ...
