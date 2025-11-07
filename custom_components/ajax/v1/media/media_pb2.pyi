from v1.common import image_pb2 as _image_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Media(_message.Message):
    __slots__ = ("info", "images")
    class Info(_message.Message):
        __slots__ = ("id", "facility_id", "image_id", "caption", "category")
        class Category(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ROAD_MAP: _ClassVar[Media.Info.Category]
            FLOOR_PLAN: _ClassVar[Media.Info.Category]
        ROAD_MAP: Media.Info.Category
        FLOOR_PLAN: Media.Info.Category
        ID_FIELD_NUMBER: _ClassVar[int]
        FACILITY_ID_FIELD_NUMBER: _ClassVar[int]
        IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
        CAPTION_FIELD_NUMBER: _ClassVar[int]
        CATEGORY_FIELD_NUMBER: _ClassVar[int]
        id: str
        facility_id: str
        image_id: str
        caption: str
        category: Media.Info.Category
        def __init__(self, id: _Optional[str] = ..., facility_id: _Optional[str] = ..., image_id: _Optional[str] = ..., caption: _Optional[str] = ..., category: _Optional[_Union[Media.Info.Category, str]] = ...) -> None: ...
    INFO_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    info: Media.Info
    images: _containers.RepeatedCompositeFieldContainer[_image_pb2.Image]
    def __init__(self, info: _Optional[_Union[Media.Info, _Mapping]] = ..., images: _Optional[_Iterable[_Union[_image_pb2.Image, _Mapping]]] = ...) -> None: ...
