from systems.ajax.api.mobile.v2.common.video.videoedge.channel import channel_pb2 as _channel_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.space.device.light import light_device_pb2 as _light_device_pb2
from v3.mobilegwsvc.commonmodels.space.device.light import light_device_id_pb2 as _light_device_id_pb2
from v3.mobilegwsvc.commonmodels.space.device.light import light_device_state_pb2 as _light_device_state_pb2
from v3.mobilegwsvc.commonmodels.space.device.light import light_device_status_pb2 as _light_device_status_pb2
from v3.mobilegwsvc.commonmodels.space.smartlock.light import light_smart_lock_pb2 as _light_smart_lock_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.light import light_video_edge_pb2 as _light_video_edge_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamLightDevicesResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("snapshot", "updates")
        class Snapshot(_message.Message):
            __slots__ = ("light_devices",)
            LIGHT_DEVICES_FIELD_NUMBER: _ClassVar[int]
            light_devices: _containers.RepeatedCompositeFieldContainer[_light_device_pb2.LightDevice]
            def __init__(self, light_devices: _Optional[_Iterable[_Union[_light_device_pb2.LightDevice, _Mapping]]] = ...) -> None: ...
        class Updates(_message.Message):
            __slots__ = ("updates",)
            UPDATES_FIELD_NUMBER: _ClassVar[int]
            updates: _containers.RepeatedCompositeFieldContainer[StreamLightDevicesResponse.Success.Update]
            def __init__(self, updates: _Optional[_Iterable[_Union[StreamLightDevicesResponse.Success.Update, _Mapping]]] = ...) -> None: ...
        class Update(_message.Message):
            __slots__ = ("device_id", "snapshot_update", "status_update", "malfunctions_update", "state_update", "light_video_edge_update", "light_video_edge_channel_update", "light_smart_lock_update")
            class SnapshotUpdate(_message.Message):
                __slots__ = ("light_device", "update_type")
                LIGHT_DEVICE_FIELD_NUMBER: _ClassVar[int]
                UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
                light_device: _light_device_pb2.LightDevice
                update_type: _response_pb2.UpdateType
                def __init__(self, light_device: _Optional[_Union[_light_device_pb2.LightDevice, _Mapping]] = ..., update_type: _Optional[_Union[_response_pb2.UpdateType, str]] = ...) -> None: ...
            class LightSmartLockUpdate(_message.Message):
                __slots__ = ("spread_properties_update",)
                class SmartLockSpreadPropertiesUpdate(_message.Message):
                    __slots__ = ("update_type", "spread_property")
                    UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
                    SPREAD_PROPERTY_FIELD_NUMBER: _ClassVar[int]
                    update_type: _response_pb2.UpdateType
                    spread_property: _light_smart_lock_pb2.LightSmartLock.SmartLockSpreadProperty
                    def __init__(self, update_type: _Optional[_Union[_response_pb2.UpdateType, str]] = ..., spread_property: _Optional[_Union[_light_smart_lock_pb2.LightSmartLock.SmartLockSpreadProperty, _Mapping]] = ...) -> None: ...
                SPREAD_PROPERTIES_UPDATE_FIELD_NUMBER: _ClassVar[int]
                spread_properties_update: StreamLightDevicesResponse.Success.Update.LightSmartLockUpdate.SmartLockSpreadPropertiesUpdate
                def __init__(self, spread_properties_update: _Optional[_Union[StreamLightDevicesResponse.Success.Update.LightSmartLockUpdate.SmartLockSpreadPropertiesUpdate, _Mapping]] = ...) -> None: ...
            class LightVideoEdgeUpdate(_message.Message):
                __slots__ = ("spread_properties_update", "name", "room_id")
                class SpreadPropertiesUpdate(_message.Message):
                    __slots__ = ("update_type", "spread_properties")
                    UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
                    SPREAD_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
                    update_type: _response_pb2.UpdateType
                    spread_properties: _light_video_edge_pb2.LightVideoEdge.SpreadProperties
                    def __init__(self, update_type: _Optional[_Union[_response_pb2.UpdateType, str]] = ..., spread_properties: _Optional[_Union[_light_video_edge_pb2.LightVideoEdge.SpreadProperties, _Mapping]] = ...) -> None: ...
                SPREAD_PROPERTIES_UPDATE_FIELD_NUMBER: _ClassVar[int]
                NAME_FIELD_NUMBER: _ClassVar[int]
                ROOM_ID_FIELD_NUMBER: _ClassVar[int]
                spread_properties_update: StreamLightDevicesResponse.Success.Update.LightVideoEdgeUpdate.SpreadPropertiesUpdate
                name: str
                room_id: str
                def __init__(self, spread_properties_update: _Optional[_Union[StreamLightDevicesResponse.Success.Update.LightVideoEdgeUpdate.SpreadPropertiesUpdate, _Mapping]] = ..., name: _Optional[str] = ..., room_id: _Optional[str] = ...) -> None: ...
            class LightVideoEdgeChannelUpdate(_message.Message):
                __slots__ = ("source_aliases", "name", "room_id", "group_id", "backup_channel_properties", "spread_properties_update")
                class SpreadPropertiesUpdate(_message.Message):
                    __slots__ = ("update_type", "spread_properties")
                    UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
                    SPREAD_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
                    update_type: _response_pb2.UpdateType
                    spread_properties: _light_video_edge_pb2.LightVideoEdgeChannel.SpreadProperties
                    def __init__(self, update_type: _Optional[_Union[_response_pb2.UpdateType, str]] = ..., spread_properties: _Optional[_Union[_light_video_edge_pb2.LightVideoEdgeChannel.SpreadProperties, _Mapping]] = ...) -> None: ...
                SOURCE_ALIASES_FIELD_NUMBER: _ClassVar[int]
                NAME_FIELD_NUMBER: _ClassVar[int]
                ROOM_ID_FIELD_NUMBER: _ClassVar[int]
                GROUP_ID_FIELD_NUMBER: _ClassVar[int]
                BACKUP_CHANNEL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
                SPREAD_PROPERTIES_UPDATE_FIELD_NUMBER: _ClassVar[int]
                source_aliases: _channel_pb2.SourceAliases
                name: str
                room_id: str
                group_id: str
                backup_channel_properties: _light_video_edge_pb2.LightVideoEdgeChannel.BackupChannelProperties
                spread_properties_update: StreamLightDevicesResponse.Success.Update.LightVideoEdgeChannelUpdate.SpreadPropertiesUpdate
                def __init__(self, source_aliases: _Optional[_Union[_channel_pb2.SourceAliases, _Mapping]] = ..., name: _Optional[str] = ..., room_id: _Optional[str] = ..., group_id: _Optional[str] = ..., backup_channel_properties: _Optional[_Union[_light_video_edge_pb2.LightVideoEdgeChannel.BackupChannelProperties, _Mapping]] = ..., spread_properties_update: _Optional[_Union[StreamLightDevicesResponse.Success.Update.LightVideoEdgeChannelUpdate.SpreadPropertiesUpdate, _Mapping]] = ...) -> None: ...
            class StatusUpdate(_message.Message):
                __slots__ = ("status", "update_type")
                STATUS_FIELD_NUMBER: _ClassVar[int]
                UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
                status: _light_device_status_pb2.LightDeviceStatus
                update_type: _response_pb2.UpdateType
                def __init__(self, status: _Optional[_Union[_light_device_status_pb2.LightDeviceStatus, _Mapping]] = ..., update_type: _Optional[_Union[_response_pb2.UpdateType, str]] = ...) -> None: ...
            class StateUpdate(_message.Message):
                __slots__ = ("state", "update_type")
                STATE_FIELD_NUMBER: _ClassVar[int]
                UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
                state: _light_device_state_pb2.LightDeviceState
                update_type: _response_pb2.UpdateType
                def __init__(self, state: _Optional[_Union[_light_device_state_pb2.LightDeviceState, str]] = ..., update_type: _Optional[_Union[_response_pb2.UpdateType, str]] = ...) -> None: ...
            DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
            SNAPSHOT_UPDATE_FIELD_NUMBER: _ClassVar[int]
            STATUS_UPDATE_FIELD_NUMBER: _ClassVar[int]
            MALFUNCTIONS_UPDATE_FIELD_NUMBER: _ClassVar[int]
            STATE_UPDATE_FIELD_NUMBER: _ClassVar[int]
            LIGHT_VIDEO_EDGE_UPDATE_FIELD_NUMBER: _ClassVar[int]
            LIGHT_VIDEO_EDGE_CHANNEL_UPDATE_FIELD_NUMBER: _ClassVar[int]
            LIGHT_SMART_LOCK_UPDATE_FIELD_NUMBER: _ClassVar[int]
            device_id: _light_device_id_pb2.LightDeviceId
            snapshot_update: StreamLightDevicesResponse.Success.Update.SnapshotUpdate
            status_update: StreamLightDevicesResponse.Success.Update.StatusUpdate
            malfunctions_update: int
            state_update: StreamLightDevicesResponse.Success.Update.StateUpdate
            light_video_edge_update: StreamLightDevicesResponse.Success.Update.LightVideoEdgeUpdate
            light_video_edge_channel_update: StreamLightDevicesResponse.Success.Update.LightVideoEdgeChannelUpdate
            light_smart_lock_update: StreamLightDevicesResponse.Success.Update.LightSmartLockUpdate
            def __init__(self, device_id: _Optional[_Union[_light_device_id_pb2.LightDeviceId, _Mapping]] = ..., snapshot_update: _Optional[_Union[StreamLightDevicesResponse.Success.Update.SnapshotUpdate, _Mapping]] = ..., status_update: _Optional[_Union[StreamLightDevicesResponse.Success.Update.StatusUpdate, _Mapping]] = ..., malfunctions_update: _Optional[int] = ..., state_update: _Optional[_Union[StreamLightDevicesResponse.Success.Update.StateUpdate, _Mapping]] = ..., light_video_edge_update: _Optional[_Union[StreamLightDevicesResponse.Success.Update.LightVideoEdgeUpdate, _Mapping]] = ..., light_video_edge_channel_update: _Optional[_Union[StreamLightDevicesResponse.Success.Update.LightVideoEdgeChannelUpdate, _Mapping]] = ..., light_smart_lock_update: _Optional[_Union[StreamLightDevicesResponse.Success.Update.LightSmartLockUpdate, _Mapping]] = ...) -> None: ...
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        UPDATES_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamLightDevicesResponse.Success.Snapshot
        updates: StreamLightDevicesResponse.Success.Updates
        def __init__(self, snapshot: _Optional[_Union[StreamLightDevicesResponse.Success.Snapshot, _Mapping]] = ..., updates: _Optional[_Union[StreamLightDevicesResponse.Success.Updates, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request",)
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamLightDevicesResponse.Success
    failure: StreamLightDevicesResponse.Failure
    def __init__(self, success: _Optional[_Union[StreamLightDevicesResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[StreamLightDevicesResponse.Failure, _Mapping]] = ...) -> None: ...
