from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StorageDeviceWriteMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STORAGE_DEVICE_WRITE_MODE_UNSPECIFIED: _ClassVar[StorageDeviceWriteMode]
    STORAGE_DEVICE_WRITE_MODE_MIRRORED: _ClassVar[StorageDeviceWriteMode]
    STORAGE_DEVICE_WRITE_MODE_ROUND_ROBIN: _ClassVar[StorageDeviceWriteMode]

class MaxRingDepth(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MAX_RING_DEPTH_UNSPECIFIED: _ClassVar[MaxRingDepth]
    MAX_RING_DEPTH_1_DAY: _ClassVar[MaxRingDepth]
    MAX_RING_DEPTH_2_DAYS: _ClassVar[MaxRingDepth]
    MAX_RING_DEPTH_3_DAYS: _ClassVar[MaxRingDepth]
    MAX_RING_DEPTH_7_DAYS: _ClassVar[MaxRingDepth]
    MAX_RING_DEPTH_14_DAYS: _ClassVar[MaxRingDepth]
    MAX_RING_DEPTH_28_DAYS: _ClassVar[MaxRingDepth]
    MAX_RING_DEPTH_30_DAYS: _ClassVar[MaxRingDepth]
    MAX_RING_DEPTH_60_DAYS: _ClassVar[MaxRingDepth]
    MAX_RING_DEPTH_90_DAYS: _ClassVar[MaxRingDepth]
    MAX_RING_DEPTH_180_DAYS: _ClassVar[MaxRingDepth]
    MAX_RING_DEPTH_360_DAYS: _ClassVar[MaxRingDepth]
    MAX_RING_DEPTH_UNLIMITED: _ClassVar[MaxRingDepth]

class RecordMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RM_UNKNOWN: _ClassVar[RecordMode]
    RM_DISABLED: _ClassVar[RecordMode]
    RM_PERMANENT: _ClassVar[RecordMode]
    RM_ON_DETECTION: _ClassVar[RecordMode]

class RecordPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RP_UNKNOWN: _ClassVar[RecordPolicy]
    RP_ALWAYS: _ClassVar[RecordPolicy]
    RP_WHEN_REQUESTED: _ClassVar[RecordPolicy]

class PlayerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PS_NONE: _ClassVar[PlayerState]
    PS_PLAYING: _ClassVar[PlayerState]
    PS_PAUSED: _ClassVar[PlayerState]
STORAGE_DEVICE_WRITE_MODE_UNSPECIFIED: StorageDeviceWriteMode
STORAGE_DEVICE_WRITE_MODE_MIRRORED: StorageDeviceWriteMode
STORAGE_DEVICE_WRITE_MODE_ROUND_ROBIN: StorageDeviceWriteMode
MAX_RING_DEPTH_UNSPECIFIED: MaxRingDepth
MAX_RING_DEPTH_1_DAY: MaxRingDepth
MAX_RING_DEPTH_2_DAYS: MaxRingDepth
MAX_RING_DEPTH_3_DAYS: MaxRingDepth
MAX_RING_DEPTH_7_DAYS: MaxRingDepth
MAX_RING_DEPTH_14_DAYS: MaxRingDepth
MAX_RING_DEPTH_28_DAYS: MaxRingDepth
MAX_RING_DEPTH_30_DAYS: MaxRingDepth
MAX_RING_DEPTH_60_DAYS: MaxRingDepth
MAX_RING_DEPTH_90_DAYS: MaxRingDepth
MAX_RING_DEPTH_180_DAYS: MaxRingDepth
MAX_RING_DEPTH_360_DAYS: MaxRingDepth
MAX_RING_DEPTH_UNLIMITED: MaxRingDepth
RM_UNKNOWN: RecordMode
RM_DISABLED: RecordMode
RM_PERMANENT: RecordMode
RM_ON_DETECTION: RecordMode
RP_UNKNOWN: RecordPolicy
RP_ALWAYS: RecordPolicy
RP_WHEN_REQUESTED: RecordPolicy
PS_NONE: PlayerState
PS_PLAYING: PlayerState
PS_PAUSED: PlayerState

class Archive(_message.Message):
    __slots__ = ("ring_depth", "stats", "frame_drop_events", "max_ring_depth", "storage_device_write_mode")
    RING_DEPTH_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    FRAME_DROP_EVENTS_FIELD_NUMBER: _ClassVar[int]
    MAX_RING_DEPTH_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DEVICE_WRITE_MODE_FIELD_NUMBER: _ClassVar[int]
    ring_depth: _duration_pb2.Duration
    stats: Stats
    frame_drop_events: FrameDropEvents
    max_ring_depth: MaxRingDepth
    storage_device_write_mode: StorageDeviceWriteMode
    def __init__(self, ring_depth: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., stats: _Optional[_Union[Stats, _Mapping]] = ..., frame_drop_events: _Optional[_Union[FrameDropEvents, _Mapping]] = ..., max_ring_depth: _Optional[_Union[MaxRingDepth, str]] = ..., storage_device_write_mode: _Optional[_Union[StorageDeviceWriteMode, str]] = ...) -> None: ...

class Stats(_message.Message):
    __slots__ = ("archive_duration",)
    ARCHIVE_DURATION_FIELD_NUMBER: _ClassVar[int]
    archive_duration: _duration_pb2.Duration
    def __init__(self, archive_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class FrameDropEvents(_message.Message):
    __slots__ = ("count", "time_ranges")
    COUNT_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGES_FIELD_NUMBER: _ClassVar[int]
    count: int
    time_ranges: _containers.RepeatedCompositeFieldContainer[_types_pb2.TimestampRange]
    def __init__(self, count: _Optional[int] = ..., time_ranges: _Optional[_Iterable[_Union[_types_pb2.TimestampRange, _Mapping]]] = ...) -> None: ...

class PlayerStatus(_message.Message):
    __slots__ = ("state", "pos")
    STATE_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    state: PlayerState
    pos: _timestamp_pb2.Timestamp
    def __init__(self, state: _Optional[_Union[PlayerState, str]] = ..., pos: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Timeline(_message.Message):
    __slots__ = ("update_type", "ts_range", "seconds", "tz_map")
    class UpdateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[Timeline.UpdateType]
        MERGE: _ClassVar[Timeline.UpdateType]
        REPLACE: _ClassVar[Timeline.UpdateType]
    NONE: Timeline.UpdateType
    MERGE: Timeline.UpdateType
    REPLACE: Timeline.UpdateType
    class TzEntry(_message.Message):
        __slots__ = ("ts", "tz_offset")
        TS_FIELD_NUMBER: _ClassVar[int]
        TZ_OFFSET_FIELD_NUMBER: _ClassVar[int]
        ts: _timestamp_pb2.Timestamp
        tz_offset: _duration_pb2.Duration
        def __init__(self, ts: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., tz_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TS_RANGE_FIELD_NUMBER: _ClassVar[int]
    SECONDS_FIELD_NUMBER: _ClassVar[int]
    TZ_MAP_FIELD_NUMBER: _ClassVar[int]
    update_type: Timeline.UpdateType
    ts_range: _types_pb2.TimestampRange
    seconds: bytes
    tz_map: _containers.RepeatedCompositeFieldContainer[Timeline.TzEntry]
    def __init__(self, update_type: _Optional[_Union[Timeline.UpdateType, str]] = ..., ts_range: _Optional[_Union[_types_pb2.TimestampRange, _Mapping]] = ..., seconds: _Optional[bytes] = ..., tz_map: _Optional[_Iterable[_Union[Timeline.TzEntry, _Mapping]]] = ...) -> None: ...
