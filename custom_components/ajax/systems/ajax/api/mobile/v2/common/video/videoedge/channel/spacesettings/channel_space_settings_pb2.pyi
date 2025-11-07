from systems.ajax.api.ecosystem.v2.commonmodels.device.common import common_arming_part_pb2 as _common_arming_part_pb2
from systems.ajax.api.mobile.v2.common.space.device import device_arming_mode_pb2 as _device_arming_mode_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChannelSpaceSettings(_message.Message):
    __slots__ = ("room_id", "group_id", "arm_in_night_mode", "device_arming_mode", "arming_capabilities")
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ARM_IN_NIGHT_MODE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ARMING_MODE_FIELD_NUMBER: _ClassVar[int]
    ARMING_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    room_id: str
    group_id: str
    arm_in_night_mode: bool
    device_arming_mode: _device_arming_mode_pb2.DeviceArmingMode
    arming_capabilities: _containers.RepeatedScalarFieldContainer[_common_arming_part_pb2.CommonArmingPart.ArmingCapability]
    def __init__(self, room_id: _Optional[str] = ..., group_id: _Optional[str] = ..., arm_in_night_mode: bool = ..., device_arming_mode: _Optional[_Union[_device_arming_mode_pb2.DeviceArmingMode, _Mapping]] = ..., arming_capabilities: _Optional[_Iterable[_Union[_common_arming_part_pb2.CommonArmingPart.ArmingCapability, str]]] = ...) -> None: ...
