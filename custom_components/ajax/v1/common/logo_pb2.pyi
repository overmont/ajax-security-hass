from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Logo(_message.Message):
    __slots__ = ("image_id", "images")
    class Image(_message.Message):
        __slots__ = ("resolution", "url")
        RESOLUTION_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        resolution: str
        url: str
        def __init__(self, resolution: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
    IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    image_id: str
    images: _containers.RepeatedCompositeFieldContainer[Logo.Image]
    def __init__(self, image_id: _Optional[str] = ..., images: _Optional[_Iterable[_Union[Logo.Image, _Mapping]]] = ...) -> None: ...
