from v3.mobilegwsvc.commonmodels.type import user_role_pb2 as _user_role_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfirmRestorePasswordRequest(_message.Message):
    __slots__ = ("email_or_phone", "user_role", "phone_token", "mail_token", "new_password_sha256_hash")
    EMAIL_OR_PHONE_FIELD_NUMBER: _ClassVar[int]
    USER_ROLE_FIELD_NUMBER: _ClassVar[int]
    PHONE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    MAIL_TOKEN_FIELD_NUMBER: _ClassVar[int]
    NEW_PASSWORD_SHA256_HASH_FIELD_NUMBER: _ClassVar[int]
    email_or_phone: str
    user_role: _user_role_pb2.UserRole
    phone_token: str
    mail_token: str
    new_password_sha256_hash: str
    def __init__(self, email_or_phone: _Optional[str] = ..., user_role: _Optional[_Union[_user_role_pb2.UserRole, str]] = ..., phone_token: _Optional[str] = ..., mail_token: _Optional[str] = ..., new_password_sha256_hash: _Optional[str] = ...) -> None: ...
