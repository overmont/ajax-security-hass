from google.protobuf import duration_pb2 as _duration_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.detector import detector_pb2 as _detector_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.channel.notification import video_notification_monitoring_state_pb2 as _video_notification_monitoring_state_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.channel.notification import video_notification_state_pb2 as _video_notification_state_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.channel.notification import video_notification_type_pb2 as _video_notification_type_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.channel.notification import video_notification_object_detection_duration_pb2 as _video_notification_object_detection_duration_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.channel.notification import video_notification_confirm_detection_with_pir_state_pb2 as _video_notification_confirm_detection_with_pir_state_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VideoNotificationSettings(_message.Message):
    __slots__ = ("notification_settings_entries", "monitoring_state", "cooldown_period", "enabled_detector_types", "object_detection_duration", "confirm_detection_with_pir", "detection_type_enabled_states", "line_crossing_settings")
    class NotificationStateEntry(_message.Message):
        __slots__ = ("type", "state", "detector_type")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        DETECTOR_TYPE_FIELD_NUMBER: _ClassVar[int]
        type: _video_notification_type_pb2.VideoNotificationType
        state: _video_notification_state_pb2.VideoNotificationState
        detector_type: _detector_pb2.DetectorType
        def __init__(self, type: _Optional[_Union[_video_notification_type_pb2.VideoNotificationType, str]] = ..., state: _Optional[_Union[_video_notification_state_pb2.VideoNotificationState, str]] = ..., detector_type: _Optional[_Union[_detector_pb2.DetectorType, str]] = ...) -> None: ...
    class LineCrossingNotificationSettings(_message.Message):
        __slots__ = ("notification_state_entries", "enabled_rules")
        NOTIFICATION_STATE_ENTRIES_FIELD_NUMBER: _ClassVar[int]
        ENABLED_RULES_FIELD_NUMBER: _ClassVar[int]
        notification_state_entries: _containers.RepeatedCompositeFieldContainer[VideoNotificationSettings.LineCrossingNotificationState]
        enabled_rules: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, notification_state_entries: _Optional[_Iterable[_Union[VideoNotificationSettings.LineCrossingNotificationState, _Mapping]]] = ..., enabled_rules: _Optional[_Iterable[int]] = ...) -> None: ...
    class LineCrossingNotificationState(_message.Message):
        __slots__ = ("rule_id", "rule_name", "state")
        RULE_ID_FIELD_NUMBER: _ClassVar[int]
        RULE_NAME_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        rule_id: int
        rule_name: str
        state: _video_notification_state_pb2.VideoNotificationState
        def __init__(self, rule_id: _Optional[int] = ..., rule_name: _Optional[str] = ..., state: _Optional[_Union[_video_notification_state_pb2.VideoNotificationState, str]] = ...) -> None: ...
    class DetectionTypeEnabledState(_message.Message):
        __slots__ = ("detection_type", "enabled")
        DETECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        detection_type: _video_notification_type_pb2.VideoNotificationType
        enabled: bool
        def __init__(self, detection_type: _Optional[_Union[_video_notification_type_pb2.VideoNotificationType, str]] = ..., enabled: bool = ...) -> None: ...
    NOTIFICATION_SETTINGS_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    MONITORING_STATE_FIELD_NUMBER: _ClassVar[int]
    COOLDOWN_PERIOD_FIELD_NUMBER: _ClassVar[int]
    ENABLED_DETECTOR_TYPES_FIELD_NUMBER: _ClassVar[int]
    OBJECT_DETECTION_DURATION_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_DETECTION_WITH_PIR_FIELD_NUMBER: _ClassVar[int]
    DETECTION_TYPE_ENABLED_STATES_FIELD_NUMBER: _ClassVar[int]
    LINE_CROSSING_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    notification_settings_entries: _containers.RepeatedCompositeFieldContainer[VideoNotificationSettings.NotificationStateEntry]
    monitoring_state: _video_notification_monitoring_state_pb2.VideoNotificationMonitoringState
    cooldown_period: _duration_pb2.Duration
    enabled_detector_types: _containers.RepeatedScalarFieldContainer[_detector_pb2.DetectorType]
    object_detection_duration: _video_notification_object_detection_duration_pb2.VideoNotificationObjectDetectionDuration
    confirm_detection_with_pir: _video_notification_confirm_detection_with_pir_state_pb2.VideoNotificationConfirmDetectionWithPirState
    detection_type_enabled_states: _containers.RepeatedCompositeFieldContainer[VideoNotificationSettings.DetectionTypeEnabledState]
    line_crossing_settings: VideoNotificationSettings.LineCrossingNotificationSettings
    def __init__(self, notification_settings_entries: _Optional[_Iterable[_Union[VideoNotificationSettings.NotificationStateEntry, _Mapping]]] = ..., monitoring_state: _Optional[_Union[_video_notification_monitoring_state_pb2.VideoNotificationMonitoringState, str]] = ..., cooldown_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., enabled_detector_types: _Optional[_Iterable[_Union[_detector_pb2.DetectorType, str]]] = ..., object_detection_duration: _Optional[_Union[_video_notification_object_detection_duration_pb2.VideoNotificationObjectDetectionDuration, str]] = ..., confirm_detection_with_pir: _Optional[_Union[_video_notification_confirm_detection_with_pir_state_pb2.VideoNotificationConfirmDetectionWithPirState, str]] = ..., detection_type_enabled_states: _Optional[_Iterable[_Union[VideoNotificationSettings.DetectionTypeEnabledState, _Mapping]]] = ..., line_crossing_settings: _Optional[_Union[VideoNotificationSettings.LineCrossingNotificationSettings, _Mapping]] = ...) -> None: ...
