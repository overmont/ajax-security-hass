from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FirmwareUpdate(_message.Message):
    __slots__ = ("target_id", "status")
    class Status(_message.Message):
        __slots__ = ("not_started", "downloading", "success", "failure", "installing")
        NOT_STARTED_FIELD_NUMBER: _ClassVar[int]
        DOWNLOADING_FIELD_NUMBER: _ClassVar[int]
        SUCCESS_FIELD_NUMBER: _ClassVar[int]
        FAILURE_FIELD_NUMBER: _ClassVar[int]
        INSTALLING_FIELD_NUMBER: _ClassVar[int]
        not_started: _empty_pb2.Empty
        downloading: int
        success: _empty_pb2.Empty
        failure: _empty_pb2.Empty
        installing: _empty_pb2.Empty
        def __init__(self, not_started: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., downloading: _Optional[int] = ..., success: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., failure: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., installing: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ...) -> None: ...
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    target_id: str
    status: FirmwareUpdate.Status
    def __init__(self, target_id: _Optional[str] = ..., status: _Optional[_Union[FirmwareUpdate.Status, _Mapping]] = ...) -> None: ...
