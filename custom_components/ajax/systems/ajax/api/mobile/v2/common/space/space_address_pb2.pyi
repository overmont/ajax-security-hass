from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceAddress(_message.Message):
    __slots__ = ("location", "city", "region", "country", "postcode")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    POSTCODE_FIELD_NUMBER: _ClassVar[int]
    location: str
    city: str
    region: str
    country: str
    postcode: str
    def __init__(self, location: _Optional[str] = ..., city: _Optional[str] = ..., region: _Optional[str] = ..., country: _Optional[str] = ..., postcode: _Optional[str] = ...) -> None: ...
