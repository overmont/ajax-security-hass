from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Address(_message.Message):
    __slots__ = ("country", "state", "city", "zip_code", "address_line1", "address_line2")
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    ZIP_CODE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_LINE1_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_LINE2_FIELD_NUMBER: _ClassVar[int]
    country: str
    state: str
    city: str
    zip_code: str
    address_line1: str
    address_line2: str
    def __init__(self, country: _Optional[str] = ..., state: _Optional[str] = ..., city: _Optional[str] = ..., zip_code: _Optional[str] = ..., address_line1: _Optional[str] = ..., address_line2: _Optional[str] = ...) -> None: ...
