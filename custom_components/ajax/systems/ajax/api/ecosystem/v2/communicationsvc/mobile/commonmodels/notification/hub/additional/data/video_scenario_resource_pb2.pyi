from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VideoScenarioResource(_message.Message):
    __slots__ = ("scenario_name", "trigger_time", "channel_metadata")
    class ChannelAlarmFrameMetadata(_message.Message):
        __slots__ = ("channel_id", "channel_name", "room_name", "frames_ready")
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
        ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
        FRAMES_READY_FIELD_NUMBER: _ClassVar[int]
        channel_id: str
        channel_name: str
        room_name: str
        frames_ready: int
        def __init__(self, channel_id: _Optional[str] = ..., channel_name: _Optional[str] = ..., room_name: _Optional[str] = ..., frames_ready: _Optional[int] = ...) -> None: ...
    SCENARIO_NAME_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_TIME_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_METADATA_FIELD_NUMBER: _ClassVar[int]
    scenario_name: str
    trigger_time: _timestamp_pb2.Timestamp
    channel_metadata: _containers.RepeatedCompositeFieldContainer[VideoScenarioResource.ChannelAlarmFrameMetadata]
    def __init__(self, scenario_name: _Optional[str] = ..., trigger_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., channel_metadata: _Optional[_Iterable[_Union[VideoScenarioResource.ChannelAlarmFrameMetadata, _Mapping]]] = ...) -> None: ...
