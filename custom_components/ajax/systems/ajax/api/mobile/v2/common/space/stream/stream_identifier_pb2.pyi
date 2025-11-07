from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class StreamIdentifier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STREAM_IDENTIFIER_UNSPECIFIED: _ClassVar[StreamIdentifier]
    STREAM_IDENTIFIER_SPACE_INTERACTION_LOCK: _ClassVar[StreamIdentifier]
STREAM_IDENTIFIER_UNSPECIFIED: StreamIdentifier
STREAM_IDENTIFIER_SPACE_INTERACTION_LOCK: StreamIdentifier
