from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StreamUnconfirmedAlarmEventsRequest(_message.Message):
    __slots__ = ("space_id", "parent_alarm_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ALARM_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    parent_alarm_id: str
    def __init__(self, space_id: _Optional[str] = ..., parent_alarm_id: _Optional[str] = ...) -> None: ...
