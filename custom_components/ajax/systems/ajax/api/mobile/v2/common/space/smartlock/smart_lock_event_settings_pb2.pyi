from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SmartLockEventSettings(_message.Message):
    __slots__ = ("lockStateChanged", "scenarioExecuted", "doorbellButtonPressed")
    LOCKSTATECHANGED_FIELD_NUMBER: _ClassVar[int]
    SCENARIOEXECUTED_FIELD_NUMBER: _ClassVar[int]
    DOORBELLBUTTONPRESSED_FIELD_NUMBER: _ClassVar[int]
    lockStateChanged: bool
    scenarioExecuted: bool
    doorbellButtonPressed: bool
    def __init__(self, lockStateChanged: bool = ..., scenarioExecuted: bool = ..., doorbellButtonPressed: bool = ...) -> None: ...
