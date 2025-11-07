from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GroupSecurity(_message.Message):
    __slots__ = ("group_id", "state", "transition")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GROUP_SECURITY_STATE_NONE: _ClassVar[GroupSecurity.State]
        GROUP_SECURITY_STATE_ARMED: _ClassVar[GroupSecurity.State]
        GROUP_SECURITY_STATE_DISARMED: _ClassVar[GroupSecurity.State]
    GROUP_SECURITY_STATE_NONE: GroupSecurity.State
    GROUP_SECURITY_STATE_ARMED: GroupSecurity.State
    GROUP_SECURITY_STATE_DISARMED: GroupSecurity.State
    class Transition(_message.Message):
        __slots__ = ("desired_state", "stage")
        class DesiredState(_message.Message):
            __slots__ = ("state", "night_mode_enabled")
            STATE_FIELD_NUMBER: _ClassVar[int]
            NIGHT_MODE_ENABLED_FIELD_NUMBER: _ClassVar[int]
            state: GroupSecurity.State
            night_mode_enabled: bool
            def __init__(self, state: _Optional[_Union[GroupSecurity.State, str]] = ..., night_mode_enabled: bool = ...) -> None: ...
        class Stage(_message.Message):
            __slots__ = ("transition_in_progress", "transition_completed")
            class TransitionInProgress(_message.Message):
                __slots__ = ("transition_requested", "awaiting_app_exit_timer_completion", "awaiting_second_stage_confirmation", "two_stage_arming_incomplete", "awaiting_vds_arming_completion")
                class TransitionRequested(_message.Message):
                    __slots__ = ()
                    def __init__(self) -> None: ...
                class AwaitingAppExitTimerCompletion(_message.Message):
                    __slots__ = ("expired_at", "started_at")
                    EXPIRED_AT_FIELD_NUMBER: _ClassVar[int]
                    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
                    expired_at: _timestamp_pb2.Timestamp
                    started_at: _timestamp_pb2.Timestamp
                    def __init__(self, expired_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
                class AwaitingSecondStageConfirmation(_message.Message):
                    __slots__ = ("expired_at", "started_at")
                    EXPIRED_AT_FIELD_NUMBER: _ClassVar[int]
                    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
                    expired_at: _timestamp_pb2.Timestamp
                    started_at: _timestamp_pb2.Timestamp
                    def __init__(self, expired_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
                class TwoStageArmingIncomplete(_message.Message):
                    __slots__ = ()
                    def __init__(self) -> None: ...
                class AwaitingVdsArmingCompletion(_message.Message):
                    __slots__ = ()
                    def __init__(self) -> None: ...
                TRANSITION_REQUESTED_FIELD_NUMBER: _ClassVar[int]
                AWAITING_APP_EXIT_TIMER_COMPLETION_FIELD_NUMBER: _ClassVar[int]
                AWAITING_SECOND_STAGE_CONFIRMATION_FIELD_NUMBER: _ClassVar[int]
                TWO_STAGE_ARMING_INCOMPLETE_FIELD_NUMBER: _ClassVar[int]
                AWAITING_VDS_ARMING_COMPLETION_FIELD_NUMBER: _ClassVar[int]
                transition_requested: GroupSecurity.Transition.Stage.TransitionInProgress.TransitionRequested
                awaiting_app_exit_timer_completion: GroupSecurity.Transition.Stage.TransitionInProgress.AwaitingAppExitTimerCompletion
                awaiting_second_stage_confirmation: GroupSecurity.Transition.Stage.TransitionInProgress.AwaitingSecondStageConfirmation
                two_stage_arming_incomplete: GroupSecurity.Transition.Stage.TransitionInProgress.TwoStageArmingIncomplete
                awaiting_vds_arming_completion: GroupSecurity.Transition.Stage.TransitionInProgress.AwaitingVdsArmingCompletion
                def __init__(self, transition_requested: _Optional[_Union[GroupSecurity.Transition.Stage.TransitionInProgress.TransitionRequested, _Mapping]] = ..., awaiting_app_exit_timer_completion: _Optional[_Union[GroupSecurity.Transition.Stage.TransitionInProgress.AwaitingAppExitTimerCompletion, _Mapping]] = ..., awaiting_second_stage_confirmation: _Optional[_Union[GroupSecurity.Transition.Stage.TransitionInProgress.AwaitingSecondStageConfirmation, _Mapping]] = ..., two_stage_arming_incomplete: _Optional[_Union[GroupSecurity.Transition.Stage.TransitionInProgress.TwoStageArmingIncomplete, _Mapping]] = ..., awaiting_vds_arming_completion: _Optional[_Union[GroupSecurity.Transition.Stage.TransitionInProgress.AwaitingVdsArmingCompletion, _Mapping]] = ...) -> None: ...
            class TransitionCompleted(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            TRANSITION_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
            TRANSITION_COMPLETED_FIELD_NUMBER: _ClassVar[int]
            transition_in_progress: GroupSecurity.Transition.Stage.TransitionInProgress
            transition_completed: GroupSecurity.Transition.Stage.TransitionCompleted
            def __init__(self, transition_in_progress: _Optional[_Union[GroupSecurity.Transition.Stage.TransitionInProgress, _Mapping]] = ..., transition_completed: _Optional[_Union[GroupSecurity.Transition.Stage.TransitionCompleted, _Mapping]] = ...) -> None: ...
        DESIRED_STATE_FIELD_NUMBER: _ClassVar[int]
        STAGE_FIELD_NUMBER: _ClassVar[int]
        desired_state: GroupSecurity.Transition.DesiredState
        stage: GroupSecurity.Transition.Stage
        def __init__(self, desired_state: _Optional[_Union[GroupSecurity.Transition.DesiredState, _Mapping]] = ..., stage: _Optional[_Union[GroupSecurity.Transition.Stage, _Mapping]] = ...) -> None: ...
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TRANSITION_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    state: GroupSecurity.State
    transition: GroupSecurity.Transition
    def __init__(self, group_id: _Optional[str] = ..., state: _Optional[_Union[GroupSecurity.State, str]] = ..., transition: _Optional[_Union[GroupSecurity.Transition, _Mapping]] = ...) -> None: ...
