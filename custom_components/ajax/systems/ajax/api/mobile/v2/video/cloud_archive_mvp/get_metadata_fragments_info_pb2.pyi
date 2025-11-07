from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2
from systems.ajax.api.mobile.v2.video.cloud_archive_mvp import fragment_info_pb2 as _fragment_info_pb2
from systems.ajax.api.mobile.v2.video.cloud_archive_mvp import tz_entry_pb2 as _tz_entry_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CloudArchiveGetMetadataFragmentsInfoRequest(_message.Message):
    __slots__ = ("video_edge_guid", "channel_guid", "metadata_type", "ts_range", "space_id")
    VIDEO_EDGE_GUID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_GUID_FIELD_NUMBER: _ClassVar[int]
    METADATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    TS_RANGE_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    video_edge_guid: str
    channel_guid: str
    metadata_type: str
    ts_range: _types_pb2.TimestampRange
    space_id: str
    def __init__(self, video_edge_guid: _Optional[str] = ..., channel_guid: _Optional[str] = ..., metadata_type: _Optional[str] = ..., ts_range: _Optional[_Union[_types_pb2.TimestampRange, _Mapping]] = ..., space_id: _Optional[str] = ...) -> None: ...

class CloudArchiveGetMetadataFragmentsInfoResponse(_message.Message):
    __slots__ = ("fragments", "tz_map")
    FRAGMENTS_FIELD_NUMBER: _ClassVar[int]
    TZ_MAP_FIELD_NUMBER: _ClassVar[int]
    fragments: _containers.RepeatedCompositeFieldContainer[_fragment_info_pb2.CloudArchiveFragmentInfo]
    tz_map: _containers.RepeatedCompositeFieldContainer[_tz_entry_pb2.CloudArchiveTzEntry]
    def __init__(self, fragments: _Optional[_Iterable[_Union[_fragment_info_pb2.CloudArchiveFragmentInfo, _Mapping]]] = ..., tz_map: _Optional[_Iterable[_Union[_tz_entry_pb2.CloudArchiveTzEntry, _Mapping]]] = ...) -> None: ...
