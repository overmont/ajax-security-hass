from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WireInputs(_message.Message):
    __slots__ = ("quantity", "is_malfunction")
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    IS_MALFUNCTION_FIELD_NUMBER: _ClassVar[int]
    quantity: int
    is_malfunction: bool
    def __init__(self, quantity: _Optional[int] = ..., is_malfunction: bool = ...) -> None: ...
