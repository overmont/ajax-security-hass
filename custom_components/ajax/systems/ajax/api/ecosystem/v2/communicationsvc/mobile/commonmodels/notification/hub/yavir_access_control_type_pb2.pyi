from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class YavirAccessControlType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    YAVIR_ACCESS_CONTROL_TYPE_UNSPECIFIED: _ClassVar[YavirAccessControlType]
    YAVIR_ACCESS_CONTROL_TYPE_KEYPAD: _ClassVar[YavirAccessControlType]
    YAVIR_ACCESS_CONTROL_TYPE_READER: _ClassVar[YavirAccessControlType]
YAVIR_ACCESS_CONTROL_TYPE_UNSPECIFIED: YavirAccessControlType
YAVIR_ACCESS_CONTROL_TYPE_KEYPAD: YavirAccessControlType
YAVIR_ACCESS_CONTROL_TYPE_READER: YavirAccessControlType
