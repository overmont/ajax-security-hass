from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class VideoNotificationSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VIDEO_SOURCE_TYPE_UNSPECIFIED: _ClassVar[VideoNotificationSourceType]
    VIDEO_EDGE: _ClassVar[VideoNotificationSourceType]
    VIDEO_SCENARIO: _ClassVar[VideoNotificationSourceType]
    SPACE_MEMBER: _ClassVar[VideoNotificationSourceType]
    COMPANY: _ClassVar[VideoNotificationSourceType]
VIDEO_SOURCE_TYPE_UNSPECIFIED: VideoNotificationSourceType
VIDEO_EDGE: VideoNotificationSourceType
VIDEO_SCENARIO: VideoNotificationSourceType
SPACE_MEMBER: VideoNotificationSourceType
COMPANY: VideoNotificationSourceType
