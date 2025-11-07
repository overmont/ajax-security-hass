from systems.ajax.api.mobile.v2.common.video.scenario.alarm import alarm_pb2 as _alarm_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AlarmSource(_message.Message):
    __slots__ = ("source_id", "alarms", "hts_alarm")
    class HtsAlarm(_message.Message):
        __slots__ = ("hts_device_type", "hts_event_codes")
        HTS_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        HTS_EVENT_CODES_FIELD_NUMBER: _ClassVar[int]
        hts_device_type: str
        hts_event_codes: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, hts_device_type: _Optional[str] = ..., hts_event_codes: _Optional[_Iterable[str]] = ...) -> None: ...
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    ALARMS_FIELD_NUMBER: _ClassVar[int]
    HTS_ALARM_FIELD_NUMBER: _ClassVar[int]
    source_id: str
    alarms: _containers.RepeatedCompositeFieldContainer[_alarm_pb2.Alarm]
    hts_alarm: AlarmSource.HtsAlarm
    def __init__(self, source_id: _Optional[str] = ..., alarms: _Optional[_Iterable[_Union[_alarm_pb2.Alarm, _Mapping]]] = ..., hts_alarm: _Optional[_Union[AlarmSource.HtsAlarm, _Mapping]] = ...) -> None: ...
