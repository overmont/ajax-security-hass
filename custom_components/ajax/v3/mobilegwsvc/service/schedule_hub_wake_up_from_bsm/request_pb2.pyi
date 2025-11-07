from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScheduleHubWakeUpFromBsmRequest(_message.Message):
    __slots__ = ("hub_id", "wake_up_time", "activity_period")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    WAKE_UP_TIME_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_PERIOD_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    wake_up_time: _timestamp_pb2.Timestamp
    activity_period: _duration_pb2.Duration
    def __init__(self, hub_id: _Optional[str] = ..., wake_up_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., activity_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
