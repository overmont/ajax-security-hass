from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CurrentServiceAgreement(_message.Message):
    __slots__ = ("agreement_version", "url")
    AGREEMENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    agreement_version: str
    url: str
    def __init__(self, agreement_version: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
