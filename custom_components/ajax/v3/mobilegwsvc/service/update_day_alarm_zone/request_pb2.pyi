from google.protobuf import duration_pb2 as _duration_pb2
from v3.mobilegwsvc.commonmodels.virtualobject import selected_device_pb2 as _selected_device_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateDayAlarmZoneRequest(_message.Message):
    __slots__ = ("hub_id", "id", "name", "open_door_alarm", "notify_about_deactivation", "intrusion_devices", "security_devices", "siren_devices", "triggers_count", "timer")
    class OpenDoorAlarm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPEN_DOOR_ALARM_UNSPECIFIED: _ClassVar[UpdateDayAlarmZoneRequest.OpenDoorAlarm]
        OPEN_DOOR_ALARM_OFF: _ClassVar[UpdateDayAlarmZoneRequest.OpenDoorAlarm]
        OPEN_DOOR_ALARM_ON: _ClassVar[UpdateDayAlarmZoneRequest.OpenDoorAlarm]
    OPEN_DOOR_ALARM_UNSPECIFIED: UpdateDayAlarmZoneRequest.OpenDoorAlarm
    OPEN_DOOR_ALARM_OFF: UpdateDayAlarmZoneRequest.OpenDoorAlarm
    OPEN_DOOR_ALARM_ON: UpdateDayAlarmZoneRequest.OpenDoorAlarm
    class NotifyAboutDeactivation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOTIFY_ABOUT_DEACTIVATION_UNSPECIFIED: _ClassVar[UpdateDayAlarmZoneRequest.NotifyAboutDeactivation]
        NOTIFY_ABOUT_DEACTIVATION_FALSE: _ClassVar[UpdateDayAlarmZoneRequest.NotifyAboutDeactivation]
        NOTIFY_ABOUT_DEACTIVATION_TRUE: _ClassVar[UpdateDayAlarmZoneRequest.NotifyAboutDeactivation]
    NOTIFY_ABOUT_DEACTIVATION_UNSPECIFIED: UpdateDayAlarmZoneRequest.NotifyAboutDeactivation
    NOTIFY_ABOUT_DEACTIVATION_FALSE: UpdateDayAlarmZoneRequest.NotifyAboutDeactivation
    NOTIFY_ABOUT_DEACTIVATION_TRUE: UpdateDayAlarmZoneRequest.NotifyAboutDeactivation
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
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPEN_DOOR_ALARM_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_ABOUT_DEACTIVATION_FIELD_NUMBER: _ClassVar[int]
    INTRUSION_DEVICES_FIELD_NUMBER: _ClassVar[int]
    SECURITY_DEVICES_FIELD_NUMBER: _ClassVar[int]
    SIREN_DEVICES_FIELD_NUMBER: _ClassVar[int]
    TRIGGERS_COUNT_FIELD_NUMBER: _ClassVar[int]
    TIMER_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    id: str
    name: str
    open_door_alarm: UpdateDayAlarmZoneRequest.OpenDoorAlarm
    notify_about_deactivation: UpdateDayAlarmZoneRequest.NotifyAboutDeactivation
    intrusion_devices: _containers.RepeatedCompositeFieldContainer[_selected_device_pb2.SelectedDevice]
    security_devices: _containers.RepeatedCompositeFieldContainer[_selected_device_pb2.SelectedDevice]
    siren_devices: _containers.RepeatedCompositeFieldContainer[_selected_device_pb2.SelectedDevice]
    triggers_count: UpdateDayAlarmZoneRequest.TriggersCount
    timer: UpdateDayAlarmZoneRequest.Timer
    def __init__(self, hub_id: _Optional[str] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., open_door_alarm: _Optional[_Union[UpdateDayAlarmZoneRequest.OpenDoorAlarm, str]] = ..., notify_about_deactivation: _Optional[_Union[UpdateDayAlarmZoneRequest.NotifyAboutDeactivation, str]] = ..., intrusion_devices: _Optional[_Iterable[_Union[_selected_device_pb2.SelectedDevice, _Mapping]]] = ..., security_devices: _Optional[_Iterable[_Union[_selected_device_pb2.SelectedDevice, _Mapping]]] = ..., siren_devices: _Optional[_Iterable[_Union[_selected_device_pb2.SelectedDevice, _Mapping]]] = ..., triggers_count: _Optional[_Union[UpdateDayAlarmZoneRequest.TriggersCount, _Mapping]] = ..., timer: _Optional[_Union[UpdateDayAlarmZoneRequest.Timer, _Mapping]] = ...) -> None: ...
