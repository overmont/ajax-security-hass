from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MonitoringState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[MonitoringState]
    ARMED: _ClassVar[MonitoringState]
    ALWAYS: _ClassVar[MonitoringState]
UNKNOWN: MonitoringState
ARMED: MonitoringState
ALWAYS: MonitoringState

class TargetVideoEdge(_message.Message):
    __slots__ = ("video_edge_id", "channels")
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    channels: _containers.RepeatedCompositeFieldContainer[TargetChannel]
    def __init__(self, video_edge_id: _Optional[str] = ..., channels: _Optional[_Iterable[_Union[TargetChannel, _Mapping]]] = ...) -> None: ...

class TargetChannel(_message.Message):
    __slots__ = ("channel_id",)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    def __init__(self, channel_id: _Optional[str] = ...) -> None: ...
