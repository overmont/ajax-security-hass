from systems.ajax.api.mobile.v2.common.video.videoedge.detector import detector_pb2 as _detector_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerDetector(_message.Message):
    __slots__ = ("id", "channel_id", "detector_type", "enabled")
    ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    id: str
    channel_id: str
    detector_type: _detector_pb2.DetectorType
    enabled: bool
    def __init__(self, id: _Optional[str] = ..., channel_id: _Optional[str] = ..., detector_type: _Optional[_Union[_detector_pb2.DetectorType, str]] = ..., enabled: bool = ...) -> None: ...
