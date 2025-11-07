from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from v1.facility import facility_pb2 as _facility_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2_1
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFacilityOnInstallationResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("facility",)
        FACILITY_FIELD_NUMBER: _ClassVar[int]
        facility: _facility_pb2.Facility
        def __init__(self, facility: _Optional[_Union[_facility_pb2.Facility, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "registration_number_not_unique", "add_device_failed", "empty_spaces_limit_exceeded")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        REGISTRATION_NUMBER_NOT_UNIQUE_FIELD_NUMBER: _ClassVar[int]
        ADD_DEVICE_FAILED_FIELD_NUMBER: _ClassVar[int]
        EMPTY_SPACES_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2_1.Error
        registration_number_not_unique: _response_pb2_1.Error
        add_device_failed: _response_pb2.AddDeviceError
        empty_spaces_limit_exceeded: _response_pb2_1.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2_1.Error, _Mapping]] = ..., registration_number_not_unique: _Optional[_Union[_response_pb2_1.Error, _Mapping]] = ..., add_device_failed: _Optional[_Union[_response_pb2.AddDeviceError, _Mapping]] = ..., empty_spaces_limit_exceeded: _Optional[_Union[_response_pb2_1.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: CreateFacilityOnInstallationResponse.Success
    failure: CreateFacilityOnInstallationResponse.Failure
    def __init__(self, success: _Optional[_Union[CreateFacilityOnInstallationResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[CreateFacilityOnInstallationResponse.Failure, _Mapping]] = ...) -> None: ...
