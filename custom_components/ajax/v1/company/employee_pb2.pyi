from v1.common import role_pb2 as _role_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Employee(_message.Message):
    __slots__ = ()
    class ComplexRole(_message.Message):
        __slots__ = ("roles",)
        ROLES_FIELD_NUMBER: _ClassVar[int]
        roles: _containers.RepeatedScalarFieldContainer[_role_pb2.Role]
        def __init__(self, roles: _Optional[_Iterable[_Union[_role_pb2.Role, str]]] = ...) -> None: ...
    class EmployeeInfo(_message.Message):
        __slots__ = ("employee_id", "first_name", "last_name", "role", "photo_id", "cluster_company_id")
        EMPLOYEE_ID_FIELD_NUMBER: _ClassVar[int]
        FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
        LAST_NAME_FIELD_NUMBER: _ClassVar[int]
        ROLE_FIELD_NUMBER: _ClassVar[int]
        PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
        employee_id: str
        first_name: str
        last_name: str
        role: Employee.ComplexRole
        photo_id: str
        cluster_company_id: str
        def __init__(self, employee_id: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., role: _Optional[_Union[Employee.ComplexRole, _Mapping]] = ..., photo_id: _Optional[str] = ..., cluster_company_id: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...
