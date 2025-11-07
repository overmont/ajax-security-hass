from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import light_indication_pb2 as _light_indication_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import common_beep_part_pb2 as _common_beep_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommonSirenPart(_message.Message):
    __slots__ = ("siren_settings", "common_beep_part", "light_indication", "siren_volume_level_capabilities", "capabilities", "extended_alarm_duration_capability")
    class ExtendedAlarmDuration(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXTENDED_ALARM_DURATION_UNSPECIFIED: _ClassVar[CommonSirenPart.ExtendedAlarmDuration]
        EXTENDED_ALARM_DURATION_NOT_SUPPORTED: _ClassVar[CommonSirenPart.ExtendedAlarmDuration]
        EXTENDED_ALARM_DURATION_RESTRICTED: _ClassVar[CommonSirenPart.ExtendedAlarmDuration]
        EXTENDED_ALARM_DURATION_ALWAYS: _ClassVar[CommonSirenPart.ExtendedAlarmDuration]
    EXTENDED_ALARM_DURATION_UNSPECIFIED: CommonSirenPart.ExtendedAlarmDuration
    EXTENDED_ALARM_DURATION_NOT_SUPPORTED: CommonSirenPart.ExtendedAlarmDuration
    EXTENDED_ALARM_DURATION_RESTRICTED: CommonSirenPart.ExtendedAlarmDuration
    EXTENDED_ALARM_DURATION_ALWAYS: CommonSirenPart.ExtendedAlarmDuration
    class SirenVolumeLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SIREN_VOLUME_LEVEL_UNSPECIFIED: _ClassVar[CommonSirenPart.SirenVolumeLevel]
        SIREN_VOLUME_LEVEL_VERY_LOUD: _ClassVar[CommonSirenPart.SirenVolumeLevel]
        SIREN_VOLUME_LEVEL_LOUD: _ClassVar[CommonSirenPart.SirenVolumeLevel]
        SIREN_VOLUME_LEVEL_QUIET: _ClassVar[CommonSirenPart.SirenVolumeLevel]
        SIREN_VOLUME_LEVEL_DISABLED: _ClassVar[CommonSirenPart.SirenVolumeLevel]
    SIREN_VOLUME_LEVEL_UNSPECIFIED: CommonSirenPart.SirenVolumeLevel
    SIREN_VOLUME_LEVEL_VERY_LOUD: CommonSirenPart.SirenVolumeLevel
    SIREN_VOLUME_LEVEL_LOUD: CommonSirenPart.SirenVolumeLevel
    SIREN_VOLUME_LEVEL_QUIET: CommonSirenPart.SirenVolumeLevel
    SIREN_VOLUME_LEVEL_DISABLED: CommonSirenPart.SirenVolumeLevel
    class Capabilities(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITIES_UNSPECIFIED: _ClassVar[CommonSirenPart.Capabilities]
        CAPABILITIES_VOLUME_TEST: _ClassVar[CommonSirenPart.Capabilities]
        CAPABILITIES_VOLUME_LIST_EXTENDED: _ClassVar[CommonSirenPart.Capabilities]
        CAPABILITIES_ALARM_DURATION_WARNING: _ClassVar[CommonSirenPart.Capabilities]
        CAPABILITIES_EXTENDED_ALARM_DURATION_SSF: _ClassVar[CommonSirenPart.Capabilities]
    CAPABILITIES_UNSPECIFIED: CommonSirenPart.Capabilities
    CAPABILITIES_VOLUME_TEST: CommonSirenPart.Capabilities
    CAPABILITIES_VOLUME_LIST_EXTENDED: CommonSirenPart.Capabilities
    CAPABILITIES_ALARM_DURATION_WARNING: CommonSirenPart.Capabilities
    CAPABILITIES_EXTENDED_ALARM_DURATION_SSF: CommonSirenPart.Capabilities
    class SirenSettings(_message.Message):
        __slots__ = ("alarm_duration", "siren_volume_level")
        ALARM_DURATION_FIELD_NUMBER: _ClassVar[int]
        SIREN_VOLUME_LEVEL_FIELD_NUMBER: _ClassVar[int]
        alarm_duration: int
        siren_volume_level: CommonSirenPart.SirenVolumeLevel
        def __init__(self, alarm_duration: _Optional[int] = ..., siren_volume_level: _Optional[_Union[CommonSirenPart.SirenVolumeLevel, str]] = ...) -> None: ...
    SIREN_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    COMMON_BEEP_PART_FIELD_NUMBER: _ClassVar[int]
    LIGHT_INDICATION_FIELD_NUMBER: _ClassVar[int]
    SIREN_VOLUME_LEVEL_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_ALARM_DURATION_CAPABILITY_FIELD_NUMBER: _ClassVar[int]
    siren_settings: CommonSirenPart.SirenSettings
    common_beep_part: _common_beep_part_pb2.CommonBeepPart
    light_indication: _light_indication_pb2.LightIndication
    siren_volume_level_capabilities: _containers.RepeatedScalarFieldContainer[CommonSirenPart.SirenVolumeLevel]
    capabilities: _containers.RepeatedScalarFieldContainer[CommonSirenPart.Capabilities]
    extended_alarm_duration_capability: CommonSirenPart.ExtendedAlarmDuration
    def __init__(self, siren_settings: _Optional[_Union[CommonSirenPart.SirenSettings, _Mapping]] = ..., common_beep_part: _Optional[_Union[_common_beep_part_pb2.CommonBeepPart, _Mapping]] = ..., light_indication: _Optional[_Union[_light_indication_pb2.LightIndication, _Mapping]] = ..., siren_volume_level_capabilities: _Optional[_Iterable[_Union[CommonSirenPart.SirenVolumeLevel, str]]] = ..., capabilities: _Optional[_Iterable[_Union[CommonSirenPart.Capabilities, str]]] = ..., extended_alarm_duration_capability: _Optional[_Union[CommonSirenPart.ExtendedAlarmDuration, str]] = ...) -> None: ...
