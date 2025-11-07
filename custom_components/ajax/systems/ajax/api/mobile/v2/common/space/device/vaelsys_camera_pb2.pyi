from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VaelsysCamera(_message.Message):
    __slots__ = ("id", "vaelsys_camera_id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    VAELSYS_CAMERA_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    vaelsys_camera_id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., vaelsys_camera_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
