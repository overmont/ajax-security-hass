from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class LightDeviceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LIGHT_DEVICE_STATE_UNSPECIFIED: _ClassVar[LightDeviceState]
    LIGHT_DEVICE_STATE_LOCKED: _ClassVar[LightDeviceState]
    LIGHT_DEVICE_STATE_SUSPENDED: _ClassVar[LightDeviceState]
    LIGHT_DEVICE_STATE_ADDING_FAILED: _ClassVar[LightDeviceState]
    LIGHT_DEVICE_STATE_TRANSFERRING_FAILED: _ClassVar[LightDeviceState]
    LIGHT_DEVICE_STATE_ADDING: _ClassVar[LightDeviceState]
    LIGHT_DEVICE_STATE_TRANSFERRING: _ClassVar[LightDeviceState]
    LIGHT_DEVICE_STATE_BATTERY_SAVING: _ClassVar[LightDeviceState]
    LIGHT_DEVICE_STATE_NOT_MIGRATED: _ClassVar[LightDeviceState]
    LIGHT_DEVICE_STATE_OFFLINE: _ClassVar[LightDeviceState]
    LIGHT_DEVICE_STATE_UPDATING: _ClassVar[LightDeviceState]
    LIGHT_DEVICE_STATE_WALK_TEST: _ClassVar[LightDeviceState]
LIGHT_DEVICE_STATE_UNSPECIFIED: LightDeviceState
LIGHT_DEVICE_STATE_LOCKED: LightDeviceState
LIGHT_DEVICE_STATE_SUSPENDED: LightDeviceState
LIGHT_DEVICE_STATE_ADDING_FAILED: LightDeviceState
LIGHT_DEVICE_STATE_TRANSFERRING_FAILED: LightDeviceState
LIGHT_DEVICE_STATE_ADDING: LightDeviceState
LIGHT_DEVICE_STATE_TRANSFERRING: LightDeviceState
LIGHT_DEVICE_STATE_BATTERY_SAVING: LightDeviceState
LIGHT_DEVICE_STATE_NOT_MIGRATED: LightDeviceState
LIGHT_DEVICE_STATE_OFFLINE: LightDeviceState
LIGHT_DEVICE_STATE_UPDATING: LightDeviceState
LIGHT_DEVICE_STATE_WALK_TEST: LightDeviceState
