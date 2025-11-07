from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FirmwareIdInfo(_message.Message):
    __slots__ = ("fw_version", "device_type", "device_subtype", "device_hw_version", "device_band")
    FW_VERSION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_HW_VERSION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BAND_FIELD_NUMBER: _ClassVar[int]
    fw_version: str
    device_type: int
    device_subtype: int
    device_hw_version: str
    device_band: int
    def __init__(self, fw_version: _Optional[str] = ..., device_type: _Optional[int] = ..., device_subtype: _Optional[int] = ..., device_hw_version: _Optional[str] = ..., device_band: _Optional[int] = ...) -> None: ...
