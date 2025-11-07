from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ajax.dcp.v1 import archive_pb2 as _archive_pb2
from ajax.dcp.v1 import ptz_pb2 as _ptz_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompressionMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CM_UNKNOWN: _ClassVar[CompressionMethod]
    CM_GZIP: _ClassVar[CompressionMethod]

class VideoStreamingQuality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VSQ_UNKNOWN: _ClassVar[VideoStreamingQuality]
    VSQ_HIGH: _ClassVar[VideoStreamingQuality]
    VSQ_MEDIUM: _ClassVar[VideoStreamingQuality]
    VSQ_LOW: _ClassVar[VideoStreamingQuality]
CM_UNKNOWN: CompressionMethod
CM_GZIP: CompressionMethod
VSQ_UNKNOWN: VideoStreamingQuality
VSQ_HIGH: VideoStreamingQuality
VSQ_MEDIUM: VideoStreamingQuality
VSQ_LOW: VideoStreamingQuality

class ClientMsg(_message.Message):
    __slots__ = ("tag", "hello", "archive_reopen", "archive_seek", "archive_play", "archive_play_range", "archive_change_range", "archive_pause", "archive_multi_play_range", "ptz_move", "ptz_zoom", "ptz_focus", "ptz_stop", "sync_marker")
    class Hello(_message.Message):
        __slots__ = ("supported_compression_methods",)
        SUPPORTED_COMPRESSION_METHODS_FIELD_NUMBER: _ClassVar[int]
        supported_compression_methods: _containers.RepeatedScalarFieldContainer[CompressionMethod]
        def __init__(self, supported_compression_methods: _Optional[_Iterable[_Union[CompressionMethod, str]]] = ...) -> None: ...
    TAG_FIELD_NUMBER: _ClassVar[int]
    HELLO_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_REOPEN_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_SEEK_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_PLAY_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_PLAY_RANGE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_CHANGE_RANGE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_PAUSE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_MULTI_PLAY_RANGE_FIELD_NUMBER: _ClassVar[int]
    PTZ_MOVE_FIELD_NUMBER: _ClassVar[int]
    PTZ_ZOOM_FIELD_NUMBER: _ClassVar[int]
    PTZ_FOCUS_FIELD_NUMBER: _ClassVar[int]
    PTZ_STOP_FIELD_NUMBER: _ClassVar[int]
    SYNC_MARKER_FIELD_NUMBER: _ClassVar[int]
    tag: int
    hello: ClientMsg.Hello
    archive_reopen: _archive_pb2.ArchiveReopen
    archive_seek: _archive_pb2.ArchiveSeek
    archive_play: _archive_pb2.ArchivePlay
    archive_play_range: _archive_pb2.ArchivePlayRange
    archive_change_range: _archive_pb2.ArchiveChangeRange
    archive_pause: _archive_pb2.ArchivePause
    archive_multi_play_range: _archive_pb2.ArchiveMultiPlayRange
    ptz_move: _ptz_pb2.PtzMove
    ptz_zoom: _ptz_pb2.PtzZoom
    ptz_focus: _ptz_pb2.PtzFocus
    ptz_stop: _ptz_pb2.PtzStop
    sync_marker: int
    def __init__(self, tag: _Optional[int] = ..., hello: _Optional[_Union[ClientMsg.Hello, _Mapping]] = ..., archive_reopen: _Optional[_Union[_archive_pb2.ArchiveReopen, _Mapping]] = ..., archive_seek: _Optional[_Union[_archive_pb2.ArchiveSeek, _Mapping]] = ..., archive_play: _Optional[_Union[_archive_pb2.ArchivePlay, _Mapping]] = ..., archive_play_range: _Optional[_Union[_archive_pb2.ArchivePlayRange, _Mapping]] = ..., archive_change_range: _Optional[_Union[_archive_pb2.ArchiveChangeRange, _Mapping]] = ..., archive_pause: _Optional[_Union[_archive_pb2.ArchivePause, _Mapping]] = ..., archive_multi_play_range: _Optional[_Union[_archive_pb2.ArchiveMultiPlayRange, _Mapping]] = ..., ptz_move: _Optional[_Union[_ptz_pb2.PtzMove, _Mapping]] = ..., ptz_zoom: _Optional[_Union[_ptz_pb2.PtzZoom, _Mapping]] = ..., ptz_focus: _Optional[_Union[_ptz_pb2.PtzFocus, _Mapping]] = ..., ptz_stop: _Optional[_Union[_ptz_pb2.PtzStop, _Mapping]] = ..., sync_marker: _Optional[int] = ...) -> None: ...

class ServerMsg(_message.Message):
    __slots__ = ("tag", "hello", "frame_data", "archive_status", "archive_timeline", "quality_report", "compressed", "sync_marker")
    class Hello(_message.Message):
        __slots__ = ("supports_archive_reopen",)
        SUPPORTS_ARCHIVE_REOPEN_FIELD_NUMBER: _ClassVar[int]
        supports_archive_reopen: bool
        def __init__(self, supports_archive_reopen: bool = ...) -> None: ...
    class Compressed(_message.Message):
        __slots__ = ("method", "data")
        METHOD_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        method: CompressionMethod
        data: bytes
        def __init__(self, method: _Optional[_Union[CompressionMethod, str]] = ..., data: _Optional[bytes] = ...) -> None: ...
    class Uncompressed(_message.Message):
        __slots__ = ("frame_data", "archive_timeline")
        FRAME_DATA_FIELD_NUMBER: _ClassVar[int]
        ARCHIVE_TIMELINE_FIELD_NUMBER: _ClassVar[int]
        frame_data: FrameData
        archive_timeline: _archive_pb2.ArchiveTimeline
        def __init__(self, frame_data: _Optional[_Union[FrameData, _Mapping]] = ..., archive_timeline: _Optional[_Union[_archive_pb2.ArchiveTimeline, _Mapping]] = ...) -> None: ...
    TAG_FIELD_NUMBER: _ClassVar[int]
    HELLO_FIELD_NUMBER: _ClassVar[int]
    FRAME_DATA_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_STATUS_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_TIMELINE_FIELD_NUMBER: _ClassVar[int]
    QUALITY_REPORT_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    SYNC_MARKER_FIELD_NUMBER: _ClassVar[int]
    tag: int
    hello: ServerMsg.Hello
    frame_data: FrameData
    archive_status: _archive_pb2.ArchivePlayerStatus
    archive_timeline: _archive_pb2.ArchiveTimeline
    quality_report: QualityReport
    compressed: ServerMsg.Compressed
    sync_marker: int
    def __init__(self, tag: _Optional[int] = ..., hello: _Optional[_Union[ServerMsg.Hello, _Mapping]] = ..., frame_data: _Optional[_Union[FrameData, _Mapping]] = ..., archive_status: _Optional[_Union[_archive_pb2.ArchivePlayerStatus, _Mapping]] = ..., archive_timeline: _Optional[_Union[_archive_pb2.ArchiveTimeline, _Mapping]] = ..., quality_report: _Optional[_Union[QualityReport, _Mapping]] = ..., compressed: _Optional[_Union[ServerMsg.Compressed, _Mapping]] = ..., sync_marker: _Optional[int] = ...) -> None: ...

class Frame(_message.Message):
    __slots__ = ("ts", "type", "data")
    TS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ts: _timestamp_pb2.Timestamp
    type: str
    data: bytes
    def __init__(self, ts: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., type: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class FrameData(_message.Message):
    __slots__ = ("frames",)
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    frames: _containers.RepeatedCompositeFieldContainer[Frame]
    def __init__(self, frames: _Optional[_Iterable[_Union[Frame, _Mapping]]] = ...) -> None: ...

class QualityReport(_message.Message):
    __slots__ = ("video_streaming_quality",)
    VIDEO_STREAMING_QUALITY_FIELD_NUMBER: _ClassVar[int]
    video_streaming_quality: VideoStreamingQuality
    def __init__(self, video_streaming_quality: _Optional[_Union[VideoStreamingQuality, str]] = ...) -> None: ...
