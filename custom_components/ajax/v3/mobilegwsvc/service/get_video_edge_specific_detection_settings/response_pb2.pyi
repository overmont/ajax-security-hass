from systems.ajax.api.mobile.v2.common.video.videoedge.detector import detector_pb2 as _detector_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetVideoEdgeSpecificDetectionSettingsResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("pir", "motion", "object")
        PIR_FIELD_NUMBER: _ClassVar[int]
        MOTION_FIELD_NUMBER: _ClassVar[int]
        OBJECT_FIELD_NUMBER: _ClassVar[int]
        pir: _detector_pb2.PirDetectorSettings
        motion: _detector_pb2.MotionDetectorSettings
        object: _detector_pb2.ObjectDetectorSettings
        def __init__(self, pir: _Optional[_Union[_detector_pb2.PirDetectorSettings, _Mapping]] = ..., motion: _Optional[_Union[_detector_pb2.MotionDetectorSettings, _Mapping]] = ..., object: _Optional[_Union[_detector_pb2.ObjectDetectorSettings, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "space_not_found", "permission_denied", "video_edge_not_found", "channel_not_found", "detector_not_found")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        DETECTOR_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        space_not_found: _response_pb2.Error
        permission_denied: _response_pb2.Error
        video_edge_not_found: _response_pb2.Error
        channel_not_found: _response_pb2.Error
        detector_not_found: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., video_edge_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., channel_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., detector_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetVideoEdgeSpecificDetectionSettingsResponse.Success
    failure: GetVideoEdgeSpecificDetectionSettingsResponse.Failure
    def __init__(self, success: _Optional[_Union[GetVideoEdgeSpecificDetectionSettingsResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[GetVideoEdgeSpecificDetectionSettingsResponse.Failure, _Mapping]] = ...) -> None: ...
