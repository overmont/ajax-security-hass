from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DayAlarmZone(_message.Message):
    __slots__ = ("id", "name", "open_door_alarm", "notify_about_deactivation", "devices_count", "triggers_count", "timer")
    class OpenDoorAlarm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPEN_DOOR_ALARM_UNSPECIFIED: _ClassVar[DayAlarmZone.OpenDoorAlarm]
        OPEN_DOOR_ALARM_OFF: _ClassVar[DayAlarmZone.OpenDoorAlarm]
        OPEN_DOOR_ALARM_ON: _ClassVar[DayAlarmZone.OpenDoorAlarm]
    OPEN_DOOR_ALARM_UNSPECIFIED: DayAlarmZone.OpenDoorAlarm
    OPEN_DOOR_ALARM_OFF: DayAlarmZone.OpenDoorAlarm
    OPEN_DOOR_ALARM_ON: DayAlarmZone.OpenDoorAlarm
    class NotifyAboutDeactivation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOTIFY_ABOUT_DEACTIVATION_UNSPECIFIED: _ClassVar[DayAlarmZone.NotifyAboutDeactivation]
        NOTIFY_ABOUT_DEACTIVATION_FALSE: _ClassVar[DayAlarmZone.NotifyAboutDeactivation]
        NOTIFY_ABOUT_DEACTIVATION_TRUE: _ClassVar[DayAlarmZone.NotifyAboutDeactivation]
    NOTIFY_ABOUT_DEACTIVATION_UNSPECIFIED: DayAlarmZone.NotifyAboutDeactivation
    NOTIFY_ABOUT_DEACTIVATION_FALSE: DayAlarmZone.NotifyAboutDeactivation
    NOTIFY_ABOUT_DEACTIVATION_TRUE: DayAlarmZone.NotifyAboutDeactivation
    class Timer(_message.Message):
        __slots__ = ("bypass_duration",)
        BYPASS_DURATION_FIELD_NUMBER: _ClassVar[int]
        bypass_duration: _duration_pb2.Duration
        def __init__(self, bypass_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    class TriggersCount(_message.Message):
        __slots__ = ("bypass_trigger_count",)
        BYPASS_TRIGGER_COUNT_FIELD_NUMBER: _ClassVar[int]
        bypass_trigger_count: int
        def __init__(self, bypass_trigger_count: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPEN_DOOR_ALARM_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_ABOUT_DEACTIVATION_FIELD_NUMBER: _ClassVar[int]
    DEVICES_COUNT_FIELD_NUMBER: _ClassVar[int]
    TRIGGERS_COUNT_FIELD_NUMBER: _ClassVar[int]
    TIMER_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    open_door_alarm: DayAlarmZone.OpenDoorAlarm
    notify_about_deactivation: DayAlarmZone.NotifyAboutDeactivation
    devices_count: int
    triggers_count: DayAlarmZone.TriggersCount
    timer: DayAlarmZone.Timer
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., open_door_alarm: _Optional[_Union[DayAlarmZone.OpenDoorAlarm, str]] = ..., notify_about_deactivation: _Optional[_Union[DayAlarmZone.NotifyAboutDeactivation, str]] = ..., devices_count: _Optional[int] = ..., triggers_count: _Optional[_Union[DayAlarmZone.TriggersCount, _Mapping]] = ..., timer: _Optional[_Union[DayAlarmZone.Timer, _Mapping]] = ...) -> None: ...
