from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetDayAlarmZoneDevicesRequest(_message.Message):
    __slots__ = ("hub_id", "day_alarm_zone_id")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DAY_ALARM_ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    day_alarm_zone_id: str
    def __init__(self, hub_id: _Optional[str] = ..., day_alarm_zone_id: _Optional[str] = ...) -> None: ...
