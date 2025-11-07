from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PhotoOnDemandDevices(_message.Message):
    __slots__ = ("devices",)
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[PhotoOnDemandDevice]
    def __init__(self, devices: _Optional[_Iterable[_Union[PhotoOnDemandDevice, _Mapping]]] = ...) -> None: ...

class PhotoOnDemandDevice(_message.Message):
    __slots__ = ("device_id", "device_type")
    class DeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEVICE_TYPE_UNSPECIFIED: _ClassVar[PhotoOnDemandDevice.DeviceType]
        DEVICE_TYPE_MOTION_CAM: _ClassVar[PhotoOnDemandDevice.DeviceType]
        DEVICE_TYPE_MOTION_CAM_OUTDOOR: _ClassVar[PhotoOnDemandDevice.DeviceType]
        DEVICE_TYPE_MOTION_CAM_PHOD: _ClassVar[PhotoOnDemandDevice.DeviceType]
        DEVICE_TYPE_MOTION_CAM_OUTDOOR_PHOD: _ClassVar[PhotoOnDemandDevice.DeviceType]
        DEVICE_TYPE_MOTION_CAM_PHOD_FIBRA: _ClassVar[PhotoOnDemandDevice.DeviceType]
        DEVICE_TYPE_MOTION_CAM_OUTDOOR_TWO_FOUR_PHOD: _ClassVar[PhotoOnDemandDevice.DeviceType]
        DEVICE_TYPE_MOTION_CAM_S_PHOD: _ClassVar[PhotoOnDemandDevice.DeviceType]
        DEVICE_TYPE_MOTION_CAM_S_PHOD_AM: _ClassVar[PhotoOnDemandDevice.DeviceType]
        DEVICE_TYPE_MOTION_CAM_SUPERIOR_PHOD: _ClassVar[PhotoOnDemandDevice.DeviceType]
        DEVICE_TYPE_MOTION_CAM_G3: _ClassVar[PhotoOnDemandDevice.DeviceType]
        DEVICE_TYPE_CURTAIN_CAM_OUTDOOR_HM_PHOD: _ClassVar[PhotoOnDemandDevice.DeviceType]
    DEVICE_TYPE_UNSPECIFIED: PhotoOnDemandDevice.DeviceType
    DEVICE_TYPE_MOTION_CAM: PhotoOnDemandDevice.DeviceType
    DEVICE_TYPE_MOTION_CAM_OUTDOOR: PhotoOnDemandDevice.DeviceType
    DEVICE_TYPE_MOTION_CAM_PHOD: PhotoOnDemandDevice.DeviceType
    DEVICE_TYPE_MOTION_CAM_OUTDOOR_PHOD: PhotoOnDemandDevice.DeviceType
    DEVICE_TYPE_MOTION_CAM_PHOD_FIBRA: PhotoOnDemandDevice.DeviceType
    DEVICE_TYPE_MOTION_CAM_OUTDOOR_TWO_FOUR_PHOD: PhotoOnDemandDevice.DeviceType
    DEVICE_TYPE_MOTION_CAM_S_PHOD: PhotoOnDemandDevice.DeviceType
    DEVICE_TYPE_MOTION_CAM_S_PHOD_AM: PhotoOnDemandDevice.DeviceType
    DEVICE_TYPE_MOTION_CAM_SUPERIOR_PHOD: PhotoOnDemandDevice.DeviceType
    DEVICE_TYPE_MOTION_CAM_G3: PhotoOnDemandDevice.DeviceType
    DEVICE_TYPE_CURTAIN_CAM_OUTDOOR_HM_PHOD: PhotoOnDemandDevice.DeviceType
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    device_type: PhotoOnDemandDevice.DeviceType
    def __init__(self, device_id: _Optional[str] = ..., device_type: _Optional[_Union[PhotoOnDemandDevice.DeviceType, str]] = ...) -> None: ...
