from v3.mobilegwsvc.commonmodels.type import user_role_pb2 as _user_role_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotAvailableForUserError(_message.Message):
    __slots__ = ("user_role",)
    USER_ROLE_FIELD_NUMBER: _ClassVar[int]
    user_role: _user_role_pb2.UserRole
    def __init__(self, user_role: _Optional[_Union[_user_role_pb2.UserRole, str]] = ...) -> None: ...
