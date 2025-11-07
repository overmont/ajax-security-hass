from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Storage(_message.Message):
    __slots__ = ("temperature_threshold", "num_ports")
    TEMPERATURE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    NUM_PORTS_FIELD_NUMBER: _ClassVar[int]
    temperature_threshold: int
    num_ports: int
    def __init__(self, temperature_threshold: _Optional[int] = ..., num_ports: _Optional[int] = ...) -> None: ...
