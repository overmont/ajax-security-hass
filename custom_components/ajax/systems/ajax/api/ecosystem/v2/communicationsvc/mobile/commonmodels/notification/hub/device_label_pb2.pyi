from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceLabel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_LABEL_UNSPECIFIED: _ClassVar[DeviceLabel]
    DEVICE_LABEL_AJAX: _ClassVar[DeviceLabel]
    DEVICE_LABEL_WHITE_LABEL: _ClassVar[DeviceLabel]
DEVICE_LABEL_UNSPECIFIED: DeviceLabel
DEVICE_LABEL_AJAX: DeviceLabel
DEVICE_LABEL_WHITE_LABEL: DeviceLabel
