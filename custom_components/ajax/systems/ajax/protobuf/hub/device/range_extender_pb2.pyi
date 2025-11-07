from google.protobuf import wrappers_pb2 as _wrappers_pb2
from systems.ajax.protobuf.hub.device import common_device_pb2 as _common_device_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RangeExtender(_message.Message):
    __slots__ = ("common_part", "externally_powered", "auto_assign_devices_mode_enabled", "led_brightness_level", "new_firmware_version_available", "latest_available_firmware_version", "avg_noise_level_value_channel1", "avg_noise_level_value_channel2", "subtype")
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[RangeExtender.Subtype]
    NO_SUBTYPE: RangeExtender.Subtype
    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    EXTERNALLY_POWERED_FIELD_NUMBER: _ClassVar[int]
    AUTO_ASSIGN_DEVICES_MODE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LED_BRIGHTNESS_LEVEL_FIELD_NUMBER: _ClassVar[int]
    NEW_FIRMWARE_VERSION_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    LATEST_AVAILABLE_FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    AVG_NOISE_LEVEL_VALUE_CHANNEL1_FIELD_NUMBER: _ClassVar[int]
    AVG_NOISE_LEVEL_VALUE_CHANNEL2_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    externally_powered: _wrappers_pb2.BoolValue
    auto_assign_devices_mode_enabled: _wrappers_pb2.BoolValue
    led_brightness_level: int
    new_firmware_version_available: _wrappers_pb2.BoolValue
    latest_available_firmware_version: _wrappers_pb2.Int32Value
    avg_noise_level_value_channel1: _wrappers_pb2.Int32Value
    avg_noise_level_value_channel2: _wrappers_pb2.Int32Value
    subtype: RangeExtender.Subtype
    def __init__(self, common_part: _Optional[_Union[_common_device_pb2.CommonDevicePart, _Mapping]] = ..., externally_powered: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., auto_assign_devices_mode_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., led_brightness_level: _Optional[int] = ..., new_firmware_version_available: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., latest_available_firmware_version: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., avg_noise_level_value_channel1: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., avg_noise_level_value_channel2: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., subtype: _Optional[_Union[RangeExtender.Subtype, str]] = ...) -> None: ...
