from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FireDeviceActionButton(_message.Message):
    __slots__ = ("mute_button", "critical_smoke_button", "critical_co_button", "postpone_button")
    class MuteCommand(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MUTE_COMMAND_UNSPECIFIED: _ClassVar[FireDeviceActionButton.MuteCommand]
        MUTE_COMMAND_OWN: _ClassVar[FireDeviceActionButton.MuteCommand]
        MUTE_COMMAND_OWN_PLUS_EXTERNAL: _ClassVar[FireDeviceActionButton.MuteCommand]
    MUTE_COMMAND_UNSPECIFIED: FireDeviceActionButton.MuteCommand
    MUTE_COMMAND_OWN: FireDeviceActionButton.MuteCommand
    MUTE_COMMAND_OWN_PLUS_EXTERNAL: FireDeviceActionButton.MuteCommand
    class RequiredPermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REQUIRED_PERMISSION_UNSPECIFIED: _ClassVar[FireDeviceActionButton.RequiredPermission]
        REQUIRED_PERMISSION_GROUPS: _ClassVar[FireDeviceActionButton.RequiredPermission]
        REQUIRED_PERMISSION_MUTE: _ClassVar[FireDeviceActionButton.RequiredPermission]
        REQUIRED_PERMISSION_HOME_AUTOMATION: _ClassVar[FireDeviceActionButton.RequiredPermission]
    REQUIRED_PERMISSION_UNSPECIFIED: FireDeviceActionButton.RequiredPermission
    REQUIRED_PERMISSION_GROUPS: FireDeviceActionButton.RequiredPermission
    REQUIRED_PERMISSION_MUTE: FireDeviceActionButton.RequiredPermission
    REQUIRED_PERMISSION_HOME_AUTOMATION: FireDeviceActionButton.RequiredPermission
    class MuteButton(_message.Message):
        __slots__ = ("mute_command", "required_permissions")
        MUTE_COMMAND_FIELD_NUMBER: _ClassVar[int]
        REQUIRED_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        mute_command: FireDeviceActionButton.MuteCommand
        required_permissions: _containers.RepeatedScalarFieldContainer[FireDeviceActionButton.RequiredPermission]
        def __init__(self, mute_command: _Optional[_Union[FireDeviceActionButton.MuteCommand, str]] = ..., required_permissions: _Optional[_Iterable[_Union[FireDeviceActionButton.RequiredPermission, str]]] = ...) -> None: ...
    class CriticalSmokeButton(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class CriticalCOButton(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class PostponeButton(_message.Message):
        __slots__ = ("required_permission",)
        REQUIRED_PERMISSION_FIELD_NUMBER: _ClassVar[int]
        required_permission: _containers.RepeatedScalarFieldContainer[FireDeviceActionButton.RequiredPermission]
        def __init__(self, required_permission: _Optional[_Iterable[_Union[FireDeviceActionButton.RequiredPermission, str]]] = ...) -> None: ...
    MUTE_BUTTON_FIELD_NUMBER: _ClassVar[int]
    CRITICAL_SMOKE_BUTTON_FIELD_NUMBER: _ClassVar[int]
    CRITICAL_CO_BUTTON_FIELD_NUMBER: _ClassVar[int]
    POSTPONE_BUTTON_FIELD_NUMBER: _ClassVar[int]
    mute_button: FireDeviceActionButton.MuteButton
    critical_smoke_button: FireDeviceActionButton.CriticalSmokeButton
    critical_co_button: FireDeviceActionButton.CriticalCOButton
    postpone_button: FireDeviceActionButton.PostponeButton
    def __init__(self, mute_button: _Optional[_Union[FireDeviceActionButton.MuteButton, _Mapping]] = ..., critical_smoke_button: _Optional[_Union[FireDeviceActionButton.CriticalSmokeButton, _Mapping]] = ..., critical_co_button: _Optional[_Union[FireDeviceActionButton.CriticalCOButton, _Mapping]] = ..., postpone_button: _Optional[_Union[FireDeviceActionButton.PostponeButton, _Mapping]] = ...) -> None: ...
