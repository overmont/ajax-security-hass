from v3.mobilegwsvc.commonmodels.accounting import postpayment_service_group_pb2 as _postpayment_service_group_pb2
from v3.mobilegwsvc.commonmodels.accounting import prepayment_service_group_pb2 as _prepayment_service_group_pb2
from v3.mobilegwsvc.commonmodels.accounting.failure import not_available_for_user_error_pb2 as _not_available_for_user_error_pb2
from v3.mobilegwsvc.commonmodels.accounting import find_available_services_context_pb2 as _find_available_services_context_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FindAvailableExtraServicesDataForSpaceResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("prepayment_flow_data", "post_payment_flow_data")
        class PrepaymentData(_message.Message):
            __slots__ = ("available_prepayment_service_groups",)
            AVAILABLE_PREPAYMENT_SERVICE_GROUPS_FIELD_NUMBER: _ClassVar[int]
            available_prepayment_service_groups: _containers.RepeatedCompositeFieldContainer[_prepayment_service_group_pb2.AvailablePrePaymentServiceGroup]
            def __init__(self, available_prepayment_service_groups: _Optional[_Iterable[_Union[_prepayment_service_group_pb2.AvailablePrePaymentServiceGroup, _Mapping]]] = ...) -> None: ...
        class PostPaymentData(_message.Message):
            __slots__ = ("available_post_payment_service_groups", "current_context")
            AVAILABLE_POST_PAYMENT_SERVICE_GROUPS_FIELD_NUMBER: _ClassVar[int]
            CURRENT_CONTEXT_FIELD_NUMBER: _ClassVar[int]
            available_post_payment_service_groups: _containers.RepeatedCompositeFieldContainer[_postpayment_service_group_pb2.AvailablePostPaymentServiceGroup]
            current_context: _find_available_services_context_pb2.FindAvailableServicesContext
            def __init__(self, available_post_payment_service_groups: _Optional[_Iterable[_Union[_postpayment_service_group_pb2.AvailablePostPaymentServiceGroup, _Mapping]]] = ..., current_context: _Optional[_Union[_find_available_services_context_pb2.FindAvailableServicesContext, _Mapping]] = ...) -> None: ...
        PREPAYMENT_FLOW_DATA_FIELD_NUMBER: _ClassVar[int]
        POST_PAYMENT_FLOW_DATA_FIELD_NUMBER: _ClassVar[int]
        prepayment_flow_data: FindAvailableExtraServicesDataForSpaceResponse.Success.PrepaymentData
        post_payment_flow_data: FindAvailableExtraServicesDataForSpaceResponse.Success.PostPaymentData
        def __init__(self, prepayment_flow_data: _Optional[_Union[FindAvailableExtraServicesDataForSpaceResponse.Success.PrepaymentData, _Mapping]] = ..., post_payment_flow_data: _Optional[_Union[FindAvailableExtraServicesDataForSpaceResponse.Success.PostPaymentData, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("internal_error", "bad_request", "available_mandatory_service_not_found", "reseller_not_found", "dealer_not_found", "not_available_for_user")
        INTERNAL_ERROR_FIELD_NUMBER: _ClassVar[int]
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_MANDATORY_SERVICE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        RESELLER_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        DEALER_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        NOT_AVAILABLE_FOR_USER_FIELD_NUMBER: _ClassVar[int]
        internal_error: _response_pb2.Error
        bad_request: _response_pb2.Error
        available_mandatory_service_not_found: _response_pb2.Error
        reseller_not_found: _response_pb2.Error
        dealer_not_found: _response_pb2.Error
        not_available_for_user: _not_available_for_user_error_pb2.NotAvailableForUserError
        def __init__(self, internal_error: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., available_mandatory_service_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., reseller_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., dealer_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., not_available_for_user: _Optional[_Union[_not_available_for_user_error_pb2.NotAvailableForUserError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: FindAvailableExtraServicesDataForSpaceResponse.Success
    failure: FindAvailableExtraServicesDataForSpaceResponse.Failure
    def __init__(self, success: _Optional[_Union[FindAvailableExtraServicesDataForSpaceResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[FindAvailableExtraServicesDataForSpaceResponse.Failure, _Mapping]] = ...) -> None: ...
