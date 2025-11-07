from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.virtualobject import day_alarm_zone_pb2 as _day_alarm_zone_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamDayAlarmZonesResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("snapshot", "created", "updated", "deleted")
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        CREATED_FIELD_NUMBER: _ClassVar[int]
        UPDATED_FIELD_NUMBER: _ClassVar[int]
        DELETED_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamDayAlarmZonesResponse.Snapshot
        created: StreamDayAlarmZonesResponse.Created
        updated: StreamDayAlarmZonesResponse.Updated
        deleted: StreamDayAlarmZonesResponse.Deleted
        def __init__(self, snapshot: _Optional[_Union[StreamDayAlarmZonesResponse.Snapshot, _Mapping]] = ..., created: _Optional[_Union[StreamDayAlarmZonesResponse.Created, _Mapping]] = ..., updated: _Optional[_Union[StreamDayAlarmZonesResponse.Updated, _Mapping]] = ..., deleted: _Optional[_Union[StreamDayAlarmZonesResponse.Deleted, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    class Snapshot(_message.Message):
        __slots__ = ("is_add_available", "is_cms_on", "day_alarm_zones")
        IS_ADD_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
        IS_CMS_ON_FIELD_NUMBER: _ClassVar[int]
        DAY_ALARM_ZONES_FIELD_NUMBER: _ClassVar[int]
        is_add_available: bool
        is_cms_on: bool
        day_alarm_zones: _containers.RepeatedCompositeFieldContainer[_day_alarm_zone_pb2.DayAlarmZone]
        def __init__(self, is_add_available: bool = ..., is_cms_on: bool = ..., day_alarm_zones: _Optional[_Iterable[_Union[_day_alarm_zone_pb2.DayAlarmZone, _Mapping]]] = ...) -> None: ...
    class Created(_message.Message):
        __slots__ = ("is_add_available", "day_alarm_zones")
        IS_ADD_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
        DAY_ALARM_ZONES_FIELD_NUMBER: _ClassVar[int]
        is_add_available: bool
        day_alarm_zones: _containers.RepeatedCompositeFieldContainer[_day_alarm_zone_pb2.DayAlarmZone]
        def __init__(self, is_add_available: bool = ..., day_alarm_zones: _Optional[_Iterable[_Union[_day_alarm_zone_pb2.DayAlarmZone, _Mapping]]] = ...) -> None: ...
    class Updated(_message.Message):
        __slots__ = ("day_alarm_zones",)
        DAY_ALARM_ZONES_FIELD_NUMBER: _ClassVar[int]
        day_alarm_zones: _containers.RepeatedCompositeFieldContainer[_day_alarm_zone_pb2.DayAlarmZone]
        def __init__(self, day_alarm_zones: _Optional[_Iterable[_Union[_day_alarm_zone_pb2.DayAlarmZone, _Mapping]]] = ...) -> None: ...
    class Deleted(_message.Message):
        __slots__ = ("is_add_available", "day_alarm_zones")
        IS_ADD_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
        DAY_ALARM_ZONES_FIELD_NUMBER: _ClassVar[int]
        is_add_available: bool
        day_alarm_zones: _containers.RepeatedCompositeFieldContainer[_day_alarm_zone_pb2.DayAlarmZone]
        def __init__(self, is_add_available: bool = ..., day_alarm_zones: _Optional[_Iterable[_Union[_day_alarm_zone_pb2.DayAlarmZone, _Mapping]]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamDayAlarmZonesResponse.Success
    failure: StreamDayAlarmZonesResponse.Failure
    def __init__(self, success: _Optional[_Union[StreamDayAlarmZonesResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[StreamDayAlarmZonesResponse.Failure, _Mapping]] = ...) -> None: ...
