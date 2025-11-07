from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import object_type_pb2 as _object_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceCommandDeviceOnRequest(_message.Message):
    __slots__ = ("hub_id", "device_id", "device_type", "channels")
    class Channel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHANNEL_UNSPECIFIED: _ClassVar[DeviceCommandDeviceOnRequest.Channel]
        CHANNEL_1: _ClassVar[DeviceCommandDeviceOnRequest.Channel]
        CHANNEL_2: _ClassVar[DeviceCommandDeviceOnRequest.Channel]
        CHANNEL_3: _ClassVar[DeviceCommandDeviceOnRequest.Channel]
        CHANNEL_4: _ClassVar[DeviceCommandDeviceOnRequest.Channel]
    CHANNEL_UNSPECIFIED: DeviceCommandDeviceOnRequest.Channel
    CHANNEL_1: DeviceCommandDeviceOnRequest.Channel
    CHANNEL_2: DeviceCommandDeviceOnRequest.Channel
    CHANNEL_3: DeviceCommandDeviceOnRequest.Channel
    CHANNEL_4: DeviceCommandDeviceOnRequest.Channel
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    device_id: str
    device_type: _object_type_pb2.ObjectType
    channels: _containers.RepeatedScalarFieldContainer[DeviceCommandDeviceOnRequest.Channel]
    def __init__(self, hub_id: _Optional[str] = ..., device_id: _Optional[str] = ..., device_type: _Optional[_Union[_object_type_pb2.ObjectType, _Mapping]] = ..., channels: _Optional[_Iterable[_Union[DeviceCommandDeviceOnRequest.Channel, str]]] = ...) -> None: ...
