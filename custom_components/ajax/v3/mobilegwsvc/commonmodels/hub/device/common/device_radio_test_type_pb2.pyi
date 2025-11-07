from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceRadioTestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_RADIO_TEST_TYPE_UNSPECIFIED: _ClassVar[DeviceRadioTestType]
    DEVICE_RADIO_TEST_TYPE_JEWELER_CHANNEL: _ClassVar[DeviceRadioTestType]
    DEVICE_RADIO_TEST_TYPE_DATA_CHANNEL: _ClassVar[DeviceRadioTestType]
    DEVICE_RADIO_TEST_TYPE_VORF_CHANNEL: _ClassVar[DeviceRadioTestType]
DEVICE_RADIO_TEST_TYPE_UNSPECIFIED: DeviceRadioTestType
DEVICE_RADIO_TEST_TYPE_JEWELER_CHANNEL: DeviceRadioTestType
DEVICE_RADIO_TEST_TYPE_DATA_CHANNEL: DeviceRadioTestType
DEVICE_RADIO_TEST_TYPE_VORF_CHANNEL: DeviceRadioTestType
