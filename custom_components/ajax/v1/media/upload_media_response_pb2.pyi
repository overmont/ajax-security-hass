from v1.common import image_pb2 as _image_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UploadMediaResponse(_message.Message):
    __slots__ = ("image_id", "images", "expiration_time")
    IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    image_id: str
    images: _containers.RepeatedCompositeFieldContainer[_image_pb2.Image]
    expiration_time: _timestamp_pb2.Timestamp
    def __init__(self, image_id: _Optional[str] = ..., images: _Optional[_Iterable[_Union[_image_pb2.Image, _Mapping]]] = ..., expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
