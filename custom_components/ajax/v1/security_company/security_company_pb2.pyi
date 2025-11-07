from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SecurityCompanyStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NO_STATE: _ClassVar[SecurityCompanyStatus]
    PENDING_APPROVAL: _ClassVar[SecurityCompanyStatus]
    APPROVED: _ClassVar[SecurityCompanyStatus]
    PENDING_REMOVAL: _ClassVar[SecurityCompanyStatus]
NO_STATE: SecurityCompanyStatus
PENDING_APPROVAL: SecurityCompanyStatus
APPROVED: SecurityCompanyStatus
PENDING_REMOVAL: SecurityCompanyStatus

class SecurityCompany(_message.Message):
    __slots__ = ("data", "details")
    DATA_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    data: SecurityCompanyData
    details: SecurityCompanyDetails
    def __init__(self, data: _Optional[_Union[SecurityCompanyData, _Mapping]] = ..., details: _Optional[_Union[SecurityCompanyDetails, _Mapping]] = ...) -> None: ...

class SecurityCompanyPreview(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: SecurityCompanyData
    def __init__(self, data: _Optional[_Union[SecurityCompanyData, _Mapping]] = ...) -> None: ...

class SecurityCompanyData(_message.Message):
    __slots__ = ("id", "name", "logo_url", "monitoring_status", "hub_user_index", "account_number_required_status")
    class AccountNumberRequiredStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACCOUNT_NUMBER_REQUIRED_STATUS_UNSPECIFIED: _ClassVar[SecurityCompanyData.AccountNumberRequiredStatus]
        ACCOUNT_NUMBER_REQUIRED_STATUS_REQUIRED: _ClassVar[SecurityCompanyData.AccountNumberRequiredStatus]
        ACCOUNT_NUMBER_REQUIRED_STATUS_NOT_REQUIRED: _ClassVar[SecurityCompanyData.AccountNumberRequiredStatus]
    ACCOUNT_NUMBER_REQUIRED_STATUS_UNSPECIFIED: SecurityCompanyData.AccountNumberRequiredStatus
    ACCOUNT_NUMBER_REQUIRED_STATUS_REQUIRED: SecurityCompanyData.AccountNumberRequiredStatus
    ACCOUNT_NUMBER_REQUIRED_STATUS_NOT_REQUIRED: SecurityCompanyData.AccountNumberRequiredStatus
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOGO_URL_FIELD_NUMBER: _ClassVar[int]
    MONITORING_STATUS_FIELD_NUMBER: _ClassVar[int]
    HUB_USER_INDEX_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NUMBER_REQUIRED_STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    logo_url: str
    monitoring_status: SecurityCompanyStatus
    hub_user_index: int
    account_number_required_status: SecurityCompanyData.AccountNumberRequiredStatus
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., logo_url: _Optional[str] = ..., monitoring_status: _Optional[_Union[SecurityCompanyStatus, str]] = ..., hub_user_index: _Optional[int] = ..., account_number_required_status: _Optional[_Union[SecurityCompanyData.AccountNumberRequiredStatus, str]] = ...) -> None: ...

class SecurityCompanyContact(_message.Message):
    __slots__ = ("phone_number", "description")
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    phone_number: str
    description: str
    def __init__(self, phone_number: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class SecurityCompanyLocation(_message.Message):
    __slots__ = ("country_code",)
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    country_code: str
    def __init__(self, country_code: _Optional[str] = ...) -> None: ...

class SecurityCompanyDetails(_message.Message):
    __slots__ = ("web_site_url", "description", "locations", "contacts", "emails")
    WEB_SITE_URL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    EMAILS_FIELD_NUMBER: _ClassVar[int]
    web_site_url: str
    description: str
    locations: _containers.RepeatedCompositeFieldContainer[SecurityCompanyLocation]
    contacts: _containers.RepeatedCompositeFieldContainer[SecurityCompanyContact]
    emails: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, web_site_url: _Optional[str] = ..., description: _Optional[str] = ..., locations: _Optional[_Iterable[_Union[SecurityCompanyLocation, _Mapping]]] = ..., contacts: _Optional[_Iterable[_Union[SecurityCompanyContact, _Mapping]]] = ..., emails: _Optional[_Iterable[str]] = ...) -> None: ...
