from v1.common import image_urls_pb2 as _image_urls_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserInfo(_message.Message):
    __slots__ = ("first_name", "last_name", "locale", "email", "phone", "image_urls", "cluster_user_id", "end_user_agreement_version", "privacy_policy_version")
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URLS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_USER_ID_FIELD_NUMBER: _ClassVar[int]
    END_USER_AGREEMENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    locale: str
    email: str
    phone: str
    image_urls: _image_urls_pb2.ImageUrls
    cluster_user_id: str
    end_user_agreement_version: int
    privacy_policy_version: int
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., locale: _Optional[str] = ..., email: _Optional[str] = ..., phone: _Optional[str] = ..., image_urls: _Optional[_Union[_image_urls_pb2.ImageUrls, _Mapping]] = ..., cluster_user_id: _Optional[str] = ..., end_user_agreement_version: _Optional[int] = ..., privacy_policy_version: _Optional[int] = ...) -> None: ...
