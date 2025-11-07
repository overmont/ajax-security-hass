from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamActuatorTestStatusResponse(_message.Message):
    __slots__ = ("success", "failure")
    class AnnunciationTestEndPoint(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ANNUNCIATION_TEST_END_POINT_UNSPECIFIED: _ClassVar[StreamActuatorTestStatusResponse.AnnunciationTestEndPoint]
        ANNUNCIATION_TEST_END_POINT_SOUNDER_TEST: _ClassVar[StreamActuatorTestStatusResponse.AnnunciationTestEndPoint]
        ANNUNCIATION_TEST_END_POINT_VAD_TEST: _ClassVar[StreamActuatorTestStatusResponse.AnnunciationTestEndPoint]
    ANNUNCIATION_TEST_END_POINT_UNSPECIFIED: StreamActuatorTestStatusResponse.AnnunciationTestEndPoint
    ANNUNCIATION_TEST_END_POINT_SOUNDER_TEST: StreamActuatorTestStatusResponse.AnnunciationTestEndPoint
    ANNUNCIATION_TEST_END_POINT_VAD_TEST: StreamActuatorTestStatusResponse.AnnunciationTestEndPoint
    class StatusTest(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_TEST_UNSPECIFIED: _ClassVar[StreamActuatorTestStatusResponse.StatusTest]
        STATUS_TEST_INACTIVE: _ClassVar[StreamActuatorTestStatusResponse.StatusTest]
        STATUS_TEST_STARTING: _ClassVar[StreamActuatorTestStatusResponse.StatusTest]
        STATUS_TEST_ACTIVE: _ClassVar[StreamActuatorTestStatusResponse.StatusTest]
        STATUS_TEST_FINISHING: _ClassVar[StreamActuatorTestStatusResponse.StatusTest]
    STATUS_TEST_UNSPECIFIED: StreamActuatorTestStatusResponse.StatusTest
    STATUS_TEST_INACTIVE: StreamActuatorTestStatusResponse.StatusTest
    STATUS_TEST_STARTING: StreamActuatorTestStatusResponse.StatusTest
    STATUS_TEST_ACTIVE: StreamActuatorTestStatusResponse.StatusTest
    STATUS_TEST_FINISHING: StreamActuatorTestStatusResponse.StatusTest
    class Success(_message.Message):
        __slots__ = ("snapshot", "update")
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        UPDATE_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamActuatorTestStatusResponse.Snapshot
        update: StreamActuatorTestStatusResponse.Update
        def __init__(self, snapshot: _Optional[_Union[StreamActuatorTestStatusResponse.Snapshot, _Mapping]] = ..., update: _Optional[_Union[StreamActuatorTestStatusResponse.Update, _Mapping]] = ...) -> None: ...
    class Snapshot(_message.Message):
        __slots__ = ("test_state_info",)
        TEST_STATE_INFO_FIELD_NUMBER: _ClassVar[int]
        test_state_info: StreamActuatorTestStatusResponse.TestStateInfo
        def __init__(self, test_state_info: _Optional[_Union[StreamActuatorTestStatusResponse.TestStateInfo, _Mapping]] = ...) -> None: ...
    class Update(_message.Message):
        __slots__ = ("test_state_info",)
        TEST_STATE_INFO_FIELD_NUMBER: _ClassVar[int]
        test_state_info: StreamActuatorTestStatusResponse.TestStateInfo
        def __init__(self, test_state_info: _Optional[_Union[StreamActuatorTestStatusResponse.TestStateInfo, _Mapping]] = ...) -> None: ...
    class TestStateInfo(_message.Message):
        __slots__ = ("annunciation_test_endpoints", "status")
        ANNUNCIATION_TEST_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        annunciation_test_endpoints: _containers.RepeatedScalarFieldContainer[StreamActuatorTestStatusResponse.AnnunciationTestEndPoint]
        status: StreamActuatorTestStatusResponse.StatusTest
        def __init__(self, annunciation_test_endpoints: _Optional[_Iterable[_Union[StreamActuatorTestStatusResponse.AnnunciationTestEndPoint, str]]] = ..., status: _Optional[_Union[StreamActuatorTestStatusResponse.StatusTest, str]] = ...) -> None: ...
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
    success: StreamActuatorTestStatusResponse.Success
    failure: StreamActuatorTestStatusResponse.Failure
    def __init__(self, success: _Optional[_Union[StreamActuatorTestStatusResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[StreamActuatorTestStatusResponse.Failure, _Mapping]] = ...) -> None: ...
