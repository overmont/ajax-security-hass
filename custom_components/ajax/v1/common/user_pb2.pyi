from v1.common import email_address_pb2 as _email_address_pb2
from v1.common import phone_number_pb2 as _phone_number_pb2
from v1.common import image_urls_pb2 as _image_urls_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ("id", "first_name", "last_name", "email", "phone", "image_urls")
    ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URLS_FIELD_NUMBER: _ClassVar[int]
    id: str
    first_name: str
    last_name: str
    email: _email_address_pb2.EmailAddress
    phone: _phone_number_pb2.PhoneNumber
    image_urls: _image_urls_pb2.ImageUrls
    def __init__(self, id: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., email: _Optional[_Union[_email_address_pb2.EmailAddress, _Mapping]] = ..., phone: _Optional[_Union[_phone_number_pb2.PhoneNumber, _Mapping]] = ..., image_urls: _Optional[_Union[_image_urls_pb2.ImageUrls, _Mapping]] = ...) -> None: ...
