from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FireZoneInfo(_message.Message):
    __slots__ = ("fire_zone_id_hex", "fire_zone_name")
    FIRE_ZONE_ID_HEX_FIELD_NUMBER: _ClassVar[int]
    FIRE_ZONE_NAME_FIELD_NUMBER: _ClassVar[int]
    fire_zone_id_hex: str
    fire_zone_name: str
    def __init__(self, fire_zone_id_hex: _Optional[str] = ..., fire_zone_name: _Optional[str] = ...) -> None: ...
