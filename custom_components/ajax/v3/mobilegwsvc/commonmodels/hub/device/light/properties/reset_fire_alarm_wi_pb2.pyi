from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ResetFireAlarmWi(_message.Message):
    __slots__ = ("wire_input_ids",)
    WIRE_INPUT_IDS_FIELD_NUMBER: _ClassVar[int]
    wire_input_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, wire_input_ids: _Optional[_Iterable[str]] = ...) -> None: ...
