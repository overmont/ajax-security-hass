from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FireZones(_message.Message):
    __slots__ = ("quantity",)
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    quantity: int
    def __init__(self, quantity: _Optional[int] = ...) -> None: ...
