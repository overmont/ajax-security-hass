from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class FragmentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FRAGMENT_STATUS_UNSPECIFIED: _ClassVar[FragmentStatus]
    FRAGMENT_STATUS_OK: _ClassVar[FragmentStatus]
    FRAGMENT_STATUS_MISSING: _ClassVar[FragmentStatus]
    FRAGMENT_STATUS_FAILED: _ClassVar[FragmentStatus]
FRAGMENT_STATUS_UNSPECIFIED: FragmentStatus
FRAGMENT_STATUS_OK: FragmentStatus
FRAGMENT_STATUS_MISSING: FragmentStatus
FRAGMENT_STATUS_FAILED: FragmentStatus
