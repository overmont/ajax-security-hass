from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteCrossZoneRequest(_message.Message):
    __slots__ = ("hub_hex_id", "cross_zone_id")
    HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    CROSS_ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    hub_hex_id: str
    cross_zone_id: str
    def __init__(self, hub_hex_id: _Optional[str] = ..., cross_zone_id: _Optional[str] = ...) -> None: ...
