from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PtzMove(_message.Message):
    __slots__ = ("speed_x", "speed_y")
    SPEED_X_FIELD_NUMBER: _ClassVar[int]
    SPEED_Y_FIELD_NUMBER: _ClassVar[int]
    speed_x: int
    speed_y: int
    def __init__(self, speed_x: _Optional[int] = ..., speed_y: _Optional[int] = ...) -> None: ...

class PtzZoom(_message.Message):
    __slots__ = ("speed",)
    SPEED_FIELD_NUMBER: _ClassVar[int]
    speed: int
    def __init__(self, speed: _Optional[int] = ...) -> None: ...

class PtzFocus(_message.Message):
    __slots__ = ("speed",)
    SPEED_FIELD_NUMBER: _ClassVar[int]
    speed: int
    def __init__(self, speed: _Optional[int] = ...) -> None: ...

class PtzStop(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
