from v3.mobilegwsvc.commonmodels.type import user_role_pb2 as _user_role_pb2
from v3.mobilegwsvc.commonmodels.type import phone_validation_type_pb2 as _phone_validation_type_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StartRegistrationRequest(_message.Message):
    __slots__ = ("user_role", "email", "phone_number", "first_name", "last_name", "password", "phone_validation_type", "locale", "news_subscription", "recaptcha_token", "recaptcha_site_key", "company_website", "company_name")
    USER_ROLE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PHONE_VALIDATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NEWS_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RECAPTCHA_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RECAPTCHA_SITE_KEY_FIELD_NUMBER: _ClassVar[int]
    COMPANY_WEBSITE_FIELD_NUMBER: _ClassVar[int]
    COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
    user_role: _user_role_pb2.UserRole
    email: str
    phone_number: str
    first_name: str
    last_name: str
    password: str
    phone_validation_type: _phone_validation_type_pb2.PhoneValidationType
    locale: str
    news_subscription: bool
    recaptcha_token: str
    recaptcha_site_key: str
    company_website: str
    company_name: str
    def __init__(self, user_role: _Optional[_Union[_user_role_pb2.UserRole, str]] = ..., email: _Optional[str] = ..., phone_number: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., password: _Optional[str] = ..., phone_validation_type: _Optional[_Union[_phone_validation_type_pb2.PhoneValidationType, str]] = ..., locale: _Optional[str] = ..., news_subscription: bool = ..., recaptcha_token: _Optional[str] = ..., recaptcha_site_key: _Optional[str] = ..., company_website: _Optional[str] = ..., company_name: _Optional[str] = ...) -> None: ...
