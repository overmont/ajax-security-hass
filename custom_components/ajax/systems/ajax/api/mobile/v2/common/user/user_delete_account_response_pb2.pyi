from systems.ajax.api.mobile.v2.common.user import user_can_be_deleted_response_pb2 as _user_can_be_deleted_response_pb2
from systems.ajax.api.mobile.v2.common.user import user_is_owner_of_company_pb2 as _user_is_owner_of_company_pb2
from systems.ajax.api.mobile.v2.common.user import user_is_employee_of_company_pb2 as _user_is_employee_of_company_pb2
from systems.ajax.api.mobile.v2.common.company import short_company_pb2 as _short_company_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserDeleteAccountResponse(_message.Message):
    __slots__ = ("company_list", "company_removal_required")
    class CompanyRemovalRequired(_message.Message):
        __slots__ = ("user_can_be_deleted_response", "user_is_owner_of_company", "user_is_employee_of_company")
        USER_CAN_BE_DELETED_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        USER_IS_OWNER_OF_COMPANY_FIELD_NUMBER: _ClassVar[int]
        USER_IS_EMPLOYEE_OF_COMPANY_FIELD_NUMBER: _ClassVar[int]
        user_can_be_deleted_response: _user_can_be_deleted_response_pb2.UserCanBeDeletedResponse
        user_is_owner_of_company: _user_is_owner_of_company_pb2.UserIsOwnerOfCompany
        user_is_employee_of_company: _user_is_employee_of_company_pb2.UserIsEmployeeOfCompany
        def __init__(self, user_can_be_deleted_response: _Optional[_Union[_user_can_be_deleted_response_pb2.UserCanBeDeletedResponse, _Mapping]] = ..., user_is_owner_of_company: _Optional[_Union[_user_is_owner_of_company_pb2.UserIsOwnerOfCompany, _Mapping]] = ..., user_is_employee_of_company: _Optional[_Union[_user_is_employee_of_company_pb2.UserIsEmployeeOfCompany, _Mapping]] = ...) -> None: ...
    class CompanyList(_message.Message):
        __slots__ = ("short_company",)
        SHORT_COMPANY_FIELD_NUMBER: _ClassVar[int]
        short_company: _containers.RepeatedCompositeFieldContainer[_short_company_pb2.ShortCompany]
        def __init__(self, short_company: _Optional[_Iterable[_Union[_short_company_pb2.ShortCompany, _Mapping]]] = ...) -> None: ...
    COMPANY_LIST_FIELD_NUMBER: _ClassVar[int]
    COMPANY_REMOVAL_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    company_list: UserDeleteAccountResponse.CompanyList
    company_removal_required: UserDeleteAccountResponse.CompanyRemovalRequired
    def __init__(self, company_list: _Optional[_Union[UserDeleteAccountResponse.CompanyList, _Mapping]] = ..., company_removal_required: _Optional[_Union[UserDeleteAccountResponse.CompanyRemovalRequired, _Mapping]] = ...) -> None: ...
