from systems.ajax.api.mobile.v2.common.accounting import accounting_company_pb2 as _accounting_company_pb2
from systems.ajax.api.mobile.v2.common.image import image_pb2 as _image_pb2
from v3.mobilegwsvc.commonmodels.type import user_role_pb2 as _user_role_pb2
from systems.ajax.api.mobile.v2.hubobject.model.company import company_info_pb2 as _company_info_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionOwner(_message.Message):
    __slots__ = ("user", "company", "accounting_company")
    class User(_message.Message):
        __slots__ = ("user_hex_id", "first_name", "last_name", "images", "user_role")
        USER_HEX_ID_FIELD_NUMBER: _ClassVar[int]
        FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
        LAST_NAME_FIELD_NUMBER: _ClassVar[int]
        IMAGES_FIELD_NUMBER: _ClassVar[int]
        USER_ROLE_FIELD_NUMBER: _ClassVar[int]
        user_hex_id: str
        first_name: str
        last_name: str
        images: _image_pb2.Images
        user_role: _user_role_pb2.UserRole
        def __init__(self, user_hex_id: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., images: _Optional[_Union[_image_pb2.Images, _Mapping]] = ..., user_role: _Optional[_Union[_user_role_pb2.UserRole, str]] = ...) -> None: ...
    USER_FIELD_NUMBER: _ClassVar[int]
    COMPANY_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTING_COMPANY_FIELD_NUMBER: _ClassVar[int]
    user: SubscriptionOwner.User
    company: _company_info_pb2.CompanyInfo
    accounting_company: _accounting_company_pb2.AccountingCompany
    def __init__(self, user: _Optional[_Union[SubscriptionOwner.User, _Mapping]] = ..., company: _Optional[_Union[_company_info_pb2.CompanyInfo, _Mapping]] = ..., accounting_company: _Optional[_Union[_accounting_company_pb2.AccountingCompany, _Mapping]] = ...) -> None: ...
