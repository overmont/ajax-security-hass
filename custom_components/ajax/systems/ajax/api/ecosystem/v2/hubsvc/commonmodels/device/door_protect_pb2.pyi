from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import common_door_protect_part_pb2 as _common_door_protect_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import common_jeweller_part_pb2 as _common_jeweller_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_battery_pb2 as _device_battery_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import fast_tamper_pb2 as _fast_tamper_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import fast_tamper_part_pb2 as _fast_tamper_part_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DoorProtect(_message.Message):
    __slots__ = ("common_jeweller_part", "common_door_protect_part", "device_battery", "deprecated_siren_triggers", "deprecated_chime_triggers")
    class DeprecatedSirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEPRECATED_SIREN_TRIGGER_UNSPECIFIED: _ClassVar[DoorProtect.DeprecatedSirenTrigger]
        DEPRECATED_SIREN_TRIGGER_REED: _ClassVar[DoorProtect.DeprecatedSirenTrigger]
        DEPRECATED_SIREN_TRIGGER_EXTRA_CONTACT: _ClassVar[DoorProtect.DeprecatedSirenTrigger]
    DEPRECATED_SIREN_TRIGGER_UNSPECIFIED: DoorProtect.DeprecatedSirenTrigger
    DEPRECATED_SIREN_TRIGGER_REED: DoorProtect.DeprecatedSirenTrigger
    DEPRECATED_SIREN_TRIGGER_EXTRA_CONTACT: DoorProtect.DeprecatedSirenTrigger
    class DeprecatedChimeTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEPRECATED_CHIME_TRIGGER_UNSPECIFIED: _ClassVar[DoorProtect.DeprecatedChimeTrigger]
        DEPRECATED_CHIME_TRIGGER_REED: _ClassVar[DoorProtect.DeprecatedChimeTrigger]
        DEPRECATED_CHIME_TRIGGER_EXTRA_CONTACT: _ClassVar[DoorProtect.DeprecatedChimeTrigger]
    DEPRECATED_CHIME_TRIGGER_UNSPECIFIED: DoorProtect.DeprecatedChimeTrigger
    DEPRECATED_CHIME_TRIGGER_REED: DoorProtect.DeprecatedChimeTrigger
    DEPRECATED_CHIME_TRIGGER_EXTRA_CONTACT: DoorProtect.DeprecatedChimeTrigger
    COMMON_JEWELLER_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_DOOR_PROTECT_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_CHIME_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
    common_door_protect_part: _common_door_protect_part_pb2.CommonDoorProtectPart
    device_battery: _device_battery_pb2.DeviceBattery
    deprecated_siren_triggers: _containers.RepeatedScalarFieldContainer[DoorProtect.DeprecatedSirenTrigger]
    deprecated_chime_triggers: _containers.RepeatedScalarFieldContainer[DoorProtect.DeprecatedChimeTrigger]
    def __init__(self, common_jeweller_part: _Optional[_Union[_common_jeweller_part_pb2.CommonJewellerPart, _Mapping]] = ..., common_door_protect_part: _Optional[_Union[_common_door_protect_part_pb2.CommonDoorProtectPart, _Mapping]] = ..., device_battery: _Optional[_Union[_device_battery_pb2.DeviceBattery, _Mapping]] = ..., deprecated_siren_triggers: _Optional[_Iterable[_Union[DoorProtect.DeprecatedSirenTrigger, str]]] = ..., deprecated_chime_triggers: _Optional[_Iterable[_Union[DoorProtect.DeprecatedChimeTrigger, str]]] = ...) -> None: ...

class DoorProtectS(_message.Message):
    __slots__ = ("common_jeweller_part", "common_door_protect_part", "device_battery", "fast_tamper_part", "deprecated_siren_triggers", "deprecated_chime_triggers", "fast_tamper")
    class DeprecatedSirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEPRECATED_SIREN_TRIGGER_UNSPECIFIED: _ClassVar[DoorProtectS.DeprecatedSirenTrigger]
        DEPRECATED_SIREN_TRIGGER_REED: _ClassVar[DoorProtectS.DeprecatedSirenTrigger]
        DEPRECATED_SIREN_TRIGGER_EXTRA_CONTACT: _ClassVar[DoorProtectS.DeprecatedSirenTrigger]
    DEPRECATED_SIREN_TRIGGER_UNSPECIFIED: DoorProtectS.DeprecatedSirenTrigger
    DEPRECATED_SIREN_TRIGGER_REED: DoorProtectS.DeprecatedSirenTrigger
    DEPRECATED_SIREN_TRIGGER_EXTRA_CONTACT: DoorProtectS.DeprecatedSirenTrigger
    class DeprecatedChimeTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEPRECATED_CHIME_TRIGGER_UNSPECIFIED: _ClassVar[DoorProtectS.DeprecatedChimeTrigger]
        DEPRECATED_CHIME_TRIGGER_REED: _ClassVar[DoorProtectS.DeprecatedChimeTrigger]
        DEPRECATED_CHIME_TRIGGER_EXTRA_CONTACT: _ClassVar[DoorProtectS.DeprecatedChimeTrigger]
    DEPRECATED_CHIME_TRIGGER_UNSPECIFIED: DoorProtectS.DeprecatedChimeTrigger
    DEPRECATED_CHIME_TRIGGER_REED: DoorProtectS.DeprecatedChimeTrigger
    DEPRECATED_CHIME_TRIGGER_EXTRA_CONTACT: DoorProtectS.DeprecatedChimeTrigger
    COMMON_JEWELLER_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_DOOR_PROTECT_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_FIELD_NUMBER: _ClassVar[int]
    FAST_TAMPER_PART_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_CHIME_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    FAST_TAMPER_FIELD_NUMBER: _ClassVar[int]
    common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
    common_door_protect_part: _common_door_protect_part_pb2.CommonDoorProtectPart
    device_battery: _device_battery_pb2.DeviceBattery
    fast_tamper_part: _fast_tamper_part_pb2.FastTamperPart
    deprecated_siren_triggers: _containers.RepeatedScalarFieldContainer[DoorProtectS.DeprecatedSirenTrigger]
    deprecated_chime_triggers: _containers.RepeatedScalarFieldContainer[DoorProtectS.DeprecatedChimeTrigger]
    fast_tamper: _fast_tamper_pb2.FastTamper
    def __init__(self, common_jeweller_part: _Optional[_Union[_common_jeweller_part_pb2.CommonJewellerPart, _Mapping]] = ..., common_door_protect_part: _Optional[_Union[_common_door_protect_part_pb2.CommonDoorProtectPart, _Mapping]] = ..., device_battery: _Optional[_Union[_device_battery_pb2.DeviceBattery, _Mapping]] = ..., fast_tamper_part: _Optional[_Union[_fast_tamper_part_pb2.FastTamperPart, _Mapping]] = ..., deprecated_siren_triggers: _Optional[_Iterable[_Union[DoorProtectS.DeprecatedSirenTrigger, str]]] = ..., deprecated_chime_triggers: _Optional[_Iterable[_Union[DoorProtectS.DeprecatedChimeTrigger, str]]] = ..., fast_tamper: _Optional[_Union[_fast_tamper_pb2.FastTamper, _Mapping]] = ...) -> None: ...
