from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.event.hub import tag_pb2 as _tag_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.event import transition_pb2 as _transition_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.event.hub import notification_type_case_pb2 as _notification_type_case_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HubEventQualifier(_message.Message):
    __slots__ = ("tag", "transition", "case")
    TAG_FIELD_NUMBER: _ClassVar[int]
    TRANSITION_FIELD_NUMBER: _ClassVar[int]
    CASE_FIELD_NUMBER: _ClassVar[int]
    tag: _tag_pb2.HubEventTag
    transition: _transition_pb2.EventTransition
    case: _notification_type_case_pb2.Case
    def __init__(self, tag: _Optional[_Union[_tag_pb2.HubEventTag, _Mapping]] = ..., transition: _Optional[_Union[_transition_pb2.EventTransition, _Mapping]] = ..., case: _Optional[_Union[_notification_type_case_pb2.Case, str]] = ...) -> None: ...
