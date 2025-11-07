from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Sensitivity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SENSITIVITY_UNSPECIFIED: _ClassVar[Sensitivity]
    SENSITIVITY_LOW: _ClassVar[Sensitivity]
    SENSITIVITY_NORMAL: _ClassVar[Sensitivity]
    SENSITIVITY_HIGH: _ClassVar[Sensitivity]
    SENSITIVITY_VERY_HIGH: _ClassVar[Sensitivity]
SENSITIVITY_UNSPECIFIED: Sensitivity
SENSITIVITY_LOW: Sensitivity
SENSITIVITY_NORMAL: Sensitivity
SENSITIVITY_HIGH: Sensitivity
SENSITIVITY_VERY_HIGH: Sensitivity
