from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FindAllCloudArchiveMetadataFragmentsInfoRequest(_message.Message):
    __slots__ = ("space_id", "video_edge_id", "channel_id", "metadata_type", "timestamp_range")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_RANGE_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    channel_id: str
    metadata_type: str
    timestamp_range: _types_pb2.TimestampRange
    def __init__(self, space_id: _Optional[str] = ..., video_edge_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., metadata_type: _Optional[str] = ..., timestamp_range: _Optional[_Union[_types_pb2.TimestampRange, _Mapping]] = ...) -> None: ...
