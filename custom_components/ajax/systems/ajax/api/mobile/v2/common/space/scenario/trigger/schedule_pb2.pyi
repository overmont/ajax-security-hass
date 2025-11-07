from google.type import dayofweek_pb2 as _dayofweek_pb2
from google.type import timeofday_pb2 as _timeofday_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScheduleTrigger(_message.Message):
    __slots__ = ("time", "days")
    TIME_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    time: _timeofday_pb2.TimeOfDay
    days: _containers.RepeatedScalarFieldContainer[_dayofweek_pb2.DayOfWeek]
    def __init__(self, time: _Optional[_Union[_timeofday_pb2.TimeOfDay, _Mapping]] = ..., days: _Optional[_Iterable[_Union[_dayofweek_pb2.DayOfWeek, str]]] = ...) -> None: ...
