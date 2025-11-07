from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateBackupChannelRequest(_message.Message):
    __slots__ = ("video_edge_id", "space_locator", "hub_id")
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    space_locator: _space_locator_pb2.SpaceLocator
    hub_id: str
    def __init__(self, video_edge_id: _Optional[str] = ..., space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ..., hub_id: _Optional[str] = ...) -> None: ...
