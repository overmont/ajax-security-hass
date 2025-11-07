from systems.ajax.api.mobile.v2.video.cloud_archive_mvp import fragment_error_pb2 as _fragment_error_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CloudArchiveStreamMetadataFragmentsDataRequest(_message.Message):
    __slots__ = ("video_edge_guid", "channel_guid", "metadata_type", "space_id", "enable_presigned_urls_for_fragment_data")
    VIDEO_EDGE_GUID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_GUID_FIELD_NUMBER: _ClassVar[int]
    METADATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PRESIGNED_URLS_FOR_FRAGMENT_DATA_FIELD_NUMBER: _ClassVar[int]
    video_edge_guid: str
    channel_guid: str
    metadata_type: str
    space_id: str
    enable_presigned_urls_for_fragment_data: bool
    def __init__(self, video_edge_guid: _Optional[str] = ..., channel_guid: _Optional[str] = ..., metadata_type: _Optional[str] = ..., space_id: _Optional[str] = ..., enable_presigned_urls_for_fragment_data: bool = ...) -> None: ...

class CloudArchiveStreamMetadataFragmentsDataResponse(_message.Message):
    __slots__ = ("tag", "session_id", "fragment_data")
    class CloudArchiveMetadataFragmentData(_message.Message):
        __slots__ = ("fragment_id", "error", "data", "data_url")
        class Frames(_message.Message):
            __slots__ = ("entries",)
            ENTRIES_FIELD_NUMBER: _ClassVar[int]
            entries: _containers.RepeatedCompositeFieldContainer[CloudArchiveStreamMetadataFragmentsDataResponse.CloudArchiveMetadataFragmentData.Frame]
            def __init__(self, entries: _Optional[_Iterable[_Union[CloudArchiveStreamMetadataFragmentsDataResponse.CloudArchiveMetadataFragmentData.Frame, _Mapping]]] = ...) -> None: ...
        class Frame(_message.Message):
            __slots__ = ("ts", "data")
            TS_FIELD_NUMBER: _ClassVar[int]
            DATA_FIELD_NUMBER: _ClassVar[int]
            ts: int
            data: bytes
            def __init__(self, ts: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...
        FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        DATA_URL_FIELD_NUMBER: _ClassVar[int]
        fragment_id: int
        error: _fragment_error_pb2.FragmentError
        data: bytes
        data_url: str
        def __init__(self, fragment_id: _Optional[int] = ..., error: _Optional[_Union[_fragment_error_pb2.FragmentError, str]] = ..., data: _Optional[bytes] = ..., data_url: _Optional[str] = ...) -> None: ...
    TAG_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_DATA_FIELD_NUMBER: _ClassVar[int]
    tag: str
    session_id: str
    fragment_data: CloudArchiveStreamMetadataFragmentsDataResponse.CloudArchiveMetadataFragmentData
    def __init__(self, tag: _Optional[str] = ..., session_id: _Optional[str] = ..., fragment_data: _Optional[_Union[CloudArchiveStreamMetadataFragmentsDataResponse.CloudArchiveMetadataFragmentData, _Mapping]] = ...) -> None: ...
