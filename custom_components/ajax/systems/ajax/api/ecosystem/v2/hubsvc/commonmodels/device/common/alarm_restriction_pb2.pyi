from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AlarmRestriction(_message.Message):
    __slots__ = ("alarm_restriction_mode", "capabilities")
    class AlarmRestrictionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALARM_RESTRICTION_MODE_UNSPECIFIED: _ClassVar[AlarmRestriction.AlarmRestrictionMode]
        ALARM_RESTRICTION_MODE_ALWAYS: _ClassVar[AlarmRestriction.AlarmRestrictionMode]
        ALARM_RESTRICTION_MODE_IF_ARMED: _ClassVar[AlarmRestriction.AlarmRestrictionMode]
    ALARM_RESTRICTION_MODE_UNSPECIFIED: AlarmRestriction.AlarmRestrictionMode
    ALARM_RESTRICTION_MODE_ALWAYS: AlarmRestriction.AlarmRestrictionMode
    ALARM_RESTRICTION_MODE_IF_ARMED: AlarmRestriction.AlarmRestrictionMode
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[AlarmRestriction.Capability]
        CAPABILITY_ALARM_RESTRICTION_MODE: _ClassVar[AlarmRestriction.Capability]
    CAPABILITY_UNSPECIFIED: AlarmRestriction.Capability
    CAPABILITY_ALARM_RESTRICTION_MODE: AlarmRestriction.Capability
    class AlarmRestrictionSettings(_message.Message):
        __slots__ = ("alarm_restriction_mode",)
        ALARM_RESTRICTION_MODE_FIELD_NUMBER: _ClassVar[int]
        alarm_restriction_mode: AlarmRestriction.AlarmRestrictionMode
        def __init__(self, alarm_restriction_mode: _Optional[_Union[AlarmRestriction.AlarmRestrictionMode, str]] = ...) -> None: ...
    ALARM_RESTRICTION_MODE_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    alarm_restriction_mode: AlarmRestriction.AlarmRestrictionMode
    capabilities: _containers.RepeatedScalarFieldContainer[AlarmRestriction.Capability]
    def __init__(self, alarm_restriction_mode: _Optional[_Union[AlarmRestriction.AlarmRestrictionMode, str]] = ..., capabilities: _Optional[_Iterable[_Union[AlarmRestriction.Capability, str]]] = ...) -> None: ...
