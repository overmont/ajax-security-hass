from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.onvif import onvif_settings_pb2 as _onvif_settings_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddVideoEdgeOnvifUserResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("settings",)
        SETTINGS_FIELD_NUMBER: _ClassVar[int]
        settings: _onvif_settings_pb2.OnvifSettings
        def __init__(self, settings: _Optional[_Union[_onvif_settings_pb2.OnvifSettings, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_armed", "space_not_found", "video_edge_not_found", "video_edge_is_offline", "unimplemented_video_edge_command", "onvif_user_already_exists", "onvif_user_limit_exceeded")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        UNIMPLEMENTED_VIDEO_EDGE_COMMAND_FIELD_NUMBER: _ClassVar[int]
        ONVIF_USER_ALREADY_EXISTS_FIELD_NUMBER: _ClassVar[int]
        ONVIF_USER_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_armed: _response_pb2.Error
        space_not_found: _response_pb2.Error
        video_edge_not_found: _response_pb2.Error
        video_edge_is_offline: _response_pb2.Error
        unimplemented_video_edge_command: _response_pb2.Error
        onvif_user_already_exists: _response_pb2.Error
        onvif_user_limit_exceeded: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., video_edge_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., video_edge_is_offline: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., unimplemented_video_edge_command: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., onvif_user_already_exists: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., onvif_user_limit_exceeded: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: AddVideoEdgeOnvifUserResponse.Success
    failure: AddVideoEdgeOnvifUserResponse.Failure
    def __init__(self, success: _Optional[_Union[AddVideoEdgeOnvifUserResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[AddVideoEdgeOnvifUserResponse.Failure, _Mapping]] = ...) -> None: ...
