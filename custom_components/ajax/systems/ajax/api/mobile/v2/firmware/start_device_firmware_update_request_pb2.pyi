from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import object_type_pb2 as _object_type_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StartDeviceFirmwareUpdateRequest(_message.Message):
    __slots__ = ("hub_id", "device_id")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    device_id: str
    def __init__(self, hub_id: _Optional[str] = ..., device_id: _Optional[str] = ...) -> None: ...

class StartDeviceFirmwareUpdateResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("message", "illegal_argument", "hub_illegal_state", "hub_offline", "update_not_found", "permission_denied")
        class HubIllegalStateError(_message.Message):
            __slots__ = ("rejection_reason", "source")
            class RejectionReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                REJECTION_REASON_UNSPECIFIED: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_HUB_SCAN: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_HUB_PWR_TEST: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_DEV_BUSY: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_DFU_IN_PROGRESS: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_RADIOTEST: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_DEV_ZONE_TEST: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_CARD_PROCESS: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_ARMED: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_EXIT_TIMER: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_ROUTE: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_DEV_OFFLINE: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_EXT_POWER: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_DEV_ALWAYS_ACTIVE: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_NOT_SUPPORTED: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_BUSES_PROBLEM: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_IWH_OBJECTS_LIMIT_ERROR: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_IWH_TEST_IN_PROGRESS: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_RING_PROBLEM: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_RING_UNREGISTERED: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_RING_DISCONNECTED: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_ACTIVE_CALL: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_FP_BUKHOOR_FORBIDDEN_TIME: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_FP_FIRE_ALARM: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_DEV_BYPASSED: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_WRONG_POWER_SUPPLY_SETTINGS: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_IN_LINES_SHORT_CIRCUIT: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_OUT_LINES_SHORT_CIRCUIT: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_WIFI_FUNC_NOT_WORK: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_DEV_POWER_OVERLOAD: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_BATTERY_LOW: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_EXTRA_COMM_CHAN_REQUIRED: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_JAMMING_DETECTED: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
                REJECTION_REASON_WALK_TEST_IN_PROGRESS: _ClassVar[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason]
            REJECTION_REASON_UNSPECIFIED: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_HUB_SCAN: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_HUB_PWR_TEST: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_DEV_BUSY: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_DFU_IN_PROGRESS: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_RADIOTEST: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_DEV_ZONE_TEST: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_CARD_PROCESS: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_ARMED: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_EXIT_TIMER: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_ROUTE: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_DEV_OFFLINE: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_EXT_POWER: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_DEV_ALWAYS_ACTIVE: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_NOT_SUPPORTED: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_BUSES_PROBLEM: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_IWH_OBJECTS_LIMIT_ERROR: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_IWH_TEST_IN_PROGRESS: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_RING_PROBLEM: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_RING_UNREGISTERED: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_RING_DISCONNECTED: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_ACTIVE_CALL: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_FP_BUKHOOR_FORBIDDEN_TIME: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_FP_FIRE_ALARM: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_DEV_BYPASSED: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_WRONG_POWER_SUPPLY_SETTINGS: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_IN_LINES_SHORT_CIRCUIT: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_OUT_LINES_SHORT_CIRCUIT: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_WIFI_FUNC_NOT_WORK: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_DEV_POWER_OVERLOAD: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_BATTERY_LOW: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_EXTRA_COMM_CHAN_REQUIRED: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_JAMMING_DETECTED: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            REJECTION_REASON_WALK_TEST_IN_PROGRESS: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            class Source(_message.Message):
                __slots__ = ("device_hex_id", "device_type", "device_type_v2")
                DEVICE_HEX_ID_FIELD_NUMBER: _ClassVar[int]
                DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
                DEVICE_TYPE_V2_FIELD_NUMBER: _ClassVar[int]
                device_hex_id: str
                device_type: str
                device_type_v2: _object_type_pb2.ObjectType
                def __init__(self, device_hex_id: _Optional[str] = ..., device_type: _Optional[str] = ..., device_type_v2: _Optional[_Union[_object_type_pb2.ObjectType, _Mapping]] = ...) -> None: ...
            REJECTION_REASON_FIELD_NUMBER: _ClassVar[int]
            SOURCE_FIELD_NUMBER: _ClassVar[int]
            rejection_reason: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason
            source: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.Source
            def __init__(self, rejection_reason: _Optional[_Union[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.RejectionReason, str]] = ..., source: _Optional[_Union[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError.Source, _Mapping]] = ...) -> None: ...
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        HUB_ILLEGAL_STATE_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        UPDATE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        message: str
        illegal_argument: _response_pb2.DefaultError
        hub_illegal_state: StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError
        hub_offline: _response_pb2.DefaultError
        update_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        def __init__(self, message: _Optional[str] = ..., illegal_argument: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_illegal_state: _Optional[_Union[StartDeviceFirmwareUpdateResponse.Failure.HubIllegalStateError, _Mapping]] = ..., hub_offline: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., update_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: StartDeviceFirmwareUpdateResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[StartDeviceFirmwareUpdateResponse.Failure, _Mapping]] = ...) -> None: ...
