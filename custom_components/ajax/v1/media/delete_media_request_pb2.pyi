from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteMediaRequest(_message.Message):
    __slots__ = ("facility_id", "media_info_id")
    FACILITY_ID_FIELD_NUMBER: _ClassVar[int]
    MEDIA_INFO_ID_FIELD_NUMBER: _ClassVar[int]
    facility_id: str
    media_info_id: str
    def __init__(self, facility_id: _Optional[str] = ..., media_info_id: _Optional[str] = ...) -> None: ...
