from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterDeviceToHubRequest(_message.Message):
    __slots__ = ("hub_id", "room_id", "group_id", "device_name", "device_qr_code", "fire_zone_id", "device_location", "lock_master_code")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_QR_CODE_FIELD_NUMBER: _ClassVar[int]
    FIRE_ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    LOCK_MASTER_CODE_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    room_id: str
    group_id: str
    device_name: str
    device_qr_code: str
    fire_zone_id: str
    device_location: str
    lock_master_code: str
    def __init__(self, hub_id: _Optional[str] = ..., room_id: _Optional[str] = ..., group_id: _Optional[str] = ..., device_name: _Optional[str] = ..., device_qr_code: _Optional[str] = ..., fire_zone_id: _Optional[str] = ..., device_location: _Optional[str] = ..., lock_master_code: _Optional[str] = ...) -> None: ...
