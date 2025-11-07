from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UserDeleteVerificationRequest(_message.Message):
    __slots__ = ("phone_token", "email_token")
    PHONE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EMAIL_TOKEN_FIELD_NUMBER: _ClassVar[int]
    phone_token: str
    email_token: str
    def __init__(self, phone_token: _Optional[str] = ..., email_token: _Optional[str] = ...) -> None: ...
