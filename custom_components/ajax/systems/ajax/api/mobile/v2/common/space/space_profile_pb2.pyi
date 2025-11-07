from systems.ajax.api.mobile.v2.common.image import image_pb2 as _image_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceProfile(_message.Message):
    __slots__ = ("name", "images")
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    name: str
    images: _image_pb2.Images
    def __init__(self, name: _Optional[str] = ..., images: _Optional[_Union[_image_pb2.Images, _Mapping]] = ...) -> None: ...
