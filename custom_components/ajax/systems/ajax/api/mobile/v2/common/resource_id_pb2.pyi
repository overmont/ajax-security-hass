from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResourceId(_message.Message):
    __slots__ = ("firmware_id",)
    class FirmwareId(_message.Message):
        __slots__ = ("device_object_type", "device_object_subtype", "device_hardware_version", "firmware_band_type", "firmware_version")
        DEVICE_OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
        DEVICE_OBJECT_SUBTYPE_FIELD_NUMBER: _ClassVar[int]
        DEVICE_HARDWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
        FIRMWARE_BAND_TYPE_FIELD_NUMBER: _ClassVar[int]
        FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
        device_object_type: int
        device_object_subtype: int
        device_hardware_version: str
        firmware_band_type: int
        firmware_version: str
        def __init__(self, device_object_type: _Optional[int] = ..., device_object_subtype: _Optional[int] = ..., device_hardware_version: _Optional[str] = ..., firmware_band_type: _Optional[int] = ..., firmware_version: _Optional[str] = ...) -> None: ...
    FIRMWARE_ID_FIELD_NUMBER: _ClassVar[int]
    firmware_id: ResourceId.FirmwareId
    def __init__(self, firmware_id: _Optional[_Union[ResourceId.FirmwareId, _Mapping]] = ...) -> None: ...
