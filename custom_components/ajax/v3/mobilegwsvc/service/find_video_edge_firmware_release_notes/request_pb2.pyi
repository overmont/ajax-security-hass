from systems.ajax.api.mobile.v2.common.video.videoedge.firmware import firmware_id_pb2 as _firmware_id_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FindVideoEdgeFirmwareReleaseNotesRequest(_message.Message):
    __slots__ = ("firmware_id", "language_code")
    FIRMWARE_ID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    firmware_id: _firmware_id_pb2.VideoEdgeFirmwareId
    language_code: str
    def __init__(self, firmware_id: _Optional[_Union[_firmware_id_pb2.VideoEdgeFirmwareId, _Mapping]] = ..., language_code: _Optional[str] = ...) -> None: ...
