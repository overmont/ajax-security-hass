from systems.ajax.protobuf.hub import image_urls_pb2 as _image_urls_pb2
from systems.ajax.protobuf.hub import name_pb2 as _name_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Group(_message.Message):
    __slots__ = ("id", "image_id", "bulk_arm_involved", "bulk_disarm_involved", "state", "name", "image_urls", "second_stage_required", "two_stage_arming_status", "chimes_status")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_STATE_INFO: _ClassVar[Group.State]
        DISARMED: _ClassVar[Group.State]
        ARMED: _ClassVar[Group.State]
    NO_STATE_INFO: Group.State
    DISARMED: Group.State
    ARMED: Group.State
    class TwoStageArmingStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_TWO_STORAGE_ARMING_STATUS: _ClassVar[Group.TwoStageArmingStatus]
        NONE: _ClassVar[Group.TwoStageArmingStatus]
        APP_EXIT_TIMER_IN_PROGRESS: _ClassVar[Group.TwoStageArmingStatus]
        SECOND_STAGE_TIMER_IN_PROGRESS: _ClassVar[Group.TwoStageArmingStatus]
        ARMING_INCOMPLETE: _ClassVar[Group.TwoStageArmingStatus]
        FINAL_DOOR_BOUNCE_TIMER_IN_PROGRESS: _ClassVar[Group.TwoStageArmingStatus]
    NO_TWO_STORAGE_ARMING_STATUS: Group.TwoStageArmingStatus
    NONE: Group.TwoStageArmingStatus
    APP_EXIT_TIMER_IN_PROGRESS: Group.TwoStageArmingStatus
    SECOND_STAGE_TIMER_IN_PROGRESS: Group.TwoStageArmingStatus
    ARMING_INCOMPLETE: Group.TwoStageArmingStatus
    FINAL_DOOR_BOUNCE_TIMER_IN_PROGRESS: Group.TwoStageArmingStatus
    class ChimesStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_CHIMES_STATUS_INFO: _ClassVar[Group.ChimesStatus]
        CHIMES_ENABLED: _ClassVar[Group.ChimesStatus]
        SIRENS_READY: _ClassVar[Group.ChimesStatus]
        TRIGGERS_READY: _ClassVar[Group.ChimesStatus]
    NO_CHIMES_STATUS_INFO: Group.ChimesStatus
    CHIMES_ENABLED: Group.ChimesStatus
    SIRENS_READY: Group.ChimesStatus
    TRIGGERS_READY: Group.ChimesStatus
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    BULK_ARM_INVOLVED_FIELD_NUMBER: _ClassVar[int]
    BULK_DISARM_INVOLVED_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URLS_FIELD_NUMBER: _ClassVar[int]
    SECOND_STAGE_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    TWO_STAGE_ARMING_STATUS_FIELD_NUMBER: _ClassVar[int]
    CHIMES_STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    image_id: str
    bulk_arm_involved: bool
    bulk_disarm_involved: bool
    state: Group.State
    name: _name_pb2.Name
    image_urls: _image_urls_pb2.ImageUrls
    second_stage_required: bool
    two_stage_arming_status: Group.TwoStageArmingStatus
    chimes_status: _containers.RepeatedScalarFieldContainer[Group.ChimesStatus]
    def __init__(self, id: _Optional[str] = ..., image_id: _Optional[str] = ..., bulk_arm_involved: bool = ..., bulk_disarm_involved: bool = ..., state: _Optional[_Union[Group.State, str]] = ..., name: _Optional[_Union[_name_pb2.Name, _Mapping]] = ..., image_urls: _Optional[_Union[_image_urls_pb2.ImageUrls, _Mapping]] = ..., second_stage_required: bool = ..., two_stage_arming_status: _Optional[_Union[Group.TwoStageArmingStatus, str]] = ..., chimes_status: _Optional[_Iterable[_Union[Group.ChimesStatus, str]]] = ...) -> None: ...
