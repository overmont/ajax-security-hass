from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SearchCompanyRequest(_message.Message):
    __slots__ = ("email", "hub_hex_id")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    email: str
    hub_hex_id: str
    def __init__(self, email: _Optional[str] = ..., hub_hex_id: _Optional[str] = ...) -> None: ...
