from v1.hub.log import hub_log_event_pb2 as _hub_log_event_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetLogEventRequest(_message.Message):
    __slots__ = ("hub_id", "time")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    time: int
    def __init__(self, hub_id: _Optional[str] = ..., time: _Optional[int] = ...) -> None: ...

class GetLogEventResponse(_message.Message):
    __slots__ = ("event",)
    EVENT_FIELD_NUMBER: _ClassVar[int]
    event: _hub_log_event_pb2.HubLogEvent
    def __init__(self, event: _Optional[_Union[_hub_log_event_pb2.HubLogEvent, _Mapping]] = ...) -> None: ...
