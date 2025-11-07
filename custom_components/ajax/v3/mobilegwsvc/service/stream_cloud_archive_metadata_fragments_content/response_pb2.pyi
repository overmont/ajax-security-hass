from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.cloudarchive import fragment_status_pb2 as _fragment_status_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamCloudArchiveMetadataFragmentsContentResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("fragment_content",)
        FRAGMENT_CONTENT_FIELD_NUMBER: _ClassVar[int]
        fragment_content: StreamCloudArchiveMetadataFragmentsContentResponse.FragmentContent
        def __init__(self, fragment_content: _Optional[_Union[StreamCloudArchiveMetadataFragmentsContentResponse.FragmentContent, _Mapping]] = ...) -> None: ...
    class FragmentContent(_message.Message):
        __slots__ = ("tag", "fragment_id", "status", "content_url")
        class Frames(_message.Message):
            __slots__ = ("entries",)
            ENTRIES_FIELD_NUMBER: _ClassVar[int]
            entries: _containers.RepeatedCompositeFieldContainer[StreamCloudArchiveMetadataFragmentsContentResponse.FragmentContent.Frame]
            def __init__(self, entries: _Optional[_Iterable[_Union[StreamCloudArchiveMetadataFragmentsContentResponse.FragmentContent.Frame, _Mapping]]] = ...) -> None: ...
        class Frame(_message.Message):
            __slots__ = ("timestamp", "data")
            TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
            DATA_FIELD_NUMBER: _ClassVar[int]
            timestamp: int
            data: bytes
            def __init__(self, timestamp: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...
        TAG_FIELD_NUMBER: _ClassVar[int]
        FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        CONTENT_URL_FIELD_NUMBER: _ClassVar[int]
        tag: str
        fragment_id: int
        status: _fragment_status_pb2.FragmentStatus
        content_url: str
        def __init__(self, tag: _Optional[str] = ..., fragment_id: _Optional[int] = ..., status: _Optional[_Union[_fragment_status_pb2.FragmentStatus, str]] = ..., content_url: _Optional[str] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_not_found")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_not_found: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamCloudArchiveMetadataFragmentsContentResponse.Success
    failure: StreamCloudArchiveMetadataFragmentsContentResponse.Failure
    def __init__(self, success: _Optional[_Union[StreamCloudArchiveMetadataFragmentsContentResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[StreamCloudArchiveMetadataFragmentsContentResponse.Failure, _Mapping]] = ...) -> None: ...
