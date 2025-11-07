from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HubPermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NO_PERMISSION_INFO: _ClassVar[HubPermission]
    DELETE_USERS: _ClassVar[HubPermission]
    INVITE_USERS: _ClassVar[HubPermission]
    CHANGE_USER_ROLE: _ClassVar[HubPermission]
    CHANGE_USER_PERMISSIONS: _ClassVar[HubPermission]
    EDIT_NOTIFICATION_PERMISSION: _ClassVar[HubPermission]
    ARM: _ClassVar[HubPermission]
    PARTIAL_ARM: _ClassVar[HubPermission]
    DISARM: _ClassVar[HubPermission]
    PANIC_BUTTON: _ClassVar[HubPermission]
    ROOMS_EDIT: _ClassVar[HubPermission]
    DEVICE_EDIT: _ClassVar[HubPermission]
    HUB_ADV_PARAMS: _ClassVar[HubPermission]
    HUB_COMMON_PARAMS: _ClassVar[HubPermission]
    SET_STATE_COMMANDS: _ClassVar[HubPermission]
    FW_UPDATES_COMMANDS: _ClassVar[HubPermission]
    CAMERA_EDIT: _ClassVar[HubPermission]
    CAMERA_WATCH: _ClassVar[HubPermission]
    GROUPS_EDIT: _ClassVar[HubPermission]
    EVENT_VISIBILITY: _ClassVar[HubPermission]
    STRUCTURE_VISIBILITY: _ClassVar[HubPermission]
    SCENARIO_EDIT: _ClassVar[HubPermission]
    EDIT_CHIMES: _ClassVar[HubPermission]
    PRIVACY_SETTINGS_ACCESS: _ClassVar[HubPermission]
    MUTE_FIRE_PROTECT: _ClassVar[HubPermission]
    BLE_ACCESS: _ClassVar[HubPermission]
    START_BUKHOOR: _ClassVar[HubPermission]
NO_PERMISSION_INFO: HubPermission
DELETE_USERS: HubPermission
INVITE_USERS: HubPermission
CHANGE_USER_ROLE: HubPermission
CHANGE_USER_PERMISSIONS: HubPermission
EDIT_NOTIFICATION_PERMISSION: HubPermission
ARM: HubPermission
PARTIAL_ARM: HubPermission
DISARM: HubPermission
PANIC_BUTTON: HubPermission
ROOMS_EDIT: HubPermission
DEVICE_EDIT: HubPermission
HUB_ADV_PARAMS: HubPermission
HUB_COMMON_PARAMS: HubPermission
SET_STATE_COMMANDS: HubPermission
FW_UPDATES_COMMANDS: HubPermission
CAMERA_EDIT: HubPermission
CAMERA_WATCH: HubPermission
GROUPS_EDIT: HubPermission
EVENT_VISIBILITY: HubPermission
STRUCTURE_VISIBILITY: HubPermission
SCENARIO_EDIT: HubPermission
EDIT_CHIMES: HubPermission
PRIVACY_SETTINGS_ACCESS: HubPermission
MUTE_FIRE_PROTECT: HubPermission
BLE_ACCESS: HubPermission
START_BUKHOOR: HubPermission

class HubPermissions(_message.Message):
    __slots__ = ("permissions",)
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedScalarFieldContainer[HubPermission]
    def __init__(self, permissions: _Optional[_Iterable[_Union[HubPermission, str]]] = ...) -> None: ...
