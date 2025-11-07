from systems.ajax.protobuf.hub import object_type_pb2 as _object_type_pb2
from systems.ajax.protobuf.hub import name_pb2 as _name_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Scenario(_message.Message):
    __slots__ = ("id", "name", "enabled", "source_type", "source_condition", "target_action", "time_before_action", "target_condition", "alarm_sources", "targets", "schedules")
    class SourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SOURCE_TYPE: _ClassVar[Scenario.SourceType]
        INSTRUCTION_FIRE_LEAK: _ClassVar[Scenario.SourceType]
        SCHEDULE: _ClassVar[Scenario.SourceType]
        BUTTON: _ClassVar[Scenario.SourceType]
    NO_SOURCE_TYPE: Scenario.SourceType
    INSTRUCTION_FIRE_LEAK: Scenario.SourceType
    SCHEDULE: Scenario.SourceType
    BUTTON: Scenario.SourceType
    class SourceCondition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SOURCE_CONDITION: _ClassVar[Scenario.SourceCondition]
        OR: _ClassVar[Scenario.SourceCondition]
        AND: _ClassVar[Scenario.SourceCondition]
    NO_SOURCE_CONDITION: Scenario.SourceCondition
    OR: Scenario.SourceCondition
    AND: Scenario.SourceCondition
    class TargetAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_TARGET_ACTION: _ClassVar[Scenario.TargetAction]
        OFF: _ClassVar[Scenario.TargetAction]
        ON: _ClassVar[Scenario.TargetAction]
        CHANGE_STAGE: _ClassVar[Scenario.TargetAction]
        DISARM: _ClassVar[Scenario.TargetAction]
        ARM: _ClassVar[Scenario.TargetAction]
        DISARM_NIGHT_MODE: _ClassVar[Scenario.TargetAction]
        ARM_NIGHT_MODE: _ClassVar[Scenario.TargetAction]
        MAKE_PHOTO: _ClassVar[Scenario.TargetAction]
    NO_TARGET_ACTION: Scenario.TargetAction
    OFF: Scenario.TargetAction
    ON: Scenario.TargetAction
    CHANGE_STAGE: Scenario.TargetAction
    DISARM: Scenario.TargetAction
    ARM: Scenario.TargetAction
    DISARM_NIGHT_MODE: Scenario.TargetAction
    ARM_NIGHT_MODE: Scenario.TargetAction
    MAKE_PHOTO: Scenario.TargetAction
    class TargetCondition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_TARGET_CONDITION_INFO: _ClassVar[Scenario.TargetCondition]
        ON_DEVICE_ARM: _ClassVar[Scenario.TargetCondition]
        ON_DEVICE_DISARM: _ClassVar[Scenario.TargetCondition]
    NO_TARGET_CONDITION_INFO: Scenario.TargetCondition
    ON_DEVICE_ARM: Scenario.TargetCondition
    ON_DEVICE_DISARM: Scenario.TargetCondition
    class AlarmSource(_message.Message):
        __slots__ = ("source_event_number", "source_object_type", "source_id")
        SOURCE_EVENT_NUMBER_FIELD_NUMBER: _ClassVar[int]
        SOURCE_OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
        SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
        source_event_number: int
        source_object_type: _object_type_pb2.ObjectType
        source_id: str
        def __init__(self, source_event_number: _Optional[int] = ..., source_object_type: _Optional[_Union[_object_type_pb2.ObjectType, str]] = ..., source_id: _Optional[str] = ...) -> None: ...
    class Target(_message.Message):
        __slots__ = ("target_object_type", "target_id")
        TARGET_OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
        TARGET_ID_FIELD_NUMBER: _ClassVar[int]
        target_object_type: _object_type_pb2.ObjectType
        target_id: str
        def __init__(self, target_object_type: _Optional[_Union[_object_type_pb2.ObjectType, str]] = ..., target_id: _Optional[str] = ...) -> None: ...
    class Schedule(_message.Message):
        __slots__ = ("id", "enabled", "week_days", "hours", "minutes", "last_run_utc", "scenario_bits")
        class WeekDays(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NO_WEEK_DAYS_INFO: _ClassVar[Scenario.Schedule.WeekDays]
            SUNDAY: _ClassVar[Scenario.Schedule.WeekDays]
            MONDAY: _ClassVar[Scenario.Schedule.WeekDays]
            TUESDAY: _ClassVar[Scenario.Schedule.WeekDays]
            WEDNESDAY: _ClassVar[Scenario.Schedule.WeekDays]
            THURSDAY: _ClassVar[Scenario.Schedule.WeekDays]
            FRIDAY: _ClassVar[Scenario.Schedule.WeekDays]
            SATURDAY: _ClassVar[Scenario.Schedule.WeekDays]
        NO_WEEK_DAYS_INFO: Scenario.Schedule.WeekDays
        SUNDAY: Scenario.Schedule.WeekDays
        MONDAY: Scenario.Schedule.WeekDays
        TUESDAY: Scenario.Schedule.WeekDays
        WEDNESDAY: Scenario.Schedule.WeekDays
        THURSDAY: Scenario.Schedule.WeekDays
        FRIDAY: Scenario.Schedule.WeekDays
        SATURDAY: Scenario.Schedule.WeekDays
        ID_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        WEEK_DAYS_FIELD_NUMBER: _ClassVar[int]
        HOURS_FIELD_NUMBER: _ClassVar[int]
        MINUTES_FIELD_NUMBER: _ClassVar[int]
        LAST_RUN_UTC_FIELD_NUMBER: _ClassVar[int]
        SCENARIO_BITS_FIELD_NUMBER: _ClassVar[int]
        id: str
        enabled: bool
        week_days: _containers.RepeatedScalarFieldContainer[Scenario.Schedule.WeekDays]
        hours: int
        minutes: int
        last_run_utc: int
        scenario_bits: int
        def __init__(self, id: _Optional[str] = ..., enabled: bool = ..., week_days: _Optional[_Iterable[_Union[Scenario.Schedule.WeekDays, str]]] = ..., hours: _Optional[int] = ..., minutes: _Optional[int] = ..., last_run_utc: _Optional[int] = ..., scenario_bits: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CONDITION_FIELD_NUMBER: _ClassVar[int]
    TARGET_ACTION_FIELD_NUMBER: _ClassVar[int]
    TIME_BEFORE_ACTION_FIELD_NUMBER: _ClassVar[int]
    TARGET_CONDITION_FIELD_NUMBER: _ClassVar[int]
    ALARM_SOURCES_FIELD_NUMBER: _ClassVar[int]
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _name_pb2.Name
    enabled: bool
    source_type: Scenario.SourceType
    source_condition: Scenario.SourceCondition
    target_action: Scenario.TargetAction
    time_before_action: int
    target_condition: _containers.RepeatedScalarFieldContainer[Scenario.TargetCondition]
    alarm_sources: _containers.RepeatedCompositeFieldContainer[Scenario.AlarmSource]
    targets: _containers.RepeatedCompositeFieldContainer[Scenario.Target]
    schedules: _containers.RepeatedCompositeFieldContainer[Scenario.Schedule]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[_Union[_name_pb2.Name, _Mapping]] = ..., enabled: bool = ..., source_type: _Optional[_Union[Scenario.SourceType, str]] = ..., source_condition: _Optional[_Union[Scenario.SourceCondition, str]] = ..., target_action: _Optional[_Union[Scenario.TargetAction, str]] = ..., time_before_action: _Optional[int] = ..., target_condition: _Optional[_Iterable[_Union[Scenario.TargetCondition, str]]] = ..., alarm_sources: _Optional[_Iterable[_Union[Scenario.AlarmSource, _Mapping]]] = ..., targets: _Optional[_Iterable[_Union[Scenario.Target, _Mapping]]] = ..., schedules: _Optional[_Iterable[_Union[Scenario.Schedule, _Mapping]]] = ...) -> None: ...
