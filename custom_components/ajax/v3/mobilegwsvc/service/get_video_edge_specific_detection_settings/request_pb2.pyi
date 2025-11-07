from systems.ajax.api.mobile.v2.common.video.videoedge.channel.detection import detector_locator_pb2 as _detector_locator_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetVideoEdgeSpecificDetectionSettingsRequest(_message.Message):
    __slots__ = ("space_id", "video_edge_id", "detector_locator")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    detector_locator: _detector_locator_pb2.DetectorLocator
    def __init__(self, space_id: _Optional[str] = ..., video_edge_id: _Optional[str] = ..., detector_locator: _Optional[_Union[_detector_locator_pb2.DetectorLocator, _Mapping]] = ...) -> None: ...
