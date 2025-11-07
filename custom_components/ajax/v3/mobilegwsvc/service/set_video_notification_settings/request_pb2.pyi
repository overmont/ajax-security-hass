import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.channel.notification import video_notification_monitoring_state_pb2 as _video_notification_monitoring_state_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.channel.notification import video_notification_state_pb2 as _video_notification_state_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.channel.notification import video_notification_type_pb2 as _video_notification_type_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.channel.notification import video_notification_object_detection_duration_pb2 as _video_notification_object_detection_duration_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.channel.notification import video_notification_confirm_detection_with_pir_state_pb2 as _video_notification_confirm_detection_with_pir_state_pb2
from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoNotificationSettingsRequest(_message.Message):
    __slots__ = ("space_locator", "video_edge_id", "channel_id", "notification_settings")
    class NotificationSettings(_message.Message):
        __slots__ = ("notification_settings_entries", "monitoring_state", "cooldown_period", "object_detection_duration", "confirm_detection_with_pir", "line_crossing_changes")
        class NotificationSettingsEntry(_message.Message):
            __slots__ = ("type", "state")
            TYPE_FIELD_NUMBER: _ClassVar[int]
            STATE_FIELD_NUMBER: _ClassVar[int]
            type: _video_notification_type_pb2.VideoNotificationType
            state: _video_notification_state_pb2.VideoNotificationState
            def __init__(self, type: _Optional[_Union[_video_notification_type_pb2.VideoNotificationType, str]] = ..., state: _Optional[_Union[_video_notification_state_pb2.VideoNotificationState, str]] = ...) -> None: ...
        class LineCrossingNotificationSettingsChange(_message.Message):
            __slots__ = ("rule_id", "state")
            RULE_ID_FIELD_NUMBER: _ClassVar[int]
            STATE_FIELD_NUMBER: _ClassVar[int]
            rule_id: int
            state: _video_notification_state_pb2.VideoNotificationState
            def __init__(self, rule_id: _Optional[int] = ..., state: _Optional[_Union[_video_notification_state_pb2.VideoNotificationState, str]] = ...) -> None: ...
        NOTIFICATION_SETTINGS_ENTRIES_FIELD_NUMBER: _ClassVar[int]
        MONITORING_STATE_FIELD_NUMBER: _ClassVar[int]
        COOLDOWN_PERIOD_FIELD_NUMBER: _ClassVar[int]
        OBJECT_DETECTION_DURATION_FIELD_NUMBER: _ClassVar[int]
        CONFIRM_DETECTION_WITH_PIR_FIELD_NUMBER: _ClassVar[int]
        LINE_CROSSING_CHANGES_FIELD_NUMBER: _ClassVar[int]
        notification_settings_entries: _containers.RepeatedCompositeFieldContainer[SetVideoNotificationSettingsRequest.NotificationSettings.NotificationSettingsEntry]
        monitoring_state: _video_notification_monitoring_state_pb2.VideoNotificationMonitoringState
        cooldown_period: _duration_pb2.Duration
        object_detection_duration: _video_notification_object_detection_duration_pb2.VideoNotificationObjectDetectionDuration
        confirm_detection_with_pir: _video_notification_confirm_detection_with_pir_state_pb2.VideoNotificationConfirmDetectionWithPirState
        line_crossing_changes: _containers.RepeatedCompositeFieldContainer[SetVideoNotificationSettingsRequest.NotificationSettings.LineCrossingNotificationSettingsChange]
        def __init__(self, notification_settings_entries: _Optional[_Iterable[_Union[SetVideoNotificationSettingsRequest.NotificationSettings.NotificationSettingsEntry, _Mapping]]] = ..., monitoring_state: _Optional[_Union[_video_notification_monitoring_state_pb2.VideoNotificationMonitoringState, str]] = ..., cooldown_period: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., object_detection_duration: _Optional[_Union[_video_notification_object_detection_duration_pb2.VideoNotificationObjectDetectionDuration, str]] = ..., confirm_detection_with_pir: _Optional[_Union[_video_notification_confirm_detection_with_pir_state_pb2.VideoNotificationConfirmDetectionWithPirState, str]] = ..., line_crossing_changes: _Optional[_Iterable[_Union[SetVideoNotificationSettingsRequest.NotificationSettings.LineCrossingNotificationSettingsChange, _Mapping]]] = ...) -> None: ...
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    video_edge_id: str
    channel_id: str
    notification_settings: SetVideoNotificationSettingsRequest.NotificationSettings
    def __init__(self, space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ..., video_edge_id: _Optional[str] = ..., channel_id: _Optional[str] = ..., notification_settings: _Optional[_Union[SetVideoNotificationSettingsRequest.NotificationSettings, _Mapping]] = ...) -> None: ...
