from systems.ajax.api.mobile.v2.common.image import image_id_pb2 as _image_id_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateAccountProfileRequest(_message.Message):
    __slots__ = ("first_name", "last_name", "locale", "image")
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    locale: str
    image: _image_id_pb2.ImageIdValue
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., locale: _Optional[str] = ..., image: _Optional[_Union[_image_id_pb2.ImageIdValue, _Mapping]] = ...) -> None: ...
