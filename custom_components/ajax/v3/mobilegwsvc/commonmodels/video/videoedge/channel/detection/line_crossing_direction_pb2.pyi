from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class LineCrossingDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LINE_CROSSING_DIRECTION_UNSPECIFIED: _ClassVar[LineCrossingDirection]
    LINE_CROSSING_DIRECTION_LEFT_TO_RIGHT: _ClassVar[LineCrossingDirection]
    LINE_CROSSING_DIRECTION_RIGHT_TO_LEFT: _ClassVar[LineCrossingDirection]
    LINE_CROSSING_DIRECTION_ANY: _ClassVar[LineCrossingDirection]
LINE_CROSSING_DIRECTION_UNSPECIFIED: LineCrossingDirection
LINE_CROSSING_DIRECTION_LEFT_TO_RIGHT: LineCrossingDirection
LINE_CROSSING_DIRECTION_RIGHT_TO_LEFT: LineCrossingDirection
LINE_CROSSING_DIRECTION_ANY: LineCrossingDirection
