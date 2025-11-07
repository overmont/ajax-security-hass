from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DealerInfo(_message.Message):
    __slots__ = ("company_hex_id", "name")
    COMPANY_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    company_hex_id: str
    name: str
    def __init__(self, company_hex_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
