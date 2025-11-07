from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VideoScenarioData(_message.Message):
    __slots__ = ("channel_metadata",)
    class FramesStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FRAMES_STATUS_UNKNOWN: _ClassVar[VideoScenarioData.FramesStatus]
        FRAMES_STATUS_IN_PROGRESS: _ClassVar[VideoScenarioData.FramesStatus]
        FRAMES_STATUS_READY: _ClassVar[VideoScenarioData.FramesStatus]
    FRAMES_STATUS_UNKNOWN: VideoScenarioData.FramesStatus
    FRAMES_STATUS_IN_PROGRESS: VideoScenarioData.FramesStatus
    FRAMES_STATUS_READY: VideoScenarioData.FramesStatus
    class ChannelAlarmFrameMetadata(_message.Message):
        __slots__ = ("video_edge_id", "channel_id", "channel_name", "room_name", "frames_ready", "frames_status")
        VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
        ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
        FRAMES_READY_FIELD_NUMBER: _ClassVar[int]
        FRAMES_STATUS_FIELD_NUMBER: _ClassVar[int]
        video_edge_id: str
        channel_id: str
        channel_name: str
        room_name: str
        frames_ready: int
        frames_status: VideoScenarioData.FramesStatus
        def __init__(self, video_edge_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., channel_name: _Optional[str] = ..., room_name: _Optional[str] = ..., frames_ready: _Optional[int] = ..., frames_status: _Optional[_Union[VideoScenarioData.FramesStatus, str]] = ...) -> None: ...
    CHANNEL_METADATA_FIELD_NUMBER: _ClassVar[int]
    channel_metadata: _containers.RepeatedCompositeFieldContainer[VideoScenarioData.ChannelAlarmFrameMetadata]
    def __init__(self, channel_metadata: _Optional[_Iterable[_Union[VideoScenarioData.ChannelAlarmFrameMetadata, _Mapping]]] = ...) -> None: ...
