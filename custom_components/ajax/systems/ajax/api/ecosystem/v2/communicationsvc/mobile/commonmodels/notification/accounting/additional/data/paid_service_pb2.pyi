from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PaidService(_message.Message):
    __slots__ = ("id", "name_res_id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_RES_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name_res_id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name_res_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
