from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BatteryStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BATTERY_STATUS_UNSPECIFIED: _ClassVar[BatteryStatus]
    BATTERY_STATUS_NOT_OK: _ClassVar[BatteryStatus]
    BATTERY_STATUS_OK: _ClassVar[BatteryStatus]
    BATTERY_STATUS_CHARGING: _ClassVar[BatteryStatus]
BATTERY_STATUS_UNSPECIFIED: BatteryStatus
BATTERY_STATUS_NOT_OK: BatteryStatus
BATTERY_STATUS_OK: BatteryStatus
BATTERY_STATUS_CHARGING: BatteryStatus

class DeviceBattery(_message.Message):
    __slots__ = ("battery_failures", "stop_charging_reasons", "battery_charge_level_percentage", "battery_status", "battery_charge_volt")
    class DeviceBatterySettings(_message.Message):
        __slots__ = ("stop_charging_reasons",)
        STOP_CHARGING_REASONS_FIELD_NUMBER: _ClassVar[int]
        stop_charging_reasons: _containers.RepeatedCompositeFieldContainer[DeviceBattery.StopChargingReason]
        def __init__(self, stop_charging_reasons: _Optional[_Iterable[_Union[DeviceBattery.StopChargingReason, _Mapping]]] = ...) -> None: ...
    class BatteryFailure(_message.Message):
        __slots__ = ("battery_failure_case", "failure_status")
        class BatteryFailureCase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            BATTERY_FAILURE_CASE_UNSPECIFIED: _ClassVar[DeviceBattery.BatteryFailure.BatteryFailureCase]
            BATTERY_FAILURE_CASE_NOT_INSTALLED: _ClassVar[DeviceBattery.BatteryFailure.BatteryFailureCase]
        BATTERY_FAILURE_CASE_UNSPECIFIED: DeviceBattery.BatteryFailure.BatteryFailureCase
        BATTERY_FAILURE_CASE_NOT_INSTALLED: DeviceBattery.BatteryFailure.BatteryFailureCase
        class FailureStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            FAILURE_STATUS_UNSPECIFIED: _ClassVar[DeviceBattery.BatteryFailure.FailureStatus]
            FAILURE_STATUS_DEFAULT: _ClassVar[DeviceBattery.BatteryFailure.FailureStatus]
            FAILURE_STATUS_ATTENTION: _ClassVar[DeviceBattery.BatteryFailure.FailureStatus]
            FAILURE_STATUS_WARNING: _ClassVar[DeviceBattery.BatteryFailure.FailureStatus]
        FAILURE_STATUS_UNSPECIFIED: DeviceBattery.BatteryFailure.FailureStatus
        FAILURE_STATUS_DEFAULT: DeviceBattery.BatteryFailure.FailureStatus
        FAILURE_STATUS_ATTENTION: DeviceBattery.BatteryFailure.FailureStatus
        FAILURE_STATUS_WARNING: DeviceBattery.BatteryFailure.FailureStatus
        BATTERY_FAILURE_CASE_FIELD_NUMBER: _ClassVar[int]
        FAILURE_STATUS_FIELD_NUMBER: _ClassVar[int]
        battery_failure_case: DeviceBattery.BatteryFailure.BatteryFailureCase
        failure_status: DeviceBattery.BatteryFailure.FailureStatus
        def __init__(self, battery_failure_case: _Optional[_Union[DeviceBattery.BatteryFailure.BatteryFailureCase, str]] = ..., failure_status: _Optional[_Union[DeviceBattery.BatteryFailure.FailureStatus, str]] = ...) -> None: ...
    class StopChargingReason(_message.Message):
        __slots__ = ("stop_charging_type", "is_enabled")
        class StopChargingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STOP_CHARGING_TYPE_UNSPECIFIED: _ClassVar[DeviceBattery.StopChargingReason.StopChargingType]
            STOP_CHARGING_TYPE_BATTERY_MALFUNCTION: _ClassVar[DeviceBattery.StopChargingReason.StopChargingType]
        STOP_CHARGING_TYPE_UNSPECIFIED: DeviceBattery.StopChargingReason.StopChargingType
        STOP_CHARGING_TYPE_BATTERY_MALFUNCTION: DeviceBattery.StopChargingReason.StopChargingType
        class IsEnabled(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            IS_ENABLED_UNSPECIFIED: _ClassVar[DeviceBattery.StopChargingReason.IsEnabled]
            IS_ENABLED_DISABLED: _ClassVar[DeviceBattery.StopChargingReason.IsEnabled]
            IS_ENABLED_ENABLED: _ClassVar[DeviceBattery.StopChargingReason.IsEnabled]
        IS_ENABLED_UNSPECIFIED: DeviceBattery.StopChargingReason.IsEnabled
        IS_ENABLED_DISABLED: DeviceBattery.StopChargingReason.IsEnabled
        IS_ENABLED_ENABLED: DeviceBattery.StopChargingReason.IsEnabled
        STOP_CHARGING_TYPE_FIELD_NUMBER: _ClassVar[int]
        IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        stop_charging_type: DeviceBattery.StopChargingReason.StopChargingType
        is_enabled: DeviceBattery.StopChargingReason.IsEnabled
        def __init__(self, stop_charging_type: _Optional[_Union[DeviceBattery.StopChargingReason.StopChargingType, str]] = ..., is_enabled: _Optional[_Union[DeviceBattery.StopChargingReason.IsEnabled, str]] = ...) -> None: ...
    BATTERY_FAILURES_FIELD_NUMBER: _ClassVar[int]
    STOP_CHARGING_REASONS_FIELD_NUMBER: _ClassVar[int]
    BATTERY_CHARGE_LEVEL_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    BATTERY_STATUS_FIELD_NUMBER: _ClassVar[int]
    BATTERY_CHARGE_VOLT_FIELD_NUMBER: _ClassVar[int]
    battery_failures: _containers.RepeatedCompositeFieldContainer[DeviceBattery.BatteryFailure]
    stop_charging_reasons: _containers.RepeatedCompositeFieldContainer[DeviceBattery.StopChargingReason]
    battery_charge_level_percentage: int
    battery_status: BatteryStatus
    battery_charge_volt: int
    def __init__(self, battery_failures: _Optional[_Iterable[_Union[DeviceBattery.BatteryFailure, _Mapping]]] = ..., stop_charging_reasons: _Optional[_Iterable[_Union[DeviceBattery.StopChargingReason, _Mapping]]] = ..., battery_charge_level_percentage: _Optional[int] = ..., battery_status: _Optional[_Union[BatteryStatus, str]] = ..., battery_charge_volt: _Optional[int] = ...) -> None: ...

class DeviceBatteryWithoutCharging(_message.Message):
    __slots__ = ("battery_charge_level_percentage", "battery_status")
    BATTERY_CHARGE_LEVEL_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    BATTERY_STATUS_FIELD_NUMBER: _ClassVar[int]
    battery_charge_level_percentage: int
    battery_status: BatteryStatus
    def __init__(self, battery_charge_level_percentage: _Optional[int] = ..., battery_status: _Optional[_Union[BatteryStatus, str]] = ...) -> None: ...
