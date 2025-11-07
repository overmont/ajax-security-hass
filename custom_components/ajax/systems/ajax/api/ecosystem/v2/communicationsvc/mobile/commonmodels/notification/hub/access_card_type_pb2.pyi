from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AccessCardType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACCESS_CARD_TYPE_UNSPECIFIED: _ClassVar[AccessCardType]
    ACCESS_CARD_TYPE_CARD: _ClassVar[AccessCardType]
    ACCESS_CARD_TYPE_TAG: _ClassVar[AccessCardType]
ACCESS_CARD_TYPE_UNSPECIFIED: AccessCardType
ACCESS_CARD_TYPE_CARD: AccessCardType
ACCESS_CARD_TYPE_TAG: AccessCardType
