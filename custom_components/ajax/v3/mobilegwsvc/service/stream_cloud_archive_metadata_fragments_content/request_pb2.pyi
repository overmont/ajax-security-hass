from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamCloudArchiveMetadataFragmentsContentRequest(_message.Message):
    __slots__ = ("init", "get")
    class Init(_message.Message):
        __slots__ = ("space_id", "video_edge_id", "channel_id", "metadata_type")
        SPACE_ID_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        METADATA_TYPE_FIELD_NUMBER: _ClassVar[int]
        space_id: str
        video_edge_id: str
        channel_id: str
        metadata_type: str
        def __init__(self, space_id: _Optional[str] = ..., video_edge_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., metadata_type: _Optional[str] = ...) -> None: ...
    class Get(_message.Message):
        __slots__ = ("tag", "entries")
        class Entry(_message.Message):
            __slots__ = ("fragment_id",)
            FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
            fragment_id: int
            def __init__(self, fragment_id: _Optional[int] = ...) -> None: ...
        TAG_FIELD_NUMBER: _ClassVar[int]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        tag: str
        entries: _containers.RepeatedCompositeFieldContainer[StreamCloudArchiveMetadataFragmentsContentRequest.Get.Entry]
        def __init__(self, tag: _Optional[str] = ..., entries: _Optional[_Iterable[_Union[StreamCloudArchiveMetadataFragmentsContentRequest.Get.Entry, _Mapping]]] = ...) -> None: ...
    INIT_FIELD_NUMBER: _ClassVar[int]
    GET_FIELD_NUMBER: _ClassVar[int]
    init: StreamCloudArchiveMetadataFragmentsContentRequest.Init
    get: StreamCloudArchiveMetadataFragmentsContentRequest.Get
    def __init__(self, init: _Optional[_Union[StreamCloudArchiveMetadataFragmentsContentRequest.Init, _Mapping]] = ..., get: _Optional[_Union[StreamCloudArchiveMetadataFragmentsContentRequest.Get, _Mapping]] = ...) -> None: ...
