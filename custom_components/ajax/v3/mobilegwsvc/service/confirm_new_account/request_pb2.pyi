from v3.mobilegwsvc.commonmodels.type import user_role_pb2 as _user_role_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfirmNewAccountRequest(_message.Message):
    __slots__ = ("user_role", "email", "phone_token", "email_token")
    USER_ROLE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EMAIL_TOKEN_FIELD_NUMBER: _ClassVar[int]
    user_role: _user_role_pb2.UserRole
    email: str
    phone_token: str
    email_token: str
    def __init__(self, user_role: _Optional[_Union[_user_role_pb2.UserRole, str]] = ..., email: _Optional[str] = ..., phone_token: _Optional[str] = ..., email_token: _Optional[str] = ...) -> None: ...
