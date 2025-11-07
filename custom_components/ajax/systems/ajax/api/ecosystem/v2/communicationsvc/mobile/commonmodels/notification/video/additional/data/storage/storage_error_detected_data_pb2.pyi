from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video.additional.data.storage import storage_device_port_number_pb2 as _storage_device_port_number_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StorageErrorDetectedData(_message.Message):
    __slots__ = ("storage_id", "storage_device_port_number")
    STORAGE_ID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DEVICE_PORT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    storage_id: str
    storage_device_port_number: _storage_device_port_number_pb2.StorageDevicePortNumber
    def __init__(self, storage_id: _Optional[str] = ..., storage_device_port_number: _Optional[_Union[_storage_device_port_number_pb2.StorageDevicePortNumber, _Mapping]] = ...) -> None: ...
