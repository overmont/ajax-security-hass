from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import object_type_pb2 as _object_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceCommandBrightnessRequest(_message.Message):
    __slots__ = ("hub_id", "device_id", "device_type", "brightness_in_percentage", "channels", "brightness_type")
    class BrightnessType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BRIGHTNESS_TYPE_UNSPECIFIED: _ClassVar[DeviceCommandBrightnessRequest.BrightnessType]
        BRIGHTNESS_TYPE_RELATIVE: _ClassVar[DeviceCommandBrightnessRequest.BrightnessType]
        BRIGHTNESS_TYPE_ABSOLUTE: _ClassVar[DeviceCommandBrightnessRequest.BrightnessType]
    BRIGHTNESS_TYPE_UNSPECIFIED: DeviceCommandBrightnessRequest.BrightnessType
    BRIGHTNESS_TYPE_RELATIVE: DeviceCommandBrightnessRequest.BrightnessType
    BRIGHTNESS_TYPE_ABSOLUTE: DeviceCommandBrightnessRequest.BrightnessType
    class Channel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHANNEL_UNSPECIFIED: _ClassVar[DeviceCommandBrightnessRequest.Channel]
        CHANNEL_1: _ClassVar[DeviceCommandBrightnessRequest.Channel]
        CHANNEL_2: _ClassVar[DeviceCommandBrightnessRequest.Channel]
        CHANNEL_3: _ClassVar[DeviceCommandBrightnessRequest.Channel]
        CHANNEL_4: _ClassVar[DeviceCommandBrightnessRequest.Channel]
    CHANNEL_UNSPECIFIED: DeviceCommandBrightnessRequest.Channel
    CHANNEL_1: DeviceCommandBrightnessRequest.Channel
    CHANNEL_2: DeviceCommandBrightnessRequest.Channel
    CHANNEL_3: DeviceCommandBrightnessRequest.Channel
    CHANNEL_4: DeviceCommandBrightnessRequest.Channel
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    BRIGHTNESS_IN_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    BRIGHTNESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    device_id: str
    device_type: _object_type_pb2.ObjectType
    brightness_in_percentage: int
    channels: _containers.RepeatedScalarFieldContainer[DeviceCommandBrightnessRequest.Channel]
    brightness_type: DeviceCommandBrightnessRequest.BrightnessType
    def __init__(self, hub_id: _Optional[str] = ..., device_id: _Optional[str] = ..., device_type: _Optional[_Union[_object_type_pb2.ObjectType, _Mapping]] = ..., brightness_in_percentage: _Optional[int] = ..., channels: _Optional[_Iterable[_Union[DeviceCommandBrightnessRequest.Channel, str]]] = ..., brightness_type: _Optional[_Union[DeviceCommandBrightnessRequest.BrightnessType, str]] = ...) -> None: ...
