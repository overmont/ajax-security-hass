from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceAppearance(_message.Message):
    __slots__ = ("device_appearance_type",)
    class DeviceAppearanceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEVICE_APPEARANCE_TYPE_UNSPECIFIED: _ClassVar[DeviceAppearance.DeviceAppearanceType]
        DEVICE_APPEARANCE_TYPE_ORDINARY: _ClassVar[DeviceAppearance.DeviceAppearanceType]
        DEVICE_APPEARANCE_TYPE_UK: _ClassVar[DeviceAppearance.DeviceAppearanceType]
    DEVICE_APPEARANCE_TYPE_UNSPECIFIED: DeviceAppearance.DeviceAppearanceType
    DEVICE_APPEARANCE_TYPE_ORDINARY: DeviceAppearance.DeviceAppearanceType
    DEVICE_APPEARANCE_TYPE_UK: DeviceAppearance.DeviceAppearanceType
    DEVICE_APPEARANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    device_appearance_type: DeviceAppearance.DeviceAppearanceType
    def __init__(self, device_appearance_type: _Optional[_Union[DeviceAppearance.DeviceAppearanceType, str]] = ...) -> None: ...
