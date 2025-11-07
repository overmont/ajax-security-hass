from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakePhotoPart(_message.Message):
    __slots__ = ("take_photo_triggers", "capabilities")
    class TriggerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TRIGGER_TYPE_UNSPECIFIED: _ClassVar[TakePhotoPart.TriggerType]
        TRIGGER_TYPE_IF_MASKING_DETECTED: _ClassVar[TakePhotoPart.TriggerType]
        TRIGGER_TYPE_IF_LID_OPENED: _ClassVar[TakePhotoPart.TriggerType]
        TRIGGER_TYPE_IF_DEVICE_MOVED: _ClassVar[TakePhotoPart.TriggerType]
    TRIGGER_TYPE_UNSPECIFIED: TakePhotoPart.TriggerType
    TRIGGER_TYPE_IF_MASKING_DETECTED: TakePhotoPart.TriggerType
    TRIGGER_TYPE_IF_LID_OPENED: TakePhotoPart.TriggerType
    TRIGGER_TYPE_IF_DEVICE_MOVED: TakePhotoPart.TriggerType
    class IsEnabled(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IS_ENABLED_UNSPECIFIED: _ClassVar[TakePhotoPart.IsEnabled]
        IS_ENABLED_DISABLED: _ClassVar[TakePhotoPart.IsEnabled]
        IS_ENABLED_ENABLED: _ClassVar[TakePhotoPart.IsEnabled]
    IS_ENABLED_UNSPECIFIED: TakePhotoPart.IsEnabled
    IS_ENABLED_DISABLED: TakePhotoPart.IsEnabled
    IS_ENABLED_ENABLED: TakePhotoPart.IsEnabled
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[TakePhotoPart.Capability]
        CAPABILITY_TAKE_PHOTO_TRIGGERS: _ClassVar[TakePhotoPart.Capability]
    CAPABILITY_UNSPECIFIED: TakePhotoPart.Capability
    CAPABILITY_TAKE_PHOTO_TRIGGERS: TakePhotoPart.Capability
    class TakePhotoPartSettings(_message.Message):
        __slots__ = ("take_photo_triggers",)
        TAKE_PHOTO_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
        take_photo_triggers: _containers.RepeatedCompositeFieldContainer[TakePhotoPart.TakePhotoTrigger]
        def __init__(self, take_photo_triggers: _Optional[_Iterable[_Union[TakePhotoPart.TakePhotoTrigger, _Mapping]]] = ...) -> None: ...
    class TakePhotoTrigger(_message.Message):
        __slots__ = ("trigger_type", "is_enabled")
        TRIGGER_TYPE_FIELD_NUMBER: _ClassVar[int]
        IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        trigger_type: TakePhotoPart.TriggerType
        is_enabled: TakePhotoPart.IsEnabled
        def __init__(self, trigger_type: _Optional[_Union[TakePhotoPart.TriggerType, str]] = ..., is_enabled: _Optional[_Union[TakePhotoPart.IsEnabled, str]] = ...) -> None: ...
    TAKE_PHOTO_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    take_photo_triggers: _containers.RepeatedCompositeFieldContainer[TakePhotoPart.TakePhotoTrigger]
    capabilities: _containers.RepeatedScalarFieldContainer[TakePhotoPart.Capability]
    def __init__(self, take_photo_triggers: _Optional[_Iterable[_Union[TakePhotoPart.TakePhotoTrigger, _Mapping]]] = ..., capabilities: _Optional[_Iterable[_Union[TakePhotoPart.Capability, str]]] = ...) -> None: ...
