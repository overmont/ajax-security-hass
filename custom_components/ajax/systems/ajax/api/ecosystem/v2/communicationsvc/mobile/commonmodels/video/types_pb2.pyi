from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VideoCodec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VC_UNKNOWN: _ClassVar[VideoCodec]
    H264: _ClassVar[VideoCodec]
    H265: _ClassVar[VideoCodec]
    MJPEG: _ClassVar[VideoCodec]
VC_UNKNOWN: VideoCodec
H264: VideoCodec
H265: VideoCodec
MJPEG: VideoCodec

class TimestampRange(_message.Message):
    __slots__ = ("min_value", "max_value")
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    min_value: _timestamp_pb2.Timestamp
    max_value: _timestamp_pb2.Timestamp
    def __init__(self, min_value: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., max_value: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
