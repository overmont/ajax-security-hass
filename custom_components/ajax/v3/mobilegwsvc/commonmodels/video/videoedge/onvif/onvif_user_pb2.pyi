from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OnvifUser(_message.Message):
    __slots__ = ("name", "role")
    class OnvifUserRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ONVIF_USER_ROLE_UNSPECIFIED: _ClassVar[OnvifUser.OnvifUserRole]
        ONVIF_USER_ROLE_ADMIN: _ClassVar[OnvifUser.OnvifUserRole]
        ONVIF_USER_ROLE_OPERATOR: _ClassVar[OnvifUser.OnvifUserRole]
        ONVIF_USER_ROLE_USER: _ClassVar[OnvifUser.OnvifUserRole]
    ONVIF_USER_ROLE_UNSPECIFIED: OnvifUser.OnvifUserRole
    ONVIF_USER_ROLE_ADMIN: OnvifUser.OnvifUserRole
    ONVIF_USER_ROLE_OPERATOR: OnvifUser.OnvifUserRole
    ONVIF_USER_ROLE_USER: OnvifUser.OnvifUserRole
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    role: OnvifUser.OnvifUserRole
    def __init__(self, name: _Optional[str] = ..., role: _Optional[_Union[OnvifUser.OnvifUserRole, str]] = ...) -> None: ...
