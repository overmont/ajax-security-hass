from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.sensor import detection_zone_test_sensor_pb2 as _detection_zone_test_sensor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamDetectionZoneTestResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("snapshot", "update", "trigger_event")
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        UPDATE_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_EVENT_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamDetectionZoneTestResponse.Snapshot
        update: StreamDetectionZoneTestResponse.Update
        trigger_event: StreamDetectionZoneTestResponse.TriggerEvent
        def __init__(self, snapshot: _Optional[_Union[StreamDetectionZoneTestResponse.Snapshot, _Mapping]] = ..., update: _Optional[_Union[StreamDetectionZoneTestResponse.Update, _Mapping]] = ..., trigger_event: _Optional[_Union[StreamDetectionZoneTestResponse.TriggerEvent, _Mapping]] = ...) -> None: ...
    class Snapshot(_message.Message):
        __slots__ = ("statuses",)
        STATUSES_FIELD_NUMBER: _ClassVar[int]
        statuses: _containers.RepeatedCompositeFieldContainer[StreamDetectionZoneTestResponse.DeviceStatus]
        def __init__(self, statuses: _Optional[_Iterable[_Union[StreamDetectionZoneTestResponse.DeviceStatus, _Mapping]]] = ...) -> None: ...
    class Update(_message.Message):
        __slots__ = ("statuses",)
        STATUSES_FIELD_NUMBER: _ClassVar[int]
        statuses: _containers.RepeatedCompositeFieldContainer[StreamDetectionZoneTestResponse.DeviceStatus]
        def __init__(self, statuses: _Optional[_Iterable[_Union[StreamDetectionZoneTestResponse.DeviceStatus, _Mapping]]] = ...) -> None: ...
    class TriggerEvent(_message.Message):
        __slots__ = ("device_id", "message_info")
        DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_INFO_FIELD_NUMBER: _ClassVar[int]
        device_id: str
        message_info: StreamDetectionZoneTestResponse.MessageInfo
        def __init__(self, device_id: _Optional[str] = ..., message_info: _Optional[_Union[StreamDetectionZoneTestResponse.MessageInfo, _Mapping]] = ...) -> None: ...
    class DeviceStatus(_message.Message):
        __slots__ = ("device_id", "device_test_status", "device_sensors")
        class DeviceTestStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DEVICE_TEST_STATUS_UNSPECIFIED: _ClassVar[StreamDetectionZoneTestResponse.DeviceStatus.DeviceTestStatus]
            DEVICE_TEST_STATUS_INACTIVE: _ClassVar[StreamDetectionZoneTestResponse.DeviceStatus.DeviceTestStatus]
            DEVICE_TEST_STATUS_AWAITING_START: _ClassVar[StreamDetectionZoneTestResponse.DeviceStatus.DeviceTestStatus]
            DEVICE_TEST_STATUS_IN_PROGRESS: _ClassVar[StreamDetectionZoneTestResponse.DeviceStatus.DeviceTestStatus]
            DEVICE_TEST_STATUS_AWAITING_FINISH: _ClassVar[StreamDetectionZoneTestResponse.DeviceStatus.DeviceTestStatus]
        DEVICE_TEST_STATUS_UNSPECIFIED: StreamDetectionZoneTestResponse.DeviceStatus.DeviceTestStatus
        DEVICE_TEST_STATUS_INACTIVE: StreamDetectionZoneTestResponse.DeviceStatus.DeviceTestStatus
        DEVICE_TEST_STATUS_AWAITING_START: StreamDetectionZoneTestResponse.DeviceStatus.DeviceTestStatus
        DEVICE_TEST_STATUS_IN_PROGRESS: StreamDetectionZoneTestResponse.DeviceStatus.DeviceTestStatus
        DEVICE_TEST_STATUS_AWAITING_FINISH: StreamDetectionZoneTestResponse.DeviceStatus.DeviceTestStatus
        DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
        DEVICE_TEST_STATUS_FIELD_NUMBER: _ClassVar[int]
        DEVICE_SENSORS_FIELD_NUMBER: _ClassVar[int]
        device_id: str
        device_test_status: StreamDetectionZoneTestResponse.DeviceStatus.DeviceTestStatus
        device_sensors: _containers.RepeatedCompositeFieldContainer[_detection_zone_test_sensor_pb2.DeviceSensor]
        def __init__(self, device_id: _Optional[str] = ..., device_test_status: _Optional[_Union[StreamDetectionZoneTestResponse.DeviceStatus.DeviceTestStatus, str]] = ..., device_sensors: _Optional[_Iterable[_Union[_detection_zone_test_sensor_pb2.DeviceSensor, _Mapping]]] = ...) -> None: ...
    class MessageInfo(_message.Message):
        __slots__ = ("device_name", "room_name", "trigger_type")
        class TriggerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TRIGGER_TYPE_UNSPECIFIED: _ClassVar[StreamDetectionZoneTestResponse.MessageInfo.TriggerType]
            TRIGGER_TYPE_DEVICE: _ClassVar[StreamDetectionZoneTestResponse.MessageInfo.TriggerType]
            TRIGGER_TYPE_LEFT_SIDE: _ClassVar[StreamDetectionZoneTestResponse.MessageInfo.TriggerType]
            TRIGGER_TYPE_RIGHT_SIDE: _ClassVar[StreamDetectionZoneTestResponse.MessageInfo.TriggerType]
        TRIGGER_TYPE_UNSPECIFIED: StreamDetectionZoneTestResponse.MessageInfo.TriggerType
        TRIGGER_TYPE_DEVICE: StreamDetectionZoneTestResponse.MessageInfo.TriggerType
        TRIGGER_TYPE_LEFT_SIDE: StreamDetectionZoneTestResponse.MessageInfo.TriggerType
        TRIGGER_TYPE_RIGHT_SIDE: StreamDetectionZoneTestResponse.MessageInfo.TriggerType
        DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_TYPE_FIELD_NUMBER: _ClassVar[int]
        device_name: str
        room_name: str
        trigger_type: StreamDetectionZoneTestResponse.MessageInfo.TriggerType
        def __init__(self, device_name: _Optional[str] = ..., room_name: _Optional[str] = ..., trigger_type: _Optional[_Union[StreamDetectionZoneTestResponse.MessageInfo.TriggerType, str]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamDetectionZoneTestResponse.Success
    failure: StreamDetectionZoneTestResponse.Failure
    def __init__(self, success: _Optional[_Union[StreamDetectionZoneTestResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[StreamDetectionZoneTestResponse.Failure, _Mapping]] = ...) -> None: ...
