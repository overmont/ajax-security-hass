from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceMigrationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_MIGRATION_STATUS_UNSPECIFIED: _ClassVar[DeviceMigrationStatus]
    DEVICE_MIGRATION_STATUS_NOT_IN_MIGRATION: _ClassVar[DeviceMigrationStatus]
    DEVICE_MIGRATION_STATUS_IN_PROCESS: _ClassVar[DeviceMigrationStatus]
DEVICE_MIGRATION_STATUS_UNSPECIFIED: DeviceMigrationStatus
DEVICE_MIGRATION_STATUS_NOT_IN_MIGRATION: DeviceMigrationStatus
DEVICE_MIGRATION_STATUS_IN_PROCESS: DeviceMigrationStatus
