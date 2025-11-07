from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConfirmedAlarmInfo(_message.Message):
    __slots__ = ("parent_alarm_id",)
    PARENT_ALARM_ID_FIELD_NUMBER: _ClassVar[int]
    parent_alarm_id: str
    def __init__(self, parent_alarm_id: _Optional[str] = ...) -> None: ...
