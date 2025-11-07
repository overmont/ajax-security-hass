from google.protobuf import timestamp_pb2 as _timestamp_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import object_type_pb2 as _object_type_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device import walk_test_sensor_pb2 as _walk_test_sensor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamWalkTestResponse(_message.Message):
    __slots__ = ("success", "failure")
    class WalkTestState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WALK_TEST_STATE_UNSPECIFIED: _ClassVar[StreamWalkTestResponse.WalkTestState]
        WALK_TEST_STATE_LAUNCH: _ClassVar[StreamWalkTestResponse.WalkTestState]
        WALK_TEST_STATE_PROCESS: _ClassVar[StreamWalkTestResponse.WalkTestState]
        WALK_TEST_STATE_STOPPED: _ClassVar[StreamWalkTestResponse.WalkTestState]
    WALK_TEST_STATE_UNSPECIFIED: StreamWalkTestResponse.WalkTestState
    WALK_TEST_STATE_LAUNCH: StreamWalkTestResponse.WalkTestState
    WALK_TEST_STATE_PROCESS: StreamWalkTestResponse.WalkTestState
    WALK_TEST_STATE_STOPPED: StreamWalkTestResponse.WalkTestState
    class Success(_message.Message):
        __slots__ = ("snapshot", "update")
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        UPDATE_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamWalkTestResponse.Snapshot
        update: StreamWalkTestResponse.Update
        def __init__(self, snapshot: _Optional[_Union[StreamWalkTestResponse.Snapshot, _Mapping]] = ..., update: _Optional[_Union[StreamWalkTestResponse.Update, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    class Snapshot(_message.Message):
        __slots__ = ("walk_test_state", "devices", "events")
        WALK_TEST_STATE_FIELD_NUMBER: _ClassVar[int]
        DEVICES_FIELD_NUMBER: _ClassVar[int]
        EVENTS_FIELD_NUMBER: _ClassVar[int]
        walk_test_state: StreamWalkTestResponse.WalkTestState
        devices: _containers.RepeatedCompositeFieldContainer[StreamWalkTestResponse.WalkTestDevice]
        events: _containers.RepeatedCompositeFieldContainer[StreamWalkTestResponse.WalkTestEvent]
        def __init__(self, walk_test_state: _Optional[_Union[StreamWalkTestResponse.WalkTestState, str]] = ..., devices: _Optional[_Iterable[_Union[StreamWalkTestResponse.WalkTestDevice, _Mapping]]] = ..., events: _Optional[_Iterable[_Union[StreamWalkTestResponse.WalkTestEvent, _Mapping]]] = ...) -> None: ...
    class Update(_message.Message):
        __slots__ = ("walk_test_state", "walk_test_events")
        WALK_TEST_STATE_FIELD_NUMBER: _ClassVar[int]
        WALK_TEST_EVENTS_FIELD_NUMBER: _ClassVar[int]
        walk_test_state: StreamWalkTestResponse.WalkTestState
        walk_test_events: StreamWalkTestResponse.WalkTestEvents
        def __init__(self, walk_test_state: _Optional[_Union[StreamWalkTestResponse.WalkTestState, str]] = ..., walk_test_events: _Optional[_Union[StreamWalkTestResponse.WalkTestEvents, _Mapping]] = ...) -> None: ...
    class WalkTestDevice(_message.Message):
        __slots__ = ("hex_id", "type", "sensors")
        HEX_ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        SENSORS_FIELD_NUMBER: _ClassVar[int]
        hex_id: str
        type: _object_type_pb2.ObjectType
        sensors: _containers.RepeatedCompositeFieldContainer[_walk_test_sensor_pb2.WalkTestSensor]
        def __init__(self, hex_id: _Optional[str] = ..., type: _Optional[_Union[_object_type_pb2.ObjectType, _Mapping]] = ..., sensors: _Optional[_Iterable[_Union[_walk_test_sensor_pb2.WalkTestSensor, _Mapping]]] = ...) -> None: ...
    class WalkTestEvents(_message.Message):
        __slots__ = ("events",)
        EVENTS_FIELD_NUMBER: _ClassVar[int]
        events: _containers.RepeatedCompositeFieldContainer[StreamWalkTestResponse.WalkTestEvent]
        def __init__(self, events: _Optional[_Iterable[_Union[StreamWalkTestResponse.WalkTestEvent, _Mapping]]] = ...) -> None: ...
    class WalkTestEvent(_message.Message):
        __slots__ = ("timestamp", "device_hex_id", "device_type", "sensor")
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        DEVICE_HEX_ID_FIELD_NUMBER: _ClassVar[int]
        DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        SENSOR_FIELD_NUMBER: _ClassVar[int]
        timestamp: _timestamp_pb2.Timestamp
        device_hex_id: str
        device_type: _object_type_pb2.ObjectType
        sensor: _walk_test_sensor_pb2.WalkTestSensor
        def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., device_hex_id: _Optional[str] = ..., device_type: _Optional[_Union[_object_type_pb2.ObjectType, _Mapping]] = ..., sensor: _Optional[_Union[_walk_test_sensor_pb2.WalkTestSensor, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamWalkTestResponse.Success
    failure: StreamWalkTestResponse.Failure
    def __init__(self, success: _Optional[_Union[StreamWalkTestResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[StreamWalkTestResponse.Failure, _Mapping]] = ...) -> None: ...
