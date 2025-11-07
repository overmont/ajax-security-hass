from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StreamFireZoneRequestV2(_message.Message):
    __slots__ = ("hub_id",)
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    def __init__(self, hub_id: _Optional[str] = ...) -> None: ...
