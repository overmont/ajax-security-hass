from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ImageUrls(_message.Message):
    __slots__ = ("small", "medium", "big", "base_path")
    SMALL_FIELD_NUMBER: _ClassVar[int]
    MEDIUM_FIELD_NUMBER: _ClassVar[int]
    BIG_FIELD_NUMBER: _ClassVar[int]
    BASE_PATH_FIELD_NUMBER: _ClassVar[int]
    small: _wrappers_pb2.StringValue
    medium: _wrappers_pb2.StringValue
    big: _wrappers_pb2.StringValue
    base_path: _wrappers_pb2.StringValue
    def __init__(self, small: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., medium: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., big: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., base_path: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
