from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OnvifInfo(_message.Message):
    __slots__ = ("user_auth_enabled",)
    USER_AUTH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    user_auth_enabled: bool
    def __init__(self, user_auth_enabled: bool = ...) -> None: ...
