from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class VideoNotificationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VIDEO_NOTIFICATION_STATE_UNSPECIFIED: _ClassVar[VideoNotificationState]
    VIDEO_NOTIFICATION_STATE_DISABLED: _ClassVar[VideoNotificationState]
    VIDEO_NOTIFICATION_STATE_ENABLED: _ClassVar[VideoNotificationState]
VIDEO_NOTIFICATION_STATE_UNSPECIFIED: VideoNotificationState
VIDEO_NOTIFICATION_STATE_DISABLED: VideoNotificationState
VIDEO_NOTIFICATION_STATE_ENABLED: VideoNotificationState
