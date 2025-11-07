from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PingPongRequest(_message.Message):
    __slots__ = ("timestamp",)
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PingPongResponse(_message.Message):
    __slots__ = ("ping_timestamp", "server_timestamp")
    PING_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SERVER_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ping_timestamp: _timestamp_pb2.Timestamp
    server_timestamp: _timestamp_pb2.Timestamp
    def __init__(self, ping_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., server_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
