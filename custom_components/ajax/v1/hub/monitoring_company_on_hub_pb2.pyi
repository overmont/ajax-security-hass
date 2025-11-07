from v1.common import phone_number_pb2 as _phone_number_pb2
from v1.common import email_address_pb2 as _email_address_pb2
from v1.common import logo_pb2 as _logo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MonitoringCompanyStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NO_STATE: _ClassVar[MonitoringCompanyStatus]
    PENDING_APPROVAL: _ClassVar[MonitoringCompanyStatus]
    APPROVED: _ClassVar[MonitoringCompanyStatus]
    IN_SLEEP_MODE: _ClassVar[MonitoringCompanyStatus]
NO_STATE: MonitoringCompanyStatus
PENDING_APPROVAL: MonitoringCompanyStatus
APPROVED: MonitoringCompanyStatus
IN_SLEEP_MODE: MonitoringCompanyStatus

class MonitoringCompanyOnHub(_message.Message):
    __slots__ = ("company_hex_id", "name", "logo", "web_site_url", "phone_numbers", "customer_inquiries_emails", "country_code", "locations", "monitoring_status")
    COMPANY_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    WEB_SITE_URL_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_INQUIRIES_EMAILS_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    MONITORING_STATUS_FIELD_NUMBER: _ClassVar[int]
    company_hex_id: str
    name: str
    logo: _logo_pb2.Logo
    web_site_url: str
    phone_numbers: _containers.RepeatedCompositeFieldContainer[_phone_number_pb2.PhoneNumber]
    customer_inquiries_emails: _containers.RepeatedCompositeFieldContainer[_email_address_pb2.EmailAddress]
    country_code: str
    locations: _containers.RepeatedScalarFieldContainer[str]
    monitoring_status: MonitoringCompanyStatus
    def __init__(self, company_hex_id: _Optional[str] = ..., name: _Optional[str] = ..., logo: _Optional[_Union[_logo_pb2.Logo, _Mapping]] = ..., web_site_url: _Optional[str] = ..., phone_numbers: _Optional[_Iterable[_Union[_phone_number_pb2.PhoneNumber, _Mapping]]] = ..., customer_inquiries_emails: _Optional[_Iterable[_Union[_email_address_pb2.EmailAddress, _Mapping]]] = ..., country_code: _Optional[str] = ..., locations: _Optional[_Iterable[str]] = ..., monitoring_status: _Optional[_Union[MonitoringCompanyStatus, str]] = ...) -> None: ...
