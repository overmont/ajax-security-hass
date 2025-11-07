from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AlarmSuppressInfo(_message.Message):
    __slots__ = ("timer_duration",)
    TIMER_DURATION_FIELD_NUMBER: _ClassVar[int]
    timer_duration: _duration_pb2.Duration
    def __init__(self, timer_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
