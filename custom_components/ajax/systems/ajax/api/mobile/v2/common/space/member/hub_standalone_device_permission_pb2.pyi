from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class HubStandaloneDevicePermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HUB_STANDALONE_DEVICE_PERMISSION_UNSPECIFIED: _ClassVar[HubStandaloneDevicePermission]
    HUB_ADV_PARAMS: _ClassVar[HubStandaloneDevicePermission]
    SET_STATE_COMMANDS: _ClassVar[HubStandaloneDevicePermission]
    FW_UPDATES_COMMANDS: _ClassVar[HubStandaloneDevicePermission]
    CAMERA_EDIT: _ClassVar[HubStandaloneDevicePermission]
    CAMERA_WATCH: _ClassVar[HubStandaloneDevicePermission]
    EDIT_CHIMES: _ClassVar[HubStandaloneDevicePermission]
    MUTE_FIRE_PROTECT: _ClassVar[HubStandaloneDevicePermission]
    BLE_ACCESS: _ClassVar[HubStandaloneDevicePermission]
    START_BUKHOOR: _ClassVar[HubStandaloneDevicePermission]
HUB_STANDALONE_DEVICE_PERMISSION_UNSPECIFIED: HubStandaloneDevicePermission
HUB_ADV_PARAMS: HubStandaloneDevicePermission
SET_STATE_COMMANDS: HubStandaloneDevicePermission
FW_UPDATES_COMMANDS: HubStandaloneDevicePermission
CAMERA_EDIT: HubStandaloneDevicePermission
CAMERA_WATCH: HubStandaloneDevicePermission
EDIT_CHIMES: HubStandaloneDevicePermission
MUTE_FIRE_PROTECT: HubStandaloneDevicePermission
BLE_ACCESS: HubStandaloneDevicePermission
START_BUKHOOR: HubStandaloneDevicePermission
