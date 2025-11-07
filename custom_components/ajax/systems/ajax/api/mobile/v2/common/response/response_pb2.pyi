from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import troubled_devices_pb2 as _troubled_devices_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Success(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DefaultError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IllegalArgumentsError(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class IllegalStateError(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class InternalError(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class UserIsOwnerOfCompanyError(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class UserIsEmployeeOfCompanyError(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class CompanyOnHubNotFoundError(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class PermissionDeniedError(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class DeadlineExceededError(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class SpaceLockedError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LimitExceededError(_message.Message):
    __slots__ = ("limit",)
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    limit: int
    def __init__(self, limit: _Optional[int] = ...) -> None: ...

class HubDetectedMalfunctionsError(_message.Message):
    __slots__ = ("troubled_devices",)
    TROUBLED_DEVICES_FIELD_NUMBER: _ClassVar[int]
    troubled_devices: _troubled_devices_pb2.TroubledDevices
    def __init__(self, troubled_devices: _Optional[_Union[_troubled_devices_pb2.TroubledDevices, _Mapping]] = ...) -> None: ...

class ActiveSubscriptionExistError(_message.Message):
    __slots__ = ("error_cause",)
    class ErrorCause(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ERROR_CAUSE_UNSPECIFIED: _ClassVar[ActiveSubscriptionExistError.ErrorCause]
    ERROR_CAUSE_UNSPECIFIED: ActiveSubscriptionExistError.ErrorCause
    ERROR_CAUSE_FIELD_NUMBER: _ClassVar[int]
    error_cause: _containers.RepeatedScalarFieldContainer[ActiveSubscriptionExistError.ErrorCause]
    def __init__(self, error_cause: _Optional[_Iterable[_Union[ActiveSubscriptionExistError.ErrorCause, str]]] = ...) -> None: ...

class HubBusyError(_message.Message):
    __slots__ = ("causes",)
    class Cause(_message.Message):
        __slots__ = ("hub_scan", "hub_pwr_test", "dev_busy", "dfu_in_progress", "radiotest", "dev_zone_test", "card_process", "armed", "exit_timer", "route", "dev_offline", "ext_power", "dev_always_active", "not_supported", "buses_problem", "iwh_objects_limit_error", "iwh_test_in_progress", "ring_problem", "ring_unregistered", "ring_disconnected", "active_call", "fp_bukhoor_forbidden_time", "fp_fire_alarm", "dev_bypassed", "wrong_power_supply_settings", "in_lines_short_circuit", "out_lines_short_circuit", "wifi_func_not_work", "dev_power_overload", "battery_low", "extra_comm_chan_required", "jamming_detected", "walk_test_in_progress")
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
        hub_scan: DefaultError
        hub_pwr_test: DefaultError
        dev_busy: DefaultError
        dfu_in_progress: DefaultError
        radiotest: DefaultError
        dev_zone_test: DefaultError
        card_process: DefaultError
        armed: DefaultError
        exit_timer: DefaultError
        route: DefaultError
        dev_offline: DefaultError
        ext_power: DefaultError
        dev_always_active: DefaultError
        not_supported: DefaultError
        buses_problem: DefaultError
        iwh_objects_limit_error: DefaultError
        iwh_test_in_progress: DefaultError
        ring_problem: DefaultError
        ring_unregistered: DefaultError
        ring_disconnected: DefaultError
        active_call: DefaultError
        fp_bukhoor_forbidden_time: DefaultError
        fp_fire_alarm: DefaultError
        dev_bypassed: DefaultError
        wrong_power_supply_settings: DefaultError
        in_lines_short_circuit: DefaultError
        out_lines_short_circuit: DefaultError
        wifi_func_not_work: DefaultError
        dev_power_overload: DefaultError
        battery_low: DefaultError
        extra_comm_chan_required: DefaultError
        jamming_detected: DefaultError
        walk_test_in_progress: DefaultError
        def __init__(self, hub_scan: _Optional[_Union[DefaultError, _Mapping]] = ..., hub_pwr_test: _Optional[_Union[DefaultError, _Mapping]] = ..., dev_busy: _Optional[_Union[DefaultError, _Mapping]] = ..., dfu_in_progress: _Optional[_Union[DefaultError, _Mapping]] = ..., radiotest: _Optional[_Union[DefaultError, _Mapping]] = ..., dev_zone_test: _Optional[_Union[DefaultError, _Mapping]] = ..., card_process: _Optional[_Union[DefaultError, _Mapping]] = ..., armed: _Optional[_Union[DefaultError, _Mapping]] = ..., exit_timer: _Optional[_Union[DefaultError, _Mapping]] = ..., route: _Optional[_Union[DefaultError, _Mapping]] = ..., dev_offline: _Optional[_Union[DefaultError, _Mapping]] = ..., ext_power: _Optional[_Union[DefaultError, _Mapping]] = ..., dev_always_active: _Optional[_Union[DefaultError, _Mapping]] = ..., not_supported: _Optional[_Union[DefaultError, _Mapping]] = ..., buses_problem: _Optional[_Union[DefaultError, _Mapping]] = ..., iwh_objects_limit_error: _Optional[_Union[DefaultError, _Mapping]] = ..., iwh_test_in_progress: _Optional[_Union[DefaultError, _Mapping]] = ..., ring_problem: _Optional[_Union[DefaultError, _Mapping]] = ..., ring_unregistered: _Optional[_Union[DefaultError, _Mapping]] = ..., ring_disconnected: _Optional[_Union[DefaultError, _Mapping]] = ..., active_call: _Optional[_Union[DefaultError, _Mapping]] = ..., fp_bukhoor_forbidden_time: _Optional[_Union[DefaultError, _Mapping]] = ..., fp_fire_alarm: _Optional[_Union[DefaultError, _Mapping]] = ..., dev_bypassed: _Optional[_Union[DefaultError, _Mapping]] = ..., wrong_power_supply_settings: _Optional[_Union[DefaultError, _Mapping]] = ..., in_lines_short_circuit: _Optional[_Union[DefaultError, _Mapping]] = ..., out_lines_short_circuit: _Optional[_Union[DefaultError, _Mapping]] = ..., wifi_func_not_work: _Optional[_Union[DefaultError, _Mapping]] = ..., dev_power_overload: _Optional[_Union[DefaultError, _Mapping]] = ..., battery_low: _Optional[_Union[DefaultError, _Mapping]] = ..., extra_comm_chan_required: _Optional[_Union[DefaultError, _Mapping]] = ..., jamming_detected: _Optional[_Union[DefaultError, _Mapping]] = ..., walk_test_in_progress: _Optional[_Union[DefaultError, _Mapping]] = ...) -> None: ...
    CAUSES_FIELD_NUMBER: _ClassVar[int]
    causes: _containers.RepeatedCompositeFieldContainer[HubBusyError.Cause]
    def __init__(self, causes: _Optional[_Iterable[_Union[HubBusyError.Cause, _Mapping]]] = ...) -> None: ...

class AddDeviceError(_message.Message):
    __slots__ = ("failed_add_hub",)
    class AddHubDeviceError(_message.Message):
        __slots__ = ("hub_in_use", "hub_not_found", "hub_offline", "hub_not_empty", "hub_error", "hub_wrong_state", "hub_busy", "hub_firmware_version_not_support_migration", "hub_claim_error", "hub_qr_code_invalid", "member_not_support_add_fibra_and_hybrid_hub", "member_not_authorized_add_hub", "member_not_authorized_add_fibra_and_hybrid_hub", "hub_in_use_in_space_with_no_admin", "hub_locked_to_another_company")
        HUB_IN_USE_FIELD_NUMBER: _ClassVar[int]
        HUB_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        HUB_NOT_EMPTY_FIELD_NUMBER: _ClassVar[int]
        HUB_ERROR_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        HUB_BUSY_FIELD_NUMBER: _ClassVar[int]
        HUB_FIRMWARE_VERSION_NOT_SUPPORT_MIGRATION_FIELD_NUMBER: _ClassVar[int]
        HUB_CLAIM_ERROR_FIELD_NUMBER: _ClassVar[int]
        HUB_QR_CODE_INVALID_FIELD_NUMBER: _ClassVar[int]
        MEMBER_NOT_SUPPORT_ADD_FIBRA_AND_HYBRID_HUB_FIELD_NUMBER: _ClassVar[int]
        MEMBER_NOT_AUTHORIZED_ADD_HUB_FIELD_NUMBER: _ClassVar[int]
        MEMBER_NOT_AUTHORIZED_ADD_FIBRA_AND_HYBRID_HUB_FIELD_NUMBER: _ClassVar[int]
        HUB_IN_USE_IN_SPACE_WITH_NO_ADMIN_FIELD_NUMBER: _ClassVar[int]
        HUB_LOCKED_TO_ANOTHER_COMPANY_FIELD_NUMBER: _ClassVar[int]
        hub_in_use: DefaultError
        hub_not_found: DefaultError
        hub_offline: DefaultError
        hub_not_empty: DefaultError
        hub_error: DefaultError
        hub_wrong_state: DefaultError
        hub_busy: DefaultError
        hub_firmware_version_not_support_migration: DefaultError
        hub_claim_error: DefaultError
        hub_qr_code_invalid: DefaultError
        member_not_support_add_fibra_and_hybrid_hub: DefaultError
        member_not_authorized_add_hub: DefaultError
        member_not_authorized_add_fibra_and_hybrid_hub: DefaultError
        hub_in_use_in_space_with_no_admin: DefaultError
        hub_locked_to_another_company: DefaultError
        def __init__(self, hub_in_use: _Optional[_Union[DefaultError, _Mapping]] = ..., hub_not_found: _Optional[_Union[DefaultError, _Mapping]] = ..., hub_offline: _Optional[_Union[DefaultError, _Mapping]] = ..., hub_not_empty: _Optional[_Union[DefaultError, _Mapping]] = ..., hub_error: _Optional[_Union[DefaultError, _Mapping]] = ..., hub_wrong_state: _Optional[_Union[DefaultError, _Mapping]] = ..., hub_busy: _Optional[_Union[DefaultError, _Mapping]] = ..., hub_firmware_version_not_support_migration: _Optional[_Union[DefaultError, _Mapping]] = ..., hub_claim_error: _Optional[_Union[DefaultError, _Mapping]] = ..., hub_qr_code_invalid: _Optional[_Union[DefaultError, _Mapping]] = ..., member_not_support_add_fibra_and_hybrid_hub: _Optional[_Union[DefaultError, _Mapping]] = ..., member_not_authorized_add_hub: _Optional[_Union[DefaultError, _Mapping]] = ..., member_not_authorized_add_fibra_and_hybrid_hub: _Optional[_Union[DefaultError, _Mapping]] = ..., hub_in_use_in_space_with_no_admin: _Optional[_Union[DefaultError, _Mapping]] = ..., hub_locked_to_another_company: _Optional[_Union[DefaultError, _Mapping]] = ...) -> None: ...
    FAILED_ADD_HUB_FIELD_NUMBER: _ClassVar[int]
    failed_add_hub: AddDeviceError.AddHubDeviceError
    def __init__(self, failed_add_hub: _Optional[_Union[AddDeviceError.AddHubDeviceError, _Mapping]] = ...) -> None: ...
