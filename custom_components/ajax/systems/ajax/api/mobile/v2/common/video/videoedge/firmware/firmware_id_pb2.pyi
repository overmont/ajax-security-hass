from systems.ajax.api.mobile.v2.common.video.videoedge.firmware import firmware_version_pb2 as _firmware_version_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VideoEdgeFirmwareId(_message.Message):
    __slots__ = ("product_type", "platform_name", "firmware_version")
    PRODUCT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_NAME_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    product_type: str
    platform_name: str
    firmware_version: _firmware_version_pb2.FirmwareVersion
    def __init__(self, product_type: _Optional[str] = ..., platform_name: _Optional[str] = ..., firmware_version: _Optional[_Union[_firmware_version_pb2.FirmwareVersion, _Mapping]] = ...) -> None: ...
