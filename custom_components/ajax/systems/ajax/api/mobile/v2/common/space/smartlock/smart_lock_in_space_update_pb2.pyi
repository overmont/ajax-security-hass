from systems.ajax.api.mobile.v2.common.space.smartlock import smart_lock_pb2 as _smart_lock_pb2
from systems.ajax.api.mobile.v2.common.space.smartlock import smart_lock_event_settings_pb2 as _smart_lock_event_settings_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SmartLockInSpaceUpdate(_message.Message):
    __slots__ = ("details", "event_settings", "room_id")
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    EVENT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    details: _smart_lock_pb2.SmartLockUpdate
    event_settings: _smart_lock_event_settings_pb2.SmartLockEventSettings
    room_id: str
    def __init__(self, details: _Optional[_Union[_smart_lock_pb2.SmartLockUpdate, _Mapping]] = ..., event_settings: _Optional[_Union[_smart_lock_event_settings_pb2.SmartLockEventSettings, _Mapping]] = ..., room_id: _Optional[str] = ...) -> None: ...
