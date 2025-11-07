from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.onvif import onvif_settings_pb2 as _onvif_settings_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.rtsp import rtsp_settings_pb2 as _rtsp_settings_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoEdgeOnvifAndRtspPortsResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("onvif_settings", "rtsp_settings")
        ONVIF_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        RTSP_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        onvif_settings: _onvif_settings_pb2.OnvifSettings
        rtsp_settings: _rtsp_settings_pb2.RtspSettings
        def __init__(self, onvif_settings: _Optional[_Union[_onvif_settings_pb2.OnvifSettings, _Mapping]] = ..., rtsp_settings: _Optional[_Union[_rtsp_settings_pb2.RtspSettings, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_armed", "space_not_found", "video_edge_not_found", "video_edge_is_offline", "unimplemented_video_edge_command", "invalid_onvif_port", "invalid_rtsp_port")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        UNIMPLEMENTED_VIDEO_EDGE_COMMAND_FIELD_NUMBER: _ClassVar[int]
        INVALID_ONVIF_PORT_FIELD_NUMBER: _ClassVar[int]
        INVALID_RTSP_PORT_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_armed: _response_pb2.Error
        space_not_found: _response_pb2.Error
        video_edge_not_found: _response_pb2.Error
        video_edge_is_offline: _response_pb2.Error
        unimplemented_video_edge_command: _response_pb2.Error
        invalid_onvif_port: _response_pb2.Error
        invalid_rtsp_port: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., video_edge_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., video_edge_is_offline: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., unimplemented_video_edge_command: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., invalid_onvif_port: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., invalid_rtsp_port: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: SetVideoEdgeOnvifAndRtspPortsResponse.Success
    failure: SetVideoEdgeOnvifAndRtspPortsResponse.Failure
    def __init__(self, success: _Optional[_Union[SetVideoEdgeOnvifAndRtspPortsResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[SetVideoEdgeOnvifAndRtspPortsResponse.Failure, _Mapping]] = ...) -> None: ...
