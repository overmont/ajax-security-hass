from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class VideoNotificationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VIDEO_NOTIFICATION_TYPE_UNSPECIFIED: _ClassVar[VideoNotificationType]
    VIDEO_NOTIFICATION_TYPE_HUMAN: _ClassVar[VideoNotificationType]
    VIDEO_NOTIFICATION_TYPE_PET: _ClassVar[VideoNotificationType]
    VIDEO_NOTIFICATION_TYPE_VEHICLE: _ClassVar[VideoNotificationType]
    VIDEO_NOTIFICATION_TYPE_PIR_MOTION: _ClassVar[VideoNotificationType]
    VIDEO_NOTIFICATION_TYPE_FRAME_MOTION: _ClassVar[VideoNotificationType]
VIDEO_NOTIFICATION_TYPE_UNSPECIFIED: VideoNotificationType
VIDEO_NOTIFICATION_TYPE_HUMAN: VideoNotificationType
VIDEO_NOTIFICATION_TYPE_PET: VideoNotificationType
VIDEO_NOTIFICATION_TYPE_VEHICLE: VideoNotificationType
VIDEO_NOTIFICATION_TYPE_PIR_MOTION: VideoNotificationType
VIDEO_NOTIFICATION_TYPE_FRAME_MOTION: VideoNotificationType
