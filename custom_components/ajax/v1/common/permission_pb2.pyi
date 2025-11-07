from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Permission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NO_PERMISSION_INFO: _ClassVar[Permission]
    DELETE_USERS: _ClassVar[Permission]
    INVITE_USERS: _ClassVar[Permission]
    CHANGE_USER_ROLE: _ClassVar[Permission]
    CHANGE_USER_PERMISSIONS: _ClassVar[Permission]
    EDIT_NOTIFICATION_PERMISSION: _ClassVar[Permission]
    ARM: _ClassVar[Permission]
    PARTIAL_ARM: _ClassVar[Permission]
    DISARM: _ClassVar[Permission]
    PANIC_BUTTON: _ClassVar[Permission]
    ROOMS_EDIT: _ClassVar[Permission]
    DEVICE_EDIT: _ClassVar[Permission]
    HUB_ADV_PARAMS: _ClassVar[Permission]
    HUB_COMMON_PARAMS: _ClassVar[Permission]
    SET_STATE_COMMANDS: _ClassVar[Permission]
    FW_UPDATES_COMMANDS: _ClassVar[Permission]
    CAMERA_EDIT: _ClassVar[Permission]
    CAMERA_WATCH: _ClassVar[Permission]
    GROUPS_EDIT: _ClassVar[Permission]
    EVENT_VISIBILITY: _ClassVar[Permission]
    STRUCTURE_VISIBILITY: _ClassVar[Permission]
    SCENARIO_EDIT: _ClassVar[Permission]
    EDIT_CHIMES: _ClassVar[Permission]
    PRIVACY_SETTINGS_ACCESS: _ClassVar[Permission]
    MUTE_FIRE_PROTECT: _ClassVar[Permission]
    BLE_ACCESS: _ClassVar[Permission]
    START_BUKHOOR: _ClassVar[Permission]
NO_PERMISSION_INFO: Permission
DELETE_USERS: Permission
INVITE_USERS: Permission
CHANGE_USER_ROLE: Permission
CHANGE_USER_PERMISSIONS: Permission
EDIT_NOTIFICATION_PERMISSION: Permission
ARM: Permission
PARTIAL_ARM: Permission
DISARM: Permission
PANIC_BUTTON: Permission
ROOMS_EDIT: Permission
DEVICE_EDIT: Permission
HUB_ADV_PARAMS: Permission
HUB_COMMON_PARAMS: Permission
SET_STATE_COMMANDS: Permission
FW_UPDATES_COMMANDS: Permission
CAMERA_EDIT: Permission
CAMERA_WATCH: Permission
GROUPS_EDIT: Permission
EVENT_VISIBILITY: Permission
STRUCTURE_VISIBILITY: Permission
SCENARIO_EDIT: Permission
EDIT_CHIMES: Permission
PRIVACY_SETTINGS_ACCESS: Permission
MUTE_FIRE_PROTECT: Permission
BLE_ACCESS: Permission
START_BUKHOOR: Permission
