from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PhotoOnDemandCompanyRights(_message.Message):
    __slots__ = ("shared_devices", "disabled", "always", "when_armed", "after_alarm")
    class Never(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Always(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class WhenArmed(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class AfterAlarm(_message.Message):
        __slots__ = ("time_to_take_photo_minutes",)
        TIME_TO_TAKE_PHOTO_MINUTES_FIELD_NUMBER: _ClassVar[int]
        time_to_take_photo_minutes: _wrappers_pb2.UInt32Value
        def __init__(self, time_to_take_photo_minutes: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...
    class PhotoOnDemandDevices(_message.Message):
        __slots__ = ("devices",)
        DEVICES_FIELD_NUMBER: _ClassVar[int]
        devices: _containers.RepeatedCompositeFieldContainer[PhotoOnDemandCompanyRights.PhotoOnDemandDevice]
        def __init__(self, devices: _Optional[_Iterable[_Union[PhotoOnDemandCompanyRights.PhotoOnDemandDevice, _Mapping]]] = ...) -> None: ...
    class PhotoOnDemandDevice(_message.Message):
        __slots__ = ("device_id", "device_type")
        class PhotoDeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NO_DEVICE_TYPE_INFO: _ClassVar[PhotoOnDemandCompanyRights.PhotoOnDemandDevice.PhotoDeviceType]
            MOTION_CAM: _ClassVar[PhotoOnDemandCompanyRights.PhotoOnDemandDevice.PhotoDeviceType]
            MOTION_CAM_OUTDOOR: _ClassVar[PhotoOnDemandCompanyRights.PhotoOnDemandDevice.PhotoDeviceType]
            MOTION_CAM_PHOD: _ClassVar[PhotoOnDemandCompanyRights.PhotoOnDemandDevice.PhotoDeviceType]
            MOTION_CAM_OUTDOOR_PHOD: _ClassVar[PhotoOnDemandCompanyRights.PhotoOnDemandDevice.PhotoDeviceType]
            MOTION_CAM_PHOD_FIBRA: _ClassVar[PhotoOnDemandCompanyRights.PhotoOnDemandDevice.PhotoDeviceType]
            MOTION_CAM_OUTDOOR_TWO_FOUR_PHOD: _ClassVar[PhotoOnDemandCompanyRights.PhotoOnDemandDevice.PhotoDeviceType]
            MOTION_CAM_HD: _ClassVar[PhotoOnDemandCompanyRights.PhotoOnDemandDevice.PhotoDeviceType]
            MOTION_CAM_S_PHOD: _ClassVar[PhotoOnDemandCompanyRights.PhotoOnDemandDevice.PhotoDeviceType]
            MOTION_CAM_S_PHOD_AM: _ClassVar[PhotoOnDemandCompanyRights.PhotoOnDemandDevice.PhotoDeviceType]
            MOTION_CAM_SUPERIOR_PHOD: _ClassVar[PhotoOnDemandCompanyRights.PhotoOnDemandDevice.PhotoDeviceType]
            MOTION_CAM_G3: _ClassVar[PhotoOnDemandCompanyRights.PhotoOnDemandDevice.PhotoDeviceType]
            CURTAIN_CAM_OUTDOOR_HM_PHOD: _ClassVar[PhotoOnDemandCompanyRights.PhotoOnDemandDevice.PhotoDeviceType]
        NO_DEVICE_TYPE_INFO: PhotoOnDemandCompanyRights.PhotoOnDemandDevice.PhotoDeviceType
        MOTION_CAM: PhotoOnDemandCompanyRights.PhotoOnDemandDevice.PhotoDeviceType
        MOTION_CAM_OUTDOOR: PhotoOnDemandCompanyRights.PhotoOnDemandDevice.PhotoDeviceType
        MOTION_CAM_PHOD: PhotoOnDemandCompanyRights.PhotoOnDemandDevice.PhotoDeviceType
        MOTION_CAM_OUTDOOR_PHOD: PhotoOnDemandCompanyRights.PhotoOnDemandDevice.PhotoDeviceType
        MOTION_CAM_PHOD_FIBRA: PhotoOnDemandCompanyRights.PhotoOnDemandDevice.PhotoDeviceType
        MOTION_CAM_OUTDOOR_TWO_FOUR_PHOD: PhotoOnDemandCompanyRights.PhotoOnDemandDevice.PhotoDeviceType
        MOTION_CAM_HD: PhotoOnDemandCompanyRights.PhotoOnDemandDevice.PhotoDeviceType
        MOTION_CAM_S_PHOD: PhotoOnDemandCompanyRights.PhotoOnDemandDevice.PhotoDeviceType
        MOTION_CAM_S_PHOD_AM: PhotoOnDemandCompanyRights.PhotoOnDemandDevice.PhotoDeviceType
        MOTION_CAM_SUPERIOR_PHOD: PhotoOnDemandCompanyRights.PhotoOnDemandDevice.PhotoDeviceType
        MOTION_CAM_G3: PhotoOnDemandCompanyRights.PhotoOnDemandDevice.PhotoDeviceType
        CURTAIN_CAM_OUTDOOR_HM_PHOD: PhotoOnDemandCompanyRights.PhotoOnDemandDevice.PhotoDeviceType
        DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
        DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        device_id: str
        device_type: PhotoOnDemandCompanyRights.PhotoOnDemandDevice.PhotoDeviceType
        def __init__(self, device_id: _Optional[str] = ..., device_type: _Optional[_Union[PhotoOnDemandCompanyRights.PhotoOnDemandDevice.PhotoDeviceType, str]] = ...) -> None: ...
    SHARED_DEVICES_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_FIELD_NUMBER: _ClassVar[int]
    WHEN_ARMED_FIELD_NUMBER: _ClassVar[int]
    AFTER_ALARM_FIELD_NUMBER: _ClassVar[int]
    shared_devices: PhotoOnDemandCompanyRights.PhotoOnDemandDevices
    disabled: PhotoOnDemandCompanyRights.Never
    always: PhotoOnDemandCompanyRights.Always
    when_armed: PhotoOnDemandCompanyRights.WhenArmed
    after_alarm: PhotoOnDemandCompanyRights.AfterAlarm
    def __init__(self, shared_devices: _Optional[_Union[PhotoOnDemandCompanyRights.PhotoOnDemandDevices, _Mapping]] = ..., disabled: _Optional[_Union[PhotoOnDemandCompanyRights.Never, _Mapping]] = ..., always: _Optional[_Union[PhotoOnDemandCompanyRights.Always, _Mapping]] = ..., when_armed: _Optional[_Union[PhotoOnDemandCompanyRights.WhenArmed, _Mapping]] = ..., after_alarm: _Optional[_Union[PhotoOnDemandCompanyRights.AfterAlarm, _Mapping]] = ...) -> None: ...
