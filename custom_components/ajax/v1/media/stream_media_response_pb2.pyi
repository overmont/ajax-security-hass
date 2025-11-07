from v1.media import media_pb2 as _media_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamMediaResponse(_message.Message):
    __slots__ = ("media",)
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    media: _containers.RepeatedCompositeFieldContainer[_media_pb2.Media]
    def __init__(self, media: _Optional[_Iterable[_Union[_media_pb2.Media, _Mapping]]] = ...) -> None: ...
