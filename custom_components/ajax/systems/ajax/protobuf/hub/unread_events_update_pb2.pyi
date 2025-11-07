from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UnreadEventsUpdate(_message.Message):
    __slots__ = ("hub_id", "event_count")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    event_count: int
    def __init__(self, hub_id: _Optional[str] = ..., event_count: _Optional[int] = ...) -> None: ...
