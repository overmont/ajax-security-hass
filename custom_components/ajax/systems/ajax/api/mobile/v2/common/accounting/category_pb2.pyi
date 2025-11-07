from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Category(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CATEGORY_UNSPECIFIED: _ClassVar[Category]
    CATEGORY_SECURITY: _ClassVar[Category]
    CATEGORY_MONITORING: _ClassVar[Category]
    CATEGORY_VIDEO: _ClassVar[Category]
    CATEGORY_TELEPHONY: _ClassVar[Category]
CATEGORY_UNSPECIFIED: Category
CATEGORY_SECURITY: Category
CATEGORY_MONITORING: Category
CATEGORY_VIDEO: Category
CATEGORY_TELEPHONY: Category
