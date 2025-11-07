from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import alarm_restriction_pb2 as _alarm_restriction_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import alarm_verification_pb2 as _alarm_verification_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import bracket_state_pb2 as _bracket_state_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import common_siren_part_pb2 as _common_siren_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import common_standard_compliance_part_pb2 as _common_standard_compliance_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_battery_pb2 as _device_battery_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_tamper_status_pb2 as _device_tamper_status_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_temperature_pb2 as _device_temperature_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import common_fibra_part_pb2 as _common_fibra_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import group_association_pb2 as _group_association_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import post_alarm_indication_pb2 as _post_alarm_indication_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeSirenFibra(_message.Message):
    __slots__ = ("common_fibra_part", "common_siren_part", "alarm_verification", "alarm_restriction", "post_alarm_indication_props", "bracket_state_part", "device_battery", "device_temperature", "device_tamper_status", "common_standard_compliance_part", "group_association")
    COMMON_FIBRA_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_SIREN_PART_FIELD_NUMBER: _ClassVar[int]
    ALARM_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    ALARM_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    POST_ALARM_INDICATION_PROPS_FIELD_NUMBER: _ClassVar[int]
    BRACKET_STATE_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TAMPER_STATUS_FIELD_NUMBER: _ClassVar[int]
    COMMON_STANDARD_COMPLIANCE_PART_FIELD_NUMBER: _ClassVar[int]
    GROUP_ASSOCIATION_FIELD_NUMBER: _ClassVar[int]
    common_fibra_part: _common_fibra_part_pb2.CommonFibraPart
    common_siren_part: _common_siren_part_pb2.CommonSirenPart
    alarm_verification: _alarm_verification_pb2.AlarmVerification
    alarm_restriction: _alarm_restriction_pb2.AlarmRestriction
    post_alarm_indication_props: _post_alarm_indication_pb2.PostAlarmIndication
    bracket_state_part: _bracket_state_pb2.BracketStatePart
    device_battery: _device_battery_pb2.DeviceBatteryWithoutCharging
    device_temperature: _device_temperature_pb2.DeviceTemperature
    device_tamper_status: _device_tamper_status_pb2.DeviceTamperStatus
    common_standard_compliance_part: _common_standard_compliance_part_pb2.CommonStandardCompliancePart
    group_association: _group_association_pb2.GroupAssociation
    def __init__(self, common_fibra_part: _Optional[_Union[_common_fibra_part_pb2.CommonFibraPart, _Mapping]] = ..., common_siren_part: _Optional[_Union[_common_siren_part_pb2.CommonSirenPart, _Mapping]] = ..., alarm_verification: _Optional[_Union[_alarm_verification_pb2.AlarmVerification, _Mapping]] = ..., alarm_restriction: _Optional[_Union[_alarm_restriction_pb2.AlarmRestriction, _Mapping]] = ..., post_alarm_indication_props: _Optional[_Union[_post_alarm_indication_pb2.PostAlarmIndication, _Mapping]] = ..., bracket_state_part: _Optional[_Union[_bracket_state_pb2.BracketStatePart, _Mapping]] = ..., device_battery: _Optional[_Union[_device_battery_pb2.DeviceBatteryWithoutCharging, _Mapping]] = ..., device_temperature: _Optional[_Union[_device_temperature_pb2.DeviceTemperature, _Mapping]] = ..., device_tamper_status: _Optional[_Union[_device_tamper_status_pb2.DeviceTamperStatus, str]] = ..., common_standard_compliance_part: _Optional[_Union[_common_standard_compliance_part_pb2.CommonStandardCompliancePart, _Mapping]] = ..., group_association: _Optional[_Union[_group_association_pb2.GroupAssociation, _Mapping]] = ...) -> None: ...
