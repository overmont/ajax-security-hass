from systems.ajax.api.mobile.v2.common.space.smartlock import smart_lock_event_settings_pb2 as _smart_lock_event_settings_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SmartLockSpaceSettings(_message.Message):
    __slots__ = ("room_id", "event_settings", "group_id")
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    room_id: str
    event_settings: _smart_lock_event_settings_pb2.SmartLockEventSettings
    group_id: str
    def __init__(self, room_id: _Optional[str] = ..., event_settings: _Optional[_Union[_smart_lock_event_settings_pb2.SmartLockEventSettings, _Mapping]] = ..., group_id: _Optional[str] = ...) -> None: ...
