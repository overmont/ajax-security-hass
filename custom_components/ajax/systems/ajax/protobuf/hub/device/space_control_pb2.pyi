from google.protobuf import wrappers_pb2 as _wrappers_pb2
from systems.ajax.protobuf.hub.device import common_device_pb2 as _common_device_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceControl(_message.Message):
    __slots__ = ("common_part", "siren_triggers", "panic_enabled", "associated_user_id", "associated_group_id", "false_press_filter", "subtype")
    class SirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_TRIGGER_INFO: _ClassVar[SpaceControl.SirenTrigger]
        SECURITY_BUTTON: _ClassVar[SpaceControl.SirenTrigger]
    NO_SIREN_TRIGGER_INFO: SpaceControl.SirenTrigger
    SECURITY_BUTTON: SpaceControl.SirenTrigger
    class FalsePressFilter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_FALSE_PRESS_FILTER_INFO: _ClassVar[SpaceControl.FalsePressFilter]
        DISABLED: _ClassVar[SpaceControl.FalsePressFilter]
        LONG_PUSH: _ClassVar[SpaceControl.FalsePressFilter]
        DOUBLE_CLICK: _ClassVar[SpaceControl.FalsePressFilter]
    NO_FALSE_PRESS_FILTER_INFO: SpaceControl.FalsePressFilter
    DISABLED: SpaceControl.FalsePressFilter
    LONG_PUSH: SpaceControl.FalsePressFilter
    DOUBLE_CLICK: SpaceControl.FalsePressFilter
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[SpaceControl.Subtype]
    NO_SUBTYPE: SpaceControl.Subtype
    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    PANIC_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_USER_ID_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    FALSE_PRESS_FILTER_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    siren_triggers: _containers.RepeatedScalarFieldContainer[SpaceControl.SirenTrigger]
    panic_enabled: bool
    associated_user_id: str
    associated_group_id: str
    false_press_filter: SpaceControl.FalsePressFilter
    subtype: SpaceControl.Subtype
    def __init__(self, common_part: _Optional[_Union[_common_device_pb2.CommonDevicePart, _Mapping]] = ..., siren_triggers: _Optional[_Iterable[_Union[SpaceControl.SirenTrigger, str]]] = ..., panic_enabled: bool = ..., associated_user_id: _Optional[str] = ..., associated_group_id: _Optional[str] = ..., false_press_filter: _Optional[_Union[SpaceControl.FalsePressFilter, str]] = ..., subtype: _Optional[_Union[SpaceControl.Subtype, str]] = ...) -> None: ...
