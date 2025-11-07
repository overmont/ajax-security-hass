from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.channel.detection import line_crossing_rule_pb2 as _line_crossing_rule_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetVideoEdgeLineCrossingSettingsResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("rules", "enabled_object_classes", "object_detector_mask", "max_rules_count")
        RULES_FIELD_NUMBER: _ClassVar[int]
        ENABLED_OBJECT_CLASSES_FIELD_NUMBER: _ClassVar[int]
        OBJECT_DETECTOR_MASK_FIELD_NUMBER: _ClassVar[int]
        MAX_RULES_COUNT_FIELD_NUMBER: _ClassVar[int]
        rules: _containers.RepeatedCompositeFieldContainer[_line_crossing_rule_pb2.LineCrossingRule]
        enabled_object_classes: _containers.RepeatedScalarFieldContainer[_types_pb2.ObjectClass]
        object_detector_mask: _types_pb2.Mask
        max_rules_count: int
        def __init__(self, rules: _Optional[_Iterable[_Union[_line_crossing_rule_pb2.LineCrossingRule, _Mapping]]] = ..., enabled_object_classes: _Optional[_Iterable[_Union[_types_pb2.ObjectClass, str]]] = ..., object_detector_mask: _Optional[_Union[_types_pb2.Mask, _Mapping]] = ..., max_rules_count: _Optional[int] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "space_not_found", "permission_denied", "video_edge_not_found", "channel_not_found", "line_crossing_settings_not_found")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        LINE_CROSSING_SETTINGS_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        space_not_found: _response_pb2.Error
        permission_denied: _response_pb2.Error
        video_edge_not_found: _response_pb2.Error
        channel_not_found: _response_pb2.Error
        line_crossing_settings_not_found: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., video_edge_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., channel_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., line_crossing_settings_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetVideoEdgeLineCrossingSettingsResponse.Success
    failure: GetVideoEdgeLineCrossingSettingsResponse.Failure
    def __init__(self, success: _Optional[_Union[GetVideoEdgeLineCrossingSettingsResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[GetVideoEdgeLineCrossingSettingsResponse.Failure, _Mapping]] = ...) -> None: ...
