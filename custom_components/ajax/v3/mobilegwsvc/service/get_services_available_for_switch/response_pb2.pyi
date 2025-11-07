from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.accounting import service_pb2 as _service_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetServicesAvailableForSwitchResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("active_service", "available_services")
        ACTIVE_SERVICE_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_SERVICES_FIELD_NUMBER: _ClassVar[int]
        active_service: _service_pb2.Service
        available_services: _containers.RepeatedCompositeFieldContainer[_service_pb2.Service]
        def __init__(self, active_service: _Optional[_Union[_service_pb2.Service, _Mapping]] = ..., available_services: _Optional[_Iterable[_Union[_service_pb2.Service, _Mapping]]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("illegal_argument", "available_service_not_found", "subscription_not_found")
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_SERVICE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIPTION_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        illegal_argument: _response_pb2.Error
        available_service_not_found: _response_pb2.Error
        subscription_not_found: _response_pb2.Error
        def __init__(self, illegal_argument: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., available_service_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., subscription_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetServicesAvailableForSwitchResponse.Success
    failure: GetServicesAvailableForSwitchResponse.Failure
    def __init__(self, success: _Optional[_Union[GetServicesAvailableForSwitchResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[GetServicesAvailableForSwitchResponse.Failure, _Mapping]] = ...) -> None: ...
