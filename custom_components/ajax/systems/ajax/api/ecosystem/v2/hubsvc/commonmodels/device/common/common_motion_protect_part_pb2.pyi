from systems.ajax.api.ecosystem.v2.commonmodels.device.common import common_arming_part_pb2 as _common_arming_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_tamper_status_pb2 as _device_tamper_status_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_temperature_pb2 as _device_temperature_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import sensitivity_part_pb2 as _sensitivity_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_siren_triggers_pb2 as _device_siren_triggers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommonMotionProtectPart(_message.Message):
    __slots__ = ("common_arming_part", "device_temperature", "sensitivity_part", "device_tamper_status", "siren_triggers")
    COMMON_ARMING_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    SENSITIVITY_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TAMPER_STATUS_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    common_arming_part: _common_arming_part_pb2.CommonArmingPart
    device_temperature: _device_temperature_pb2.DeviceTemperature
    sensitivity_part: _sensitivity_part_pb2.SensitivityPart
    device_tamper_status: _device_tamper_status_pb2.DeviceTamperStatus
    siren_triggers: _device_siren_triggers_pb2.SirenTriggers
    def __init__(self, common_arming_part: _Optional[_Union[_common_arming_part_pb2.CommonArmingPart, _Mapping]] = ..., device_temperature: _Optional[_Union[_device_temperature_pb2.DeviceTemperature, _Mapping]] = ..., sensitivity_part: _Optional[_Union[_sensitivity_part_pb2.SensitivityPart, _Mapping]] = ..., device_tamper_status: _Optional[_Union[_device_tamper_status_pb2.DeviceTamperStatus, str]] = ..., siren_triggers: _Optional[_Union[_device_siren_triggers_pb2.SirenTriggers, _Mapping]] = ...) -> None: ...
