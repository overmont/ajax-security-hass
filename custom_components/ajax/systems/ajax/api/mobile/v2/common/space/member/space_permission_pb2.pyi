from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SpacePermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPACE_PERMISSION_NONE: _ClassVar[SpacePermission]
    DELETE_MEMBERS: _ClassVar[SpacePermission]
    INVITE_MEMBERS: _ClassVar[SpacePermission]
    CHANGE_MEMBER_ROLE: _ClassVar[SpacePermission]
    CHANGE_MEMBER_PERMISSIONS: _ClassVar[SpacePermission]
    CHANGE_MEMBER_NOTIFICATION_SETTINGS: _ClassVar[SpacePermission]
    ARM: _ClassVar[SpacePermission]
    NIGHT_MODE_ARM_DISARM: _ClassVar[SpacePermission]
    DISARM: _ClassVar[SpacePermission]
    PANIC_BUTTON: _ClassVar[SpacePermission]
    ROOMS_EDIT: _ClassVar[SpacePermission]
    DEVICE_EDIT: _ClassVar[SpacePermission]
    GROUPS_EDIT: _ClassVar[SpacePermission]
    EVENT_VISIBILITY: _ClassVar[SpacePermission]
    STRUCTURE_VISIBILITY: _ClassVar[SpacePermission]
    SCENARIO_EDIT: _ClassVar[SpacePermission]
    PRIVACY_SETTINGS_ACCESS: _ClassVar[SpacePermission]
    SETTINGS_EDIT: _ClassVar[SpacePermission]
SPACE_PERMISSION_NONE: SpacePermission
DELETE_MEMBERS: SpacePermission
INVITE_MEMBERS: SpacePermission
CHANGE_MEMBER_ROLE: SpacePermission
CHANGE_MEMBER_PERMISSIONS: SpacePermission
CHANGE_MEMBER_NOTIFICATION_SETTINGS: SpacePermission
ARM: SpacePermission
NIGHT_MODE_ARM_DISARM: SpacePermission
DISARM: SpacePermission
PANIC_BUTTON: SpacePermission
ROOMS_EDIT: SpacePermission
DEVICE_EDIT: SpacePermission
GROUPS_EDIT: SpacePermission
EVENT_VISIBILITY: SpacePermission
STRUCTURE_VISIBILITY: SpacePermission
SCENARIO_EDIT: SpacePermission
PRIVACY_SETTINGS_ACCESS: SpacePermission
SETTINGS_EDIT: SpacePermission
