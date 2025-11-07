from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class VideoMonitoringState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VIDEO_MONITORING_STATE_UNSPECIFIED: _ClassVar[VideoMonitoringState]
    VIDEO_MONITORING_STATE_ENABLED: _ClassVar[VideoMonitoringState]
    VIDEO_MONITORING_STATE_DISABLED: _ClassVar[VideoMonitoringState]
VIDEO_MONITORING_STATE_UNSPECIFIED: VideoMonitoringState
VIDEO_MONITORING_STATE_ENABLED: VideoMonitoringState
VIDEO_MONITORING_STATE_DISABLED: VideoMonitoringState
