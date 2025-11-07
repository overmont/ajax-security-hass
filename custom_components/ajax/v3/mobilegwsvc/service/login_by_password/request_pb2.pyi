from v3.mobilegwsvc.commonmodels.type import user_role_pb2 as _user_role_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoginByPasswordRequest(_message.Message):
    __slots__ = ("email", "password_sha256_hash", "user_role")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_SHA256_HASH_FIELD_NUMBER: _ClassVar[int]
    USER_ROLE_FIELD_NUMBER: _ClassVar[int]
    email: str
    password_sha256_hash: str
    user_role: _user_role_pb2.UserRole
    def __init__(self, email: _Optional[str] = ..., password_sha256_hash: _Optional[str] = ..., user_role: _Optional[_Union[_user_role_pb2.UserRole, str]] = ...) -> None: ...
