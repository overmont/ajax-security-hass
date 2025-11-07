from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import space_pb2 as _space_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OfflineEventCount(_message.Message):
    __slots__ = ("isAlarm", "event_count", "grouping_key", "hub_hex_id", "space")
    ISALARM_FIELD_NUMBER: _ClassVar[int]
    EVENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    GROUPING_KEY_FIELD_NUMBER: _ClassVar[int]
    HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_FIELD_NUMBER: _ClassVar[int]
    isAlarm: bool
    event_count: int
    grouping_key: int
    hub_hex_id: str
    space: _space_pb2.NotificationSpace
    def __init__(self, isAlarm: bool = ..., event_count: _Optional[int] = ..., grouping_key: _Optional[int] = ..., hub_hex_id: _Optional[str] = ..., space: _Optional[_Union[_space_pb2.NotificationSpace, _Mapping]] = ...) -> None: ...
