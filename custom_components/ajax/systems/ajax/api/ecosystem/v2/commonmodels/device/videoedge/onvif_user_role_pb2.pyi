from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class OnvifUserRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ONVIF_USER_ROLE_UNSPECIFIED: _ClassVar[OnvifUserRole]
    ONVIF_USER_ROLE_ADMIN: _ClassVar[OnvifUserRole]
    ONVIF_USER_ROLE_OPERATOR: _ClassVar[OnvifUserRole]
    ONVIF_USER_ROLE_USER: _ClassVar[OnvifUserRole]
ONVIF_USER_ROLE_UNSPECIFIED: OnvifUserRole
ONVIF_USER_ROLE_ADMIN: OnvifUserRole
ONVIF_USER_ROLE_OPERATOR: OnvifUserRole
ONVIF_USER_ROLE_USER: OnvifUserRole
