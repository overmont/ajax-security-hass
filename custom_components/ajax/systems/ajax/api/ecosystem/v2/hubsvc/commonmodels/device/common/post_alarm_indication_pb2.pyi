from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PostAlarmIndication(_message.Message):
    __slots__ = ("post_alarm_indication_mode", "capabilities")
    class PostAlarmIndicationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        POST_ALARM_INDICATION_MODE_UNSPECIFIED: _ClassVar[PostAlarmIndication.PostAlarmIndicationMode]
        POST_ALARM_INDICATION_MODE_DISABLED: _ClassVar[PostAlarmIndication.PostAlarmIndicationMode]
        POST_ALARM_INDICATION_MODE_ENABLED: _ClassVar[PostAlarmIndication.PostAlarmIndicationMode]
    POST_ALARM_INDICATION_MODE_UNSPECIFIED: PostAlarmIndication.PostAlarmIndicationMode
    POST_ALARM_INDICATION_MODE_DISABLED: PostAlarmIndication.PostAlarmIndicationMode
    POST_ALARM_INDICATION_MODE_ENABLED: PostAlarmIndication.PostAlarmIndicationMode
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[PostAlarmIndication.Capability]
        CAPABILITY_POST_ALARM_INDICATION: _ClassVar[PostAlarmIndication.Capability]
    CAPABILITY_UNSPECIFIED: PostAlarmIndication.Capability
    CAPABILITY_POST_ALARM_INDICATION: PostAlarmIndication.Capability
    class PostAlarmIndicationSettings(_message.Message):
        __slots__ = ("post_alarm_indication_mode",)
        POST_ALARM_INDICATION_MODE_FIELD_NUMBER: _ClassVar[int]
        post_alarm_indication_mode: PostAlarmIndication.PostAlarmIndicationMode
        def __init__(self, post_alarm_indication_mode: _Optional[_Union[PostAlarmIndication.PostAlarmIndicationMode, str]] = ...) -> None: ...
    POST_ALARM_INDICATION_MODE_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    post_alarm_indication_mode: PostAlarmIndication.PostAlarmIndicationMode
    capabilities: _containers.RepeatedScalarFieldContainer[PostAlarmIndication.Capability]
    def __init__(self, post_alarm_indication_mode: _Optional[_Union[PostAlarmIndication.PostAlarmIndicationMode, str]] = ..., capabilities: _Optional[_Iterable[_Union[PostAlarmIndication.Capability, str]]] = ...) -> None: ...
