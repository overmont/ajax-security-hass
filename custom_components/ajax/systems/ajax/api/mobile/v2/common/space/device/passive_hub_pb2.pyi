from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PassiveHub(_message.Message):
    __slots__ = ("id", "room_id", "add_hub_by_qr_transition", "transfer_hub_settings_transition")
    class AddHubByQrTransition(_message.Message):
        __slots__ = ("stage",)
        class Stage(_message.Message):
            __slots__ = ("transition_in_progress", "transition_failed")
            class TransitionInProgress(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class TransitionFailed(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            TRANSITION_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
            TRANSITION_FAILED_FIELD_NUMBER: _ClassVar[int]
            transition_in_progress: PassiveHub.AddHubByQrTransition.Stage.TransitionInProgress
            transition_failed: PassiveHub.AddHubByQrTransition.Stage.TransitionFailed
            def __init__(self, transition_in_progress: _Optional[_Union[PassiveHub.AddHubByQrTransition.Stage.TransitionInProgress, _Mapping]] = ..., transition_failed: _Optional[_Union[PassiveHub.AddHubByQrTransition.Stage.TransitionFailed, _Mapping]] = ...) -> None: ...
        STAGE_FIELD_NUMBER: _ClassVar[int]
        stage: PassiveHub.AddHubByQrTransition.Stage
        def __init__(self, stage: _Optional[_Union[PassiveHub.AddHubByQrTransition.Stage, _Mapping]] = ...) -> None: ...
    class TransferHubSettingsTransition(_message.Message):
        __slots__ = ("stage",)
        class Stage(_message.Message):
            __slots__ = ("transition_in_progress", "transition_failed", "transition_completed")
            class TransitionInProgress(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class TransitionFailed(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class TransitionCompleted(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            TRANSITION_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
            TRANSITION_FAILED_FIELD_NUMBER: _ClassVar[int]
            TRANSITION_COMPLETED_FIELD_NUMBER: _ClassVar[int]
            transition_in_progress: PassiveHub.TransferHubSettingsTransition.Stage.TransitionInProgress
            transition_failed: PassiveHub.TransferHubSettingsTransition.Stage.TransitionFailed
            transition_completed: PassiveHub.TransferHubSettingsTransition.Stage.TransitionCompleted
            def __init__(self, transition_in_progress: _Optional[_Union[PassiveHub.TransferHubSettingsTransition.Stage.TransitionInProgress, _Mapping]] = ..., transition_failed: _Optional[_Union[PassiveHub.TransferHubSettingsTransition.Stage.TransitionFailed, _Mapping]] = ..., transition_completed: _Optional[_Union[PassiveHub.TransferHubSettingsTransition.Stage.TransitionCompleted, _Mapping]] = ...) -> None: ...
        STAGE_FIELD_NUMBER: _ClassVar[int]
        stage: PassiveHub.TransferHubSettingsTransition.Stage
        def __init__(self, stage: _Optional[_Union[PassiveHub.TransferHubSettingsTransition.Stage, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    ADD_HUB_BY_QR_TRANSITION_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_HUB_SETTINGS_TRANSITION_FIELD_NUMBER: _ClassVar[int]
    id: str
    room_id: str
    add_hub_by_qr_transition: PassiveHub.AddHubByQrTransition
    transfer_hub_settings_transition: PassiveHub.TransferHubSettingsTransition
    def __init__(self, id: _Optional[str] = ..., room_id: _Optional[str] = ..., add_hub_by_qr_transition: _Optional[_Union[PassiveHub.AddHubByQrTransition, _Mapping]] = ..., transfer_hub_settings_transition: _Optional[_Union[PassiveHub.TransferHubSettingsTransition, _Mapping]] = ...) -> None: ...
