from google.protobuf import timestamp_pb2 as _timestamp_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamFireZoneResponseV2(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("snapshot", "updates")
        class Snapshot(_message.Message):
            __slots__ = ("fire_zones",)
            class FireZoneSnapshot(_message.Message):
                __slots__ = ("fire_zone_id_hex", "fire_zone_state", "fire_alarm_state", "test_state", "disablement_state", "fault_state")
                FIRE_ZONE_ID_HEX_FIELD_NUMBER: _ClassVar[int]
                FIRE_ZONE_STATE_FIELD_NUMBER: _ClassVar[int]
                FIRE_ALARM_STATE_FIELD_NUMBER: _ClassVar[int]
                TEST_STATE_FIELD_NUMBER: _ClassVar[int]
                DISABLEMENT_STATE_FIELD_NUMBER: _ClassVar[int]
                FAULT_STATE_FIELD_NUMBER: _ClassVar[int]
                fire_zone_id_hex: str
                fire_zone_state: StreamFireZoneResponseV2.Success.FireZoneState
                fire_alarm_state: StreamFireZoneResponseV2.Success.FireAlarmState
                test_state: StreamFireZoneResponseV2.Success.TestState
                disablement_state: StreamFireZoneResponseV2.Success.DisablementState
                fault_state: StreamFireZoneResponseV2.Success.FaultState
                def __init__(self, fire_zone_id_hex: _Optional[str] = ..., fire_zone_state: _Optional[_Union[StreamFireZoneResponseV2.Success.FireZoneState, _Mapping]] = ..., fire_alarm_state: _Optional[_Union[StreamFireZoneResponseV2.Success.FireAlarmState, _Mapping]] = ..., test_state: _Optional[_Union[StreamFireZoneResponseV2.Success.TestState, _Mapping]] = ..., disablement_state: _Optional[_Union[StreamFireZoneResponseV2.Success.DisablementState, _Mapping]] = ..., fault_state: _Optional[_Union[StreamFireZoneResponseV2.Success.FaultState, _Mapping]] = ...) -> None: ...
            FIRE_ZONES_FIELD_NUMBER: _ClassVar[int]
            fire_zones: _containers.RepeatedCompositeFieldContainer[StreamFireZoneResponseV2.Success.Snapshot.FireZoneSnapshot]
            def __init__(self, fire_zones: _Optional[_Iterable[_Union[StreamFireZoneResponseV2.Success.Snapshot.FireZoneSnapshot, _Mapping]]] = ...) -> None: ...
        class Updates(_message.Message):
            __slots__ = ("updates",)
            UPDATES_FIELD_NUMBER: _ClassVar[int]
            updates: _containers.RepeatedCompositeFieldContainer[StreamFireZoneResponseV2.Success.Update]
            def __init__(self, updates: _Optional[_Iterable[_Union[StreamFireZoneResponseV2.Success.Update, _Mapping]]] = ...) -> None: ...
        class Update(_message.Message):
            __slots__ = ("fire_zone_id_hex", "fire_zone_state", "fire_alarm_state", "test_state", "disablement_state", "fault_state")
            FIRE_ZONE_ID_HEX_FIELD_NUMBER: _ClassVar[int]
            FIRE_ZONE_STATE_FIELD_NUMBER: _ClassVar[int]
            FIRE_ALARM_STATE_FIELD_NUMBER: _ClassVar[int]
            TEST_STATE_FIELD_NUMBER: _ClassVar[int]
            DISABLEMENT_STATE_FIELD_NUMBER: _ClassVar[int]
            FAULT_STATE_FIELD_NUMBER: _ClassVar[int]
            fire_zone_id_hex: str
            fire_zone_state: StreamFireZoneResponseV2.Success.FireZoneState
            fire_alarm_state: StreamFireZoneResponseV2.Success.FireAlarmState
            test_state: StreamFireZoneResponseV2.Success.TestState
            disablement_state: StreamFireZoneResponseV2.Success.DisablementState
            fault_state: StreamFireZoneResponseV2.Success.FaultState
            def __init__(self, fire_zone_id_hex: _Optional[str] = ..., fire_zone_state: _Optional[_Union[StreamFireZoneResponseV2.Success.FireZoneState, _Mapping]] = ..., fire_alarm_state: _Optional[_Union[StreamFireZoneResponseV2.Success.FireAlarmState, _Mapping]] = ..., test_state: _Optional[_Union[StreamFireZoneResponseV2.Success.TestState, _Mapping]] = ..., disablement_state: _Optional[_Union[StreamFireZoneResponseV2.Success.DisablementState, _Mapping]] = ..., fault_state: _Optional[_Union[StreamFireZoneResponseV2.Success.FaultState, _Mapping]] = ...) -> None: ...
        class FireZoneState(_message.Message):
            __slots__ = ("name", "device_count")
            NAME_FIELD_NUMBER: _ClassVar[int]
            DEVICE_COUNT_FIELD_NUMBER: _ClassVar[int]
            name: str
            device_count: int
            def __init__(self, name: _Optional[str] = ..., device_count: _Optional[int] = ...) -> None: ...
        class FireAlarmState(_message.Message):
            __slots__ = ("state", "fire_alarm_details")
            class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                STATE_UNSPECIFIED: _ClassVar[StreamFireZoneResponseV2.Success.FireAlarmState.State]
                STATE_NOT_IN_ALARM: _ClassVar[StreamFireZoneResponseV2.Success.FireAlarmState.State]
                STATE_IN_ALARM: _ClassVar[StreamFireZoneResponseV2.Success.FireAlarmState.State]
            STATE_UNSPECIFIED: StreamFireZoneResponseV2.Success.FireAlarmState.State
            STATE_NOT_IN_ALARM: StreamFireZoneResponseV2.Success.FireAlarmState.State
            STATE_IN_ALARM: StreamFireZoneResponseV2.Success.FireAlarmState.State
            class AlarmReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                ALARM_REASON_UNSPECIFIED: _ClassVar[StreamFireZoneResponseV2.Success.FireAlarmState.AlarmReason]
                ALARM_REASON_SMOKE: _ClassVar[StreamFireZoneResponseV2.Success.FireAlarmState.AlarmReason]
                ALARM_REASON_TEMP: _ClassVar[StreamFireZoneResponseV2.Success.FireAlarmState.AlarmReason]
                ALARM_REASON_TEMP_DIFF: _ClassVar[StreamFireZoneResponseV2.Success.FireAlarmState.AlarmReason]
                ALARM_REASON_WIRE_INPUT: _ClassVar[StreamFireZoneResponseV2.Success.FireAlarmState.AlarmReason]
                ALARM_REASON_MCP: _ClassVar[StreamFireZoneResponseV2.Success.FireAlarmState.AlarmReason]
            ALARM_REASON_UNSPECIFIED: StreamFireZoneResponseV2.Success.FireAlarmState.AlarmReason
            ALARM_REASON_SMOKE: StreamFireZoneResponseV2.Success.FireAlarmState.AlarmReason
            ALARM_REASON_TEMP: StreamFireZoneResponseV2.Success.FireAlarmState.AlarmReason
            ALARM_REASON_TEMP_DIFF: StreamFireZoneResponseV2.Success.FireAlarmState.AlarmReason
            ALARM_REASON_WIRE_INPUT: StreamFireZoneResponseV2.Success.FireAlarmState.AlarmReason
            ALARM_REASON_MCP: StreamFireZoneResponseV2.Success.FireAlarmState.AlarmReason
            class FireAlarmDetails(_message.Message):
                __slots__ = ("start_timestamp", "alarm_reason", "room_id_hex", "alarm_started_device_id_hex", "alarm_started_device_location")
                START_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
                ALARM_REASON_FIELD_NUMBER: _ClassVar[int]
                ROOM_ID_HEX_FIELD_NUMBER: _ClassVar[int]
                ALARM_STARTED_DEVICE_ID_HEX_FIELD_NUMBER: _ClassVar[int]
                ALARM_STARTED_DEVICE_LOCATION_FIELD_NUMBER: _ClassVar[int]
                start_timestamp: _timestamp_pb2.Timestamp
                alarm_reason: StreamFireZoneResponseV2.Success.FireAlarmState.AlarmReason
                room_id_hex: str
                alarm_started_device_id_hex: str
                alarm_started_device_location: str
                def __init__(self, start_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., alarm_reason: _Optional[_Union[StreamFireZoneResponseV2.Success.FireAlarmState.AlarmReason, str]] = ..., room_id_hex: _Optional[str] = ..., alarm_started_device_id_hex: _Optional[str] = ..., alarm_started_device_location: _Optional[str] = ...) -> None: ...
            STATE_FIELD_NUMBER: _ClassVar[int]
            FIRE_ALARM_DETAILS_FIELD_NUMBER: _ClassVar[int]
            state: StreamFireZoneResponseV2.Success.FireAlarmState.State
            fire_alarm_details: StreamFireZoneResponseV2.Success.FireAlarmState.FireAlarmDetails
            def __init__(self, state: _Optional[_Union[StreamFireZoneResponseV2.Success.FireAlarmState.State, str]] = ..., fire_alarm_details: _Optional[_Union[StreamFireZoneResponseV2.Success.FireAlarmState.FireAlarmDetails, _Mapping]] = ...) -> None: ...
        class TestState(_message.Message):
            __slots__ = ("state", "tests_count")
            class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                STATE_UNSPECIFIED: _ClassVar[StreamFireZoneResponseV2.Success.TestState.State]
                STATE_NOT_IN_TEST: _ClassVar[StreamFireZoneResponseV2.Success.TestState.State]
                STATE_IN_TEST: _ClassVar[StreamFireZoneResponseV2.Success.TestState.State]
            STATE_UNSPECIFIED: StreamFireZoneResponseV2.Success.TestState.State
            STATE_NOT_IN_TEST: StreamFireZoneResponseV2.Success.TestState.State
            STATE_IN_TEST: StreamFireZoneResponseV2.Success.TestState.State
            STATE_FIELD_NUMBER: _ClassVar[int]
            TESTS_COUNT_FIELD_NUMBER: _ClassVar[int]
            state: StreamFireZoneResponseV2.Success.TestState.State
            tests_count: int
            def __init__(self, state: _Optional[_Union[StreamFireZoneResponseV2.Success.TestState.State, str]] = ..., tests_count: _Optional[int] = ...) -> None: ...
        class DisablementState(_message.Message):
            __slots__ = ("disablement_zone_state", "disablement_parts_state", "disablement_count")
            class DisablementPart(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                DISABLEMENT_PART_UNSPECIFIED: _ClassVar[StreamFireZoneResponseV2.Success.DisablementState.DisablementPart]
                DISABLEMENT_PART_SMOKE: _ClassVar[StreamFireZoneResponseV2.Success.DisablementState.DisablementPart]
                DISABLEMENT_PART_TEMP: _ClassVar[StreamFireZoneResponseV2.Success.DisablementState.DisablementPart]
                DISABLEMENT_PART_SOUNDER: _ClassVar[StreamFireZoneResponseV2.Success.DisablementState.DisablementPart]
                DISABLEMENT_PART_VAD: _ClassVar[StreamFireZoneResponseV2.Success.DisablementState.DisablementPart]
                DISABLEMENT_PART_INPUT: _ClassVar[StreamFireZoneResponseV2.Success.DisablementState.DisablementPart]
                DISABLEMENT_PART_OUTPUT: _ClassVar[StreamFireZoneResponseV2.Success.DisablementState.DisablementPart]
                DISABLEMENT_PART_MCP: _ClassVar[StreamFireZoneResponseV2.Success.DisablementState.DisablementPart]
            DISABLEMENT_PART_UNSPECIFIED: StreamFireZoneResponseV2.Success.DisablementState.DisablementPart
            DISABLEMENT_PART_SMOKE: StreamFireZoneResponseV2.Success.DisablementState.DisablementPart
            DISABLEMENT_PART_TEMP: StreamFireZoneResponseV2.Success.DisablementState.DisablementPart
            DISABLEMENT_PART_SOUNDER: StreamFireZoneResponseV2.Success.DisablementState.DisablementPart
            DISABLEMENT_PART_VAD: StreamFireZoneResponseV2.Success.DisablementState.DisablementPart
            DISABLEMENT_PART_INPUT: StreamFireZoneResponseV2.Success.DisablementState.DisablementPart
            DISABLEMENT_PART_OUTPUT: StreamFireZoneResponseV2.Success.DisablementState.DisablementPart
            DISABLEMENT_PART_MCP: StreamFireZoneResponseV2.Success.DisablementState.DisablementPart
            class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                STATE_UNSPECIFIED: _ClassVar[StreamFireZoneResponseV2.Success.DisablementState.State]
                STATE_NOT_PRESENT: _ClassVar[StreamFireZoneResponseV2.Success.DisablementState.State]
                STATE_ENABLED: _ClassVar[StreamFireZoneResponseV2.Success.DisablementState.State]
                STATE_PARTIAL_DISABLEMENT: _ClassVar[StreamFireZoneResponseV2.Success.DisablementState.State]
                STATE_FULL_DISABLEMENT: _ClassVar[StreamFireZoneResponseV2.Success.DisablementState.State]
            STATE_UNSPECIFIED: StreamFireZoneResponseV2.Success.DisablementState.State
            STATE_NOT_PRESENT: StreamFireZoneResponseV2.Success.DisablementState.State
            STATE_ENABLED: StreamFireZoneResponseV2.Success.DisablementState.State
            STATE_PARTIAL_DISABLEMENT: StreamFireZoneResponseV2.Success.DisablementState.State
            STATE_FULL_DISABLEMENT: StreamFireZoneResponseV2.Success.DisablementState.State
            class DisablementPartState(_message.Message):
                __slots__ = ("disablement_part", "state")
                DISABLEMENT_PART_FIELD_NUMBER: _ClassVar[int]
                STATE_FIELD_NUMBER: _ClassVar[int]
                disablement_part: StreamFireZoneResponseV2.Success.DisablementState.DisablementPart
                state: StreamFireZoneResponseV2.Success.DisablementState.State
                def __init__(self, disablement_part: _Optional[_Union[StreamFireZoneResponseV2.Success.DisablementState.DisablementPart, str]] = ..., state: _Optional[_Union[StreamFireZoneResponseV2.Success.DisablementState.State, str]] = ...) -> None: ...
            DISABLEMENT_ZONE_STATE_FIELD_NUMBER: _ClassVar[int]
            DISABLEMENT_PARTS_STATE_FIELD_NUMBER: _ClassVar[int]
            DISABLEMENT_COUNT_FIELD_NUMBER: _ClassVar[int]
            disablement_zone_state: StreamFireZoneResponseV2.Success.DisablementState.State
            disablement_parts_state: _containers.RepeatedCompositeFieldContainer[StreamFireZoneResponseV2.Success.DisablementState.DisablementPartState]
            disablement_count: int
            def __init__(self, disablement_zone_state: _Optional[_Union[StreamFireZoneResponseV2.Success.DisablementState.State, str]] = ..., disablement_parts_state: _Optional[_Iterable[_Union[StreamFireZoneResponseV2.Success.DisablementState.DisablementPartState, _Mapping]]] = ..., disablement_count: _Optional[int] = ...) -> None: ...
        class FaultState(_message.Message):
            __slots__ = ("state", "faults_count")
            class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                STATE_UNSPECIFIED: _ClassVar[StreamFireZoneResponseV2.Success.FaultState.State]
                STATE_NOT_IN_FAULT: _ClassVar[StreamFireZoneResponseV2.Success.FaultState.State]
                STATE_IN_FAULT: _ClassVar[StreamFireZoneResponseV2.Success.FaultState.State]
            STATE_UNSPECIFIED: StreamFireZoneResponseV2.Success.FaultState.State
            STATE_NOT_IN_FAULT: StreamFireZoneResponseV2.Success.FaultState.State
            STATE_IN_FAULT: StreamFireZoneResponseV2.Success.FaultState.State
            STATE_FIELD_NUMBER: _ClassVar[int]
            FAULTS_COUNT_FIELD_NUMBER: _ClassVar[int]
            state: StreamFireZoneResponseV2.Success.FaultState.State
            faults_count: int
            def __init__(self, state: _Optional[_Union[StreamFireZoneResponseV2.Success.FaultState.State, str]] = ..., faults_count: _Optional[int] = ...) -> None: ...
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        UPDATES_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamFireZoneResponseV2.Success.Snapshot
        updates: StreamFireZoneResponseV2.Success.Updates
        def __init__(self, snapshot: _Optional[_Union[StreamFireZoneResponseV2.Success.Snapshot, _Mapping]] = ..., updates: _Optional[_Union[StreamFireZoneResponseV2.Success.Updates, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("message", "bad_request", "hub_not_found", "illegal_argument", "request_timeout")
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        HUB_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        REQUEST_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        message: str
        bad_request: _response_pb2.Error
        hub_not_found: _response_pb2.Error
        illegal_argument: _response_pb2.Error
        request_timeout: _response_pb2.Error
        def __init__(self, message: _Optional[str] = ..., bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., illegal_argument: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., request_timeout: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamFireZoneResponseV2.Success
    failure: StreamFireZoneResponseV2.Failure
    def __init__(self, success: _Optional[_Union[StreamFireZoneResponseV2.Success, _Mapping]] = ..., failure: _Optional[_Union[StreamFireZoneResponseV2.Failure, _Mapping]] = ...) -> None: ...
