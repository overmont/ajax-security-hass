from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetScenarioTriggerOptionsRequest(_message.Message):
    __slots__ = ("space_id", "trigger_options_type")
    class TriggerOptionsType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TRIGGER_OPTIONS_TYPE_UNSPECIFIED: _ClassVar[GetScenarioTriggerOptionsRequest.TriggerOptionsType]
        TRIGGER_OPTIONS_TYPE_TEMPERATURE: _ClassVar[GetScenarioTriggerOptionsRequest.TriggerOptionsType]
        TRIGGER_OPTIONS_TYPE_ALARMING_DEVICE: _ClassVar[GetScenarioTriggerOptionsRequest.TriggerOptionsType]
        TRIGGER_OPTIONS_TYPE_CROSS_ZONE: _ClassVar[GetScenarioTriggerOptionsRequest.TriggerOptionsType]
        TRIGGER_OPTIONS_TYPE_SMART_LOCK: _ClassVar[GetScenarioTriggerOptionsRequest.TriggerOptionsType]
        TRIGGER_OPTIONS_TYPE_VIDEO_DETECTION: _ClassVar[GetScenarioTriggerOptionsRequest.TriggerOptionsType]
    TRIGGER_OPTIONS_TYPE_UNSPECIFIED: GetScenarioTriggerOptionsRequest.TriggerOptionsType
    TRIGGER_OPTIONS_TYPE_TEMPERATURE: GetScenarioTriggerOptionsRequest.TriggerOptionsType
    TRIGGER_OPTIONS_TYPE_ALARMING_DEVICE: GetScenarioTriggerOptionsRequest.TriggerOptionsType
    TRIGGER_OPTIONS_TYPE_CROSS_ZONE: GetScenarioTriggerOptionsRequest.TriggerOptionsType
    TRIGGER_OPTIONS_TYPE_SMART_LOCK: GetScenarioTriggerOptionsRequest.TriggerOptionsType
    TRIGGER_OPTIONS_TYPE_VIDEO_DETECTION: GetScenarioTriggerOptionsRequest.TriggerOptionsType
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_OPTIONS_TYPE_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    trigger_options_type: GetScenarioTriggerOptionsRequest.TriggerOptionsType
    def __init__(self, space_id: _Optional[str] = ..., trigger_options_type: _Optional[_Union[GetScenarioTriggerOptionsRequest.TriggerOptionsType, str]] = ...) -> None: ...
