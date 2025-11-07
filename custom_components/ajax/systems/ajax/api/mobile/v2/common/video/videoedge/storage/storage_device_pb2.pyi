from google.protobuf import timestamp_pb2 as _timestamp_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StorageMediaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STORAGE_MEDIA_TYPE_UNSPECIFIED: _ClassVar[StorageMediaType]
    STORAGE_MEDIA_TYPE_SATA: _ClassVar[StorageMediaType]
    STORAGE_MEDIA_TYPE_SD: _ClassVar[StorageMediaType]
    STORAGE_MEDIA_TYPE_USB: _ClassVar[StorageMediaType]

class StorageDeviceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DS_NONE: _ClassVar[StorageDeviceState]
    DS_IDLE: _ClassVar[StorageDeviceState]
    DS_NEED_FORMAT: _ClassVar[StorageDeviceState]
    DS_FORMATTING: _ClassVar[StorageDeviceState]
    DS_READY: _ClassVar[StorageDeviceState]

class StorageError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SE_OTHER: _ClassVar[StorageError]
    SE_OK: _ClassVar[StorageError]
    SE_FORMAT_FAILED: _ClassVar[StorageError]
    SE_REPAIR_FAILED: _ClassVar[StorageError]
    SE_MOUNT_FAILED: _ClassVar[StorageError]
    SE_UNMOUNT_FAILED: _ClassVar[StorageError]
    SE_WRITE_FAILED: _ClassVar[StorageError]
    SE_ARCHIVE_KEY_FINGERPRINT_MISMATCH: _ClassVar[StorageError]
    SE_UNSUPPORTED_ARCHIVE_VERSION: _ClassVar[StorageError]

class PartitionTableType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PT_NONE: _ClassVar[PartitionTableType]
    PT_DOS: _ClassVar[PartitionTableType]
    PT_GPT: _ClassVar[PartitionTableType]
STORAGE_MEDIA_TYPE_UNSPECIFIED: StorageMediaType
STORAGE_MEDIA_TYPE_SATA: StorageMediaType
STORAGE_MEDIA_TYPE_SD: StorageMediaType
STORAGE_MEDIA_TYPE_USB: StorageMediaType
DS_NONE: StorageDeviceState
DS_IDLE: StorageDeviceState
DS_NEED_FORMAT: StorageDeviceState
DS_FORMATTING: StorageDeviceState
DS_READY: StorageDeviceState
SE_OTHER: StorageError
SE_OK: StorageError
SE_FORMAT_FAILED: StorageError
SE_REPAIR_FAILED: StorageError
SE_MOUNT_FAILED: StorageError
SE_UNMOUNT_FAILED: StorageError
SE_WRITE_FAILED: StorageError
SE_ARCHIVE_KEY_FINGERPRINT_MISMATCH: StorageError
SE_UNSUPPORTED_ARCHIVE_VERSION: StorageError
PT_NONE: PartitionTableType
PT_DOS: PartitionTableType
PT_GPT: PartitionTableType

class StorageDevice(_message.Message):
    __slots__ = ("guid", "vendor", "model", "serial", "size_total", "status", "info", "size_used", "temperature", "disk_write_errors", "media_type", "port_number")
    GUID_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    SIZE_TOTAL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    SIZE_USED_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    DISK_WRITE_ERRORS_FIELD_NUMBER: _ClassVar[int]
    MEDIA_TYPE_FIELD_NUMBER: _ClassVar[int]
    PORT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    guid: str
    vendor: str
    model: str
    serial: str
    size_total: int
    status: StorageDeviceStatus
    info: StorageDeviceInfo
    size_used: int
    temperature: int
    disk_write_errors: DiskWriteErrors
    media_type: StorageMediaType
    port_number: StorageDevicePortNumber
    def __init__(self, guid: _Optional[str] = ..., vendor: _Optional[str] = ..., model: _Optional[str] = ..., serial: _Optional[str] = ..., size_total: _Optional[int] = ..., status: _Optional[_Union[StorageDeviceStatus, _Mapping]] = ..., info: _Optional[_Union[StorageDeviceInfo, _Mapping]] = ..., size_used: _Optional[int] = ..., temperature: _Optional[int] = ..., disk_write_errors: _Optional[_Union[DiskWriteErrors, _Mapping]] = ..., media_type: _Optional[_Union[StorageMediaType, str]] = ..., port_number: _Optional[_Union[StorageDevicePortNumber, _Mapping]] = ...) -> None: ...

class StorageDevicePortNumber(_message.Message):
    __slots__ = ("actual_number", "display_number")
    ACTUAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NUMBER_FIELD_NUMBER: _ClassVar[int]
    actual_number: int
    display_number: int
    def __init__(self, actual_number: _Optional[int] = ..., display_number: _Optional[int] = ...) -> None: ...

class StorageDeviceStatus(_message.Message):
    __slots__ = ("state", "error")
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    state: StorageDeviceState
    error: StorageError
    def __init__(self, state: _Optional[_Union[StorageDeviceState, str]] = ..., error: _Optional[_Union[StorageError, str]] = ...) -> None: ...

class StorageDeviceInfo(_message.Message):
    __slots__ = ("partition_table_type",)
    PARTITION_TABLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    partition_table_type: PartitionTableType
    def __init__(self, partition_table_type: _Optional[_Union[PartitionTableType, str]] = ...) -> None: ...

class DiskWriteErrors(_message.Message):
    __slots__ = ("count", "last_errors_timestamps")
    COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_ERRORS_TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    count: int
    last_errors_timestamps: _containers.RepeatedCompositeFieldContainer[_timestamp_pb2.Timestamp]
    def __init__(self, count: _Optional[int] = ..., last_errors_timestamps: _Optional[_Iterable[_Union[_timestamp_pb2.Timestamp, _Mapping]]] = ...) -> None: ...
