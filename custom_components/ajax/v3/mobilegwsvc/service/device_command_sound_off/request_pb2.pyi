from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import object_type_pb2 as _object_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceCommandSoundOffRequest(_message.Message):
    __slots__ = ("hub_id", "device_id", "object_type", "mute_source_alarm")
    class MuteSourceAlarm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MUTE_SOURCE_ALARM_UNSPECIFIED: _ClassVar[DeviceCommandSoundOffRequest.MuteSourceAlarm]
        MUTE_SOURCE_ALARM_MUTE_OWN: _ClassVar[DeviceCommandSoundOffRequest.MuteSourceAlarm]
        MUTE_SOURCE_ALARM_MUTE_EXTERNAL: _ClassVar[DeviceCommandSoundOffRequest.MuteSourceAlarm]
    MUTE_SOURCE_ALARM_UNSPECIFIED: DeviceCommandSoundOffRequest.MuteSourceAlarm
    MUTE_SOURCE_ALARM_MUTE_OWN: DeviceCommandSoundOffRequest.MuteSourceAlarm
    MUTE_SOURCE_ALARM_MUTE_EXTERNAL: DeviceCommandSoundOffRequest.MuteSourceAlarm
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    MUTE_SOURCE_ALARM_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    device_id: str
    object_type: _object_type_pb2.ObjectType
    mute_source_alarm: _containers.RepeatedScalarFieldContainer[DeviceCommandSoundOffRequest.MuteSourceAlarm]
    def __init__(self, hub_id: _Optional[str] = ..., device_id: _Optional[str] = ..., object_type: _Optional[_Union[_object_type_pb2.ObjectType, _Mapping]] = ..., mute_source_alarm: _Optional[_Iterable[_Union[DeviceCommandSoundOffRequest.MuteSourceAlarm, str]]] = ...) -> None: ...
