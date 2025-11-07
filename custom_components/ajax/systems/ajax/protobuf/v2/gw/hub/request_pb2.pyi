from systems.ajax.protobuf.auth import auth_pb2 as _auth_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetHubForMigrationRequest(_message.Message):
    __slots__ = ("user_id", "user_role", "hub_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ROLE_FIELD_NUMBER: _ClassVar[int]
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    user_role: _auth_pb2.UserRole
    hub_id: str
    def __init__(self, user_id: _Optional[str] = ..., user_role: _Optional[_Union[_auth_pb2.UserRole, str]] = ..., hub_id: _Optional[str] = ...) -> None: ...
