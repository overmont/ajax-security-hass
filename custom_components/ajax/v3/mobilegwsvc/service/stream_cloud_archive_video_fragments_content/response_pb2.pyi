from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.cloudarchive import fragment_status_pb2 as _fragment_status_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamCloudArchiveVideoFragmentsContentResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("fragment_content", "fragment_part_content", "init")
        FRAGMENT_CONTENT_FIELD_NUMBER: _ClassVar[int]
        FRAGMENT_PART_CONTENT_FIELD_NUMBER: _ClassVar[int]
        INIT_FIELD_NUMBER: _ClassVar[int]
        fragment_content: StreamCloudArchiveVideoFragmentsContentResponse.FragmentContent
        fragment_part_content: StreamCloudArchiveVideoFragmentsContentResponse.FragmentPartContent
        init: StreamCloudArchiveVideoFragmentsContentResponse.Init
        def __init__(self, fragment_content: _Optional[_Union[StreamCloudArchiveVideoFragmentsContentResponse.FragmentContent, _Mapping]] = ..., fragment_part_content: _Optional[_Union[StreamCloudArchiveVideoFragmentsContentResponse.FragmentPartContent, _Mapping]] = ..., init: _Optional[_Union[StreamCloudArchiveVideoFragmentsContentResponse.Init, _Mapping]] = ...) -> None: ...
    class Init(_message.Message):
        __slots__ = ("playback_duration_interval",)
        PLAYBACK_DURATION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
        playback_duration_interval: _duration_pb2.Duration
        def __init__(self, playback_duration_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    class FragmentContent(_message.Message):
        __slots__ = ("tag", "fragment_id", "status", "content_url")
        TAG_FIELD_NUMBER: _ClassVar[int]
        FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        CONTENT_URL_FIELD_NUMBER: _ClassVar[int]
        tag: str
        fragment_id: int
        status: _fragment_status_pb2.FragmentStatus
        content_url: str
        def __init__(self, tag: _Optional[str] = ..., fragment_id: _Optional[int] = ..., status: _Optional[_Union[_fragment_status_pb2.FragmentStatus, str]] = ..., content_url: _Optional[str] = ...) -> None: ...
    class FragmentPartContent(_message.Message):
        __slots__ = ("tag", "fragment_id", "offset", "status", "content_url", "content_url_headers")
        class Header(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        TAG_FIELD_NUMBER: _ClassVar[int]
        FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        CONTENT_URL_FIELD_NUMBER: _ClassVar[int]
        CONTENT_URL_HEADERS_FIELD_NUMBER: _ClassVar[int]
        tag: str
        fragment_id: int
        offset: int
        status: _fragment_status_pb2.FragmentStatus
        content_url: str
        content_url_headers: _containers.RepeatedCompositeFieldContainer[StreamCloudArchiveVideoFragmentsContentResponse.FragmentPartContent.Header]
        def __init__(self, tag: _Optional[str] = ..., fragment_id: _Optional[int] = ..., offset: _Optional[int] = ..., status: _Optional[_Union[_fragment_status_pb2.FragmentStatus, str]] = ..., content_url: _Optional[str] = ..., content_url_headers: _Optional[_Iterable[_Union[StreamCloudArchiveVideoFragmentsContentResponse.FragmentPartContent.Header, _Mapping]]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_not_found", "playback_limit_exceeded", "cloud_archive_not_found")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PLAYBACK_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
        CLOUD_ARCHIVE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_not_found: _response_pb2.Error
        playback_limit_exceeded: _response_pb2.Error
        cloud_archive_not_found: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., playback_limit_exceeded: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., cloud_archive_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamCloudArchiveVideoFragmentsContentResponse.Success
    failure: StreamCloudArchiveVideoFragmentsContentResponse.Failure
    def __init__(self, success: _Optional[_Union[StreamCloudArchiveVideoFragmentsContentResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[StreamCloudArchiveVideoFragmentsContentResponse.Failure, _Mapping]] = ...) -> None: ...
