from google.protobuf import duration_pb2 as _duration_pb2
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2
from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExportArchiveRequest(_message.Message):
    __slots__ = ("video_edge_id", "channel_id", "export_ranges", "stream_type", "with_audio", "with_figures", "video_source_type", "space_locator")
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    EXPORT_RANGES_FIELD_NUMBER: _ClassVar[int]
    STREAM_TYPE_FIELD_NUMBER: _ClassVar[int]
    WITH_AUDIO_FIELD_NUMBER: _ClassVar[int]
    WITH_FIGURES_FIELD_NUMBER: _ClassVar[int]
    VIDEO_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    channel_id: str
    export_ranges: _containers.RepeatedCompositeFieldContainer[_types_pb2.TimestampRange]
    stream_type: _types_pb2.StreamType
    with_audio: bool
    with_figures: bool
    video_source_type: _types_pb2.VideoSourceType
    space_locator: _space_locator_pb2.SpaceLocator
    def __init__(self, video_edge_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., export_ranges: _Optional[_Iterable[_Union[_types_pb2.TimestampRange, _Mapping]]] = ..., stream_type: _Optional[_Union[_types_pb2.StreamType, str]] = ..., with_audio: bool = ..., with_figures: bool = ..., video_source_type: _Optional[_Union[_types_pb2.VideoSourceType, str]] = ..., space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ...) -> None: ...

class ExportArchiveResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("export_id",)
        EXPORT_ID_FIELD_NUMBER: _ClassVar[int]
        export_id: str
        def __init__(self, export_id: _Optional[str] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "video_edge_not_found", "permission_denied", "channel_not_found", "too_many_parallel_exports", "archive_out_of_requested_time_range", "video_edge_is_offline", "cloud_archive_not_found", "exports_limit_exceeded")
        class ExportsLimitExceededError(_message.Message):
            __slots__ = ("timeout",)
            TIMEOUT_FIELD_NUMBER: _ClassVar[int]
            timeout: _duration_pb2.Duration
            def __init__(self, timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        TOO_MANY_PARALLEL_EXPORTS_FIELD_NUMBER: _ClassVar[int]
        ARCHIVE_OUT_OF_REQUESTED_TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        CLOUD_ARCHIVE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        EXPORTS_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        video_edge_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        channel_not_found: _response_pb2.DefaultError
        too_many_parallel_exports: _response_pb2.DefaultError
        archive_out_of_requested_time_range: _response_pb2.DefaultError
        video_edge_is_offline: _response_pb2.DefaultError
        cloud_archive_not_found: _response_pb2.DefaultError
        exports_limit_exceeded: ExportArchiveResponse.Failure.ExportsLimitExceededError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., video_edge_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., channel_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., too_many_parallel_exports: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., archive_out_of_requested_time_range: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., video_edge_is_offline: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., cloud_archive_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., exports_limit_exceeded: _Optional[_Union[ExportArchiveResponse.Failure.ExportsLimitExceededError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: ExportArchiveResponse.Success
    failure: ExportArchiveResponse.Failure
    def __init__(self, success: _Optional[_Union[ExportArchiveResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[ExportArchiveResponse.Failure, _Mapping]] = ...) -> None: ...
