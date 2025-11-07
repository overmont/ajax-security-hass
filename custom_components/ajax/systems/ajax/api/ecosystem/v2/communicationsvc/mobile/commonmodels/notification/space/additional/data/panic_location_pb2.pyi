from google.protobuf import timestamp_pb2 as _timestamp_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceLocationInfo(_message.Message):
    __slots__ = ("latitude", "longitude", "acc", "speed", "time")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ACC_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    latitude: str
    longitude: str
    acc: float
    speed: float
    time: _timestamp_pb2.Timestamp
    def __init__(self, latitude: _Optional[str] = ..., longitude: _Optional[str] = ..., acc: _Optional[float] = ..., speed: _Optional[float] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
