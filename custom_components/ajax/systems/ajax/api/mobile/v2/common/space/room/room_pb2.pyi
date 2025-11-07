from systems.ajax.api.mobile.v2.common.image import image_pb2 as _image_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Room(_message.Message):
    __slots__ = ("id", "name", "images", "sorting_key")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    SORTING_KEY_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    images: _image_pb2.Images
    sorting_key: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., images: _Optional[_Union[_image_pb2.Images, _Mapping]] = ..., sorting_key: _Optional[str] = ...) -> None: ...
