from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.mediadevice import media_device_settings_pb2 as _media_device_settings_pb2
from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetMediaDeviceDesiredSettingsRequest(_message.Message):
    __slots__ = ("video_edge_id", "media_device_id", "channel_settings", "space_locator")
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    MEDIA_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    media_device_id: str
    channel_settings: _media_device_settings_pb2.ChannelSettings
    space_locator: _space_locator_pb2.SpaceLocator
    def __init__(self, video_edge_id: _Optional[str] = ..., media_device_id: _Optional[str] = ..., channel_settings: _Optional[_Union[_media_device_settings_pb2.ChannelSettings, _Mapping]] = ..., space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ...) -> None: ...

class SetMediaDeviceDesiredSettingsResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_armed", "video_edge_not_found", "device_not_found", "device_unavailable", "device_setup_in_progress", "channel_not_found", "video_edge_is_offline")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        DEVICE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        DEVICE_UNAVAILABLE_FIELD_NUMBER: _ClassVar[int]
        DEVICE_SETUP_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        video_edge_not_found: _response_pb2.DefaultError
        device_not_found: _response_pb2.DefaultError
        device_unavailable: _response_pb2.DefaultError
        device_setup_in_progress: _response_pb2.DefaultError
        channel_not_found: _response_pb2.DefaultError
        video_edge_is_offline: _response_pb2.DefaultError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., video_edge_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., device_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., device_unavailable: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., device_setup_in_progress: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., channel_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., video_edge_is_offline: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: SetMediaDeviceDesiredSettingsResponse.Success
    failure: SetMediaDeviceDesiredSettingsResponse.Failure
    def __init__(self, success: _Optional[_Union[SetMediaDeviceDesiredSettingsResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[SetMediaDeviceDesiredSettingsResponse.Failure, _Mapping]] = ...) -> None: ...
