from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.firmware import resource_id_pb2 as _resource_id_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceFirmwareUpdate(_message.Message):
    __slots__ = ("device_id", "resource_id", "status", "is_critical")
    class Status(_message.Message):
        __slots__ = ("not_started", "downloading", "downloaded", "installing", "completed", "failed")
        NOT_STARTED_FIELD_NUMBER: _ClassVar[int]
        DOWNLOADING_FIELD_NUMBER: _ClassVar[int]
        DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
        INSTALLING_FIELD_NUMBER: _ClassVar[int]
        COMPLETED_FIELD_NUMBER: _ClassVar[int]
        FAILED_FIELD_NUMBER: _ClassVar[int]
        not_started: _empty_pb2.Empty
        downloading: int
        downloaded: _empty_pb2.Empty
        installing: _empty_pb2.Empty
        completed: _empty_pb2.Empty
        failed: _empty_pb2.Empty
        def __init__(self, not_started: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., downloading: _Optional[int] = ..., downloaded: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., installing: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., completed: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., failed: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ...) -> None: ...
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    IS_CRITICAL_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    resource_id: _resource_id_pb2.ResourceId
    status: DeviceFirmwareUpdate.Status
    is_critical: _wrappers_pb2.BoolValue
    def __init__(self, device_id: _Optional[str] = ..., resource_id: _Optional[_Union[_resource_id_pb2.ResourceId, _Mapping]] = ..., status: _Optional[_Union[DeviceFirmwareUpdate.Status, _Mapping]] = ..., is_critical: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...
