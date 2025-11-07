from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import object_type_pb2 as _object_type_pb2
from google.type import dayofweek_pb2 as _dayofweek_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScheduledAccess(_message.Message):
    __slots__ = ("id", "name", "targets", "schedules", "enabled", "notification_enabled")
    class Target(_message.Message):
        __slots__ = ("device_id", "device_type")
        DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
        DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        device_id: str
        device_type: _object_type_pb2.ObjectType
        def __init__(self, device_id: _Optional[str] = ..., device_type: _Optional[_Union[_object_type_pb2.ObjectType, _Mapping]] = ...) -> None: ...
    class Schedule(_message.Message):
        __slots__ = ("week_days", "start_hour", "start_minute", "end_hour", "end_minute", "is_active")
        WEEK_DAYS_FIELD_NUMBER: _ClassVar[int]
        START_HOUR_FIELD_NUMBER: _ClassVar[int]
        START_MINUTE_FIELD_NUMBER: _ClassVar[int]
        END_HOUR_FIELD_NUMBER: _ClassVar[int]
        END_MINUTE_FIELD_NUMBER: _ClassVar[int]
        IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
        week_days: _containers.RepeatedScalarFieldContainer[_dayofweek_pb2.DayOfWeek]
        start_hour: int
        start_minute: int
        end_hour: int
        end_minute: int
        is_active: bool
        def __init__(self, week_days: _Optional[_Iterable[_Union[_dayofweek_pb2.DayOfWeek, str]]] = ..., start_hour: _Optional[int] = ..., start_minute: _Optional[int] = ..., end_hour: _Optional[int] = ..., end_minute: _Optional[int] = ..., is_active: bool = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    targets: _containers.RepeatedCompositeFieldContainer[ScheduledAccess.Target]
    schedules: _containers.RepeatedCompositeFieldContainer[ScheduledAccess.Schedule]
    enabled: bool
    notification_enabled: bool
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., targets: _Optional[_Iterable[_Union[ScheduledAccess.Target, _Mapping]]] = ..., schedules: _Optional[_Iterable[_Union[ScheduledAccess.Schedule, _Mapping]]] = ..., enabled: bool = ..., notification_enabled: bool = ...) -> None: ...
