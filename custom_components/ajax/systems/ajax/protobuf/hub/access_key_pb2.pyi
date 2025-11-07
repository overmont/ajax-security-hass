from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AccessKeyUpdate(_message.Message):
    __slots__ = ("keyId",)
    KEYID_FIELD_NUMBER: _ClassVar[int]
    keyId: str
    def __init__(self, keyId: _Optional[str] = ...) -> None: ...
