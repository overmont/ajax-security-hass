from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OWNER: _ClassVar[Role]
    SENIOR_CMS_ENGINEER: _ClassVar[Role]
    CMS_ENGINEER: _ClassVar[Role]
    HEAD_OF_INSTALLERS: _ClassVar[Role]
    INSTALLER: _ClassVar[Role]
    HEAD_OF_OPERATORS: _ClassVar[Role]
    OPERATOR: _ClassVar[Role]
    RAPID_RESPONSE_TEAM: _ClassVar[Role]
    SUBSCRIPTION_MANAGER: _ClassVar[Role]
    SENIOR_SUBSCRIPTION_MANAGER: _ClassVar[Role]
OWNER: Role
SENIOR_CMS_ENGINEER: Role
CMS_ENGINEER: Role
HEAD_OF_INSTALLERS: Role
INSTALLER: Role
HEAD_OF_OPERATORS: Role
OPERATOR: Role
RAPID_RESPONSE_TEAM: Role
SUBSCRIPTION_MANAGER: Role
SENIOR_SUBSCRIPTION_MANAGER: Role
