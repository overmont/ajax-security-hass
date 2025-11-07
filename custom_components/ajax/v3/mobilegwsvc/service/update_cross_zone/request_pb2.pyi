from systems.ajax.api.mobile.v2.common.space.device import hub_device_pb2 as _hub_device_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateCrossZoneRequest(_message.Message):
    __slots__ = ("hub_hex_id", "id", "name", "confirmation_timeout", "confirmation_alarms_count", "unconfirmed_alarm_type", "count_repeated_alarms", "reset_bypass", "include_entry_delay", "tamper_confirmation", "sirens_react_on_confirmation", "included_devices")
    class UnconfirmedAlarmType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNCONFIRMED_ALARM_TYPE_UNSPECIFIED: _ClassVar[UpdateCrossZoneRequest.UnconfirmedAlarmType]
        UNCONFIRMED_ALARM_TYPE_DO_NOT_NOTIFY: _ClassVar[UpdateCrossZoneRequest.UnconfirmedAlarmType]
        UNCONFIRMED_ALARM_TYPE_POSTPONED_WARNING: _ClassVar[UpdateCrossZoneRequest.UnconfirmedAlarmType]
        UNCONFIRMED_ALARM_TYPE_INSTANT_WARNING: _ClassVar[UpdateCrossZoneRequest.UnconfirmedAlarmType]
        UNCONFIRMED_ALARM_TYPE_ALARM: _ClassVar[UpdateCrossZoneRequest.UnconfirmedAlarmType]
    UNCONFIRMED_ALARM_TYPE_UNSPECIFIED: UpdateCrossZoneRequest.UnconfirmedAlarmType
    UNCONFIRMED_ALARM_TYPE_DO_NOT_NOTIFY: UpdateCrossZoneRequest.UnconfirmedAlarmType
    UNCONFIRMED_ALARM_TYPE_POSTPONED_WARNING: UpdateCrossZoneRequest.UnconfirmedAlarmType
    UNCONFIRMED_ALARM_TYPE_INSTANT_WARNING: UpdateCrossZoneRequest.UnconfirmedAlarmType
    UNCONFIRMED_ALARM_TYPE_ALARM: UpdateCrossZoneRequest.UnconfirmedAlarmType
    class IncludedDevices(_message.Message):
        __slots__ = ("included_devices",)
        INCLUDED_DEVICES_FIELD_NUMBER: _ClassVar[int]
        included_devices: _containers.RepeatedCompositeFieldContainer[_hub_device_pb2.HubDevice]
        def __init__(self, included_devices: _Optional[_Iterable[_Union[_hub_device_pb2.HubDevice, _Mapping]]] = ...) -> None: ...
    HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIRMATION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    CONFIRMATION_ALARMS_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNCONFIRMED_ALARM_TYPE_FIELD_NUMBER: _ClassVar[int]
    COUNT_REPEATED_ALARMS_FIELD_NUMBER: _ClassVar[int]
    RESET_BYPASS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ENTRY_DELAY_FIELD_NUMBER: _ClassVar[int]
    TAMPER_CONFIRMATION_FIELD_NUMBER: _ClassVar[int]
    SIRENS_REACT_ON_CONFIRMATION_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_DEVICES_FIELD_NUMBER: _ClassVar[int]
    hub_hex_id: str
    id: str
    name: str
    confirmation_timeout: int
    confirmation_alarms_count: int
    unconfirmed_alarm_type: UpdateCrossZoneRequest.UnconfirmedAlarmType
    count_repeated_alarms: bool
    reset_bypass: bool
    include_entry_delay: bool
    tamper_confirmation: bool
    sirens_react_on_confirmation: bool
    included_devices: UpdateCrossZoneRequest.IncludedDevices
    def __init__(self, hub_hex_id: _Optional[str] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., confirmation_timeout: _Optional[int] = ..., confirmation_alarms_count: _Optional[int] = ..., unconfirmed_alarm_type: _Optional[_Union[UpdateCrossZoneRequest.UnconfirmedAlarmType, str]] = ..., count_repeated_alarms: bool = ..., reset_bypass: bool = ..., include_entry_delay: bool = ..., tamper_confirmation: bool = ..., sirens_react_on_confirmation: bool = ..., included_devices: _Optional[_Union[UpdateCrossZoneRequest.IncludedDevices, _Mapping]] = ...) -> None: ...
