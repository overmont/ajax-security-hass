from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class FragmentError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FE_OTHER: _ClassVar[FragmentError]
    FE_OK: _ClassVar[FragmentError]
    FE_MISSING: _ClassVar[FragmentError]
    FE_FAILED: _ClassVar[FragmentError]
FE_OTHER: FragmentError
FE_OK: FragmentError
FE_MISSING: FragmentError
FE_FAILED: FragmentError
