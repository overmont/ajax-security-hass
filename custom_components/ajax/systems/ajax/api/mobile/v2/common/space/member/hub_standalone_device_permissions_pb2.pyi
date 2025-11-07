from systems.ajax.api.mobile.v2.common.space.member import hub_standalone_device_permission_pb2 as _hub_standalone_device_permission_pb2
from systems.ajax.api.mobile.v2.common.space.member import hub_restore_after_alarm_permission_pb2 as _hub_restore_after_alarm_permission_pb2
from systems.ajax.api.mobile.v2.common.space.member import photo_on_demand_device_permissions_pb2 as _photo_on_demand_device_permissions_pb2
from systems.ajax.api.mobile.v2.common.space.member import hub_standalone_device_extended_permission_pb2 as _hub_standalone_device_extended_permission_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HubStandaloneDevicePermissions(_message.Message):
    __slots__ = ("hub_id", "hub_permissions", "hub_restore_after_alarm_permissions", "photo_on_demand_device_permissions", "hub_permissions_extended")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    HUB_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    HUB_RESTORE_AFTER_ALARM_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ON_DEMAND_DEVICE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    HUB_PERMISSIONS_EXTENDED_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    hub_permissions: _containers.RepeatedScalarFieldContainer[_hub_standalone_device_permission_pb2.HubStandaloneDevicePermission]
    hub_restore_after_alarm_permissions: _containers.RepeatedScalarFieldContainer[_hub_restore_after_alarm_permission_pb2.HubRestoreAfterAlarmPermission]
    photo_on_demand_device_permissions: _containers.RepeatedCompositeFieldContainer[_photo_on_demand_device_permissions_pb2.PhotoOnDemandDevicePermissions]
    hub_permissions_extended: _containers.RepeatedScalarFieldContainer[_hub_standalone_device_extended_permission_pb2.HubStandaloneDevicePermissionExtended]
    def __init__(self, hub_id: _Optional[str] = ..., hub_permissions: _Optional[_Iterable[_Union[_hub_standalone_device_permission_pb2.HubStandaloneDevicePermission, str]]] = ..., hub_restore_after_alarm_permissions: _Optional[_Iterable[_Union[_hub_restore_after_alarm_permission_pb2.HubRestoreAfterAlarmPermission, str]]] = ..., photo_on_demand_device_permissions: _Optional[_Iterable[_Union[_photo_on_demand_device_permissions_pb2.PhotoOnDemandDevicePermissions, _Mapping]]] = ..., hub_permissions_extended: _Optional[_Iterable[_Union[_hub_standalone_device_extended_permission_pb2.HubStandaloneDevicePermissionExtended, str]]] = ...) -> None: ...
