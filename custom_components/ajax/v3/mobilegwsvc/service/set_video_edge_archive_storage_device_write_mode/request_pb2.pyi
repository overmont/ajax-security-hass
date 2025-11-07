from systems.ajax.api.mobile.v2.common.video.videoedge.archive import archive_pb2 as _archive_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoEdgeArchiveStorageDeviceWriteModeRequest(_message.Message):
    __slots__ = ("space_id", "video_edge_id", "storage_device_write_mode")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DEVICE_WRITE_MODE_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    storage_device_write_mode: _archive_pb2.StorageDeviceWriteMode
    def __init__(self, space_id: _Optional[str] = ..., video_edge_id: _Optional[str] = ..., storage_device_write_mode: _Optional[_Union[_archive_pb2.StorageDeviceWriteMode, str]] = ...) -> None: ...
