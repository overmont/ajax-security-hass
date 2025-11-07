from systems.ajax.api.mobile.v2.common.image import image_pb2 as _image_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Account(_message.Message):
    __slots__ = ("user_hex_id", "first_name", "last_name", "locale", "email", "phone", "images", "end_user_agreement_version", "privacy_policy_version", "privacy_notice_version")
    USER_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    END_USER_AGREEMENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_NOTICE_VERSION_FIELD_NUMBER: _ClassVar[int]
    user_hex_id: str
    first_name: str
    last_name: str
    locale: str
    email: str
    phone: str
    images: _image_pb2.Images
    end_user_agreement_version: int
    privacy_policy_version: int
    privacy_notice_version: int
    def __init__(self, user_hex_id: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., locale: _Optional[str] = ..., email: _Optional[str] = ..., phone: _Optional[str] = ..., images: _Optional[_Union[_image_pb2.Images, _Mapping]] = ..., end_user_agreement_version: _Optional[int] = ..., privacy_policy_version: _Optional[int] = ..., privacy_notice_version: _Optional[int] = ...) -> None: ...
