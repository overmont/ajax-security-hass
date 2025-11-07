from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SmartLockControl(_message.Message):
    __slots__ = ("state", "unlatch_info")
    class UnlatchState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNLATCH_STATE_UNSPECIFIED: _ClassVar[SmartLockControl.UnlatchState]
        UNLATCH_STATE_LATCHED: _ClassVar[SmartLockControl.UnlatchState]
        UNLATCH_STATE_PENDING_UNLATCHED: _ClassVar[SmartLockControl.UnlatchState]
        UNLATCH_STATE_UNLATCHED: _ClassVar[SmartLockControl.UnlatchState]
    UNLATCH_STATE_UNSPECIFIED: SmartLockControl.UnlatchState
    UNLATCH_STATE_LATCHED: SmartLockControl.UnlatchState
    UNLATCH_STATE_PENDING_UNLATCHED: SmartLockControl.UnlatchState
    UNLATCH_STATE_UNLATCHED: SmartLockControl.UnlatchState
    class LockState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOCK_STATE_UNSPECIFIED: _ClassVar[SmartLockControl.LockState]
        LOCK_STATE_LOCKED: _ClassVar[SmartLockControl.LockState]
        LOCK_STATE_PENDING_LOCKED: _ClassVar[SmartLockControl.LockState]
        LOCK_STATE_UNLOCKED: _ClassVar[SmartLockControl.LockState]
        LOCK_STATE_PENDING_UNLOCKED: _ClassVar[SmartLockControl.LockState]
    LOCK_STATE_UNSPECIFIED: SmartLockControl.LockState
    LOCK_STATE_LOCKED: SmartLockControl.LockState
    LOCK_STATE_PENDING_LOCKED: SmartLockControl.LockState
    LOCK_STATE_UNLOCKED: SmartLockControl.LockState
    LOCK_STATE_PENDING_UNLOCKED: SmartLockControl.LockState
    class UnlatchInfo(_message.Message):
        __slots__ = ("state",)
        STATE_FIELD_NUMBER: _ClassVar[int]
        state: SmartLockControl.UnlatchState
        def __init__(self, state: _Optional[_Union[SmartLockControl.UnlatchState, str]] = ...) -> None: ...
    STATE_FIELD_NUMBER: _ClassVar[int]
    UNLATCH_INFO_FIELD_NUMBER: _ClassVar[int]
    state: SmartLockControl.LockState
    unlatch_info: SmartLockControl.UnlatchInfo
    def __init__(self, state: _Optional[_Union[SmartLockControl.LockState, str]] = ..., unlatch_info: _Optional[_Union[SmartLockControl.UnlatchInfo, _Mapping]] = ...) -> None: ...
