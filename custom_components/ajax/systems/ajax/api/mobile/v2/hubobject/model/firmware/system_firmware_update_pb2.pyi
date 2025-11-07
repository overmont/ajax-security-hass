from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SystemFirmwareUpdate(_message.Message):
    __slots__ = ("firmware_version", "status", "firmware_version_raw")
    class Status(_message.Message):
        __slots__ = ("not_started", "downloading")
        NOT_STARTED_FIELD_NUMBER: _ClassVar[int]
        DOWNLOADING_FIELD_NUMBER: _ClassVar[int]
        not_started: _empty_pb2.Empty
        downloading: _empty_pb2.Empty
        def __init__(self, not_started: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., downloading: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ...) -> None: ...
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_RAW_FIELD_NUMBER: _ClassVar[int]
    firmware_version: str
    status: SystemFirmwareUpdate.Status
    firmware_version_raw: int
    def __init__(self, firmware_version: _Optional[str] = ..., status: _Optional[_Union[SystemFirmwareUpdate.Status, _Mapping]] = ..., firmware_version_raw: _Optional[int] = ...) -> None: ...
