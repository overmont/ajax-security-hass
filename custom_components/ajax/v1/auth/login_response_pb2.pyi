from v1.user import user_company_pb2 as _user_company_pb2
from v1.user import user_info_pb2 as _user_info_pb2
from v1.company import employee_pb2 as _employee_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoginResponse(_message.Message):
    __slots__ = ("user_id", "session_token", "company_id", "employee_info", "user_companies", "user_info")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    EMPLOYEE_INFO_FIELD_NUMBER: _ClassVar[int]
    USER_COMPANIES_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    session_token: str
    company_id: str
    employee_info: _employee_pb2.Employee.EmployeeInfo
    user_companies: _containers.RepeatedCompositeFieldContainer[_user_company_pb2.UserCompany]
    user_info: _user_info_pb2.UserInfo
    def __init__(self, user_id: _Optional[str] = ..., session_token: _Optional[str] = ..., company_id: _Optional[str] = ..., employee_info: _Optional[_Union[_employee_pb2.Employee.EmployeeInfo, _Mapping]] = ..., user_companies: _Optional[_Iterable[_Union[_user_company_pb2.UserCompany, _Mapping]]] = ..., user_info: _Optional[_Union[_user_info_pb2.UserInfo, _Mapping]] = ...) -> None: ...
