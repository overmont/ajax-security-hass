from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FirmwareUpdateFinishedData(_message.Message):
    __slots__ = ("firmware_id",)
    class VideoEdgeFirmwareId(_message.Message):
        __slots__ = ("product_type", "platform_name", "firmware_version")
        class FirmwareVersion(_message.Message):
            __slots__ = ("major", "minor", "extra")
            MAJOR_FIELD_NUMBER: _ClassVar[int]
            MINOR_FIELD_NUMBER: _ClassVar[int]
            EXTRA_FIELD_NUMBER: _ClassVar[int]
            major: int
            minor: int
            extra: str
            def __init__(self, major: _Optional[int] = ..., minor: _Optional[int] = ..., extra: _Optional[str] = ...) -> None: ...
        PRODUCT_TYPE_FIELD_NUMBER: _ClassVar[int]
        PLATFORM_NAME_FIELD_NUMBER: _ClassVar[int]
        FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
        product_type: str
        platform_name: str
        firmware_version: FirmwareUpdateFinishedData.VideoEdgeFirmwareId.FirmwareVersion
        def __init__(self, product_type: _Optional[str] = ..., platform_name: _Optional[str] = ..., firmware_version: _Optional[_Union[FirmwareUpdateFinishedData.VideoEdgeFirmwareId.FirmwareVersion, _Mapping]] = ...) -> None: ...
    FIRMWARE_ID_FIELD_NUMBER: _ClassVar[int]
    firmware_id: FirmwareUpdateFinishedData.VideoEdgeFirmwareId
    def __init__(self, firmware_id: _Optional[_Union[FirmwareUpdateFinishedData.VideoEdgeFirmwareId, _Mapping]] = ...) -> None: ...
