from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import object_type_pb2 as _object_type_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetScenarioTargetOptionsRequest(_message.Message):
    __slots__ = ("space_id", "target_options_type", "selected_trigger_object")
    class TargetOptionsType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TARGET_OPTIONS_TYPE_UNSPECIFIED: _ClassVar[GetScenarioTargetOptionsRequest.TargetOptionsType]
        TARGET_OPTIONS_TYPE_SCHEDULE_ACCESS: _ClassVar[GetScenarioTargetOptionsRequest.TargetOptionsType]
        TARGET_OPTIONS_TYPE_PHOD: _ClassVar[GetScenarioTargetOptionsRequest.TargetOptionsType]
        TARGET_OPTIONS_TYPE_SWITCHING_STATE: _ClassVar[GetScenarioTargetOptionsRequest.TargetOptionsType]
        TARGET_OPTIONS_TYPE_VIDEO_EDGE: _ClassVar[GetScenarioTargetOptionsRequest.TargetOptionsType]
        TARGET_OPTIONS_TYPE_SMART_LOCK: _ClassVar[GetScenarioTargetOptionsRequest.TargetOptionsType]
    TARGET_OPTIONS_TYPE_UNSPECIFIED: GetScenarioTargetOptionsRequest.TargetOptionsType
    TARGET_OPTIONS_TYPE_SCHEDULE_ACCESS: GetScenarioTargetOptionsRequest.TargetOptionsType
    TARGET_OPTIONS_TYPE_PHOD: GetScenarioTargetOptionsRequest.TargetOptionsType
    TARGET_OPTIONS_TYPE_SWITCHING_STATE: GetScenarioTargetOptionsRequest.TargetOptionsType
    TARGET_OPTIONS_TYPE_VIDEO_EDGE: GetScenarioTargetOptionsRequest.TargetOptionsType
    TARGET_OPTIONS_TYPE_SMART_LOCK: GetScenarioTargetOptionsRequest.TargetOptionsType
    class SelectedTriggerObject(_message.Message):
        __slots__ = ("hub_selected_trigger_object",)
        HUB_SELECTED_TRIGGER_OBJECT_FIELD_NUMBER: _ClassVar[int]
        hub_selected_trigger_object: GetScenarioTargetOptionsRequest.SelectedTriggerHubObject
        def __init__(self, hub_selected_trigger_object: _Optional[_Union[GetScenarioTargetOptionsRequest.SelectedTriggerHubObject, _Mapping]] = ...) -> None: ...
    class SelectedTriggerHubObject(_message.Message):
        __slots__ = ("object_id", "object_type")
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
        object_id: str
        object_type: _object_type_pb2.ObjectType
        def __init__(self, object_id: _Optional[str] = ..., object_type: _Optional[_Union[_object_type_pb2.ObjectType, _Mapping]] = ...) -> None: ...
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_OPTIONS_TYPE_FIELD_NUMBER: _ClassVar[int]
    SELECTED_TRIGGER_OBJECT_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    target_options_type: GetScenarioTargetOptionsRequest.TargetOptionsType
    selected_trigger_object: GetScenarioTargetOptionsRequest.SelectedTriggerObject
    def __init__(self, space_id: _Optional[str] = ..., target_options_type: _Optional[_Union[GetScenarioTargetOptionsRequest.TargetOptionsType, str]] = ..., selected_trigger_object: _Optional[_Union[GetScenarioTargetOptionsRequest.SelectedTriggerObject, _Mapping]] = ...) -> None: ...
