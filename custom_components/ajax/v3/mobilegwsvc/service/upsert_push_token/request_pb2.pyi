from v3.mobilegwsvc.commonmodels.type import user_role_pb2 as _user_role_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PushTokenType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PUSH_TOKEN_TYPE_UNSPECIFIED: _ClassVar[PushTokenType]
    PUSH_TOKEN_TYPE_IOS_REGULAR: _ClassVar[PushTokenType]
    PUSH_TOKEN_TYPE_IOS_REGULAR_CRITICAL: _ClassVar[PushTokenType]
    PUSH_TOKEN_TYPE_IOS_SANDBOX: _ClassVar[PushTokenType]
    PUSH_TOKEN_TYPE_IOS_SANDBOX_CRITICAL: _ClassVar[PushTokenType]
    PUSH_TOKEN_TYPE_AOS_FCM: _ClassVar[PushTokenType]
    PUSH_TOKEN_TYPE_IOS_REGULAR_CRITICAL_MUTABLE: _ClassVar[PushTokenType]
    PUSH_TOKEN_TYPE_IOS_SANDBOX_CRITICAL_MUTABLE: _ClassVar[PushTokenType]
    PUSH_TOKEN_TYPE_APPLE_WATCH_REGULAR: _ClassVar[PushTokenType]
    PUSH_TOKEN_TYPE_APPLE_WATCH_REGULAR_SANDBOX: _ClassVar[PushTokenType]
PUSH_TOKEN_TYPE_UNSPECIFIED: PushTokenType
PUSH_TOKEN_TYPE_IOS_REGULAR: PushTokenType
PUSH_TOKEN_TYPE_IOS_REGULAR_CRITICAL: PushTokenType
PUSH_TOKEN_TYPE_IOS_SANDBOX: PushTokenType
PUSH_TOKEN_TYPE_IOS_SANDBOX_CRITICAL: PushTokenType
PUSH_TOKEN_TYPE_AOS_FCM: PushTokenType
PUSH_TOKEN_TYPE_IOS_REGULAR_CRITICAL_MUTABLE: PushTokenType
PUSH_TOKEN_TYPE_IOS_SANDBOX_CRITICAL_MUTABLE: PushTokenType
PUSH_TOKEN_TYPE_APPLE_WATCH_REGULAR: PushTokenType
PUSH_TOKEN_TYPE_APPLE_WATCH_REGULAR_SANDBOX: PushTokenType

class UpsertPushTokenRequest(_message.Message):
    __slots__ = ("user_hex_id", "user_role", "push_token", "push_token_type", "voip_push_token")
    USER_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ROLE_FIELD_NUMBER: _ClassVar[int]
    PUSH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PUSH_TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    VOIP_PUSH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    user_hex_id: str
    user_role: _user_role_pb2.UserRole
    push_token: str
    push_token_type: PushTokenType
    voip_push_token: str
    def __init__(self, user_hex_id: _Optional[str] = ..., user_role: _Optional[_Union[_user_role_pb2.UserRole, str]] = ..., push_token: _Optional[str] = ..., push_token_type: _Optional[_Union[PushTokenType, str]] = ..., voip_push_token: _Optional[str] = ...) -> None: ...
