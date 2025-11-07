from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import bypass_part_pb2 as _bypass_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import cms_device_index_pb2 as _cms_device_index_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_common_capabilities_pb2 as _device_common_capabilities_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_malfunctions_pb2 as _device_malfunctions_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_migration_status_pb2 as _device_migration_status_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_profile_pb2 as _device_profile_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_telemetry_pb2 as _device_telemetry_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import self_monitoring_part_pb2 as _self_monitoring_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import object_type_pb2 as _object_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommonFibraPart(_message.Message):
    __slots__ = ("device_profile", "device_telemetry", "device_malfunctions", "cms_device_index", "fibra_line", "line_voltage", "bypass_part", "device_common_capabilities", "device_migration_status", "line_extender", "self_monitoring_part")
    DEVICE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    DEVICE_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    CMS_DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
    FIBRA_LINE_FIELD_NUMBER: _ClassVar[int]
    LINE_VOLTAGE_FIELD_NUMBER: _ClassVar[int]
    BYPASS_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_COMMON_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    DEVICE_MIGRATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    LINE_EXTENDER_FIELD_NUMBER: _ClassVar[int]
    SELF_MONITORING_PART_FIELD_NUMBER: _ClassVar[int]
    device_profile: _device_profile_pb2.DeviceProfile
    device_telemetry: _device_telemetry_pb2.DeviceTelemetry
    device_malfunctions: _device_malfunctions_pb2.DeviceMalfunctions
    cms_device_index: _cms_device_index_pb2.CmsDeviceIndex
    fibra_line: FibraLine
    line_voltage: LineVoltage
    bypass_part: _bypass_part_pb2.BypassPart
    device_common_capabilities: _containers.RepeatedScalarFieldContainer[_device_common_capabilities_pb2.DeviceCommonCapability]
    device_migration_status: _device_migration_status_pb2.DeviceMigrationStatus
    line_extender: LineExtender
    self_monitoring_part: _self_monitoring_part_pb2.SelfMonitoringPart
    def __init__(self, device_profile: _Optional[_Union[_device_profile_pb2.DeviceProfile, _Mapping]] = ..., device_telemetry: _Optional[_Union[_device_telemetry_pb2.DeviceTelemetry, _Mapping]] = ..., device_malfunctions: _Optional[_Union[_device_malfunctions_pb2.DeviceMalfunctions, _Mapping]] = ..., cms_device_index: _Optional[_Union[_cms_device_index_pb2.CmsDeviceIndex, _Mapping]] = ..., fibra_line: _Optional[_Union[FibraLine, _Mapping]] = ..., line_voltage: _Optional[_Union[LineVoltage, _Mapping]] = ..., bypass_part: _Optional[_Union[_bypass_part_pb2.BypassPart, _Mapping]] = ..., device_common_capabilities: _Optional[_Iterable[_Union[_device_common_capabilities_pb2.DeviceCommonCapability, str]]] = ..., device_migration_status: _Optional[_Union[_device_migration_status_pb2.DeviceMigrationStatus, str]] = ..., line_extender: _Optional[_Union[LineExtender, _Mapping]] = ..., self_monitoring_part: _Optional[_Union[_self_monitoring_part_pb2.SelfMonitoringPart, _Mapping]] = ...) -> None: ...

class LineVoltage(_message.Message):
    __slots__ = ("value", "line_voltage_status")
    class LineVoltageStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LINE_VOLTAGE_STATUS_UNSPECIFIED: _ClassVar[LineVoltage.LineVoltageStatus]
        LINE_VOLTAGE_STATUS_ALERT: _ClassVar[LineVoltage.LineVoltageStatus]
        LINE_VOLTAGE_STATUS_OK: _ClassVar[LineVoltage.LineVoltageStatus]
    LINE_VOLTAGE_STATUS_UNSPECIFIED: LineVoltage.LineVoltageStatus
    LINE_VOLTAGE_STATUS_ALERT: LineVoltage.LineVoltageStatus
    LINE_VOLTAGE_STATUS_OK: LineVoltage.LineVoltageStatus
    VALUE_FIELD_NUMBER: _ClassVar[int]
    LINE_VOLTAGE_STATUS_FIELD_NUMBER: _ClassVar[int]
    value: int
    line_voltage_status: LineVoltage.LineVoltageStatus
    def __init__(self, value: _Optional[int] = ..., line_voltage_status: _Optional[_Union[LineVoltage.LineVoltageStatus, str]] = ...) -> None: ...

class LineExtender(_message.Message):
    __slots__ = ("name", "output", "index", "object_type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    output: int
    index: int
    object_type: _object_type_pb2.ObjectType
    def __init__(self, name: _Optional[str] = ..., output: _Optional[int] = ..., index: _Optional[int] = ..., object_type: _Optional[_Union[_object_type_pb2.ObjectType, _Mapping]] = ...) -> None: ...

class FibraLine(_message.Message):
    __slots__ = ("line", "ring")
    class Line(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: int
        def __init__(self, value: _Optional[int] = ...) -> None: ...
    class Ring(_message.Message):
        __slots__ = ("input", "output")
        INPUT_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_FIELD_NUMBER: _ClassVar[int]
        input: int
        output: int
        def __init__(self, input: _Optional[int] = ..., output: _Optional[int] = ...) -> None: ...
    LINE_FIELD_NUMBER: _ClassVar[int]
    RING_FIELD_NUMBER: _ClassVar[int]
    line: FibraLine.Line
    ring: FibraLine.Ring
    def __init__(self, line: _Optional[_Union[FibraLine.Line, _Mapping]] = ..., ring: _Optional[_Union[FibraLine.Ring, _Mapping]] = ...) -> None: ...
