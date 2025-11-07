from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import object_type_pb2 as _object_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SwitchStateAction(_message.Message):
    __slots__ = ("targets", "action_type")
    class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTION_TYPE_UNSPECIFIED: _ClassVar[SwitchStateAction.ActionType]
        ACTION_TYPE_SWITCH_OFF: _ClassVar[SwitchStateAction.ActionType]
        ACTION_TYPE_SWITCH_ON: _ClassVar[SwitchStateAction.ActionType]
        ACTION_TYPE_SWITCH_STATE: _ClassVar[SwitchStateAction.ActionType]
        ACTION_TYPE_UNLATCH: _ClassVar[SwitchStateAction.ActionType]
    ACTION_TYPE_UNSPECIFIED: SwitchStateAction.ActionType
    ACTION_TYPE_SWITCH_OFF: SwitchStateAction.ActionType
    ACTION_TYPE_SWITCH_ON: SwitchStateAction.ActionType
    ACTION_TYPE_SWITCH_STATE: SwitchStateAction.ActionType
    ACTION_TYPE_UNLATCH: SwitchStateAction.ActionType
    class Target(_message.Message):
        __slots__ = ("hub_device", "smart_lock")
        class HubDevice(_message.Message):
            __slots__ = ("id", "hub_id", "object_type", "channels")
            class Channel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                CHANNEL_UNSPECIFIED: _ClassVar[SwitchStateAction.Target.HubDevice.Channel]
                CHANNEL_1: _ClassVar[SwitchStateAction.Target.HubDevice.Channel]
                CHANNEL_2: _ClassVar[SwitchStateAction.Target.HubDevice.Channel]
                CHANNEL_3: _ClassVar[SwitchStateAction.Target.HubDevice.Channel]
                CHANNEL_4: _ClassVar[SwitchStateAction.Target.HubDevice.Channel]
            CHANNEL_UNSPECIFIED: SwitchStateAction.Target.HubDevice.Channel
            CHANNEL_1: SwitchStateAction.Target.HubDevice.Channel
            CHANNEL_2: SwitchStateAction.Target.HubDevice.Channel
            CHANNEL_3: SwitchStateAction.Target.HubDevice.Channel
            CHANNEL_4: SwitchStateAction.Target.HubDevice.Channel
            ID_FIELD_NUMBER: _ClassVar[int]
            HUB_ID_FIELD_NUMBER: _ClassVar[int]
            OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
            CHANNELS_FIELD_NUMBER: _ClassVar[int]
            id: str
            hub_id: str
            object_type: _object_type_pb2.ObjectType
            channels: _containers.RepeatedScalarFieldContainer[SwitchStateAction.Target.HubDevice.Channel]
            def __init__(self, id: _Optional[str] = ..., hub_id: _Optional[str] = ..., object_type: _Optional[_Union[_object_type_pb2.ObjectType, _Mapping]] = ..., channels: _Optional[_Iterable[_Union[SwitchStateAction.Target.HubDevice.Channel, str]]] = ...) -> None: ...
        class SmartLock(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        HUB_DEVICE_FIELD_NUMBER: _ClassVar[int]
        SMART_LOCK_FIELD_NUMBER: _ClassVar[int]
        hub_device: SwitchStateAction.Target.HubDevice
        smart_lock: SwitchStateAction.Target.SmartLock
        def __init__(self, hub_device: _Optional[_Union[SwitchStateAction.Target.HubDevice, _Mapping]] = ..., smart_lock: _Optional[_Union[SwitchStateAction.Target.SmartLock, _Mapping]] = ...) -> None: ...
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    targets: _containers.RepeatedCompositeFieldContainer[SwitchStateAction.Target]
    action_type: SwitchStateAction.ActionType
    def __init__(self, targets: _Optional[_Iterable[_Union[SwitchStateAction.Target, _Mapping]]] = ..., action_type: _Optional[_Union[SwitchStateAction.ActionType, str]] = ...) -> None: ...
