from google.protobuf import duration_pb2 as _duration_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import fan_speed_settings_pb2 as _fan_speed_settings_pb2
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import onvif_user_role_pb2 as _onvif_user_role_pb2
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import max_ring_depth_pb2 as _max_ring_depth_pb2
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import local_user_permissions_pb2 as _local_user_permissions_pb2
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import network_pb2 as _network_pb2
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import video_notificaton_type_pb2 as _video_notificaton_type_pb2
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import video_notification_state_pb2 as _video_notification_state_pb2
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import alert_with_siren_pb2 as _alert_with_siren_pb2
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import notification_event_type_pb2 as _notification_event_type_pb2
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import video_notification_monitoring_state_pb2 as _video_notification_monitoring_state_pb2
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import video_notification_confirm_detection_with_pir_state_pb2 as _video_notification_confirm_detection_with_pir_state_pb2
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import video_nofification_object_detection_duration_pb2 as _video_nofification_object_detection_duration_pb2
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import media_settings_pb2 as _media_settings_pb2
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import detector_settings_pb2 as _detector_settings_pb2
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge.archive import record_mode_pb2 as _record_mode_pb2
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge.archive import record_policy_pb2 as _record_policy_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VideoConnectionTypePart(_message.Message):
    __slots__ = ("ethernet",)
    ETHERNET_FIELD_NUMBER: _ClassVar[int]
    ethernet: _network_pb2.NetworkConfiguration
    def __init__(self, ethernet: _Optional[_Union[_network_pb2.NetworkConfiguration, _Mapping]] = ...) -> None: ...

class VideoArchivePart(_message.Message):
    __slots__ = ("max_ring_depth",)
    MAX_RING_DEPTH_FIELD_NUMBER: _ClassVar[int]
    max_ring_depth: _max_ring_depth_pb2.MaxRingDepth
    def __init__(self, max_ring_depth: _Optional[_Union[_max_ring_depth_pb2.MaxRingDepth, str]] = ...) -> None: ...

class VideoLocalUsersPart(_message.Message):
    __slots__ = ("users",)
    class VideoLocalUser(_message.Message):
        __slots__ = ("name", "password", "permissions")
        NAME_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        name: str
        password: str
        permissions: _local_user_permissions_pb2.LocalUserPermissions
        def __init__(self, name: _Optional[str] = ..., password: _Optional[str] = ..., permissions: _Optional[_Union[_local_user_permissions_pb2.LocalUserPermissions, _Mapping]] = ...) -> None: ...
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[VideoLocalUsersPart.VideoLocalUser]
    def __init__(self, users: _Optional[_Iterable[_Union[VideoLocalUsersPart.VideoLocalUser, _Mapping]]] = ...) -> None: ...

class TimeZonePart(_message.Message):
    __slots__ = ("time_zone_id",)
    TIME_ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    time_zone_id: str
    def __init__(self, time_zone_id: _Optional[str] = ...) -> None: ...

class LogoLedBrightnessPart(_message.Message):
    __slots__ = ("brightness",)
    BRIGHTNESS_FIELD_NUMBER: _ClassVar[int]
    brightness: int
    def __init__(self, brightness: _Optional[int] = ...) -> None: ...

class RingButtonSoundPart(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class FanSettingsPart(_message.Message):
    __slots__ = ("fan_speed_settings",)
    FAN_SPEED_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    fan_speed_settings: _fan_speed_settings_pb2.FanSpeedSettings
    def __init__(self, fan_speed_settings: _Optional[_Union[_fan_speed_settings_pb2.FanSpeedSettings, _Mapping]] = ...) -> None: ...

class CloudConnectionPart(_message.Message):
    __slots__ = ("server_ping_interval", "connection_failure_alarm_delay", "mute_connection_alarms")
    SERVER_PING_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FAILURE_ALARM_DELAY_FIELD_NUMBER: _ClassVar[int]
    MUTE_CONNECTION_ALARMS_FIELD_NUMBER: _ClassVar[int]
    server_ping_interval: _duration_pb2.Duration
    connection_failure_alarm_delay: _duration_pb2.Duration
    mute_connection_alarms: bool
    def __init__(self, server_ping_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., connection_failure_alarm_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., mute_connection_alarms: bool = ...) -> None: ...

class OnvifConnectionPart(_message.Message):
    __slots__ = ("onvif_user_auth_enabled", "onvif_http_port", "rtsp_http_port", "users")
    class OnvifUser(_message.Message):
        __slots__ = ("username", "password", "role")
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        ROLE_FIELD_NUMBER: _ClassVar[int]
        username: str
        password: str
        role: _onvif_user_role_pb2.OnvifUserRole
        def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ..., role: _Optional[_Union[_onvif_user_role_pb2.OnvifUserRole, str]] = ...) -> None: ...
    ONVIF_USER_AUTH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ONVIF_HTTP_PORT_FIELD_NUMBER: _ClassVar[int]
    RTSP_HTTP_PORT_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    onvif_user_auth_enabled: bool
    onvif_http_port: int
    rtsp_http_port: int
    users: _containers.RepeatedCompositeFieldContainer[OnvifConnectionPart.OnvifUser]
    def __init__(self, onvif_user_auth_enabled: bool = ..., onvif_http_port: _Optional[int] = ..., rtsp_http_port: _Optional[int] = ..., users: _Optional[_Iterable[_Union[OnvifConnectionPart.OnvifUser, _Mapping]]] = ...) -> None: ...

class ChimePart(_message.Message):
    __slots__ = ("off", "mechanical", "digital", "siren_mode")
    class OffMode(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class MechanicalMode(_message.Message):
        __slots__ = ("duration",)
        DURATION_FIELD_NUMBER: _ClassVar[int]
        duration: _duration_pb2.Duration
        def __init__(self, duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    class DigitalMode(_message.Message):
        __slots__ = ("duration",)
        DURATION_FIELD_NUMBER: _ClassVar[int]
        duration: _duration_pb2.Duration
        def __init__(self, duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    class SirenMode(_message.Message):
        __slots__ = ("chime_signal",)
        CHIME_SIGNAL_FIELD_NUMBER: _ClassVar[int]
        chime_signal: int
        def __init__(self, chime_signal: _Optional[int] = ...) -> None: ...
    OFF_FIELD_NUMBER: _ClassVar[int]
    MECHANICAL_FIELD_NUMBER: _ClassVar[int]
    DIGITAL_FIELD_NUMBER: _ClassVar[int]
    SIREN_MODE_FIELD_NUMBER: _ClassVar[int]
    off: ChimePart.OffMode
    mechanical: ChimePart.MechanicalMode
    digital: ChimePart.DigitalMode
    siren_mode: ChimePart.SirenMode
    def __init__(self, off: _Optional[_Union[ChimePart.OffMode, _Mapping]] = ..., mechanical: _Optional[_Union[ChimePart.MechanicalMode, _Mapping]] = ..., digital: _Optional[_Union[ChimePart.DigitalMode, _Mapping]] = ..., siren_mode: _Optional[_Union[ChimePart.SirenMode, _Mapping]] = ...) -> None: ...

class RecordingPreferencesPart(_message.Message):
    __slots__ = ("primary_source", "nvr_source", "cloud_archive_source")
    class RecordingPreference(_message.Message):
        __slots__ = ("record_mode", "record_policy", "record_duration", "cooldown_interval")
        RECORD_MODE_FIELD_NUMBER: _ClassVar[int]
        RECORD_POLICY_FIELD_NUMBER: _ClassVar[int]
        RECORD_DURATION_FIELD_NUMBER: _ClassVar[int]
        COOLDOWN_INTERVAL_FIELD_NUMBER: _ClassVar[int]
        record_mode: _record_mode_pb2.RecordMode
        record_policy: _record_policy_pb2.RecordPolicy
        record_duration: _duration_pb2.Duration
        cooldown_interval: _duration_pb2.Duration
        def __init__(self, record_mode: _Optional[_Union[_record_mode_pb2.RecordMode, str]] = ..., record_policy: _Optional[_Union[_record_policy_pb2.RecordPolicy, str]] = ..., record_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., cooldown_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    PRIMARY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    NVR_SOURCE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_ARCHIVE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    primary_source: RecordingPreferencesPart.RecordingPreference
    nvr_source: RecordingPreferencesPart.RecordingPreference
    cloud_archive_source: RecordingPreferencesPart.RecordingPreference
    def __init__(self, primary_source: _Optional[_Union[RecordingPreferencesPart.RecordingPreference, _Mapping]] = ..., nvr_source: _Optional[_Union[RecordingPreferencesPart.RecordingPreference, _Mapping]] = ..., cloud_archive_source: _Optional[_Union[RecordingPreferencesPart.RecordingPreference, _Mapping]] = ...) -> None: ...

class NotificationSettingsPart(_message.Message):
    __slots__ = ("settings", "cooldown_period", "monitoring_state", "object_detection_duration", "confirm_detection_with_pir")
    class NotificationSettingsEntry(_message.Message):
        __slots__ = ("type", "alert_with_siren", "notification_event_type", "state")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        ALERT_WITH_SIREN_FIELD_NUMBER: _ClassVar[int]
        NOTIFICATION_EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        type: _video_notificaton_type_pb2.VideoNotificationType
        alert_with_siren: _alert_with_siren_pb2.AlertWithSiren
        notification_event_type: _notification_event_type_pb2.NotificationEventType
        state: _video_notification_state_pb2.VideoNotificationState
        def __init__(self, type: _Optional[_Union[_video_notificaton_type_pb2.VideoNotificationType, str]] = ..., alert_with_siren: _Optional[_Union[_alert_with_siren_pb2.AlertWithSiren, str]] = ..., notification_event_type: _Optional[_Union[_notification_event_type_pb2.NotificationEventType, str]] = ..., state: _Optional[_Union[_video_notification_state_pb2.VideoNotificationState, str]] = ...) -> None: ...
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    COOLDOWN_PERIOD_FIELD_NUMBER: _ClassVar[int]
    MONITORING_STATE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_DETECTION_DURATION_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_DETECTION_WITH_PIR_FIELD_NUMBER: _ClassVar[int]
    settings: _containers.RepeatedCompositeFieldContainer[NotificationSettingsPart.NotificationSettingsEntry]
    cooldown_period: _duration_pb2.Duration
    monitoring_state: _video_notification_monitoring_state_pb2.VideoNotificationMonitoringState
    object_detection_duration: _video_nofification_object_detection_duration_pb2.VideoNotificationObjectDetectionDuration
    confirm_detection_with_pir: _video_notification_confirm_detection_with_pir_state_pb2.VideoNotificationConfirmDetectionWithPirState
    def __init__(self, settings: _Optional[_Iterable[_Union[NotificationSettingsPart.NotificationSettingsEntry, _Mapping]]] = ..., cooldown_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., monitoring_state: _Optional[_Union[_video_notification_monitoring_state_pb2.VideoNotificationMonitoringState, str]] = ..., object_detection_duration: _Optional[_Union[_video_nofification_object_detection_duration_pb2.VideoNotificationObjectDetectionDuration, str]] = ..., confirm_detection_with_pir: _Optional[_Union[_video_notification_confirm_detection_with_pir_state_pb2.VideoNotificationConfirmDetectionWithPirState, str]] = ...) -> None: ...

class DetectionSettingsPart(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: _containers.RepeatedCompositeFieldContainer[_detector_settings_pb2.DetectorSettings]
    def __init__(self, settings: _Optional[_Iterable[_Union[_detector_settings_pb2.DetectorSettings, _Mapping]]] = ...) -> None: ...

class MediaSettingsPart(_message.Message):
    __slots__ = ("image_settings", "mainstream_video_stream_settings", "substream_video_stream_settings", "audio_settings", "audio_output_settings")
    IMAGE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MAINSTREAM_VIDEO_STREAM_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SUBSTREAM_VIDEO_STREAM_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_OUTPUT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    image_settings: _media_settings_pb2.ImageSettings
    mainstream_video_stream_settings: _media_settings_pb2.VideoStreamSettings
    substream_video_stream_settings: _media_settings_pb2.VideoStreamSettings
    audio_settings: _media_settings_pb2.AudioSettings
    audio_output_settings: _media_settings_pb2.AudioOutputSettings
    def __init__(self, image_settings: _Optional[_Union[_media_settings_pb2.ImageSettings, _Mapping]] = ..., mainstream_video_stream_settings: _Optional[_Union[_media_settings_pb2.VideoStreamSettings, _Mapping]] = ..., substream_video_stream_settings: _Optional[_Union[_media_settings_pb2.VideoStreamSettings, _Mapping]] = ..., audio_settings: _Optional[_Union[_media_settings_pb2.AudioSettings, _Mapping]] = ..., audio_output_settings: _Optional[_Union[_media_settings_pb2.AudioOutputSettings, _Mapping]] = ...) -> None: ...

class MotionDetectionLedIndicationPart(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class RingButtonBellPart(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...
