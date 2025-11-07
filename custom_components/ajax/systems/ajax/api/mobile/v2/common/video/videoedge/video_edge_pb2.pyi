from systems.ajax.api.mobile.v2.common.video.videoedge.about import about_pb2 as _about_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.archive import archive_pb2 as _archive_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.backupchannel import backup_channel_info_pb2 as _backup_channel_info_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.channel import channel_pb2 as _channel_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.detector import detector_pb2 as _detector_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.diagnostics import diagnostics_settings_pb2 as _diagnostics_settings_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.firmware import firmware_pb2 as _firmware_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.leds import leds_pb2 as _leds_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.mcu import mcu_pb2 as _mcu_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.mediadevice import media_device_pb2 as _media_device_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.network import network_pb2 as _network_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.network import network_interface_pb2 as _network_interface_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.spacesettings import video_edge_space_settings_pb2 as _video_edge_space_settings_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.storage import storage_pb2 as _storage_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.storage import storage_device_pb2 as _storage_device_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.system import system_info_pb2 as _system_info_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.onvif import onvif_info_pb2 as _onvif_info_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConnectionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE: _ClassVar[ConnectionState]
    OFFLINE: _ClassVar[ConnectionState]
    ONLINE: _ClassVar[ConnectionState]
NONE: ConnectionState
OFFLINE: ConnectionState
ONLINE: ConnectionState

class VideoEdge(_message.Message):
    __slots__ = ("guid", "name", "connection_state", "archive", "devices", "channels", "detectors", "network", "diagnostics_settings", "system_info", "network_interfaces", "storage_devices", "firmware", "about", "leds", "storage", "mcu", "onvif_info", "space_settings", "backup_channel_info")
    GUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_STATE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    DETECTORS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_INFO_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACES_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DEVICES_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_FIELD_NUMBER: _ClassVar[int]
    ABOUT_FIELD_NUMBER: _ClassVar[int]
    LEDS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    MCU_FIELD_NUMBER: _ClassVar[int]
    ONVIF_INFO_FIELD_NUMBER: _ClassVar[int]
    SPACE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_CHANNEL_INFO_FIELD_NUMBER: _ClassVar[int]
    guid: str
    name: str
    connection_state: ConnectionState
    archive: _archive_pb2.Archive
    devices: _containers.RepeatedCompositeFieldContainer[_media_device_pb2.MediaDevice]
    channels: _containers.RepeatedCompositeFieldContainer[_channel_pb2.Channel]
    detectors: _containers.RepeatedCompositeFieldContainer[_detector_pb2.Detector]
    network: _network_pb2.Network
    diagnostics_settings: _diagnostics_settings_pb2.DiagnosticsSettings
    system_info: _system_info_pb2.SystemInfo
    network_interfaces: _containers.RepeatedCompositeFieldContainer[_network_interface_pb2.NetworkInterface]
    storage_devices: _containers.RepeatedCompositeFieldContainer[_storage_device_pb2.StorageDevice]
    firmware: _firmware_pb2.Firmware
    about: _about_pb2.About
    leds: _leds_pb2.Leds
    storage: _storage_pb2.Storage
    mcu: _mcu_pb2.Mcu
    onvif_info: _onvif_info_pb2.OnvifInfo
    space_settings: _video_edge_space_settings_pb2.VideoEdgeSpaceSettings
    backup_channel_info: _backup_channel_info_pb2.BackupChannelInfo
    def __init__(self, guid: _Optional[str] = ..., name: _Optional[str] = ..., connection_state: _Optional[_Union[ConnectionState, str]] = ..., archive: _Optional[_Union[_archive_pb2.Archive, _Mapping]] = ..., devices: _Optional[_Iterable[_Union[_media_device_pb2.MediaDevice, _Mapping]]] = ..., channels: _Optional[_Iterable[_Union[_channel_pb2.Channel, _Mapping]]] = ..., detectors: _Optional[_Iterable[_Union[_detector_pb2.Detector, _Mapping]]] = ..., network: _Optional[_Union[_network_pb2.Network, _Mapping]] = ..., diagnostics_settings: _Optional[_Union[_diagnostics_settings_pb2.DiagnosticsSettings, _Mapping]] = ..., system_info: _Optional[_Union[_system_info_pb2.SystemInfo, _Mapping]] = ..., network_interfaces: _Optional[_Iterable[_Union[_network_interface_pb2.NetworkInterface, _Mapping]]] = ..., storage_devices: _Optional[_Iterable[_Union[_storage_device_pb2.StorageDevice, _Mapping]]] = ..., firmware: _Optional[_Union[_firmware_pb2.Firmware, _Mapping]] = ..., about: _Optional[_Union[_about_pb2.About, _Mapping]] = ..., leds: _Optional[_Union[_leds_pb2.Leds, _Mapping]] = ..., storage: _Optional[_Union[_storage_pb2.Storage, _Mapping]] = ..., mcu: _Optional[_Union[_mcu_pb2.Mcu, _Mapping]] = ..., onvif_info: _Optional[_Union[_onvif_info_pb2.OnvifInfo, _Mapping]] = ..., space_settings: _Optional[_Union[_video_edge_space_settings_pb2.VideoEdgeSpaceSettings, _Mapping]] = ..., backup_channel_info: _Optional[_Union[_backup_channel_info_pb2.BackupChannelInfo, _Mapping]] = ...) -> None: ...
