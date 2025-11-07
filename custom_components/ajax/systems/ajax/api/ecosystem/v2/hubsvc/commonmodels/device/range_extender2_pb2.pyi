from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import common_jeweller_part_pb2 as _common_jeweller_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import common_wings_part_pb2 as _common_wings_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_battery_pb2 as _device_battery_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_tamper_status_pb2 as _device_tamper_status_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import external_power_pb2 as _external_power_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import jeweller_communication_part_pb2 as _jeweller_communication_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import malfunction_badge_part_pb2 as _malfunction_badge_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import ethernet_part_pb2 as _ethernet_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.rangeextender import main_chanel_connection_pb2 as _main_chanel_connection_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RangeExtender2(_message.Message):
    __slots__ = ("common_jeweller_part", "common_wings_part", "device_battery_part", "device_tamper_status", "external_power_part", "malfunction_badge_part", "main_chanel_connection_part", "ethernet_part")
    COMMON_JEWELLER_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_WINGS_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TAMPER_STATUS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_POWER_PART_FIELD_NUMBER: _ClassVar[int]
    MALFUNCTION_BADGE_PART_FIELD_NUMBER: _ClassVar[int]
    MAIN_CHANEL_CONNECTION_PART_FIELD_NUMBER: _ClassVar[int]
    ETHERNET_PART_FIELD_NUMBER: _ClassVar[int]
    common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
    common_wings_part: _common_wings_part_pb2.CommonWingsPart
    device_battery_part: _device_battery_pb2.DeviceBattery
    device_tamper_status: _device_tamper_status_pb2.DeviceTamperStatus
    external_power_part: _external_power_pb2.ExternalPower
    malfunction_badge_part: _malfunction_badge_part_pb2.MalfunctionBadgePart
    main_chanel_connection_part: _main_chanel_connection_pb2.MainChanelConnectionPart
    ethernet_part: _ethernet_part_pb2.EthernetPart
    def __init__(self, common_jeweller_part: _Optional[_Union[_common_jeweller_part_pb2.CommonJewellerPart, _Mapping]] = ..., common_wings_part: _Optional[_Union[_common_wings_part_pb2.CommonWingsPart, _Mapping]] = ..., device_battery_part: _Optional[_Union[_device_battery_pb2.DeviceBattery, _Mapping]] = ..., device_tamper_status: _Optional[_Union[_device_tamper_status_pb2.DeviceTamperStatus, str]] = ..., external_power_part: _Optional[_Union[_external_power_pb2.ExternalPower, _Mapping]] = ..., malfunction_badge_part: _Optional[_Union[_malfunction_badge_part_pb2.MalfunctionBadgePart, _Mapping]] = ..., main_chanel_connection_part: _Optional[_Union[_main_chanel_connection_pb2.MainChanelConnectionPart, _Mapping]] = ..., ethernet_part: _Optional[_Union[_ethernet_part_pb2.EthernetPart, _Mapping]] = ...) -> None: ...

class RangeExtender2Fire(_message.Message):
    __slots__ = ("common_jeweller_part", "common_wings_part", "device_battery_without_charging_part", "device_tamper_status", "external_power_part", "malfunction_badge_part", "main_chanel_connection_part", "ethernet_part")
    COMMON_JEWELLER_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_WINGS_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_WITHOUT_CHARGING_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TAMPER_STATUS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_POWER_PART_FIELD_NUMBER: _ClassVar[int]
    MALFUNCTION_BADGE_PART_FIELD_NUMBER: _ClassVar[int]
    MAIN_CHANEL_CONNECTION_PART_FIELD_NUMBER: _ClassVar[int]
    ETHERNET_PART_FIELD_NUMBER: _ClassVar[int]
    common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
    common_wings_part: _common_wings_part_pb2.CommonWingsPart
    device_battery_without_charging_part: _device_battery_pb2.DeviceBatteryWithoutCharging
    device_tamper_status: _device_tamper_status_pb2.DeviceTamperStatus
    external_power_part: _external_power_pb2.ExternalPower
    malfunction_badge_part: _malfunction_badge_part_pb2.MalfunctionBadgePart
    main_chanel_connection_part: _main_chanel_connection_pb2.MainChanelConnectionPart
    ethernet_part: _ethernet_part_pb2.EthernetPart
    def __init__(self, common_jeweller_part: _Optional[_Union[_common_jeweller_part_pb2.CommonJewellerPart, _Mapping]] = ..., common_wings_part: _Optional[_Union[_common_wings_part_pb2.CommonWingsPart, _Mapping]] = ..., device_battery_without_charging_part: _Optional[_Union[_device_battery_pb2.DeviceBatteryWithoutCharging, _Mapping]] = ..., device_tamper_status: _Optional[_Union[_device_tamper_status_pb2.DeviceTamperStatus, str]] = ..., external_power_part: _Optional[_Union[_external_power_pb2.ExternalPower, _Mapping]] = ..., malfunction_badge_part: _Optional[_Union[_malfunction_badge_part_pb2.MalfunctionBadgePart, _Mapping]] = ..., main_chanel_connection_part: _Optional[_Union[_main_chanel_connection_pb2.MainChanelConnectionPart, _Mapping]] = ..., ethernet_part: _Optional[_Union[_ethernet_part_pb2.EthernetPart, _Mapping]] = ...) -> None: ...

class RangeExtender2S(_message.Message):
    __slots__ = ("common_jeweller_part", "common_wings_part", "device_battery", "device_tamper_status", "external_power_part", "jeweller_communication_part", "malfunction_badge_part", "main_chanel_connection_part", "ethernet_part")
    COMMON_JEWELLER_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_WINGS_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TAMPER_STATUS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_POWER_PART_FIELD_NUMBER: _ClassVar[int]
    JEWELLER_COMMUNICATION_PART_FIELD_NUMBER: _ClassVar[int]
    MALFUNCTION_BADGE_PART_FIELD_NUMBER: _ClassVar[int]
    MAIN_CHANEL_CONNECTION_PART_FIELD_NUMBER: _ClassVar[int]
    ETHERNET_PART_FIELD_NUMBER: _ClassVar[int]
    common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
    common_wings_part: _common_wings_part_pb2.CommonWingsPart
    device_battery: _device_battery_pb2.DeviceBattery
    device_tamper_status: _device_tamper_status_pb2.DeviceTamperStatus
    external_power_part: _external_power_pb2.ExternalPower
    jeweller_communication_part: _jeweller_communication_part_pb2.JewellerCommunicationPart
    malfunction_badge_part: _malfunction_badge_part_pb2.MalfunctionBadgePart
    main_chanel_connection_part: _main_chanel_connection_pb2.MainChanelConnectionPart
    ethernet_part: _ethernet_part_pb2.EthernetPart
    def __init__(self, common_jeweller_part: _Optional[_Union[_common_jeweller_part_pb2.CommonJewellerPart, _Mapping]] = ..., common_wings_part: _Optional[_Union[_common_wings_part_pb2.CommonWingsPart, _Mapping]] = ..., device_battery: _Optional[_Union[_device_battery_pb2.DeviceBattery, _Mapping]] = ..., device_tamper_status: _Optional[_Union[_device_tamper_status_pb2.DeviceTamperStatus, str]] = ..., external_power_part: _Optional[_Union[_external_power_pb2.ExternalPower, _Mapping]] = ..., jeweller_communication_part: _Optional[_Union[_jeweller_communication_part_pb2.JewellerCommunicationPart, _Mapping]] = ..., malfunction_badge_part: _Optional[_Union[_malfunction_badge_part_pb2.MalfunctionBadgePart, _Mapping]] = ..., main_chanel_connection_part: _Optional[_Union[_main_chanel_connection_pb2.MainChanelConnectionPart, _Mapping]] = ..., ethernet_part: _Optional[_Union[_ethernet_part_pb2.EthernetPart, _Mapping]] = ...) -> None: ...
