from google.protobuf import timestamp_pb2 as _timestamp_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SourceImageInfo(_message.Message):
    __slots__ = ("base_image_url",)
    BASE_IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    base_image_url: str
    def __init__(self, base_image_url: _Optional[str] = ...) -> None: ...
