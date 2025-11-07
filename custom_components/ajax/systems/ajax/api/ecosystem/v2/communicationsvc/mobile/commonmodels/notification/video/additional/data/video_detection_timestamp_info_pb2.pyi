from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VideoDetectionTimestampInfo(_message.Message):
    __slots__ = ("detection_timestamp",)
    DETECTION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    detection_timestamp: _timestamp_pb2.Timestamp
    def __init__(self, detection_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
