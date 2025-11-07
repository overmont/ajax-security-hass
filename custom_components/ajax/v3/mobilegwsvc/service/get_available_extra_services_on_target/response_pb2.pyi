from v3.mobilegwsvc.commonmodels.accounting import available_extra_service_group_pb2 as _available_extra_service_group_pb2
from v3.mobilegwsvc.commonmodels.accounting import find_available_services_context_pb2 as _find_available_services_context_pb2
from v3.mobilegwsvc.commonmodels.accounting.failure import not_available_for_user_error_pb2 as _not_available_for_user_error_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAvailableExtraServicesOnTargetResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("available_extra_service_groups", "current_context")
        AVAILABLE_EXTRA_SERVICE_GROUPS_FIELD_NUMBER: _ClassVar[int]
        CURRENT_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        available_extra_service_groups: _containers.RepeatedCompositeFieldContainer[_available_extra_service_group_pb2.AvailableExtraServiceGroup]
        current_context: _find_available_services_context_pb2.FindAvailableServicesContext
        def __init__(self, available_extra_service_groups: _Optional[_Iterable[_Union[_available_extra_service_group_pb2.AvailableExtraServiceGroup, _Mapping]]] = ..., current_context: _Optional[_Union[_find_available_services_context_pb2.FindAvailableServicesContext, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "available_mandatory_service_not_found", "reseller_not_found", "dealer_not_found", "not_available_for_user")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_MANDATORY_SERVICE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        RESELLER_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        DEALER_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        NOT_AVAILABLE_FOR_USER_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        available_mandatory_service_not_found: _response_pb2.Error
        reseller_not_found: _response_pb2.Error
        dealer_not_found: _response_pb2.Error
        not_available_for_user: _not_available_for_user_error_pb2.NotAvailableForUserError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., available_mandatory_service_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., reseller_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., dealer_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., not_available_for_user: _Optional[_Union[_not_available_for_user_error_pb2.NotAvailableForUserError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetAvailableExtraServicesOnTargetResponse.Success
    failure: GetAvailableExtraServicesOnTargetResponse.Failure
    def __init__(self, success: _Optional[_Union[GetAvailableExtraServicesOnTargetResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[GetAvailableExtraServicesOnTargetResponse.Failure, _Mapping]] = ...) -> None: ...
