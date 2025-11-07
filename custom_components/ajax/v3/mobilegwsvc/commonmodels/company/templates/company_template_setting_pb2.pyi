from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import common_parts_pb2 as _common_parts_pb2
from systems.ajax.api.ecosystem.v2.commonmodels.device.common.type import device_type_pb2 as _device_type_pb2
from systems.ajax.api.ecosystem.v2.commonmodels.device.common import common_arming_part_pb2 as _common_arming_part_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompanyTemplateSetting(_message.Message):
    __slots__ = ("type", "company_connection_details", "company_connection_type", "video_connection_type", "video_archive", "local_users", "time_zone", "led_brightness", "fan_settings", "cloud_connection", "onvif_connection", "recording_preferences", "media_settings", "chime", "notification_settings", "detection_settings", "common_arming_part_settings", "ring_button_sound", "motion_detection_led_indication")
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[CompanyTemplateSetting.Mode]
        MODE_GENERIC: _ClassVar[CompanyTemplateSetting.Mode]
        MODE_PEER_TO_PEER: _ClassVar[CompanyTemplateSetting.Mode]
        MODE_AJAX_SIP: _ClassVar[CompanyTemplateSetting.Mode]
    MODE_UNSPECIFIED: CompanyTemplateSetting.Mode
    MODE_GENERIC: CompanyTemplateSetting.Mode
    MODE_PEER_TO_PEER: CompanyTemplateSetting.Mode
    MODE_AJAX_SIP: CompanyTemplateSetting.Mode
    class CompanyConnectionDetails(_message.Message):
        __slots__ = ("company_name", "company_number", "address", "port", "stun_address", "stun_port", "connection_type")
        class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            MODE_UNSPECIFIED: _ClassVar[CompanyTemplateSetting.CompanyConnectionDetails.Mode]
            MODE_GENERIC: _ClassVar[CompanyTemplateSetting.CompanyConnectionDetails.Mode]
            MODE_PEER_TO_PEER: _ClassVar[CompanyTemplateSetting.CompanyConnectionDetails.Mode]
            MODE_AJAX_SIP: _ClassVar[CompanyTemplateSetting.CompanyConnectionDetails.Mode]
        MODE_UNSPECIFIED: CompanyTemplateSetting.CompanyConnectionDetails.Mode
        MODE_GENERIC: CompanyTemplateSetting.CompanyConnectionDetails.Mode
        MODE_PEER_TO_PEER: CompanyTemplateSetting.CompanyConnectionDetails.Mode
        MODE_AJAX_SIP: CompanyTemplateSetting.CompanyConnectionDetails.Mode
        COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
        COMPANY_NUMBER_FIELD_NUMBER: _ClassVar[int]
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        PORT_FIELD_NUMBER: _ClassVar[int]
        STUN_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        STUN_PORT_FIELD_NUMBER: _ClassVar[int]
        CONNECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
        company_name: str
        company_number: str
        address: str
        port: int
        stun_address: str
        stun_port: int
        connection_type: CompanyTemplateSetting.CompanyConnectionDetails.Mode
        def __init__(self, company_name: _Optional[str] = ..., company_number: _Optional[str] = ..., address: _Optional[str] = ..., port: _Optional[int] = ..., stun_address: _Optional[str] = ..., stun_port: _Optional[int] = ..., connection_type: _Optional[_Union[CompanyTemplateSetting.CompanyConnectionDetails.Mode, str]] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COMPANY_CONNECTION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    COMPANY_CONNECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_CONNECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    LOCAL_USERS_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    LED_BRIGHTNESS_FIELD_NUMBER: _ClassVar[int]
    FAN_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    ONVIF_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    RECORDING_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    MEDIA_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CHIME_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DETECTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    COMMON_ARMING_PART_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    RING_BUTTON_SOUND_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTION_LED_INDICATION_FIELD_NUMBER: _ClassVar[int]
    type: _device_type_pb2.DeviceType
    company_connection_details: CompanyTemplateSetting.CompanyConnectionDetails
    company_connection_type: CompanyTemplateSetting.Mode
    video_connection_type: _common_parts_pb2.VideoConnectionTypePart
    video_archive: _common_parts_pb2.VideoArchivePart
    local_users: _common_parts_pb2.VideoLocalUsersPart
    time_zone: _common_parts_pb2.TimeZonePart
    led_brightness: _common_parts_pb2.LogoLedBrightnessPart
    fan_settings: _common_parts_pb2.FanSettingsPart
    cloud_connection: _common_parts_pb2.CloudConnectionPart
    onvif_connection: _common_parts_pb2.OnvifConnectionPart
    recording_preferences: _common_parts_pb2.RecordingPreferencesPart
    media_settings: _common_parts_pb2.MediaSettingsPart
    chime: _common_parts_pb2.ChimePart
    notification_settings: _common_parts_pb2.NotificationSettingsPart
    detection_settings: _common_parts_pb2.DetectionSettingsPart
    common_arming_part_settings: _common_arming_part_pb2.CommonArmingPart.CommonArmingPartSettings
    ring_button_sound: _common_parts_pb2.RingButtonSoundPart
    motion_detection_led_indication: _common_parts_pb2.MotionDetectionLedIndicationPart
    def __init__(self, type: _Optional[_Union[_device_type_pb2.DeviceType, _Mapping]] = ..., company_connection_details: _Optional[_Union[CompanyTemplateSetting.CompanyConnectionDetails, _Mapping]] = ..., company_connection_type: _Optional[_Union[CompanyTemplateSetting.Mode, str]] = ..., video_connection_type: _Optional[_Union[_common_parts_pb2.VideoConnectionTypePart, _Mapping]] = ..., video_archive: _Optional[_Union[_common_parts_pb2.VideoArchivePart, _Mapping]] = ..., local_users: _Optional[_Union[_common_parts_pb2.VideoLocalUsersPart, _Mapping]] = ..., time_zone: _Optional[_Union[_common_parts_pb2.TimeZonePart, _Mapping]] = ..., led_brightness: _Optional[_Union[_common_parts_pb2.LogoLedBrightnessPart, _Mapping]] = ..., fan_settings: _Optional[_Union[_common_parts_pb2.FanSettingsPart, _Mapping]] = ..., cloud_connection: _Optional[_Union[_common_parts_pb2.CloudConnectionPart, _Mapping]] = ..., onvif_connection: _Optional[_Union[_common_parts_pb2.OnvifConnectionPart, _Mapping]] = ..., recording_preferences: _Optional[_Union[_common_parts_pb2.RecordingPreferencesPart, _Mapping]] = ..., media_settings: _Optional[_Union[_common_parts_pb2.MediaSettingsPart, _Mapping]] = ..., chime: _Optional[_Union[_common_parts_pb2.ChimePart, _Mapping]] = ..., notification_settings: _Optional[_Union[_common_parts_pb2.NotificationSettingsPart, _Mapping]] = ..., detection_settings: _Optional[_Union[_common_parts_pb2.DetectionSettingsPart, _Mapping]] = ..., common_arming_part_settings: _Optional[_Union[_common_arming_part_pb2.CommonArmingPart.CommonArmingPartSettings, _Mapping]] = ..., ring_button_sound: _Optional[_Union[_common_parts_pb2.RingButtonSoundPart, _Mapping]] = ..., motion_detection_led_indication: _Optional[_Union[_common_parts_pb2.MotionDetectionLedIndicationPart, _Mapping]] = ...) -> None: ...
