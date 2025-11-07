from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Image(_message.Message):
    __slots__ = ("url", "resolution")
    class Resolution(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESOLUTION_UNSPECIFIED: _ClassVar[Image.Resolution]
        _300x300: _ClassVar[Image.Resolution]
        _128x128: _ClassVar[Image.Resolution]
        _64x64: _ClassVar[Image.Resolution]
        _100x100: _ClassVar[Image.Resolution]
        _200x200: _ClassVar[Image.Resolution]
    RESOLUTION_UNSPECIFIED: Image.Resolution
    _300x300: Image.Resolution
    _128x128: Image.Resolution
    _64x64: Image.Resolution
    _100x100: Image.Resolution
    _200x200: Image.Resolution
    URL_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    url: str
    resolution: Image.Resolution
    def __init__(self, url: _Optional[str] = ..., resolution: _Optional[_Union[Image.Resolution, str]] = ...) -> None: ...

class Images(_message.Message):
    __slots__ = ("images", "image_id")
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    images: _containers.RepeatedCompositeFieldContainer[Image]
    image_id: str
    def __init__(self, images: _Optional[_Iterable[_Union[Image, _Mapping]]] = ..., image_id: _Optional[str] = ...) -> None: ...
