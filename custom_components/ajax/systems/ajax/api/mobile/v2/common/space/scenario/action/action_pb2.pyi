from systems.ajax.api.mobile.v2.common.space.scenario.action import change_arming_state_pb2 as _change_arming_state_pb2
from systems.ajax.api.mobile.v2.common.space.scenario.action import switch_state_pb2 as _switch_state_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Action(_message.Message):
    __slots__ = ("change_arming_state", "switch_state")
    CHANGE_ARMING_STATE_FIELD_NUMBER: _ClassVar[int]
    SWITCH_STATE_FIELD_NUMBER: _ClassVar[int]
    change_arming_state: _change_arming_state_pb2.ChangeArmingStateAction
    switch_state: _switch_state_pb2.SwitchStateAction
    def __init__(self, change_arming_state: _Optional[_Union[_change_arming_state_pb2.ChangeArmingStateAction, _Mapping]] = ..., switch_state: _Optional[_Union[_switch_state_pb2.SwitchStateAction, _Mapping]] = ...) -> None: ...
