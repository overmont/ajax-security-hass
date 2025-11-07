from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CloudArchive(_message.Message):
    __slots__ = ("status", "storage_enabled", "video_stream_settings_locked")
    class CloudArchiveStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CLOUD_ARCHIVE_STATUS_UNSPECIFIED: _ClassVar[CloudArchive.CloudArchiveStatus]
        CLOUD_ARCHIVE_STATUS_ACTIVATED: _ClassVar[CloudArchive.CloudArchiveStatus]
        CLOUD_ARCHIVE_STATUS_NOT_ACTIVATED: _ClassVar[CloudArchive.CloudArchiveStatus]
    CLOUD_ARCHIVE_STATUS_UNSPECIFIED: CloudArchive.CloudArchiveStatus
    CLOUD_ARCHIVE_STATUS_ACTIVATED: CloudArchive.CloudArchiveStatus
    CLOUD_ARCHIVE_STATUS_NOT_ACTIVATED: CloudArchive.CloudArchiveStatus
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    VIDEO_STREAM_SETTINGS_LOCKED_FIELD_NUMBER: _ClassVar[int]
    status: CloudArchive.CloudArchiveStatus
    storage_enabled: bool
    video_stream_settings_locked: bool
    def __init__(self, status: _Optional[_Union[CloudArchive.CloudArchiveStatus, str]] = ..., storage_enabled: bool = ..., video_stream_settings_locked: bool = ...) -> None: ...
