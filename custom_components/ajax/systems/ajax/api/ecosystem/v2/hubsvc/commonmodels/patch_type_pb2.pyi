from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class PatchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PATCH_TYPE_UNSPECIFIED: _ClassVar[PatchType]
    PATCH_TYPE_ADDED: _ClassVar[PatchType]
    PATCH_TYPE_REMOVED: _ClassVar[PatchType]
PATCH_TYPE_UNSPECIFIED: PatchType
PATCH_TYPE_ADDED: PatchType
PATCH_TYPE_REMOVED: PatchType
