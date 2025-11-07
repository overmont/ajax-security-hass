from systems.ajax.api.mobile.v2.common.accounting import service_type_pb2 as _service_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccountingCompany(_message.Message):
    __slots__ = ("companyHexId", "name", "service_type", "details")
    COMPANYHEXID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    companyHexId: str
    name: str
    service_type: _service_type_pb2.ServiceType
    details: CompanyDetails
    def __init__(self, companyHexId: _Optional[str] = ..., name: _Optional[str] = ..., service_type: _Optional[_Union[_service_type_pb2.ServiceType, str]] = ..., details: _Optional[_Union[CompanyDetails, _Mapping]] = ...) -> None: ...

class CompanyContact(_message.Message):
    __slots__ = ("phone_number", "description")
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    phone_number: str
    description: str
    def __init__(self, phone_number: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class CompanyDetails(_message.Message):
    __slots__ = ("web_site_url", "contacts", "emails", "logo_url")
    WEB_SITE_URL_FIELD_NUMBER: _ClassVar[int]
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    EMAILS_FIELD_NUMBER: _ClassVar[int]
    LOGO_URL_FIELD_NUMBER: _ClassVar[int]
    web_site_url: str
    contacts: _containers.RepeatedCompositeFieldContainer[CompanyContact]
    emails: _containers.RepeatedScalarFieldContainer[str]
    logo_url: str
    def __init__(self, web_site_url: _Optional[str] = ..., contacts: _Optional[_Iterable[_Union[CompanyContact, _Mapping]]] = ..., emails: _Optional[_Iterable[str]] = ..., logo_url: _Optional[str] = ...) -> None: ...
