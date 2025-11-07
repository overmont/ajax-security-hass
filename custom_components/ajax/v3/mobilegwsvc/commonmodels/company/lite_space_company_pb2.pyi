from systems.ajax.api.mobile.v2.hubobject.model.company import company_info_pb2 as _company_info_pb2
from v3.mobilegwsvc.commonmodels.company import company_provided_service_pb2 as _company_provided_service_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LiteSpaceCompany(_message.Message):
    __slots__ = ("company_info", "space_member_id", "hub_user_index", "sorting_key", "company_provided_services")
    COMPANY_INFO_FIELD_NUMBER: _ClassVar[int]
    SPACE_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    HUB_USER_INDEX_FIELD_NUMBER: _ClassVar[int]
    SORTING_KEY_FIELD_NUMBER: _ClassVar[int]
    COMPANY_PROVIDED_SERVICES_FIELD_NUMBER: _ClassVar[int]
    company_info: _company_info_pb2.CompanyInfo
    space_member_id: str
    hub_user_index: int
    sorting_key: str
    company_provided_services: _containers.RepeatedScalarFieldContainer[_company_provided_service_pb2.CompanyProvidedService]
    def __init__(self, company_info: _Optional[_Union[_company_info_pb2.CompanyInfo, _Mapping]] = ..., space_member_id: _Optional[str] = ..., hub_user_index: _Optional[int] = ..., sorting_key: _Optional[str] = ..., company_provided_services: _Optional[_Iterable[_Union[_company_provided_service_pb2.CompanyProvidedService, str]]] = ...) -> None: ...
