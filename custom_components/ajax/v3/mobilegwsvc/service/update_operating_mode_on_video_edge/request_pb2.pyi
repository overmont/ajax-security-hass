from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.mcu import operating_mode_pb2 as _operating_mode_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateOperatingModeRequest(_message.Message):
    __slots__ = ("space_locator", "video_edge_id", "operating_mode")
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATING_MODE_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    video_edge_id: str
    operating_mode: _operating_mode_pb2.OperatingMode
    def __init__(self, space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ..., video_edge_id: _Optional[str] = ..., operating_mode: _Optional[_Union[_operating_mode_pb2.OperatingMode, str]] = ...) -> None: ...
