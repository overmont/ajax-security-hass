from systems.ajax.api.mobile.v2.common.space.security.group import group_mode_space_security_pb2 as _group_mode_space_security_pb2
from systems.ajax.api.mobile.v2.common.space.security.regular import regular_mode_space_security_pb2 as _regular_mode_space_security_pb2
from systems.ajax.api.mobile.v2.common.space.security import displayed_space_security_state_pb2 as _displayed_space_security_state_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceSecurityMode(_message.Message):
    __slots__ = ("regular_mode", "group_mode", "displayed_security_state")
    REGULAR_MODE_FIELD_NUMBER: _ClassVar[int]
    GROUP_MODE_FIELD_NUMBER: _ClassVar[int]
    DISPLAYED_SECURITY_STATE_FIELD_NUMBER: _ClassVar[int]
    regular_mode: _regular_mode_space_security_pb2.RegularModeSpaceSecurity
    group_mode: _group_mode_space_security_pb2.GroupModeSpaceSecurity
    displayed_security_state: _displayed_space_security_state_pb2.DisplayedSpaceSecurityState
    def __init__(self, regular_mode: _Optional[_Union[_regular_mode_space_security_pb2.RegularModeSpaceSecurity, _Mapping]] = ..., group_mode: _Optional[_Union[_group_mode_space_security_pb2.GroupModeSpaceSecurity, _Mapping]] = ..., displayed_security_state: _Optional[_Union[_displayed_space_security_state_pb2.DisplayedSpaceSecurityState, str]] = ...) -> None: ...
