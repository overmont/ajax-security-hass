from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoEdgeDetectorsEnabledRequest(_message.Message):
    __slots__ = ("space_id", "video_edge_id", "detectors")
    class DetectorEnabled(_message.Message):
        __slots__ = ("detector_id", "enabled")
        DETECTOR_ID_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        detector_id: str
        enabled: bool
        def __init__(self, detector_id: _Optional[str] = ..., enabled: bool = ...) -> None: ...
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    DETECTORS_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    detectors: _containers.RepeatedCompositeFieldContainer[SetVideoEdgeDetectorsEnabledRequest.DetectorEnabled]
    def __init__(self, space_id: _Optional[str] = ..., video_edge_id: _Optional[str] = ..., detectors: _Optional[_Iterable[_Union[SetVideoEdgeDetectorsEnabledRequest.DetectorEnabled, _Mapping]]] = ...) -> None: ...
