from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class HubUserType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NO_HUB_USER_TYPE_INFO: _ClassVar[HubUserType]
    USER: _ClassVar[HubUserType]
    PRO: _ClassVar[HubUserType]
    COMPANY: _ClassVar[HubUserType]
NO_HUB_USER_TYPE_INFO: HubUserType
USER: HubUserType
PRO: HubUserType
COMPANY: HubUserType
