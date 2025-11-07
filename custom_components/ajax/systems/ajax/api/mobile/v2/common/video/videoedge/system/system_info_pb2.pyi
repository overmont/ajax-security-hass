from google.protobuf import duration_pb2 as _duration_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.firmware import firmware_version_pb2 as _firmware_version_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.mediadevice.discovering import discovery_address_pb2 as _discovery_address_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.system import system_info_flag_pb2 as _system_info_flag_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SystemInfo(_message.Message):
    __slots__ = ("lid_closed", "uptime", "average_cpu_consumption", "ram_consumption", "firmware_version", "product_type", "platform_name", "timezone_id", "uuid", "discovery_addresses", "flags", "fan_states", "fan_status")
    class FanStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FAN_STATUS_UNSPECIFIED: _ClassVar[SystemInfo.FanStatus]
        FAN_STATUS_OK: _ClassVar[SystemInfo.FanStatus]
        FAN_STATUS_ERROR: _ClassVar[SystemInfo.FanStatus]
    FAN_STATUS_UNSPECIFIED: SystemInfo.FanStatus
    FAN_STATUS_OK: SystemInfo.FanStatus
    FAN_STATUS_ERROR: SystemInfo.FanStatus
    class FanState(_message.Message):
        __slots__ = ("id", "rpm")
        ID_FIELD_NUMBER: _ClassVar[int]
        RPM_FIELD_NUMBER: _ClassVar[int]
        id: int
        rpm: int
        def __init__(self, id: _Optional[int] = ..., rpm: _Optional[int] = ...) -> None: ...
    LID_CLOSED_FIELD_NUMBER: _ClassVar[int]
    UPTIME_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_CPU_CONSUMPTION_FIELD_NUMBER: _ClassVar[int]
    RAM_CONSUMPTION_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_NAME_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_ID_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    DISCOVERY_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    FAN_STATES_FIELD_NUMBER: _ClassVar[int]
    FAN_STATUS_FIELD_NUMBER: _ClassVar[int]
    lid_closed: bool
    uptime: _duration_pb2.Duration
    average_cpu_consumption: int
    ram_consumption: int
    firmware_version: _firmware_version_pb2.FirmwareVersion
    product_type: str
    platform_name: str
    timezone_id: str
    uuid: str
    discovery_addresses: _containers.RepeatedCompositeFieldContainer[_discovery_address_pb2.DiscoveryAddress]
    flags: _containers.RepeatedScalarFieldContainer[_system_info_flag_pb2.SystemInfoFlag]
    fan_states: _containers.RepeatedCompositeFieldContainer[SystemInfo.FanState]
    fan_status: SystemInfo.FanStatus
    def __init__(self, lid_closed: bool = ..., uptime: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., average_cpu_consumption: _Optional[int] = ..., ram_consumption: _Optional[int] = ..., firmware_version: _Optional[_Union[_firmware_version_pb2.FirmwareVersion, _Mapping]] = ..., product_type: _Optional[str] = ..., platform_name: _Optional[str] = ..., timezone_id: _Optional[str] = ..., uuid: _Optional[str] = ..., discovery_addresses: _Optional[_Iterable[_Union[_discovery_address_pb2.DiscoveryAddress, _Mapping]]] = ..., flags: _Optional[_Iterable[_Union[_system_info_flag_pb2.SystemInfoFlag, str]]] = ..., fan_states: _Optional[_Iterable[_Union[SystemInfo.FanState, _Mapping]]] = ..., fan_status: _Optional[_Union[SystemInfo.FanStatus, str]] = ...) -> None: ...
