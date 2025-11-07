from systems.ajax.api.mobile.v2.hubobject.model.company import company_info_pb2 as _company_info_pb2
from systems.ajax.api.mobile.v2.common.space.company import company_billing_info_pb2 as _company_billing_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceCobrandedCompany(_message.Message):
    __slots__ = ("company_info", "company_billing_info")
    COMPANY_INFO_FIELD_NUMBER: _ClassVar[int]
    COMPANY_BILLING_INFO_FIELD_NUMBER: _ClassVar[int]
    company_info: _company_info_pb2.CompanyInfo
    company_billing_info: _company_billing_info_pb2.CompanyBillingInfo
    def __init__(self, company_info: _Optional[_Union[_company_info_pb2.CompanyInfo, _Mapping]] = ..., company_billing_info: _Optional[_Union[_company_billing_info_pb2.CompanyBillingInfo, _Mapping]] = ...) -> None: ...
