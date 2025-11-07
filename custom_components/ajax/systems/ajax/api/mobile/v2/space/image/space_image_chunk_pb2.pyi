from systems.ajax.api.mobile.v2.common.image import image_data_chunk_pb2 as _image_data_chunk_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceImageChunk(_message.Message):
    __slots__ = ("meta_chunk", "data_chunk")
    class MetaChunk(_message.Message):
        __slots__ = ("file_name", "space_id")
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        SPACE_ID_FIELD_NUMBER: _ClassVar[int]
        file_name: str
        space_id: str
        def __init__(self, file_name: _Optional[str] = ..., space_id: _Optional[str] = ...) -> None: ...
    META_CHUNK_FIELD_NUMBER: _ClassVar[int]
    DATA_CHUNK_FIELD_NUMBER: _ClassVar[int]
    meta_chunk: SpaceImageChunk.MetaChunk
    data_chunk: _image_data_chunk_pb2.ImageDataChunk
    def __init__(self, meta_chunk: _Optional[_Union[SpaceImageChunk.MetaChunk, _Mapping]] = ..., data_chunk: _Optional[_Union[_image_data_chunk_pb2.ImageDataChunk, _Mapping]] = ...) -> None: ...
