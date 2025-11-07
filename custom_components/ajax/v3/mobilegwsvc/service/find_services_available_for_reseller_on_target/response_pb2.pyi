from v3.mobilegwsvc.commonmodels.accounting import service_pb2 as _service_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FindServicesAvailableForResellerOnTargetResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("services",)
        SERVICES_FIELD_NUMBER: _ClassVar[int]
        services: _containers.RepeatedCompositeFieldContainer[_service_pb2.Service]
        def __init__(self, services: _Optional[_Iterable[_Union[_service_pb2.Service, _Mapping]]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request",)
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: FindServicesAvailableForResellerOnTargetResponse.Success
    failure: FindServicesAvailableForResellerOnTargetResponse.Failure
    def __init__(self, success: _Optional[_Union[FindServicesAvailableForResellerOnTargetResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[FindServicesAvailableForResellerOnTargetResponse.Failure, _Mapping]] = ...) -> None: ...
