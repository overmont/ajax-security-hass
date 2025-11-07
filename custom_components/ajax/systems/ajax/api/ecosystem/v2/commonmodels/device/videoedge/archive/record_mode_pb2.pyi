from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class RecordMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RECORD_MODE_UNSPECIFIED: _ClassVar[RecordMode]
    RECORD_MODE_DISABLED: _ClassVar[RecordMode]
    RECORD_MODE_PERMANENT: _ClassVar[RecordMode]
    RECORD_MODE_ON_DETECTION: _ClassVar[RecordMode]
RECORD_MODE_UNSPECIFIED: RecordMode
RECORD_MODE_DISABLED: RecordMode
RECORD_MODE_PERMANENT: RecordMode
RECORD_MODE_ON_DETECTION: RecordMode
