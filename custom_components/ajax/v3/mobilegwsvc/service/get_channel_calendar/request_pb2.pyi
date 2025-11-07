from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetChannelCalendarRequest(_message.Message):
    __slots__ = ("space_id", "video_edge_id", "channel_id", "source_type")
    class SourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SOURCE_TYPE_UNSPECIFIED: _ClassVar[GetChannelCalendarRequest.SourceType]
        SOURCE_TYPE_VIDEO_EDGE_ARCHIVE: _ClassVar[GetChannelCalendarRequest.SourceType]
        SOURCE_TYPE_CLOUD_ARCHIVE: _ClassVar[GetChannelCalendarRequest.SourceType]
    SOURCE_TYPE_UNSPECIFIED: GetChannelCalendarRequest.SourceType
    SOURCE_TYPE_VIDEO_EDGE_ARCHIVE: GetChannelCalendarRequest.SourceType
    SOURCE_TYPE_CLOUD_ARCHIVE: GetChannelCalendarRequest.SourceType
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    channel_id: str
    source_type: GetChannelCalendarRequest.SourceType
    def __init__(self, space_id: _Optional[str] = ..., video_edge_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., source_type: _Optional[_Union[GetChannelCalendarRequest.SourceType, str]] = ...) -> None: ...
