from v3.mobilegwsvc.commonmodels.type import user_role_pb2 as _user_role_pb2
from v3.mobilegwsvc.commonmodels.type import phone_validation_type_pb2 as _phone_validation_type_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResendConfirmationCodesRequest(_message.Message):
    __slots__ = ("user_role", "email", "phone_number", "phone_validation_type")
    USER_ROLE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PHONE_VALIDATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    user_role: _user_role_pb2.UserRole
    email: str
    phone_number: str
    phone_validation_type: _phone_validation_type_pb2.PhoneValidationType
    def __init__(self, user_role: _Optional[_Union[_user_role_pb2.UserRole, str]] = ..., email: _Optional[str] = ..., phone_number: _Optional[str] = ..., phone_validation_type: _Optional[_Union[_phone_validation_type_pb2.PhoneValidationType, str]] = ...) -> None: ...
