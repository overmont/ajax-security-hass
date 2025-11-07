from google.type import datetime_pb2 as _datetime_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LifeQualityDataDiscreteness(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LIFE_QUALITY_DATA_DISCRETENESS_UNSPECIFIED: _ClassVar[LifeQualityDataDiscreteness]
    LIFE_QUALITY_DATA_DISCRETENESS_MINUTE: _ClassVar[LifeQualityDataDiscreteness]
    LIFE_QUALITY_DATA_DISCRETENESS_HOUR: _ClassVar[LifeQualityDataDiscreteness]
    LIFE_QUALITY_DATA_DISCRETENESS_DAY: _ClassVar[LifeQualityDataDiscreteness]
    LIFE_QUALITY_DATA_DISCRETENESS_MONTH: _ClassVar[LifeQualityDataDiscreteness]
LIFE_QUALITY_DATA_DISCRETENESS_UNSPECIFIED: LifeQualityDataDiscreteness
LIFE_QUALITY_DATA_DISCRETENESS_MINUTE: LifeQualityDataDiscreteness
LIFE_QUALITY_DATA_DISCRETENESS_HOUR: LifeQualityDataDiscreteness
LIFE_QUALITY_DATA_DISCRETENESS_DAY: LifeQualityDataDiscreteness
LIFE_QUALITY_DATA_DISCRETENESS_MONTH: LifeQualityDataDiscreteness

class LifeQualityDataItem(_message.Message):
    __slots__ = ("value_y", "value_y_range")
    VALUE_Y_FIELD_NUMBER: _ClassVar[int]
    VALUE_Y_RANGE_FIELD_NUMBER: _ClassVar[int]
    value_y: float
    value_y_range: LifeQualityDataRange
    def __init__(self, value_y: _Optional[float] = ..., value_y_range: _Optional[_Union[LifeQualityDataRange, _Mapping]] = ...) -> None: ...

class LifeQualityDataRange(_message.Message):
    __slots__ = ("min_value_y", "max_value_y")
    MIN_VALUE_Y_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_Y_FIELD_NUMBER: _ClassVar[int]
    min_value_y: float
    max_value_y: float
    def __init__(self, min_value_y: _Optional[float] = ..., max_value_y: _Optional[float] = ...) -> None: ...

class LifeQualityDataResponse(_message.Message):
    __slots__ = ("values_temperature", "values_humidity", "values_airquality")
    class ValuesTemperatureEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: LifeQualityDataItem
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[LifeQualityDataItem, _Mapping]] = ...) -> None: ...
    class ValuesHumidityEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: LifeQualityDataItem
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[LifeQualityDataItem, _Mapping]] = ...) -> None: ...
    class ValuesAirqualityEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: LifeQualityDataItem
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[LifeQualityDataItem, _Mapping]] = ...) -> None: ...
    VALUES_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    VALUES_HUMIDITY_FIELD_NUMBER: _ClassVar[int]
    VALUES_AIRQUALITY_FIELD_NUMBER: _ClassVar[int]
    values_temperature: _containers.MessageMap[int, LifeQualityDataItem]
    values_humidity: _containers.MessageMap[int, LifeQualityDataItem]
    values_airquality: _containers.MessageMap[int, LifeQualityDataItem]
    def __init__(self, values_temperature: _Optional[_Mapping[int, LifeQualityDataItem]] = ..., values_humidity: _Optional[_Mapping[int, LifeQualityDataItem]] = ..., values_airquality: _Optional[_Mapping[int, LifeQualityDataItem]] = ...) -> None: ...

class LifeQualityDataRequest(_message.Message):
    __slots__ = ("hub_hex_id", "device_hex_id", "discreteness", "time_zone", "start_timestamp", "end_timestamp")
    HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    DISCRETENESS_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    hub_hex_id: str
    device_hex_id: str
    discreteness: LifeQualityDataDiscreteness
    time_zone: _datetime_pb2.TimeZone
    start_timestamp: int
    end_timestamp: int
    def __init__(self, hub_hex_id: _Optional[str] = ..., device_hex_id: _Optional[str] = ..., discreteness: _Optional[_Union[LifeQualityDataDiscreteness, str]] = ..., time_zone: _Optional[_Union[_datetime_pb2.TimeZone, _Mapping]] = ..., start_timestamp: _Optional[int] = ..., end_timestamp: _Optional[int] = ...) -> None: ...

class StreamLifeQualityDataRequest(_message.Message):
    __slots__ = ("hub_hex_id", "device_hex_id", "discreteness", "time_zone", "start_timestamp")
    HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    DISCRETENESS_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    hub_hex_id: str
    device_hex_id: str
    discreteness: LifeQualityDataDiscreteness
    time_zone: _datetime_pb2.TimeZone
    start_timestamp: int
    def __init__(self, hub_hex_id: _Optional[str] = ..., device_hex_id: _Optional[str] = ..., discreteness: _Optional[_Union[LifeQualityDataDiscreteness, str]] = ..., time_zone: _Optional[_Union[_datetime_pb2.TimeZone, _Mapping]] = ..., start_timestamp: _Optional[int] = ...) -> None: ...
