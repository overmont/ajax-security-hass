from v1.media import media_pb2 as _media_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateMediaInfoResponse(_message.Message):
    __slots__ = ("info",)
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: _media_pb2.Media.Info
    def __init__(self, info: _Optional[_Union[_media_pb2.Media.Info, _Mapping]] = ...) -> None: ...
