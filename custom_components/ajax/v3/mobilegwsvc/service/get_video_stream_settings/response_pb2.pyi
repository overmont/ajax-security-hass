from systems.ajax.api.mobile.v2.common.video.videoedge.mediadevice import media_device_capabilities_pb2 as _media_device_capabilities_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.mediadevice import media_device_settings_pb2 as _media_device_settings_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.video import setting_availability_mode_pb2 as _setting_availability_mode_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetVideoStreamSettingsResponse(_message.Message):
    __slots__ = ("success", "failure")
    class SettingsLimitationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SETTINGS_LIMITATION_MODE_UNSPECIFIED: _ClassVar[GetVideoStreamSettingsResponse.SettingsLimitationMode]
        SETTINGS_LIMITATION_MODE_NOT_LIMITED: _ClassVar[GetVideoStreamSettingsResponse.SettingsLimitationMode]
        SETTINGS_LIMITATION_MODE_LIMITED_BY_EXTRA_SERVICES: _ClassVar[GetVideoStreamSettingsResponse.SettingsLimitationMode]
    SETTINGS_LIMITATION_MODE_UNSPECIFIED: GetVideoStreamSettingsResponse.SettingsLimitationMode
    SETTINGS_LIMITATION_MODE_NOT_LIMITED: GetVideoStreamSettingsResponse.SettingsLimitationMode
    SETTINGS_LIMITATION_MODE_LIMITED_BY_EXTRA_SERVICES: GetVideoStreamSettingsResponse.SettingsLimitationMode
    class Success(_message.Message):
        __slots__ = ("main_settings", "sub_settings", "main_availability", "sub_availability", "main_limitations", "sub_limitations", "settings_limitation_mode")
        MAIN_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        SUB_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        MAIN_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
        SUB_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
        MAIN_LIMITATIONS_FIELD_NUMBER: _ClassVar[int]
        SUB_LIMITATIONS_FIELD_NUMBER: _ClassVar[int]
        SETTINGS_LIMITATION_MODE_FIELD_NUMBER: _ClassVar[int]
        main_settings: _media_device_settings_pb2.VideoSettings.Stream
        sub_settings: _media_device_settings_pb2.VideoSettings.Stream
        main_availability: GetVideoStreamSettingsResponse.VideoStreamSettingsAvailability
        sub_availability: GetVideoStreamSettingsResponse.VideoStreamSettingsAvailability
        main_limitations: _media_device_capabilities_pb2.VideoCapabilities.Stream
        sub_limitations: _media_device_capabilities_pb2.VideoCapabilities.Stream
        settings_limitation_mode: GetVideoStreamSettingsResponse.SettingsLimitationMode
        def __init__(self, main_settings: _Optional[_Union[_media_device_settings_pb2.VideoSettings.Stream, _Mapping]] = ..., sub_settings: _Optional[_Union[_media_device_settings_pb2.VideoSettings.Stream, _Mapping]] = ..., main_availability: _Optional[_Union[GetVideoStreamSettingsResponse.VideoStreamSettingsAvailability, _Mapping]] = ..., sub_availability: _Optional[_Union[GetVideoStreamSettingsResponse.VideoStreamSettingsAvailability, _Mapping]] = ..., main_limitations: _Optional[_Union[_media_device_capabilities_pb2.VideoCapabilities.Stream, _Mapping]] = ..., sub_limitations: _Optional[_Union[_media_device_capabilities_pb2.VideoCapabilities.Stream, _Mapping]] = ..., settings_limitation_mode: _Optional[_Union[GetVideoStreamSettingsResponse.SettingsLimitationMode, str]] = ...) -> None: ...
    class VideoStreamSettingsAvailability(_message.Message):
        __slots__ = ("resolution", "codec", "fps", "bitrate_type", "bitrate", "gop_size", "quality")
        RESOLUTION_FIELD_NUMBER: _ClassVar[int]
        CODEC_FIELD_NUMBER: _ClassVar[int]
        FPS_FIELD_NUMBER: _ClassVar[int]
        BITRATE_TYPE_FIELD_NUMBER: _ClassVar[int]
        BITRATE_FIELD_NUMBER: _ClassVar[int]
        GOP_SIZE_FIELD_NUMBER: _ClassVar[int]
        QUALITY_FIELD_NUMBER: _ClassVar[int]
        resolution: _setting_availability_mode_pb2.SettingAvailabilityMode
        codec: _setting_availability_mode_pb2.SettingAvailabilityMode
        fps: _setting_availability_mode_pb2.SettingAvailabilityMode
        bitrate_type: _setting_availability_mode_pb2.SettingAvailabilityMode
        bitrate: _setting_availability_mode_pb2.SettingAvailabilityMode
        gop_size: _setting_availability_mode_pb2.SettingAvailabilityMode
        quality: _setting_availability_mode_pb2.SettingAvailabilityMode
        def __init__(self, resolution: _Optional[_Union[_setting_availability_mode_pb2.SettingAvailabilityMode, str]] = ..., codec: _Optional[_Union[_setting_availability_mode_pb2.SettingAvailabilityMode, str]] = ..., fps: _Optional[_Union[_setting_availability_mode_pb2.SettingAvailabilityMode, str]] = ..., bitrate_type: _Optional[_Union[_setting_availability_mode_pb2.SettingAvailabilityMode, str]] = ..., bitrate: _Optional[_Union[_setting_availability_mode_pb2.SettingAvailabilityMode, str]] = ..., gop_size: _Optional[_Union[_setting_availability_mode_pb2.SettingAvailabilityMode, str]] = ..., quality: _Optional[_Union[_setting_availability_mode_pb2.SettingAvailabilityMode, str]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_not_found", "video_edge_not_found", "channel_not_found", "stream_settings_not_found")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        STREAM_SETTINGS_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_not_found: _response_pb2.Error
        video_edge_not_found: _response_pb2.Error
        channel_not_found: _response_pb2.Error
        stream_settings_not_found: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., video_edge_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., channel_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., stream_settings_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetVideoStreamSettingsResponse.Success
    failure: GetVideoStreamSettingsResponse.Failure
    def __init__(self, success: _Optional[_Union[GetVideoStreamSettingsResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[GetVideoStreamSettingsResponse.Failure, _Mapping]] = ...) -> None: ...
