from systems.ajax.api.mobile.v2.common.video.videoedge.about import about_pb2 as _about_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VideoEdgeAdditionalInfo(_message.Message):
    __slots__ = ("color", "type")
    COLOR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    color: _about_pb2.About.Color
    type: _about_pb2.About.Type
    def __init__(self, color: _Optional[_Union[_about_pb2.About.Color, str]] = ..., type: _Optional[_Union[_about_pb2.About.Type, str]] = ...) -> None: ...
