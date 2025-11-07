from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SlaveBusId(_message.Message):
    __slots__ = ("slave_bus_id",)
    SLAVE_BUS_ID_FIELD_NUMBER: _ClassVar[int]
    slave_bus_id: int
    def __init__(self, slave_bus_id: _Optional[int] = ...) -> None: ...
