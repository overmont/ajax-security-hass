from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FacilityAccessRightsRequest(_message.Message):
    __slots__ = ("facility_id", "seconds")
    FACILITY_ID_FIELD_NUMBER: _ClassVar[int]
    SECONDS_FIELD_NUMBER: _ClassVar[int]
    facility_id: str
    seconds: int
    def __init__(self, facility_id: _Optional[str] = ..., seconds: _Optional[int] = ...) -> None: ...
