from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import common_jeweller_part_pb2 as _common_jeweller_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import common_wings_part_pb2 as _common_wings_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.smartlock import smart_lock_part_pb2 as _smart_lock_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.smartlock import smart_lock_yale_part_pb2 as _smart_lock_yale_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_battery_pb2 as _device_battery_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SmartLockYale(_message.Message):
    __slots__ = ("common_jeweller_part", "smart_lock_part", "smart_lock_yale_part", "common_wings_part", "device_battery")
    COMMON_JEWELLER_PART_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_PART_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_YALE_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_WINGS_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_FIELD_NUMBER: _ClassVar[int]
    common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
    smart_lock_part: _smart_lock_part_pb2.SmartLockPart
    smart_lock_yale_part: _smart_lock_yale_part_pb2.SmartLockYalePart
    common_wings_part: _common_wings_part_pb2.CommonWingsPart
    device_battery: _device_battery_pb2.DeviceBatteryWithoutCharging
    def __init__(self, common_jeweller_part: _Optional[_Union[_common_jeweller_part_pb2.CommonJewellerPart, _Mapping]] = ..., smart_lock_part: _Optional[_Union[_smart_lock_part_pb2.SmartLockPart, _Mapping]] = ..., smart_lock_yale_part: _Optional[_Union[_smart_lock_yale_part_pb2.SmartLockYalePart, _Mapping]] = ..., common_wings_part: _Optional[_Union[_common_wings_part_pb2.CommonWingsPart, _Mapping]] = ..., device_battery: _Optional[_Union[_device_battery_pb2.DeviceBatteryWithoutCharging, _Mapping]] = ...) -> None: ...
