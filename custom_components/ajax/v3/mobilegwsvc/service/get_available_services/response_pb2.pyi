from v3.mobilegwsvc.commonmodels.accounting import service_pb2 as _service_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.type import user_role_pb2 as _user_role_pb2
from v3.mobilegwsvc.commonmodels.accounting import reseller_pb2 as _reseller_pb2
from systems.ajax.api.mobile.v2.common.accounting import accounting_company_pb2 as _accounting_company_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAvailableServicesResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("available_services", "ungrouped_available_services_list", "available_service_groups_list")
        AVAILABLE_SERVICES_FIELD_NUMBER: _ClassVar[int]
        UNGROUPED_AVAILABLE_SERVICES_LIST_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_SERVICE_GROUPS_LIST_FIELD_NUMBER: _ClassVar[int]
        available_services: _containers.RepeatedCompositeFieldContainer[GetAvailableServicesResponse.AvailableService]
        ungrouped_available_services_list: GetAvailableServicesResponse.AvailableServicesList
        available_service_groups_list: GetAvailableServicesResponse.AvailableServiceGroupsList
        def __init__(self, available_services: _Optional[_Iterable[_Union[GetAvailableServicesResponse.AvailableService, _Mapping]]] = ..., ungrouped_available_services_list: _Optional[_Union[GetAvailableServicesResponse.AvailableServicesList, _Mapping]] = ..., available_service_groups_list: _Optional[_Union[GetAvailableServicesResponse.AvailableServiceGroupsList, _Mapping]] = ...) -> None: ...
    class AvailableServicesList(_message.Message):
        __slots__ = ("ungrouped_available_services",)
        UNGROUPED_AVAILABLE_SERVICES_FIELD_NUMBER: _ClassVar[int]
        ungrouped_available_services: _containers.RepeatedCompositeFieldContainer[GetAvailableServicesResponse.AvailableService]
        def __init__(self, ungrouped_available_services: _Optional[_Iterable[_Union[GetAvailableServicesResponse.AvailableService, _Mapping]]] = ...) -> None: ...
    class AvailableServiceGroupsList(_message.Message):
        __slots__ = ("available_service_groups",)
        AVAILABLE_SERVICE_GROUPS_FIELD_NUMBER: _ClassVar[int]
        available_service_groups: _containers.RepeatedCompositeFieldContainer[GetAvailableServicesResponse.AvailableServicesGroup]
        def __init__(self, available_service_groups: _Optional[_Iterable[_Union[GetAvailableServicesResponse.AvailableServicesGroup, _Mapping]]] = ...) -> None: ...
    class AvailableService(_message.Message):
        __slots__ = ("service", "resellers", "reseller_infos")
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        RESELLERS_FIELD_NUMBER: _ClassVar[int]
        RESELLER_INFOS_FIELD_NUMBER: _ClassVar[int]
        service: _service_pb2.Service
        resellers: _containers.RepeatedCompositeFieldContainer[_accounting_company_pb2.AccountingCompany]
        reseller_infos: _containers.RepeatedCompositeFieldContainer[_reseller_pb2.Reseller]
        def __init__(self, service: _Optional[_Union[_service_pb2.Service, _Mapping]] = ..., resellers: _Optional[_Iterable[_Union[_accounting_company_pb2.AccountingCompany, _Mapping]]] = ..., reseller_infos: _Optional[_Iterable[_Union[_reseller_pb2.Reseller, _Mapping]]] = ...) -> None: ...
    class AvailableServicesGroup(_message.Message):
        __slots__ = ("id", "name", "lokalise_id", "item", "order")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        LOKALISE_ID_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        ORDER_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        lokalise_id: str
        item: _containers.RepeatedCompositeFieldContainer[GetAvailableServicesResponse.AvailableServicesGroupItem]
        order: int
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., lokalise_id: _Optional[str] = ..., item: _Optional[_Iterable[_Union[GetAvailableServicesResponse.AvailableServicesGroupItem, _Mapping]]] = ..., order: _Optional[int] = ...) -> None: ...
    class AvailableServicesGroupItem(_message.Message):
        __slots__ = ("order", "service")
        ORDER_FIELD_NUMBER: _ClassVar[int]
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        order: int
        service: GetAvailableServicesResponse.AvailableService
        def __init__(self, order: _Optional[int] = ..., service: _Optional[_Union[GetAvailableServicesResponse.AvailableService, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "available_mandatory_service_not_found", "reseller_not_found", "dealer_not_found", "not_available_for_user")
        class NotAvailableForUserError(_message.Message):
            __slots__ = ("user_role",)
            USER_ROLE_FIELD_NUMBER: _ClassVar[int]
            user_role: _user_role_pb2.UserRole
            def __init__(self, user_role: _Optional[_Union[_user_role_pb2.UserRole, str]] = ...) -> None: ...
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_MANDATORY_SERVICE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        RESELLER_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        DEALER_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        NOT_AVAILABLE_FOR_USER_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        available_mandatory_service_not_found: _response_pb2.Error
        reseller_not_found: _response_pb2.Error
        dealer_not_found: _response_pb2.Error
        not_available_for_user: GetAvailableServicesResponse.Failure.NotAvailableForUserError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., available_mandatory_service_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., reseller_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., dealer_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., not_available_for_user: _Optional[_Union[GetAvailableServicesResponse.Failure.NotAvailableForUserError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetAvailableServicesResponse.Success
    failure: GetAvailableServicesResponse.Failure
    def __init__(self, success: _Optional[_Union[GetAvailableServicesResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[GetAvailableServicesResponse.Failure, _Mapping]] = ...) -> None: ...
