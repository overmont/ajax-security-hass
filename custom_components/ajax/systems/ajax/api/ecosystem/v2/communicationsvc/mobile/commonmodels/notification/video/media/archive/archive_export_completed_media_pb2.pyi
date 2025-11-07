from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.video import types_pb2 as _types_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ArchiveExportCompletedMedia(_message.Message):
    __slots__ = ("recordings",)
    class ExportedRecording(_message.Message):
        __slots__ = ("codec", "start_timestamp", "timezone_offset", "url", "file_name")
        CODEC_FIELD_NUMBER: _ClassVar[int]
        START_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        TIMEZONE_OFFSET_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        codec: _types_pb2.VideoCodec
        start_timestamp: _timestamp_pb2.Timestamp
        timezone_offset: _duration_pb2.Duration
        url: str
        file_name: str
        def __init__(self, codec: _Optional[_Union[_types_pb2.VideoCodec, str]] = ..., start_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., timezone_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., url: _Optional[str] = ..., file_name: _Optional[str] = ...) -> None: ...
    RECORDINGS_FIELD_NUMBER: _ClassVar[int]
    recordings: _containers.RepeatedCompositeFieldContainer[ArchiveExportCompletedMedia.ExportedRecording]
    def __init__(self, recordings: _Optional[_Iterable[_Union[ArchiveExportCompletedMedia.ExportedRecording, _Mapping]]] = ...) -> None: ...
