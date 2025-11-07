from google.protobuf import field_mask_pb2 as _field_mask_pb2
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
from systems.ajax.api.mobile.v2.common.video.videoedge import video_edge_pb2 as _video_edge_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.channel import channel_source_settings_pb2 as _channel_source_settings_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge import video_edge_base_pb2 as _video_edge_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamVideoEdgeResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("initial_state", "completely_changed", "partially_changed", "channel_source_settings_update")
        class InitialState(_message.Message):
            __slots__ = ("video_edge", "channel_source_settings")
            VIDEO_EDGE_FIELD_NUMBER: _ClassVar[int]
            CHANNEL_SOURCE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
            video_edge: _video_edge_pb2.VideoEdge
            channel_source_settings: _containers.RepeatedCompositeFieldContainer[_channel_source_settings_pb2.ChannelSourceSettings]
            def __init__(self, video_edge: _Optional[_Union[_video_edge_pb2.VideoEdge, _Mapping]] = ..., channel_source_settings: _Optional[_Iterable[_Union[_channel_source_settings_pb2.ChannelSourceSettings, _Mapping]]] = ...) -> None: ...
        class CompletelyChanged(_message.Message):
            __slots__ = ("video_edge_base",)
            VIDEO_EDGE_BASE_FIELD_NUMBER: _ClassVar[int]
            video_edge_base: _video_edge_base_pb2.VideoEdgeBase
            def __init__(self, video_edge_base: _Optional[_Union[_video_edge_base_pb2.VideoEdgeBase, _Mapping]] = ...) -> None: ...
        class PartiallyChanged(_message.Message):
            __slots__ = ("video_edge_id", "device", "channel", "archive", "detector", "network", "diagnostics_settings", "system_info", "connection_state", "network_interface", "storage_device", "firmware", "leds", "name", "storage", "mcu", "onvif_info", "space_settings", "backup_channel_info", "mask", "update_type")
            VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
            DEVICE_FIELD_NUMBER: _ClassVar[int]
            CHANNEL_FIELD_NUMBER: _ClassVar[int]
            ARCHIVE_FIELD_NUMBER: _ClassVar[int]
            DETECTOR_FIELD_NUMBER: _ClassVar[int]
            NETWORK_FIELD_NUMBER: _ClassVar[int]
            DIAGNOSTICS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
            SYSTEM_INFO_FIELD_NUMBER: _ClassVar[int]
            CONNECTION_STATE_FIELD_NUMBER: _ClassVar[int]
            NETWORK_INTERFACE_FIELD_NUMBER: _ClassVar[int]
            STORAGE_DEVICE_FIELD_NUMBER: _ClassVar[int]
            FIRMWARE_FIELD_NUMBER: _ClassVar[int]
            LEDS_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            STORAGE_FIELD_NUMBER: _ClassVar[int]
            MCU_FIELD_NUMBER: _ClassVar[int]
            ONVIF_INFO_FIELD_NUMBER: _ClassVar[int]
            SPACE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
            BACKUP_CHANNEL_INFO_FIELD_NUMBER: _ClassVar[int]
            MASK_FIELD_NUMBER: _ClassVar[int]
            UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
            video_edge_id: str
            device: _media_device_pb2.MediaDevice
            channel: _channel_pb2.Channel
            archive: _archive_pb2.Archive
            detector: _detector_pb2.Detector
            network: _network_pb2.Network
            diagnostics_settings: _diagnostics_settings_pb2.DiagnosticsSettings
            system_info: _system_info_pb2.SystemInfo
            connection_state: _video_edge_pb2.ConnectionState
            network_interface: _network_interface_pb2.NetworkInterface
            storage_device: _storage_device_pb2.StorageDevice
            firmware: _firmware_pb2.Firmware
            leds: _leds_pb2.Leds
            name: str
            storage: _storage_pb2.Storage
            mcu: _mcu_pb2.Mcu
            onvif_info: _onvif_info_pb2.OnvifInfo
            space_settings: _video_edge_space_settings_pb2.VideoEdgeSpaceSettings
            backup_channel_info: _backup_channel_info_pb2.BackupChannelInfo
            mask: _field_mask_pb2.FieldMask
            update_type: _response_pb2.UpdateType
            def __init__(self, video_edge_id: _Optional[str] = ..., device: _Optional[_Union[_media_device_pb2.MediaDevice, _Mapping]] = ..., channel: _Optional[_Union[_channel_pb2.Channel, _Mapping]] = ..., archive: _Optional[_Union[_archive_pb2.Archive, _Mapping]] = ..., detector: _Optional[_Union[_detector_pb2.Detector, _Mapping]] = ..., network: _Optional[_Union[_network_pb2.Network, _Mapping]] = ..., diagnostics_settings: _Optional[_Union[_diagnostics_settings_pb2.DiagnosticsSettings, _Mapping]] = ..., system_info: _Optional[_Union[_system_info_pb2.SystemInfo, _Mapping]] = ..., connection_state: _Optional[_Union[_video_edge_pb2.ConnectionState, str]] = ..., network_interface: _Optional[_Union[_network_interface_pb2.NetworkInterface, _Mapping]] = ..., storage_device: _Optional[_Union[_storage_device_pb2.StorageDevice, _Mapping]] = ..., firmware: _Optional[_Union[_firmware_pb2.Firmware, _Mapping]] = ..., leds: _Optional[_Union[_leds_pb2.Leds, _Mapping]] = ..., name: _Optional[str] = ..., storage: _Optional[_Union[_storage_pb2.Storage, _Mapping]] = ..., mcu: _Optional[_Union[_mcu_pb2.Mcu, _Mapping]] = ..., onvif_info: _Optional[_Union[_onvif_info_pb2.OnvifInfo, _Mapping]] = ..., space_settings: _Optional[_Union[_video_edge_space_settings_pb2.VideoEdgeSpaceSettings, _Mapping]] = ..., backup_channel_info: _Optional[_Union[_backup_channel_info_pb2.BackupChannelInfo, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., update_type: _Optional[_Union[_response_pb2.UpdateType, str]] = ...) -> None: ...
        class ChannelSourceSettingsUpdate(_message.Message):
            __slots__ = ("nvr_source_settings_updates",)
            class NvrSourceSettingsUpdates(_message.Message):
                __slots__ = ("nvr_source_settings_updates",)
                NVR_SOURCE_SETTINGS_UPDATES_FIELD_NUMBER: _ClassVar[int]
                nvr_source_settings_updates: _containers.RepeatedCompositeFieldContainer[StreamVideoEdgeResponse.Success.ChannelSourceSettingsUpdate.NvrSourceSettingsUpdate]
                def __init__(self, nvr_source_settings_updates: _Optional[_Iterable[_Union[StreamVideoEdgeResponse.Success.ChannelSourceSettingsUpdate.NvrSourceSettingsUpdate, _Mapping]]] = ...) -> None: ...
            class NvrSourceSettingsUpdate(_message.Message):
                __slots__ = ("video_edge_id", "channel_id", "snapshot", "video_edge_name", "video_edge_connection_state", "record_mode", "record_policy", "storage_device", "channel_states", "update_type")
                class ChannelStates(_message.Message):
                    __slots__ = ("channel_states",)
                    CHANNEL_STATES_FIELD_NUMBER: _ClassVar[int]
                    channel_states: _containers.RepeatedScalarFieldContainer[_channel_pb2.ChannelState]
                    def __init__(self, channel_states: _Optional[_Iterable[_Union[_channel_pb2.ChannelState, str]]] = ...) -> None: ...
                VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
                CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
                SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
                VIDEO_EDGE_NAME_FIELD_NUMBER: _ClassVar[int]
                VIDEO_EDGE_CONNECTION_STATE_FIELD_NUMBER: _ClassVar[int]
                RECORD_MODE_FIELD_NUMBER: _ClassVar[int]
                RECORD_POLICY_FIELD_NUMBER: _ClassVar[int]
                STORAGE_DEVICE_FIELD_NUMBER: _ClassVar[int]
                CHANNEL_STATES_FIELD_NUMBER: _ClassVar[int]
                UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
                video_edge_id: str
                channel_id: str
                snapshot: _channel_source_settings_pb2.NvrSourceSettings
                video_edge_name: str
                video_edge_connection_state: _video_edge_pb2.ConnectionState
                record_mode: _archive_pb2.RecordMode
                record_policy: _archive_pb2.RecordPolicy
                storage_device: _channel_source_settings_pb2.NvrSourceSettings.StorageDevice
                channel_states: StreamVideoEdgeResponse.Success.ChannelSourceSettingsUpdate.NvrSourceSettingsUpdate.ChannelStates
                update_type: _response_pb2.UpdateType
                def __init__(self, video_edge_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., snapshot: _Optional[_Union[_channel_source_settings_pb2.NvrSourceSettings, _Mapping]] = ..., video_edge_name: _Optional[str] = ..., video_edge_connection_state: _Optional[_Union[_video_edge_pb2.ConnectionState, str]] = ..., record_mode: _Optional[_Union[_archive_pb2.RecordMode, str]] = ..., record_policy: _Optional[_Union[_archive_pb2.RecordPolicy, str]] = ..., storage_device: _Optional[_Union[_channel_source_settings_pb2.NvrSourceSettings.StorageDevice, _Mapping]] = ..., channel_states: _Optional[_Union[StreamVideoEdgeResponse.Success.ChannelSourceSettingsUpdate.NvrSourceSettingsUpdate.ChannelStates, _Mapping]] = ..., update_type: _Optional[_Union[_response_pb2.UpdateType, str]] = ...) -> None: ...
            NVR_SOURCE_SETTINGS_UPDATES_FIELD_NUMBER: _ClassVar[int]
            nvr_source_settings_updates: StreamVideoEdgeResponse.Success.ChannelSourceSettingsUpdate.NvrSourceSettingsUpdates
            def __init__(self, nvr_source_settings_updates: _Optional[_Union[StreamVideoEdgeResponse.Success.ChannelSourceSettingsUpdate.NvrSourceSettingsUpdates, _Mapping]] = ...) -> None: ...
        INITIAL_STATE_FIELD_NUMBER: _ClassVar[int]
        COMPLETELY_CHANGED_FIELD_NUMBER: _ClassVar[int]
        PARTIALLY_CHANGED_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_SOURCE_SETTINGS_UPDATE_FIELD_NUMBER: _ClassVar[int]
        initial_state: StreamVideoEdgeResponse.Success.InitialState
        completely_changed: StreamVideoEdgeResponse.Success.CompletelyChanged
        partially_changed: StreamVideoEdgeResponse.Success.PartiallyChanged
        channel_source_settings_update: StreamVideoEdgeResponse.Success.ChannelSourceSettingsUpdate
        def __init__(self, initial_state: _Optional[_Union[StreamVideoEdgeResponse.Success.InitialState, _Mapping]] = ..., completely_changed: _Optional[_Union[StreamVideoEdgeResponse.Success.CompletelyChanged, _Mapping]] = ..., partially_changed: _Optional[_Union[StreamVideoEdgeResponse.Success.PartiallyChanged, _Mapping]] = ..., channel_source_settings_update: _Optional[_Union[StreamVideoEdgeResponse.Success.ChannelSourceSettingsUpdate, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "space_not_found", "video_edge_not_found", "permission_denied")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        space_not_found: _response_pb2.Error
        video_edge_not_found: _response_pb2.Error
        permission_denied: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., video_edge_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamVideoEdgeResponse.Success
    failure: StreamVideoEdgeResponse.Failure
    def __init__(self, success: _Optional[_Union[StreamVideoEdgeResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[StreamVideoEdgeResponse.Failure, _Mapping]] = ...) -> None: ...
