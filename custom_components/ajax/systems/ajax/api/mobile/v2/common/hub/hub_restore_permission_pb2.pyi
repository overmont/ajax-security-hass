from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HubRestorePermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NO_RESTORE_PERMISSION_INFO: _ClassVar[HubRestorePermission]
    RESTORE_CONFIRMED_ALARMS: _ClassVar[HubRestorePermission]
    RESTORE_CONFIRMED_HU_ALARMS: _ClassVar[HubRestorePermission]
    RESTORE_UNCONFIRMED_ALARMS: _ClassVar[HubRestorePermission]
    RESTORE_UNCONFIRMED_HU_ALARMS: _ClassVar[HubRestorePermission]
    RESTORE_TAMPER_ACTIVATION: _ClassVar[HubRestorePermission]
    RESTORE_EXTERNAL_POWER_ACTIVATION: _ClassVar[HubRestorePermission]
    RESTORE_ATS_ACTIVATION: _ClassVar[HubRestorePermission]
    RESTORE_OTHER_FAULT_ACTIVATION: _ClassVar[HubRestorePermission]
NO_RESTORE_PERMISSION_INFO: HubRestorePermission
RESTORE_CONFIRMED_ALARMS: HubRestorePermission
RESTORE_CONFIRMED_HU_ALARMS: HubRestorePermission
RESTORE_UNCONFIRMED_ALARMS: HubRestorePermission
RESTORE_UNCONFIRMED_HU_ALARMS: HubRestorePermission
RESTORE_TAMPER_ACTIVATION: HubRestorePermission
RESTORE_EXTERNAL_POWER_ACTIVATION: HubRestorePermission
RESTORE_ATS_ACTIVATION: HubRestorePermission
RESTORE_OTHER_FAULT_ACTIVATION: HubRestorePermission

class HubRestorePermissions(_message.Message):
    __slots__ = ("restore_permissions",)
    RESTORE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    restore_permissions: _containers.RepeatedScalarFieldContainer[HubRestorePermission]
    def __init__(self, restore_permissions: _Optional[_Iterable[_Union[HubRestorePermission, str]]] = ...) -> None: ...
