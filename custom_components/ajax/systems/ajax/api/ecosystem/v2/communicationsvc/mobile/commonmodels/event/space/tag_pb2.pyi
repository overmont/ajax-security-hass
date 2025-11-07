from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UnknownEvent(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceArmed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceArmedWithMalfunctions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceDisarmed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceDuressDisarmed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceNightModeOn(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceNightModeOnWithMalfunctions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceNightModeOff(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceDuressNightModeOff(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceGroupArmed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceGroupArmedWithMalfunctions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceGroupDisarmed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceGroupDuressDisarmed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpacePanicButtonPressed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PermanentPermissionsRequestReceived(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemporaryPermissionsRequestReceived(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RequestedPermanentPermissionsApproved(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RequestedTemporaryPermissionsApproved(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RequestedFullPermissionsRejected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TimezoneChanged(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Added(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Removed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Created(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Deleted(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NotifiedAboutRemoving(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceGroupAutoArmed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceGroupAutoArmedWithMalfunctions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceGroupAutoDisarmed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceAutoArmed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceAutoArmedWithMalfunctions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceAutoDisarmed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class JoinSpaceRequestReceived(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class JoinSpaceRequestDeclined(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExitDelayComplete(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceEventTag(_message.Message):
    __slots__ = ("space_armed", "space_disarmed", "space_night_mode_on", "space_night_mode_off", "space_group_armed", "space_group_disarmed", "permanent_permissions_request_received", "temporary_permissions_request_received", "requested_permanent_permissions_approved", "requested_temporary_permissions_approved", "requested_full_permissions_rejected", "space_group_armed_with_malfunctions", "space_armed_with_malfunctions", "space_night_mode_on_with_malfunctions", "space_duress_disarmed", "space_duress_night_mode_off", "space_group_duress_disarmed", "space_panic_button_pressed", "timezone_changed", "added", "removed", "created", "deleted", "notified_about_removing", "exit_delay_complete", "space_group_auto_armed", "space_group_auto_armed_with_malfunctions", "space_group_auto_disarmed", "space_auto_armed", "space_auto_armed_with_malfunctions", "space_auto_disarmed", "join_space_request_received", "join_space_request_declined", "unknown_event")
    SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
    SPACE_DISARMED_FIELD_NUMBER: _ClassVar[int]
    SPACE_NIGHT_MODE_ON_FIELD_NUMBER: _ClassVar[int]
    SPACE_NIGHT_MODE_OFF_FIELD_NUMBER: _ClassVar[int]
    SPACE_GROUP_ARMED_FIELD_NUMBER: _ClassVar[int]
    SPACE_GROUP_DISARMED_FIELD_NUMBER: _ClassVar[int]
    PERMANENT_PERMISSIONS_REQUEST_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_PERMISSIONS_REQUEST_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_PERMANENT_PERMISSIONS_APPROVED_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_TEMPORARY_PERMISSIONS_APPROVED_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_FULL_PERMISSIONS_REJECTED_FIELD_NUMBER: _ClassVar[int]
    SPACE_GROUP_ARMED_WITH_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    SPACE_ARMED_WITH_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    SPACE_NIGHT_MODE_ON_WITH_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    SPACE_DURESS_DISARMED_FIELD_NUMBER: _ClassVar[int]
    SPACE_DURESS_NIGHT_MODE_OFF_FIELD_NUMBER: _ClassVar[int]
    SPACE_GROUP_DURESS_DISARMED_FIELD_NUMBER: _ClassVar[int]
    SPACE_PANIC_BUTTON_PRESSED_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_CHANGED_FIELD_NUMBER: _ClassVar[int]
    ADDED_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    NOTIFIED_ABOUT_REMOVING_FIELD_NUMBER: _ClassVar[int]
    EXIT_DELAY_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    SPACE_GROUP_AUTO_ARMED_FIELD_NUMBER: _ClassVar[int]
    SPACE_GROUP_AUTO_ARMED_WITH_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    SPACE_GROUP_AUTO_DISARMED_FIELD_NUMBER: _ClassVar[int]
    SPACE_AUTO_ARMED_FIELD_NUMBER: _ClassVar[int]
    SPACE_AUTO_ARMED_WITH_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    SPACE_AUTO_DISARMED_FIELD_NUMBER: _ClassVar[int]
    JOIN_SPACE_REQUEST_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    JOIN_SPACE_REQUEST_DECLINED_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_EVENT_FIELD_NUMBER: _ClassVar[int]
    space_armed: SpaceArmed
    space_disarmed: SpaceDisarmed
    space_night_mode_on: SpaceNightModeOn
    space_night_mode_off: SpaceNightModeOff
    space_group_armed: SpaceGroupArmed
    space_group_disarmed: SpaceGroupDisarmed
    permanent_permissions_request_received: PermanentPermissionsRequestReceived
    temporary_permissions_request_received: TemporaryPermissionsRequestReceived
    requested_permanent_permissions_approved: RequestedPermanentPermissionsApproved
    requested_temporary_permissions_approved: RequestedTemporaryPermissionsApproved
    requested_full_permissions_rejected: RequestedFullPermissionsRejected
    space_group_armed_with_malfunctions: SpaceGroupArmedWithMalfunctions
    space_armed_with_malfunctions: SpaceArmedWithMalfunctions
    space_night_mode_on_with_malfunctions: SpaceNightModeOnWithMalfunctions
    space_duress_disarmed: SpaceDuressDisarmed
    space_duress_night_mode_off: SpaceDuressNightModeOff
    space_group_duress_disarmed: SpaceGroupDuressDisarmed
    space_panic_button_pressed: SpacePanicButtonPressed
    timezone_changed: TimezoneChanged
    added: Added
    removed: Removed
    created: Created
    deleted: Deleted
    notified_about_removing: NotifiedAboutRemoving
    exit_delay_complete: ExitDelayComplete
    space_group_auto_armed: SpaceGroupAutoArmed
    space_group_auto_armed_with_malfunctions: SpaceGroupAutoArmedWithMalfunctions
    space_group_auto_disarmed: SpaceGroupAutoDisarmed
    space_auto_armed: SpaceAutoArmed
    space_auto_armed_with_malfunctions: SpaceAutoArmedWithMalfunctions
    space_auto_disarmed: SpaceAutoDisarmed
    join_space_request_received: JoinSpaceRequestReceived
    join_space_request_declined: JoinSpaceRequestDeclined
    unknown_event: UnknownEvent
    def __init__(self, space_armed: _Optional[_Union[SpaceArmed, _Mapping]] = ..., space_disarmed: _Optional[_Union[SpaceDisarmed, _Mapping]] = ..., space_night_mode_on: _Optional[_Union[SpaceNightModeOn, _Mapping]] = ..., space_night_mode_off: _Optional[_Union[SpaceNightModeOff, _Mapping]] = ..., space_group_armed: _Optional[_Union[SpaceGroupArmed, _Mapping]] = ..., space_group_disarmed: _Optional[_Union[SpaceGroupDisarmed, _Mapping]] = ..., permanent_permissions_request_received: _Optional[_Union[PermanentPermissionsRequestReceived, _Mapping]] = ..., temporary_permissions_request_received: _Optional[_Union[TemporaryPermissionsRequestReceived, _Mapping]] = ..., requested_permanent_permissions_approved: _Optional[_Union[RequestedPermanentPermissionsApproved, _Mapping]] = ..., requested_temporary_permissions_approved: _Optional[_Union[RequestedTemporaryPermissionsApproved, _Mapping]] = ..., requested_full_permissions_rejected: _Optional[_Union[RequestedFullPermissionsRejected, _Mapping]] = ..., space_group_armed_with_malfunctions: _Optional[_Union[SpaceGroupArmedWithMalfunctions, _Mapping]] = ..., space_armed_with_malfunctions: _Optional[_Union[SpaceArmedWithMalfunctions, _Mapping]] = ..., space_night_mode_on_with_malfunctions: _Optional[_Union[SpaceNightModeOnWithMalfunctions, _Mapping]] = ..., space_duress_disarmed: _Optional[_Union[SpaceDuressDisarmed, _Mapping]] = ..., space_duress_night_mode_off: _Optional[_Union[SpaceDuressNightModeOff, _Mapping]] = ..., space_group_duress_disarmed: _Optional[_Union[SpaceGroupDuressDisarmed, _Mapping]] = ..., space_panic_button_pressed: _Optional[_Union[SpacePanicButtonPressed, _Mapping]] = ..., timezone_changed: _Optional[_Union[TimezoneChanged, _Mapping]] = ..., added: _Optional[_Union[Added, _Mapping]] = ..., removed: _Optional[_Union[Removed, _Mapping]] = ..., created: _Optional[_Union[Created, _Mapping]] = ..., deleted: _Optional[_Union[Deleted, _Mapping]] = ..., notified_about_removing: _Optional[_Union[NotifiedAboutRemoving, _Mapping]] = ..., exit_delay_complete: _Optional[_Union[ExitDelayComplete, _Mapping]] = ..., space_group_auto_armed: _Optional[_Union[SpaceGroupAutoArmed, _Mapping]] = ..., space_group_auto_armed_with_malfunctions: _Optional[_Union[SpaceGroupAutoArmedWithMalfunctions, _Mapping]] = ..., space_group_auto_disarmed: _Optional[_Union[SpaceGroupAutoDisarmed, _Mapping]] = ..., space_auto_armed: _Optional[_Union[SpaceAutoArmed, _Mapping]] = ..., space_auto_armed_with_malfunctions: _Optional[_Union[SpaceAutoArmedWithMalfunctions, _Mapping]] = ..., space_auto_disarmed: _Optional[_Union[SpaceAutoDisarmed, _Mapping]] = ..., join_space_request_received: _Optional[_Union[JoinSpaceRequestReceived, _Mapping]] = ..., join_space_request_declined: _Optional[_Union[JoinSpaceRequestDeclined, _Mapping]] = ..., unknown_event: _Optional[_Union[UnknownEvent, _Mapping]] = ...) -> None: ...
