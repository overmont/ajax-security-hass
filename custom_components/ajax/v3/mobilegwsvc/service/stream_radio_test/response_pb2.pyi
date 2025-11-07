from google.protobuf import timestamp_pb2 as _timestamp_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.hub.device.common import device_radio_test_type_pb2 as _device_radio_test_type_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_signal_level_pb2 as _device_signal_level_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamRadioTestResponse(_message.Message):
    __slots__ = ("success", "failure")
    class RadioTestStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RADIO_TEST_STATUS_UNSPECIFIED: _ClassVar[StreamRadioTestResponse.RadioTestStatus]
        RADIO_TEST_STATUS_READY_TO_START: _ClassVar[StreamRadioTestResponse.RadioTestStatus]
        RADIO_TEST_STATUS_STARTING: _ClassVar[StreamRadioTestResponse.RadioTestStatus]
        RADIO_TEST_STATUS_IN_PROGRESS: _ClassVar[StreamRadioTestResponse.RadioTestStatus]
        RADIO_TEST_STATUS_STOPPING: _ClassVar[StreamRadioTestResponse.RadioTestStatus]
    RADIO_TEST_STATUS_UNSPECIFIED: StreamRadioTestResponse.RadioTestStatus
    RADIO_TEST_STATUS_READY_TO_START: StreamRadioTestResponse.RadioTestStatus
    RADIO_TEST_STATUS_STARTING: StreamRadioTestResponse.RadioTestStatus
    RADIO_TEST_STATUS_IN_PROGRESS: StreamRadioTestResponse.RadioTestStatus
    RADIO_TEST_STATUS_STOPPING: StreamRadioTestResponse.RadioTestStatus
    class Success(_message.Message):
        __slots__ = ("snapshot",)
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamRadioTestResponse.Snapshot
        def __init__(self, snapshot: _Optional[_Union[StreamRadioTestResponse.Snapshot, _Mapping]] = ...) -> None: ...
    class Snapshot(_message.Message):
        __slots__ = ("info",)
        INFO_FIELD_NUMBER: _ClassVar[int]
        info: StreamRadioTestResponse.RadioTestInfo
        def __init__(self, info: _Optional[_Union[StreamRadioTestResponse.RadioTestInfo, _Mapping]] = ...) -> None: ...
    class RadioTestInfo(_message.Message):
        __slots__ = ("device_id", "status", "test_type", "signal_level", "started_at")
        DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        TEST_TYPE_FIELD_NUMBER: _ClassVar[int]
        SIGNAL_LEVEL_FIELD_NUMBER: _ClassVar[int]
        STARTED_AT_FIELD_NUMBER: _ClassVar[int]
        device_id: str
        status: StreamRadioTestResponse.RadioTestStatus
        test_type: _device_radio_test_type_pb2.DeviceRadioTestType
        signal_level: _device_signal_level_pb2.DeviceSignalLevel
        started_at: _timestamp_pb2.Timestamp
        def __init__(self, device_id: _Optional[str] = ..., status: _Optional[_Union[StreamRadioTestResponse.RadioTestStatus, str]] = ..., test_type: _Optional[_Union[_device_radio_test_type_pb2.DeviceRadioTestType, str]] = ..., signal_level: _Optional[_Union[_device_signal_level_pb2.DeviceSignalLevel, str]] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "device_not_found")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        DEVICE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        device_not_found: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., device_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamRadioTestResponse.Success
    failure: StreamRadioTestResponse.Failure
    def __init__(self, success: _Optional[_Union[StreamRadioTestResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[StreamRadioTestResponse.Failure, _Mapping]] = ...) -> None: ...
