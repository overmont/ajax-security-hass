from google.type import datetime_pb2 as _datetime_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TimeZone(_message.Message):
    __slots__ = ("time_zone",)
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    time_zone: _datetime_pb2.TimeZone
    def __init__(self, time_zone: _Optional[_Union[_datetime_pb2.TimeZone, _Mapping]] = ...) -> None: ...
