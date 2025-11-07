from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class RestorePermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NO_RESTORE_PERMISSION_INFO: _ClassVar[RestorePermission]
    RESTORE_CONFIRMED_ALARMS: _ClassVar[RestorePermission]
    RESTORE_CONFIRMED_HU_ALARMS: _ClassVar[RestorePermission]
    RESTORE_UNCONFIRMED_ALARMS: _ClassVar[RestorePermission]
    RESTORE_UNCONFIRMED_HU_ALARMS: _ClassVar[RestorePermission]
    RESTORE_TAMPER_ACTIVATION: _ClassVar[RestorePermission]
    RESTORE_EXTERNAL_POWER_ACTIVATION: _ClassVar[RestorePermission]
    RESTORE_ATS_ACTIVATION: _ClassVar[RestorePermission]
    RESTORE_OTHER_FAULT_ACTIVATION: _ClassVar[RestorePermission]
NO_RESTORE_PERMISSION_INFO: RestorePermission
RESTORE_CONFIRMED_ALARMS: RestorePermission
RESTORE_CONFIRMED_HU_ALARMS: RestorePermission
RESTORE_UNCONFIRMED_ALARMS: RestorePermission
RESTORE_UNCONFIRMED_HU_ALARMS: RestorePermission
RESTORE_TAMPER_ACTIVATION: RestorePermission
RESTORE_EXTERNAL_POWER_ACTIVATION: RestorePermission
RESTORE_ATS_ACTIVATION: RestorePermission
RESTORE_OTHER_FAULT_ACTIVATION: RestorePermission
