from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2_1
from systems.ajax.api.mobile.v2.common.space import space_lite_pb2 as _space_lite_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSpaceResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("lite_space",)
        LITE_SPACE_FIELD_NUMBER: _ClassVar[int]
        lite_space: _space_lite_pb2.LiteSpace
        def __init__(self, lite_space: _Optional[_Union[_space_lite_pb2.LiteSpace, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "add_device_failed", "empty_spaces_limit_exceeded")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        ADD_DEVICE_FAILED_FIELD_NUMBER: _ClassVar[int]
        EMPTY_SPACES_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        add_device_failed: _response_pb2_1.AddDeviceError
        empty_spaces_limit_exceeded: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., add_device_failed: _Optional[_Union[_response_pb2_1.AddDeviceError, _Mapping]] = ..., empty_spaces_limit_exceeded: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: CreateSpaceResponse.Success
    failure: CreateSpaceResponse.Failure
    def __init__(self, success: _Optional[_Union[CreateSpaceResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[CreateSpaceResponse.Failure, _Mapping]] = ...) -> None: ...
