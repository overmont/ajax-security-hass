from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceCommandManageLinesPowerSupplyRequest(_message.Message):
    __slots__ = ("hub_id", "actions")
    class Action(_message.Message):
        __slots__ = ("bus_id", "switch_state")
        class SwitchState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SWITCH_STATE_UNSPECIFIED: _ClassVar[DeviceCommandManageLinesPowerSupplyRequest.Action.SwitchState]
            SWITCH_STATE_DISABLED: _ClassVar[DeviceCommandManageLinesPowerSupplyRequest.Action.SwitchState]
            SWITCH_STATE_ENABLED: _ClassVar[DeviceCommandManageLinesPowerSupplyRequest.Action.SwitchState]
        SWITCH_STATE_UNSPECIFIED: DeviceCommandManageLinesPowerSupplyRequest.Action.SwitchState
        SWITCH_STATE_DISABLED: DeviceCommandManageLinesPowerSupplyRequest.Action.SwitchState
        SWITCH_STATE_ENABLED: DeviceCommandManageLinesPowerSupplyRequest.Action.SwitchState
        BUS_ID_FIELD_NUMBER: _ClassVar[int]
        SWITCH_STATE_FIELD_NUMBER: _ClassVar[int]
        bus_id: int
        switch_state: DeviceCommandManageLinesPowerSupplyRequest.Action.SwitchState
        def __init__(self, bus_id: _Optional[int] = ..., switch_state: _Optional[_Union[DeviceCommandManageLinesPowerSupplyRequest.Action.SwitchState, str]] = ...) -> None: ...
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    actions: _containers.RepeatedCompositeFieldContainer[DeviceCommandManageLinesPowerSupplyRequest.Action]
    def __init__(self, hub_id: _Optional[str] = ..., actions: _Optional[_Iterable[_Union[DeviceCommandManageLinesPowerSupplyRequest.Action, _Mapping]]] = ...) -> None: ...
