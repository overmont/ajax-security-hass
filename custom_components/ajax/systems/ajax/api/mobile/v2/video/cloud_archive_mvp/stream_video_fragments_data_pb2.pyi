from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2
from systems.ajax.api.mobile.v2.video.cloud_archive_mvp import fragment_error_pb2 as _fragment_error_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CloudArchiveStreamVideoFragmentsDataRequest(_message.Message):
    __slots__ = ("video_edge_guid", "channel_guid", "stream_type", "space_id", "enable_presigned_urls_for_fragment_data", "enable_presigned_urls_for_fragment_part_data")
    VIDEO_EDGE_GUID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_GUID_FIELD_NUMBER: _ClassVar[int]
    STREAM_TYPE_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PRESIGNED_URLS_FOR_FRAGMENT_DATA_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PRESIGNED_URLS_FOR_FRAGMENT_PART_DATA_FIELD_NUMBER: _ClassVar[int]
    video_edge_guid: str
    channel_guid: str
    stream_type: _types_pb2.StreamType
    space_id: str
    enable_presigned_urls_for_fragment_data: bool
    enable_presigned_urls_for_fragment_part_data: bool
    def __init__(self, video_edge_guid: _Optional[str] = ..., channel_guid: _Optional[str] = ..., stream_type: _Optional[_Union[_types_pb2.StreamType, str]] = ..., space_id: _Optional[str] = ..., enable_presigned_urls_for_fragment_data: bool = ..., enable_presigned_urls_for_fragment_part_data: bool = ...) -> None: ...

class CloudArchiveStreamVideoFragmentsDataResponse(_message.Message):
    __slots__ = ("tag", "session_id", "fragment_data", "fragment_part_data")
    class CloudArchiveVideoFragmentData(_message.Message):
        __slots__ = ("fragment_id", "error", "data", "data_url")
        FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        DATA_URL_FIELD_NUMBER: _ClassVar[int]
        fragment_id: int
        error: _fragment_error_pb2.FragmentError
        data: bytes
        data_url: str
        def __init__(self, fragment_id: _Optional[int] = ..., error: _Optional[_Union[_fragment_error_pb2.FragmentError, str]] = ..., data: _Optional[bytes] = ..., data_url: _Optional[str] = ...) -> None: ...
    class CloudArchiveVideoFragmentPartData(_message.Message):
        __slots__ = ("fragment_id", "offset", "error", "data", "data_url", "data_url_header")
        class Header(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        DATA_URL_FIELD_NUMBER: _ClassVar[int]
        DATA_URL_HEADER_FIELD_NUMBER: _ClassVar[int]
        fragment_id: int
        offset: int
        error: _fragment_error_pb2.FragmentError
        data: bytes
        data_url: str
        data_url_header: CloudArchiveStreamVideoFragmentsDataResponse.CloudArchiveVideoFragmentPartData.Header
        def __init__(self, fragment_id: _Optional[int] = ..., offset: _Optional[int] = ..., error: _Optional[_Union[_fragment_error_pb2.FragmentError, str]] = ..., data: _Optional[bytes] = ..., data_url: _Optional[str] = ..., data_url_header: _Optional[_Union[CloudArchiveStreamVideoFragmentsDataResponse.CloudArchiveVideoFragmentPartData.Header, _Mapping]] = ...) -> None: ...
    TAG_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_DATA_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_PART_DATA_FIELD_NUMBER: _ClassVar[int]
    tag: str
    session_id: str
    fragment_data: CloudArchiveStreamVideoFragmentsDataResponse.CloudArchiveVideoFragmentData
    fragment_part_data: CloudArchiveStreamVideoFragmentsDataResponse.CloudArchiveVideoFragmentPartData
    def __init__(self, tag: _Optional[str] = ..., session_id: _Optional[str] = ..., fragment_data: _Optional[_Union[CloudArchiveStreamVideoFragmentsDataResponse.CloudArchiveVideoFragmentData, _Mapping]] = ..., fragment_part_data: _Optional[_Union[CloudArchiveStreamVideoFragmentsDataResponse.CloudArchiveVideoFragmentPartData, _Mapping]] = ...) -> None: ...
