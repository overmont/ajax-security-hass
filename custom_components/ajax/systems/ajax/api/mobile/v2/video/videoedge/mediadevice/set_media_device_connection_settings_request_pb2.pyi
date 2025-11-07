from systems.ajax.api.mobile.v2.common.video.videoedge.mediadevice import media_device_pb2 as _media_device_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.mediadevice import media_device_settings_pb2 as _media_device_settings_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.mediadevice import media_device_capabilities_pb2 as _media_device_capabilities_pb2
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetMediaDeviceConnectionSettingsRequest(_message.Message):
    __slots__ = ("video_edge_id", "media_device_id", "connection_settings", "space_locator")
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    MEDIA_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    media_device_id: str
    connection_settings: _media_device_settings_pb2.ConnectionSettings
    space_locator: _space_locator_pb2.SpaceLocator
    def __init__(self, video_edge_id: _Optional[str] = ..., media_device_id: _Optional[str] = ..., connection_settings: _Optional[_Union[_media_device_settings_pb2.ConnectionSettings, _Mapping]] = ..., space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ...) -> None: ...

class SetMediaDeviceConnectionSettingsResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("capabilities",)
        CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
        capabilities: _media_device_capabilities_pb2.MediaDeviceCapabilities
        def __init__(self, capabilities: _Optional[_Union[_media_device_capabilities_pb2.MediaDeviceCapabilities, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_armed", "video_edge_not_found", "device_not_found", "connection_failed", "video_edge_is_offline")
        class ConnectionFailedError(_message.Message):
            __slots__ = ("media_device_state",)
            MEDIA_DEVICE_STATE_FIELD_NUMBER: _ClassVar[int]
            media_device_state: _media_device_pb2.MediaDeviceState
            def __init__(self, media_device_state: _Optional[_Union[_media_device_pb2.MediaDeviceState, str]] = ...) -> None: ...
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        DEVICE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        CONNECTION_FAILED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        video_edge_not_found: _response_pb2.DefaultError
        device_not_found: _response_pb2.DefaultError
        connection_failed: SetMediaDeviceConnectionSettingsResponse.Failure.ConnectionFailedError
        video_edge_is_offline: _response_pb2.DefaultError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., video_edge_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., device_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., connection_failed: _Optional[_Union[SetMediaDeviceConnectionSettingsResponse.Failure.ConnectionFailedError, _Mapping]] = ..., video_edge_is_offline: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: SetMediaDeviceConnectionSettingsResponse.Success
    failure: SetMediaDeviceConnectionSettingsResponse.Failure
    def __init__(self, success: _Optional[_Union[SetMediaDeviceConnectionSettingsResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[SetMediaDeviceConnectionSettingsResponse.Failure, _Mapping]] = ...) -> None: ...
