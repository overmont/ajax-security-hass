from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import object_type_pb2 as _object_type_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UPDATE_TYPE_UNSPECIFIED: _ClassVar[UpdateType]
    UPDATE_TYPE_ADD: _ClassVar[UpdateType]
    UPDATE_TYPE_UPDATE: _ClassVar[UpdateType]
    UPDATE_TYPE_REMOVE: _ClassVar[UpdateType]
UPDATE_TYPE_UNSPECIFIED: UpdateType
UPDATE_TYPE_ADD: UpdateType
UPDATE_TYPE_UPDATE: UpdateType
UPDATE_TYPE_REMOVE: UpdateType

class Error(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Success(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HubBusyError(_message.Message):
    __slots__ = ("error_cause",)
    ERROR_CAUSE_FIELD_NUMBER: _ClassVar[int]
    error_cause: ErrorCause
    def __init__(self, error_cause: _Optional[_Union[ErrorCause, _Mapping]] = ...) -> None: ...

class HubWrongStateError(_message.Message):
    __slots__ = ("error_cause",)
    ERROR_CAUSE_FIELD_NUMBER: _ClassVar[int]
    error_cause: ErrorCause
    def __init__(self, error_cause: _Optional[_Union[ErrorCause, _Mapping]] = ...) -> None: ...

class ErrorCause(_message.Message):
    __slots__ = ("hub_scan", "hub_pwr_test", "dev_busy", "dfu_in_progress", "radiotest", "dev_zone_test", "card_process", "armed", "exit_timer", "route", "dev_offline", "ext_power", "dev_always_active", "not_supported", "buses_problem", "iwh_objects_limit_error", "iwh_test_in_progress", "ring_problem", "ring_unregistered", "ring_disconnected", "active_call", "fp_bukhoor_forbidden_time", "fp_fire_alarm", "dev_bypassed", "wrong_power_supply_settings", "in_lines_short_circuit", "out_lines_short_circuit", "wifi_func_not_work", "dev_power_overload", "battery_low", "extra_comm_chan_required", "jamming_detected", "walk_test_in_progress", "source")
    class Source(_message.Message):
        __slots__ = ("device_hex_id", "object_type")
        DEVICE_HEX_ID_FIELD_NUMBER: _ClassVar[int]
        OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
        device_hex_id: str
        object_type: _object_type_pb2.ObjectType
        def __init__(self, device_hex_id: _Optional[str] = ..., object_type: _Optional[_Union[_object_type_pb2.ObjectType, _Mapping]] = ...) -> None: ...
    HUB_SCAN_FIELD_NUMBER: _ClassVar[int]
    HUB_PWR_TEST_FIELD_NUMBER: _ClassVar[int]
    DEV_BUSY_FIELD_NUMBER: _ClassVar[int]
    DFU_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    RADIOTEST_FIELD_NUMBER: _ClassVar[int]
    DEV_ZONE_TEST_FIELD_NUMBER: _ClassVar[int]
    CARD_PROCESS_FIELD_NUMBER: _ClassVar[int]
    ARMED_FIELD_NUMBER: _ClassVar[int]
    EXIT_TIMER_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    DEV_OFFLINE_FIELD_NUMBER: _ClassVar[int]
    EXT_POWER_FIELD_NUMBER: _ClassVar[int]
    DEV_ALWAYS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    NOT_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    BUSES_PROBLEM_FIELD_NUMBER: _ClassVar[int]
    IWH_OBJECTS_LIMIT_ERROR_FIELD_NUMBER: _ClassVar[int]
    IWH_TEST_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    RING_PROBLEM_FIELD_NUMBER: _ClassVar[int]
    RING_UNREGISTERED_FIELD_NUMBER: _ClassVar[int]
    RING_DISCONNECTED_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CALL_FIELD_NUMBER: _ClassVar[int]
    FP_BUKHOOR_FORBIDDEN_TIME_FIELD_NUMBER: _ClassVar[int]
    FP_FIRE_ALARM_FIELD_NUMBER: _ClassVar[int]
    DEV_BYPASSED_FIELD_NUMBER: _ClassVar[int]
    WRONG_POWER_SUPPLY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    IN_LINES_SHORT_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    OUT_LINES_SHORT_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    WIFI_FUNC_NOT_WORK_FIELD_NUMBER: _ClassVar[int]
    DEV_POWER_OVERLOAD_FIELD_NUMBER: _ClassVar[int]
    BATTERY_LOW_FIELD_NUMBER: _ClassVar[int]
    EXTRA_COMM_CHAN_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    JAMMING_DETECTED_FIELD_NUMBER: _ClassVar[int]
    WALK_TEST_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    hub_scan: Error
    hub_pwr_test: Error
    dev_busy: Error
    dfu_in_progress: Error
    radiotest: Error
    dev_zone_test: Error
    card_process: Error
    armed: Error
    exit_timer: Error
    route: Error
    dev_offline: Error
    ext_power: Error
    dev_always_active: Error
    not_supported: Error
    buses_problem: Error
    iwh_objects_limit_error: Error
    iwh_test_in_progress: Error
    ring_problem: Error
    ring_unregistered: Error
    ring_disconnected: Error
    active_call: Error
    fp_bukhoor_forbidden_time: Error
    fp_fire_alarm: Error
    dev_bypassed: Error
    wrong_power_supply_settings: Error
    in_lines_short_circuit: Error
    out_lines_short_circuit: Error
    wifi_func_not_work: Error
    dev_power_overload: Error
    battery_low: Error
    extra_comm_chan_required: Error
    jamming_detected: Error
    walk_test_in_progress: Error
    source: ErrorCause.Source
    def __init__(self, hub_scan: _Optional[_Union[Error, _Mapping]] = ..., hub_pwr_test: _Optional[_Union[Error, _Mapping]] = ..., dev_busy: _Optional[_Union[Error, _Mapping]] = ..., dfu_in_progress: _Optional[_Union[Error, _Mapping]] = ..., radiotest: _Optional[_Union[Error, _Mapping]] = ..., dev_zone_test: _Optional[_Union[Error, _Mapping]] = ..., card_process: _Optional[_Union[Error, _Mapping]] = ..., armed: _Optional[_Union[Error, _Mapping]] = ..., exit_timer: _Optional[_Union[Error, _Mapping]] = ..., route: _Optional[_Union[Error, _Mapping]] = ..., dev_offline: _Optional[_Union[Error, _Mapping]] = ..., ext_power: _Optional[_Union[Error, _Mapping]] = ..., dev_always_active: _Optional[_Union[Error, _Mapping]] = ..., not_supported: _Optional[_Union[Error, _Mapping]] = ..., buses_problem: _Optional[_Union[Error, _Mapping]] = ..., iwh_objects_limit_error: _Optional[_Union[Error, _Mapping]] = ..., iwh_test_in_progress: _Optional[_Union[Error, _Mapping]] = ..., ring_problem: _Optional[_Union[Error, _Mapping]] = ..., ring_unregistered: _Optional[_Union[Error, _Mapping]] = ..., ring_disconnected: _Optional[_Union[Error, _Mapping]] = ..., active_call: _Optional[_Union[Error, _Mapping]] = ..., fp_bukhoor_forbidden_time: _Optional[_Union[Error, _Mapping]] = ..., fp_fire_alarm: _Optional[_Union[Error, _Mapping]] = ..., dev_bypassed: _Optional[_Union[Error, _Mapping]] = ..., wrong_power_supply_settings: _Optional[_Union[Error, _Mapping]] = ..., in_lines_short_circuit: _Optional[_Union[Error, _Mapping]] = ..., out_lines_short_circuit: _Optional[_Union[Error, _Mapping]] = ..., wifi_func_not_work: _Optional[_Union[Error, _Mapping]] = ..., dev_power_overload: _Optional[_Union[Error, _Mapping]] = ..., battery_low: _Optional[_Union[Error, _Mapping]] = ..., extra_comm_chan_required: _Optional[_Union[Error, _Mapping]] = ..., jamming_detected: _Optional[_Union[Error, _Mapping]] = ..., walk_test_in_progress: _Optional[_Union[Error, _Mapping]] = ..., source: _Optional[_Union[ErrorCause.Source, _Mapping]] = ...) -> None: ...
