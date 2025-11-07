from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.channel import channel_pb2 as _channel_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Stream(_message.Message):
    __slots__ = ("id", "channel_guid", "device_info", "dcp_tag", "type", "filter", "live", "archive")
    class Live(_message.Message):
        __slots__ = ("input_rtc_stream_id", "use_ptz")
        INPUT_RTC_STREAM_ID_FIELD_NUMBER: _ClassVar[int]
        USE_PTZ_FIELD_NUMBER: _ClassVar[int]
        input_rtc_stream_id: str
        use_ptz: bool
        def __init__(self, input_rtc_stream_id: _Optional[str] = ..., use_ptz: bool = ...) -> None: ...
    class Archive(_message.Message):
        __slots__ = ("ts_range", "pos_update_interval", "group_id")
        TS_RANGE_FIELD_NUMBER: _ClassVar[int]
        POS_UPDATE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        ts_range: _types_pb2.TimestampRange
        pos_update_interval: _duration_pb2.Duration
        group_id: str
        def __init__(self, ts_range: _Optional[_Union[_types_pb2.TimestampRange, _Mapping]] = ..., pos_update_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., group_id: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_GUID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    DCP_TAG_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    LIVE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    id: str
    channel_guid: str
    device_info: _channel_pb2.MediaDeviceInfo
    dcp_tag: int
    type: _types_pb2.StreamType
    filter: _containers.RepeatedCompositeFieldContainer[_types_pb2.FrameTypeId]
    live: Stream.Live
    archive: Stream.Archive
    def __init__(self, id: _Optional[str] = ..., channel_guid: _Optional[str] = ..., device_info: _Optional[_Union[_channel_pb2.MediaDeviceInfo, _Mapping]] = ..., dcp_tag: _Optional[int] = ..., type: _Optional[_Union[_types_pb2.StreamType, str]] = ..., filter: _Optional[_Iterable[_Union[_types_pb2.FrameTypeId, _Mapping]]] = ..., live: _Optional[_Union[Stream.Live, _Mapping]] = ..., archive: _Optional[_Union[Stream.Archive, _Mapping]] = ...) -> None: ...
