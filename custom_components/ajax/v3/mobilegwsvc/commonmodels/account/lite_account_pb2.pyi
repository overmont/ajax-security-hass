from v3.mobilegwsvc.commonmodels.type import user_role_pb2 as _user_role_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LiteAccount(_message.Message):
    __slots__ = ("user_hex_id", "user_role", "first_name", "last_name", "locale", "end_user_agreement_version", "privacy_policy_version", "email", "privacy_notice_version")
    USER_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ROLE_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    END_USER_AGREEMENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_NOTICE_VERSION_FIELD_NUMBER: _ClassVar[int]
    user_hex_id: str
    user_role: _user_role_pb2.UserRole
    first_name: str
    last_name: str
    locale: str
    end_user_agreement_version: int
    privacy_policy_version: int
    email: str
    privacy_notice_version: int
    def __init__(self, user_hex_id: _Optional[str] = ..., user_role: _Optional[_Union[_user_role_pb2.UserRole, str]] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., locale: _Optional[str] = ..., end_user_agreement_version: _Optional[int] = ..., privacy_policy_version: _Optional[int] = ..., email: _Optional[str] = ..., privacy_notice_version: _Optional[int] = ...) -> None: ...
