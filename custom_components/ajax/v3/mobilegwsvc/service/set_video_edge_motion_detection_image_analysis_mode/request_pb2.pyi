from systems.ajax.api.mobile.v2.common.video.videoedge.channel.detection import image_analysis_mode_pb2 as _image_analysis_mode_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoEdgeMotionDetectionImageAnalysisModeRequest(_message.Message):
    __slots__ = ("space_id", "video_edge_id", "channel_id", "image_analysis_mode")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ANALYSIS_MODE_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    channel_id: str
    image_analysis_mode: _image_analysis_mode_pb2.ImageAnalysisMode
    def __init__(self, space_id: _Optional[str] = ..., video_edge_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., image_analysis_mode: _Optional[_Union[_image_analysis_mode_pb2.ImageAnalysisMode, str]] = ...) -> None: ...
