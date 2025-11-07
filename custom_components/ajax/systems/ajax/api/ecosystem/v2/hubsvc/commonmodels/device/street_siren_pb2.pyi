from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import alarm_restriction_pb2 as _alarm_restriction_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import alarm_verification_pb2 as _alarm_verification_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import common_siren_part_pb2 as _common_siren_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import common_standard_compliance_part_pb2 as _common_standard_compliance_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_battery_pb2 as _device_battery_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_tamper_status_pb2 as _device_tamper_status_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_temperature_pb2 as _device_temperature_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import common_jeweller_part_pb2 as _common_jeweller_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import group_association_pb2 as _group_association_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import post_alarm_indication_pb2 as _post_alarm_indication_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import external_power_pb2 as _external_power_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import gyroscope_pb2 as _gyroscope_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import radio_interference_detection_part_pb2 as _radio_interference_detection_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import common_siren_tamper_part_pb2 as _common_siren_tamper_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import common_wings_part_pb2 as _common_wings_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import light_indication_area_part_pb2 as _light_indication_area_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import common_sound_compliance_pattern_part_pb2 as _common_sound_compliance_pattern_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import bracket_state_pb2 as _bracket_state_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreetSiren(_message.Message):
    __slots__ = ("common_jeweller_part", "common_siren_part", "alarm_verification", "alarm_restriction", "post_alarm_indication_props", "device_battery", "device_temperature", "device_tamper_status", "common_standard_compliance_part", "group_association", "external_power", "gyroscope", "common_wings_part")
    COMMON_JEWELLER_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_SIREN_PART_FIELD_NUMBER: _ClassVar[int]
    ALARM_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    ALARM_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    POST_ALARM_INDICATION_PROPS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TAMPER_STATUS_FIELD_NUMBER: _ClassVar[int]
    COMMON_STANDARD_COMPLIANCE_PART_FIELD_NUMBER: _ClassVar[int]
    GROUP_ASSOCIATION_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_POWER_FIELD_NUMBER: _ClassVar[int]
    GYROSCOPE_FIELD_NUMBER: _ClassVar[int]
    COMMON_WINGS_PART_FIELD_NUMBER: _ClassVar[int]
    common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
    common_siren_part: _common_siren_part_pb2.CommonSirenPart
    alarm_verification: _alarm_verification_pb2.AlarmVerification
    alarm_restriction: _alarm_restriction_pb2.AlarmRestriction
    post_alarm_indication_props: _post_alarm_indication_pb2.PostAlarmIndication
    device_battery: _device_battery_pb2.DeviceBatteryWithoutCharging
    device_temperature: _device_temperature_pb2.DeviceTemperature
    device_tamper_status: _device_tamper_status_pb2.DeviceTamperStatus
    common_standard_compliance_part: _common_standard_compliance_part_pb2.CommonStandardCompliancePart
    group_association: _group_association_pb2.GroupAssociation
    external_power: _external_power_pb2.ExternalPower
    gyroscope: _gyroscope_pb2.Gyroscope
    common_wings_part: _common_wings_part_pb2.CommonWingsPart
    def __init__(self, common_jeweller_part: _Optional[_Union[_common_jeweller_part_pb2.CommonJewellerPart, _Mapping]] = ..., common_siren_part: _Optional[_Union[_common_siren_part_pb2.CommonSirenPart, _Mapping]] = ..., alarm_verification: _Optional[_Union[_alarm_verification_pb2.AlarmVerification, _Mapping]] = ..., alarm_restriction: _Optional[_Union[_alarm_restriction_pb2.AlarmRestriction, _Mapping]] = ..., post_alarm_indication_props: _Optional[_Union[_post_alarm_indication_pb2.PostAlarmIndication, _Mapping]] = ..., device_battery: _Optional[_Union[_device_battery_pb2.DeviceBatteryWithoutCharging, _Mapping]] = ..., device_temperature: _Optional[_Union[_device_temperature_pb2.DeviceTemperature, _Mapping]] = ..., device_tamper_status: _Optional[_Union[_device_tamper_status_pb2.DeviceTamperStatus, str]] = ..., common_standard_compliance_part: _Optional[_Union[_common_standard_compliance_part_pb2.CommonStandardCompliancePart, _Mapping]] = ..., group_association: _Optional[_Union[_group_association_pb2.GroupAssociation, _Mapping]] = ..., external_power: _Optional[_Union[_external_power_pb2.ExternalPower, _Mapping]] = ..., gyroscope: _Optional[_Union[_gyroscope_pb2.Gyroscope, _Mapping]] = ..., common_wings_part: _Optional[_Union[_common_wings_part_pb2.CommonWingsPart, _Mapping]] = ...) -> None: ...

class StreetSirenPlusG3(_message.Message):
    __slots__ = ("common_jeweller_part", "common_siren_part", "alarm_verification_part", "alarm_restriction_part", "post_alarm_indication_part", "device_battery_without_charging_part", "device_temperature_part", "common_siren_tamper_part", "common_standard_compliance_part", "group_association_part", "external_power_part", "bracket_state_part", "common_wings_part", "common_sound_compliance_pattern_part", "radio_interference_detection_part", "light_indication_area_part", "device_tamper_status")
    COMMON_JEWELLER_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_SIREN_PART_FIELD_NUMBER: _ClassVar[int]
    ALARM_VERIFICATION_PART_FIELD_NUMBER: _ClassVar[int]
    ALARM_RESTRICTION_PART_FIELD_NUMBER: _ClassVar[int]
    POST_ALARM_INDICATION_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_WITHOUT_CHARGING_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TEMPERATURE_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_SIREN_TAMPER_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_STANDARD_COMPLIANCE_PART_FIELD_NUMBER: _ClassVar[int]
    GROUP_ASSOCIATION_PART_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_POWER_PART_FIELD_NUMBER: _ClassVar[int]
    BRACKET_STATE_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_WINGS_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_SOUND_COMPLIANCE_PATTERN_PART_FIELD_NUMBER: _ClassVar[int]
    RADIO_INTERFERENCE_DETECTION_PART_FIELD_NUMBER: _ClassVar[int]
    LIGHT_INDICATION_AREA_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TAMPER_STATUS_FIELD_NUMBER: _ClassVar[int]
    common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
    common_siren_part: _common_siren_part_pb2.CommonSirenPart
    alarm_verification_part: _alarm_verification_pb2.AlarmVerification
    alarm_restriction_part: _alarm_restriction_pb2.AlarmRestriction
    post_alarm_indication_part: _post_alarm_indication_pb2.PostAlarmIndication
    device_battery_without_charging_part: _device_battery_pb2.DeviceBatteryWithoutCharging
    device_temperature_part: _device_temperature_pb2.DeviceTemperature
    common_siren_tamper_part: _common_siren_tamper_part_pb2.CommonSirenTamperPart
    common_standard_compliance_part: _common_standard_compliance_part_pb2.CommonStandardCompliancePart
    group_association_part: _group_association_pb2.GroupAssociation
    external_power_part: _external_power_pb2.ExternalPower
    bracket_state_part: _bracket_state_pb2.BracketStatePart
    common_wings_part: _common_wings_part_pb2.CommonWingsPart
    common_sound_compliance_pattern_part: _common_sound_compliance_pattern_part_pb2.CommonSoundCompliancePatternPart
    radio_interference_detection_part: _radio_interference_detection_part_pb2.RadioInterferenceDetectionPart
    light_indication_area_part: _light_indication_area_part_pb2.LightIndicationAreaPart
    device_tamper_status: _device_tamper_status_pb2.DeviceTamperStatus
    def __init__(self, common_jeweller_part: _Optional[_Union[_common_jeweller_part_pb2.CommonJewellerPart, _Mapping]] = ..., common_siren_part: _Optional[_Union[_common_siren_part_pb2.CommonSirenPart, _Mapping]] = ..., alarm_verification_part: _Optional[_Union[_alarm_verification_pb2.AlarmVerification, _Mapping]] = ..., alarm_restriction_part: _Optional[_Union[_alarm_restriction_pb2.AlarmRestriction, _Mapping]] = ..., post_alarm_indication_part: _Optional[_Union[_post_alarm_indication_pb2.PostAlarmIndication, _Mapping]] = ..., device_battery_without_charging_part: _Optional[_Union[_device_battery_pb2.DeviceBatteryWithoutCharging, _Mapping]] = ..., device_temperature_part: _Optional[_Union[_device_temperature_pb2.DeviceTemperature, _Mapping]] = ..., common_siren_tamper_part: _Optional[_Union[_common_siren_tamper_part_pb2.CommonSirenTamperPart, _Mapping]] = ..., common_standard_compliance_part: _Optional[_Union[_common_standard_compliance_part_pb2.CommonStandardCompliancePart, _Mapping]] = ..., group_association_part: _Optional[_Union[_group_association_pb2.GroupAssociation, _Mapping]] = ..., external_power_part: _Optional[_Union[_external_power_pb2.ExternalPower, _Mapping]] = ..., bracket_state_part: _Optional[_Union[_bracket_state_pb2.BracketStatePart, _Mapping]] = ..., common_wings_part: _Optional[_Union[_common_wings_part_pb2.CommonWingsPart, _Mapping]] = ..., common_sound_compliance_pattern_part: _Optional[_Union[_common_sound_compliance_pattern_part_pb2.CommonSoundCompliancePatternPart, _Mapping]] = ..., radio_interference_detection_part: _Optional[_Union[_radio_interference_detection_part_pb2.RadioInterferenceDetectionPart, _Mapping]] = ..., light_indication_area_part: _Optional[_Union[_light_indication_area_part_pb2.LightIndicationAreaPart, _Mapping]] = ..., device_tamper_status: _Optional[_Union[_device_tamper_status_pb2.DeviceTamperStatus, str]] = ...) -> None: ...
