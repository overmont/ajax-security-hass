from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.channel.detection import line_crossing_direction_pb2 as _line_crossing_direction_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddVideoEdgeLineCrossingRuleRequest(_message.Message):
    __slots__ = ("space_id", "video_edge_id", "channel_id", "name", "points", "direction", "object_classes")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CLASSES_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    channel_id: str
    name: str
    points: _containers.RepeatedCompositeFieldContainer[_types_pb2.Point2f]
    direction: _line_crossing_direction_pb2.LineCrossingDirection
    object_classes: _containers.RepeatedScalarFieldContainer[_types_pb2.ObjectClass]
    def __init__(self, space_id: _Optional[str] = ..., video_edge_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., name: _Optional[str] = ..., points: _Optional[_Iterable[_Union[_types_pb2.Point2f, _Mapping]]] = ..., direction: _Optional[_Union[_line_crossing_direction_pb2.LineCrossingDirection, str]] = ..., object_classes: _Optional[_Iterable[_Union[_types_pb2.ObjectClass, str]]] = ...) -> None: ...
