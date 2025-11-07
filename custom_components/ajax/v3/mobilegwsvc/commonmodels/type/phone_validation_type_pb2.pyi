from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class PhoneValidationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PHONE_VALIDATION_TYPE_UNSPECIFIED: _ClassVar[PhoneValidationType]
    PHONE_VALIDATION_TYPE_SMS: _ClassVar[PhoneValidationType]
    PHONE_VALIDATION_TYPE_CALL: _ClassVar[PhoneValidationType]
PHONE_VALIDATION_TYPE_UNSPECIFIED: PhoneValidationType
PHONE_VALIDATION_TYPE_SMS: PhoneValidationType
PHONE_VALIDATION_TYPE_CALL: PhoneValidationType
