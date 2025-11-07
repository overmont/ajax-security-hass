from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HubLogEvent(_message.Message):
    __slots__ = ("id", "video_scenario_triggered")
    ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_SCENARIO_TRIGGERED_FIELD_NUMBER: _ClassVar[int]
    id: str
    video_scenario_triggered: VideoScenarioTriggeredEvent
    def __init__(self, id: _Optional[str] = ..., video_scenario_triggered: _Optional[_Union[VideoScenarioTriggeredEvent, _Mapping]] = ...) -> None: ...

class VideoScenarioTriggeredEvent(_message.Message):
    __slots__ = ("scenario_name", "channel_gifs", "triggered_time")
    class ChannelGif(_message.Message):
        __slots__ = ("channel_guid", "channel_name", "room_name", "frames", "video_edge_id")
        CHANNEL_GUID_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
        ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
        FRAMES_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
        channel_guid: str
        channel_name: str
        room_name: str
        frames: _containers.RepeatedScalarFieldContainer[str]
        video_edge_id: str
        def __init__(self, channel_guid: _Optional[str] = ..., channel_name: _Optional[str] = ..., room_name: _Optional[str] = ..., frames: _Optional[_Iterable[str]] = ..., video_edge_id: _Optional[str] = ...) -> None: ...
    SCENARIO_NAME_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_GIFS_FIELD_NUMBER: _ClassVar[int]
    TRIGGERED_TIME_FIELD_NUMBER: _ClassVar[int]
    scenario_name: str
    channel_gifs: _containers.RepeatedCompositeFieldContainer[VideoScenarioTriggeredEvent.ChannelGif]
    triggered_time: _timestamp_pb2.Timestamp
    def __init__(self, scenario_name: _Optional[str] = ..., channel_gifs: _Optional[_Iterable[_Union[VideoScenarioTriggeredEvent.ChannelGif, _Mapping]]] = ..., triggered_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
