from systems.ajax.api.mobile.v2.common.image import image_pb2 as _image_pb2
from systems.ajax.api.mobile.v2.common.space.company import company_billing_info_pb2 as _company_billing_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BillingCompany(_message.Message):
    __slots__ = ("company_logo", "company_name", "company_billing_info")
    COMPANY_LOGO_FIELD_NUMBER: _ClassVar[int]
    COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPANY_BILLING_INFO_FIELD_NUMBER: _ClassVar[int]
    company_logo: _image_pb2.Images
    company_name: str
    company_billing_info: _company_billing_info_pb2.CompanyBillingInfo
    def __init__(self, company_logo: _Optional[_Union[_image_pb2.Images, _Mapping]] = ..., company_name: _Optional[str] = ..., company_billing_info: _Optional[_Union[_company_billing_info_pb2.CompanyBillingInfo, _Mapping]] = ...) -> None: ...
