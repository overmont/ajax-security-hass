from google.protobuf import empty_pb2 as _empty_pb2
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.mediadevice import media_device_pb2 as _media_device_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.mediadevice.discovering import discovery_address_pb2 as _discovery_address_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.about import about_pb2 as _about_pb2
from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DiscoverMediaDevicesRequest(_message.Message):
    __slots__ = ("video_edge_id", "filter", "space_locator")
    class Filter(_message.Message):
        __slots__ = ("protocols",)
        PROTOCOLS_FIELD_NUMBER: _ClassVar[int]
        protocols: _containers.RepeatedScalarFieldContainer[_media_device_pb2.MediaDeviceProtocol]
        def __init__(self, protocols: _Optional[_Iterable[_Union[_media_device_pb2.MediaDeviceProtocol, str]]] = ...) -> None: ...
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    filter: DiscoverMediaDevicesRequest.Filter
    space_locator: _space_locator_pb2.SpaceLocator
    def __init__(self, video_edge_id: _Optional[str] = ..., filter: _Optional[_Union[DiscoverMediaDevicesRequest.Filter, _Mapping]] = ..., space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ...) -> None: ...

class DiscoverMediaDevicesResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("instant_discovering_result", "device_added", "device_removed", "device_updated", "unknown")
        INSTANT_DISCOVERING_RESULT_FIELD_NUMBER: _ClassVar[int]
        DEVICE_ADDED_FIELD_NUMBER: _ClassVar[int]
        DEVICE_REMOVED_FIELD_NUMBER: _ClassVar[int]
        DEVICE_UPDATED_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN_FIELD_NUMBER: _ClassVar[int]
        instant_discovering_result: DiscoverMediaDevicesResponse.InstantDiscoveringResult
        device_added: DiscoverMediaDevicesResponse.DiscoveredMediaDevice
        device_removed: DiscoverMediaDevicesResponse.DiscoveredMediaDevice
        device_updated: DiscoverMediaDevicesResponse.DiscoveredMediaDevice
        unknown: _empty_pb2.Empty
        def __init__(self, instant_discovering_result: _Optional[_Union[DiscoverMediaDevicesResponse.InstantDiscoveringResult, _Mapping]] = ..., device_added: _Optional[_Union[DiscoverMediaDevicesResponse.DiscoveredMediaDevice, _Mapping]] = ..., device_removed: _Optional[_Union[DiscoverMediaDevicesResponse.DiscoveredMediaDevice, _Mapping]] = ..., device_updated: _Optional[_Union[DiscoverMediaDevicesResponse.DiscoveredMediaDevice, _Mapping]] = ..., unknown: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ...) -> None: ...
    class InstantDiscoveringResult(_message.Message):
        __slots__ = ("devices",)
        DEVICES_FIELD_NUMBER: _ClassVar[int]
        devices: _containers.RepeatedCompositeFieldContainer[DiscoverMediaDevicesResponse.DiscoveredMediaDevice]
        def __init__(self, devices: _Optional[_Iterable[_Union[DiscoverMediaDevicesResponse.DiscoveredMediaDevice, _Mapping]]] = ...) -> None: ...
    class DiscoveredMediaDevice(_message.Message):
        __slots__ = ("uuid", "vendor", "model", "addresses", "already_added", "name", "video_edge_info", "available_to_add", "already_added_new")
        UUID_FIELD_NUMBER: _ClassVar[int]
        VENDOR_FIELD_NUMBER: _ClassVar[int]
        MODEL_FIELD_NUMBER: _ClassVar[int]
        ADDRESSES_FIELD_NUMBER: _ClassVar[int]
        ALREADY_ADDED_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_INFO_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_TO_ADD_FIELD_NUMBER: _ClassVar[int]
        ALREADY_ADDED_NEW_FIELD_NUMBER: _ClassVar[int]
        uuid: str
        vendor: str
        model: str
        addresses: _containers.RepeatedCompositeFieldContainer[_discovery_address_pb2.DiscoveryAddress]
        already_added: bool
        name: str
        video_edge_info: DiscoverMediaDevicesResponse.DiscoveredVideoEdgeInfo
        available_to_add: DiscoverMediaDevicesResponse.AvailableToAdd
        already_added_new: DiscoverMediaDevicesResponse.AlreadyAdded
        def __init__(self, uuid: _Optional[str] = ..., vendor: _Optional[str] = ..., model: _Optional[str] = ..., addresses: _Optional[_Iterable[_Union[_discovery_address_pb2.DiscoveryAddress, _Mapping]]] = ..., already_added: bool = ..., name: _Optional[str] = ..., video_edge_info: _Optional[_Union[DiscoverMediaDevicesResponse.DiscoveredVideoEdgeInfo, _Mapping]] = ..., available_to_add: _Optional[_Union[DiscoverMediaDevicesResponse.AvailableToAdd, _Mapping]] = ..., already_added_new: _Optional[_Union[DiscoverMediaDevicesResponse.AlreadyAdded, _Mapping]] = ...) -> None: ...
    class AvailableToAdd(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class AlreadyAdded(_message.Message):
        __slots__ = ("media_device_id", "available_channel_ids_on_media_device")
        MEDIA_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_CHANNEL_IDS_ON_MEDIA_DEVICE_FIELD_NUMBER: _ClassVar[int]
        media_device_id: str
        available_channel_ids_on_media_device: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, media_device_id: _Optional[str] = ..., available_channel_ids_on_media_device: _Optional[_Iterable[str]] = ...) -> None: ...
    class DiscoveredVideoEdgeInfo(_message.Message):
        __slots__ = ("video_edge_id", "type", "installed", "room_id", "group_id", "channels", "color")
        VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        INSTALLED_FIELD_NUMBER: _ClassVar[int]
        ROOM_ID_FIELD_NUMBER: _ClassVar[int]
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNELS_FIELD_NUMBER: _ClassVar[int]
        COLOR_FIELD_NUMBER: _ClassVar[int]
        video_edge_id: str
        type: _about_pb2.About.Type
        installed: bool
        room_id: str
        group_id: str
        channels: _containers.RepeatedCompositeFieldContainer[DiscoverMediaDevicesResponse.AvailableChannel]
        color: _about_pb2.About.Color
        def __init__(self, video_edge_id: _Optional[str] = ..., type: _Optional[_Union[_about_pb2.About.Type, str]] = ..., installed: bool = ..., room_id: _Optional[str] = ..., group_id: _Optional[str] = ..., channels: _Optional[_Iterable[_Union[DiscoverMediaDevicesResponse.AvailableChannel, _Mapping]]] = ..., color: _Optional[_Union[_about_pb2.About.Color, str]] = ...) -> None: ...
    class AvailableChannel(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_armed", "video_edge_not_found", "video_edge_is_offline", "role_access_required")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        ROLE_ACCESS_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        video_edge_not_found: _response_pb2.DefaultError
        video_edge_is_offline: _response_pb2.DefaultError
        role_access_required: _response_pb2.DefaultError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., video_edge_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., video_edge_is_offline: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., role_access_required: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: DiscoverMediaDevicesResponse.Success
    failure: DiscoverMediaDevicesResponse.Failure
    def __init__(self, success: _Optional[_Union[DiscoverMediaDevicesResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[DiscoverMediaDevicesResponse.Failure, _Mapping]] = ...) -> None: ...
