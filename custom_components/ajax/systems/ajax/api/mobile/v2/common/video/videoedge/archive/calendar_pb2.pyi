from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Calendar(_message.Message):
    __slots__ = ("start_day", "days", "tz_map")
    class TzEntry(_message.Message):
        __slots__ = ("day", "offsets")
        DAY_FIELD_NUMBER: _ClassVar[int]
        OFFSETS_FIELD_NUMBER: _ClassVar[int]
        day: _timestamp_pb2.Timestamp
        offsets: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, day: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., offsets: _Optional[_Iterable[int]] = ...) -> None: ...
    START_DAY_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    TZ_MAP_FIELD_NUMBER: _ClassVar[int]
    start_day: _timestamp_pb2.Timestamp
    days: bytes
    tz_map: _containers.RepeatedCompositeFieldContainer[Calendar.TzEntry]
    def __init__(self, start_day: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., days: _Optional[bytes] = ..., tz_map: _Optional[_Iterable[_Union[Calendar.TzEntry, _Mapping]]] = ...) -> None: ...
