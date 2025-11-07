from v3.mobilegwsvc.commonmodels.accounting import service_pb2 as _service_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.accounting import accounting_company_pb2 as _accounting_company_pb2
from v3.mobilegwsvc.commonmodels.accounting import service_switch_availability_status_pb2 as _service_switch_availability_status_pb2
from v3.mobilegwsvc.commonmodels.accounting import enriched_target_info_pb2 as _enriched_target_info_pb2
from v3.mobilegwsvc.commonmodels.accounting import extra_service_state_pb2 as _extra_service_state_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetActiveServicesResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("active_services",)
        ACTIVE_SERVICES_FIELD_NUMBER: _ClassVar[int]
        active_services: _containers.RepeatedCompositeFieldContainer[GetActiveServicesResponse.ActiveService]
        def __init__(self, active_services: _Optional[_Iterable[_Union[GetActiveServicesResponse.ActiveService, _Mapping]]] = ...) -> None: ...
    class ActiveService(_message.Message):
        __slots__ = ("service", "accounting_company", "subscription_id", "service_switch_availability_status", "enriched_target_info", "service_state")
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        ACCOUNTING_COMPANY_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
        SERVICE_SWITCH_AVAILABILITY_STATUS_FIELD_NUMBER: _ClassVar[int]
        ENRICHED_TARGET_INFO_FIELD_NUMBER: _ClassVar[int]
        SERVICE_STATE_FIELD_NUMBER: _ClassVar[int]
        service: _service_pb2.Service
        accounting_company: _accounting_company_pb2.AccountingCompany
        subscription_id: str
        service_switch_availability_status: _service_switch_availability_status_pb2.ServiceSwitchAvailabilityStatus
        enriched_target_info: _containers.RepeatedCompositeFieldContainer[_enriched_target_info_pb2.EnrichedTargetInfo]
        service_state: _extra_service_state_pb2.ExtraServiceState.Active
        def __init__(self, service: _Optional[_Union[_service_pb2.Service, _Mapping]] = ..., accounting_company: _Optional[_Union[_accounting_company_pb2.AccountingCompany, _Mapping]] = ..., subscription_id: _Optional[str] = ..., service_switch_availability_status: _Optional[_Union[_service_switch_availability_status_pb2.ServiceSwitchAvailabilityStatus, str]] = ..., enriched_target_info: _Optional[_Iterable[_Union[_enriched_target_info_pb2.EnrichedTargetInfo, _Mapping]]] = ..., service_state: _Optional[_Union[_extra_service_state_pb2.ExtraServiceState.Active, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "not_found_active_mandatory_service")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        NOT_FOUND_ACTIVE_MANDATORY_SERVICE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        not_found_active_mandatory_service: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., not_found_active_mandatory_service: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetActiveServicesResponse.Success
    failure: GetActiveServicesResponse.Failure
    def __init__(self, success: _Optional[_Union[GetActiveServicesResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[GetActiveServicesResponse.Failure, _Mapping]] = ...) -> None: ...
