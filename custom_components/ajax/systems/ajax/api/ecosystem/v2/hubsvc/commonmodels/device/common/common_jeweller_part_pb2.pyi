from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import assigned_extender_pb2 as _assigned_extender_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import bypass_part_pb2 as _bypass_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import cms_device_index_pb2 as _cms_device_index_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_common_capabilities_pb2 as _device_common_capabilities_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_malfunctions_pb2 as _device_malfunctions_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_migration_status_pb2 as _device_migration_status_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_profile_pb2 as _device_profile_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_telemetry_pb2 as _device_telemetry_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_transmission_power_mode_pb2 as _device_transmission_power_mode_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import self_monitoring_part_pb2 as _self_monitoring_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_transmission_power_mode_part_pb2 as _device_transmission_power_mode_part_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommonJewellerPart(_message.Message):
    __slots__ = ("device_profile", "device_telemetry", "device_transmission_power_mode", "device_malfunctions", "assigned_extender", "cms_device_index", "bypass_part", "device_migration_status", "device_common_capabilities", "self_monitoring_part", "device_transmission_power_mode_part")
    DEVICE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TRANSMISSION_POWER_MODE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_EXTENDER_FIELD_NUMBER: _ClassVar[int]
    CMS_DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
    BYPASS_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_MIGRATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_COMMON_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    SELF_MONITORING_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TRANSMISSION_POWER_MODE_PART_FIELD_NUMBER: _ClassVar[int]
    device_profile: _device_profile_pb2.DeviceProfile
    device_telemetry: _device_telemetry_pb2.DeviceTelemetry
    device_transmission_power_mode: _device_transmission_power_mode_pb2.DeviceTransmissionPowerMode
    device_malfunctions: _device_malfunctions_pb2.DeviceMalfunctions
    assigned_extender: _assigned_extender_pb2.AssignedExtender
    cms_device_index: _cms_device_index_pb2.CmsDeviceIndex
    bypass_part: _bypass_part_pb2.BypassPart
    device_migration_status: _device_migration_status_pb2.DeviceMigrationStatus
    device_common_capabilities: _containers.RepeatedScalarFieldContainer[_device_common_capabilities_pb2.DeviceCommonCapability]
    self_monitoring_part: _self_monitoring_part_pb2.SelfMonitoringPart
    device_transmission_power_mode_part: _device_transmission_power_mode_part_pb2.DeviceTransmissionPowerModePart
    def __init__(self, device_profile: _Optional[_Union[_device_profile_pb2.DeviceProfile, _Mapping]] = ..., device_telemetry: _Optional[_Union[_device_telemetry_pb2.DeviceTelemetry, _Mapping]] = ..., device_transmission_power_mode: _Optional[_Union[_device_transmission_power_mode_pb2.DeviceTransmissionPowerMode, str]] = ..., device_malfunctions: _Optional[_Union[_device_malfunctions_pb2.DeviceMalfunctions, _Mapping]] = ..., assigned_extender: _Optional[_Union[_assigned_extender_pb2.AssignedExtender, _Mapping]] = ..., cms_device_index: _Optional[_Union[_cms_device_index_pb2.CmsDeviceIndex, _Mapping]] = ..., bypass_part: _Optional[_Union[_bypass_part_pb2.BypassPart, _Mapping]] = ..., device_migration_status: _Optional[_Union[_device_migration_status_pb2.DeviceMigrationStatus, str]] = ..., device_common_capabilities: _Optional[_Iterable[_Union[_device_common_capabilities_pb2.DeviceCommonCapability, str]]] = ..., self_monitoring_part: _Optional[_Union[_self_monitoring_part_pb2.SelfMonitoringPart, _Mapping]] = ..., device_transmission_power_mode_part: _Optional[_Union[_device_transmission_power_mode_part_pb2.DeviceTransmissionPowerModePart, _Mapping]] = ...) -> None: ...
