from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USER: _ClassVar[UserRole]
    PRO: _ClassVar[UserRole]
    COMPANY: _ClassVar[UserRole]
USER: UserRole
PRO: UserRole
COMPANY: UserRole

class LoginRequest(_message.Message):
    __slots__ = ("login", "password", "user_role")
    LOGIN_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    USER_ROLE_FIELD_NUMBER: _ClassVar[int]
    login: str
    password: str
    user_role: UserRole
    def __init__(self, login: _Optional[str] = ..., password: _Optional[str] = ..., user_role: _Optional[_Union[UserRole, str]] = ...) -> None: ...

class LoginResponse(_message.Message):
    __slots__ = ("user_id", "user_role", "email", "first_name", "last_name", "phone_number")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ROLE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    user_role: UserRole
    email: str
    first_name: str
    last_name: str
    phone_number: str
    def __init__(self, user_id: _Optional[str] = ..., user_role: _Optional[_Union[UserRole, str]] = ..., email: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., phone_number: _Optional[str] = ...) -> None: ...
