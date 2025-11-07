from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegularModeSpaceSecurity(_message.Message):
    __slots__ = ("space_state", "transition")
    class SpaceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REGULAR_MODE_SPACE_SECURITY_STATE_NONE: _ClassVar[RegularModeSpaceSecurity.SpaceState]
        REGULAR_MODE_SPACE_SECURITY_STATE_ARMED: _ClassVar[RegularModeSpaceSecurity.SpaceState]
        REGULAR_MODE_SPACE_SECURITY_STATE_DISARMED: _ClassVar[RegularModeSpaceSecurity.SpaceState]
        REGULAR_MODE_SPACE_SECURITY_STATE_NIGHT_MODE: _ClassVar[RegularModeSpaceSecurity.SpaceState]
    REGULAR_MODE_SPACE_SECURITY_STATE_NONE: RegularModeSpaceSecurity.SpaceState
    REGULAR_MODE_SPACE_SECURITY_STATE_ARMED: RegularModeSpaceSecurity.SpaceState
    REGULAR_MODE_SPACE_SECURITY_STATE_DISARMED: RegularModeSpaceSecurity.SpaceState
    REGULAR_MODE_SPACE_SECURITY_STATE_NIGHT_MODE: RegularModeSpaceSecurity.SpaceState
    class Transition(_message.Message):
        __slots__ = ("desired_state", "stage")
        class Stage(_message.Message):
            __slots__ = ("transition_in_progress", "transition_completed")
            class TransitionInProgress(_message.Message):
                __slots__ = ("transition_requested", "awaiting_app_exit_timer_completion", "awaiting_second_stage_confirmation", "two_stage_arming_incomplete", "awaiting_vds_arming_completion")
                class TransitionRequested(_message.Message):
                    __slots__ = ()
                    def __init__(self) -> None: ...
                class TransitioningHub(_message.Message):
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
                class TransitioningOtherDevices(_message.Message):
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
                transition_requested: RegularModeSpaceSecurity.Transition.Stage.TransitionInProgress.TransitionRequested
                awaiting_app_exit_timer_completion: RegularModeSpaceSecurity.Transition.Stage.TransitionInProgress.AwaitingAppExitTimerCompletion
                awaiting_second_stage_confirmation: RegularModeSpaceSecurity.Transition.Stage.TransitionInProgress.AwaitingSecondStageConfirmation
                two_stage_arming_incomplete: RegularModeSpaceSecurity.Transition.Stage.TransitionInProgress.TwoStageArmingIncomplete
                awaiting_vds_arming_completion: RegularModeSpaceSecurity.Transition.Stage.TransitionInProgress.AwaitingVdsArmingCompletion
                def __init__(self, transition_requested: _Optional[_Union[RegularModeSpaceSecurity.Transition.Stage.TransitionInProgress.TransitionRequested, _Mapping]] = ..., awaiting_app_exit_timer_completion: _Optional[_Union[RegularModeSpaceSecurity.Transition.Stage.TransitionInProgress.AwaitingAppExitTimerCompletion, _Mapping]] = ..., awaiting_second_stage_confirmation: _Optional[_Union[RegularModeSpaceSecurity.Transition.Stage.TransitionInProgress.AwaitingSecondStageConfirmation, _Mapping]] = ..., two_stage_arming_incomplete: _Optional[_Union[RegularModeSpaceSecurity.Transition.Stage.TransitionInProgress.TwoStageArmingIncomplete, _Mapping]] = ..., awaiting_vds_arming_completion: _Optional[_Union[RegularModeSpaceSecurity.Transition.Stage.TransitionInProgress.AwaitingVdsArmingCompletion, _Mapping]] = ...) -> None: ...
            class TransitionCompleted(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            TRANSITION_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
            TRANSITION_COMPLETED_FIELD_NUMBER: _ClassVar[int]
            transition_in_progress: RegularModeSpaceSecurity.Transition.Stage.TransitionInProgress
            transition_completed: RegularModeSpaceSecurity.Transition.Stage.TransitionCompleted
            def __init__(self, transition_in_progress: _Optional[_Union[RegularModeSpaceSecurity.Transition.Stage.TransitionInProgress, _Mapping]] = ..., transition_completed: _Optional[_Union[RegularModeSpaceSecurity.Transition.Stage.TransitionCompleted, _Mapping]] = ...) -> None: ...
        DESIRED_STATE_FIELD_NUMBER: _ClassVar[int]
        STAGE_FIELD_NUMBER: _ClassVar[int]
        desired_state: RegularModeSpaceSecurity.SpaceState
        stage: RegularModeSpaceSecurity.Transition.Stage
        def __init__(self, desired_state: _Optional[_Union[RegularModeSpaceSecurity.SpaceState, str]] = ..., stage: _Optional[_Union[RegularModeSpaceSecurity.Transition.Stage, _Mapping]] = ...) -> None: ...
    SPACE_STATE_FIELD_NUMBER: _ClassVar[int]
    TRANSITION_FIELD_NUMBER: _ClassVar[int]
    space_state: RegularModeSpaceSecurity.SpaceState
    transition: RegularModeSpaceSecurity.Transition
    def __init__(self, space_state: _Optional[_Union[RegularModeSpaceSecurity.SpaceState, str]] = ..., transition: _Optional[_Union[RegularModeSpaceSecurity.Transition, _Mapping]] = ...) -> None: ...
