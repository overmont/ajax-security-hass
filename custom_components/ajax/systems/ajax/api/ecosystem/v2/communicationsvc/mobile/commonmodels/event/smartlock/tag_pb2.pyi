from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Added(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Removed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConnectionLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LockedManually(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LockedByExternalUser(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LockedBySpaceMember(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LockedByScenario(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LockingFailed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BatteryLow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DoorbellPressed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LockedAutomatically(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LockedByKeypad(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class KeypadTemporarilyDisabled(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LockedByMatter(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockEventTag(_message.Message):
    __slots__ = ("added", "removed", "connection_loss", "locked_manually", "locked_by_external_user", "locked_by_space_member", "locked_by_scenario", "locking_failed", "battery_low", "doorbell_pressed", "locked_automatically", "locked_by_keypad", "keypad_temporarily_disabled", "locked_by_matter")
    ADDED_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_LOSS_FIELD_NUMBER: _ClassVar[int]
    LOCKED_MANUALLY_FIELD_NUMBER: _ClassVar[int]
    LOCKED_BY_EXTERNAL_USER_FIELD_NUMBER: _ClassVar[int]
    LOCKED_BY_SPACE_MEMBER_FIELD_NUMBER: _ClassVar[int]
    LOCKED_BY_SCENARIO_FIELD_NUMBER: _ClassVar[int]
    LOCKING_FAILED_FIELD_NUMBER: _ClassVar[int]
    BATTERY_LOW_FIELD_NUMBER: _ClassVar[int]
    DOORBELL_PRESSED_FIELD_NUMBER: _ClassVar[int]
    LOCKED_AUTOMATICALLY_FIELD_NUMBER: _ClassVar[int]
    LOCKED_BY_KEYPAD_FIELD_NUMBER: _ClassVar[int]
    KEYPAD_TEMPORARILY_DISABLED_FIELD_NUMBER: _ClassVar[int]
    LOCKED_BY_MATTER_FIELD_NUMBER: _ClassVar[int]
    added: Added
    removed: Removed
    connection_loss: ConnectionLoss
    locked_manually: LockedManually
    locked_by_external_user: LockedByExternalUser
    locked_by_space_member: LockedBySpaceMember
    locked_by_scenario: LockedByScenario
    locking_failed: LockingFailed
    battery_low: BatteryLow
    doorbell_pressed: DoorbellPressed
    locked_automatically: LockedAutomatically
    locked_by_keypad: LockedByKeypad
    keypad_temporarily_disabled: KeypadTemporarilyDisabled
    locked_by_matter: LockedByMatter
    def __init__(self, added: _Optional[_Union[Added, _Mapping]] = ..., removed: _Optional[_Union[Removed, _Mapping]] = ..., connection_loss: _Optional[_Union[ConnectionLoss, _Mapping]] = ..., locked_manually: _Optional[_Union[LockedManually, _Mapping]] = ..., locked_by_external_user: _Optional[_Union[LockedByExternalUser, _Mapping]] = ..., locked_by_space_member: _Optional[_Union[LockedBySpaceMember, _Mapping]] = ..., locked_by_scenario: _Optional[_Union[LockedByScenario, _Mapping]] = ..., locking_failed: _Optional[_Union[LockingFailed, _Mapping]] = ..., battery_low: _Optional[_Union[BatteryLow, _Mapping]] = ..., doorbell_pressed: _Optional[_Union[DoorbellPressed, _Mapping]] = ..., locked_automatically: _Optional[_Union[LockedAutomatically, _Mapping]] = ..., locked_by_keypad: _Optional[_Union[LockedByKeypad, _Mapping]] = ..., keypad_temporarily_disabled: _Optional[_Union[KeypadTemporarilyDisabled, _Mapping]] = ..., locked_by_matter: _Optional[_Union[LockedByMatter, _Mapping]] = ...) -> None: ...
