from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExtraServiceState(_message.Message):
    __slots__ = ("active", "suspended", "deactivated")
    class Active(_message.Message):
        __slots__ = ("renews_on", "expires_on")
        RENEWS_ON_FIELD_NUMBER: _ClassVar[int]
        EXPIRES_ON_FIELD_NUMBER: _ClassVar[int]
        renews_on: _timestamp_pb2.Timestamp
        expires_on: _timestamp_pb2.Timestamp
        def __init__(self, renews_on: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expires_on: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class Suspended(_message.Message):
        __slots__ = ("paused_on",)
        PAUSED_ON_FIELD_NUMBER: _ClassVar[int]
        paused_on: _timestamp_pb2.Timestamp
        def __init__(self, paused_on: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class Deactivated(_message.Message):
        __slots__ = ("expired_on",)
        EXPIRED_ON_FIELD_NUMBER: _ClassVar[int]
        expired_on: _timestamp_pb2.Timestamp
        def __init__(self, expired_on: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    SUSPENDED_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATED_FIELD_NUMBER: _ClassVar[int]
    active: ExtraServiceState.Active
    suspended: ExtraServiceState.Suspended
    deactivated: ExtraServiceState.Deactivated
    def __init__(self, active: _Optional[_Union[ExtraServiceState.Active, _Mapping]] = ..., suspended: _Optional[_Union[ExtraServiceState.Suspended, _Mapping]] = ..., deactivated: _Optional[_Union[ExtraServiceState.Deactivated, _Mapping]] = ...) -> None: ...
