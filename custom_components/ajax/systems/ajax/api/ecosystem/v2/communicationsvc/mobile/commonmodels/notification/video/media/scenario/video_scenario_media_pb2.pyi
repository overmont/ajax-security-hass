from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VideoScenarioMedia(_message.Message):
    __slots__ = ("channel_metadata",)
    class ChannelAlarmFrameMetadata(_message.Message):
        __slots__ = ("video_edge_id", "channel_id", "channel_name", "room_name", "frame_data_result")
        VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
        ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
        FRAME_DATA_RESULT_FIELD_NUMBER: _ClassVar[int]
        video_edge_id: str
        channel_id: str
        channel_name: str
        room_name: str
        frame_data_result: VideoScenarioMedia.FrameDataResult
        def __init__(self, video_edge_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., channel_name: _Optional[str] = ..., room_name: _Optional[str] = ..., frame_data_result: _Optional[_Union[VideoScenarioMedia.FrameDataResult, _Mapping]] = ...) -> None: ...
    class FrameDataResult(_message.Message):
        __slots__ = ("url_list", "permission_denied")
        URL_LIST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        url_list: VideoScenarioMedia.UrlList
        permission_denied: VideoScenarioMedia.PermissionDenied
        def __init__(self, url_list: _Optional[_Union[VideoScenarioMedia.UrlList, _Mapping]] = ..., permission_denied: _Optional[_Union[VideoScenarioMedia.PermissionDenied, _Mapping]] = ...) -> None: ...
    class UrlList(_message.Message):
        __slots__ = ("urls",)
        URLS_FIELD_NUMBER: _ClassVar[int]
        urls: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, urls: _Optional[_Iterable[str]] = ...) -> None: ...
    class PermissionDenied(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    CHANNEL_METADATA_FIELD_NUMBER: _ClassVar[int]
    channel_metadata: _containers.RepeatedCompositeFieldContainer[VideoScenarioMedia.ChannelAlarmFrameMetadata]
    def __init__(self, channel_metadata: _Optional[_Iterable[_Union[VideoScenarioMedia.ChannelAlarmFrameMetadata, _Mapping]]] = ...) -> None: ...
