from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceCommandSetWalkTestRequest(_message.Message):
    __slots__ = ("hub_id", "activate", "deactivate")
    class Activate(_message.Message):
        __slots__ = ("timeout_minutes",)
        TIMEOUT_MINUTES_FIELD_NUMBER: _ClassVar[int]
        timeout_minutes: int
        def __init__(self, timeout_minutes: _Optional[int] = ...) -> None: ...
    class Deactivate(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVATE_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATE_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    activate: DeviceCommandSetWalkTestRequest.Activate
    deactivate: DeviceCommandSetWalkTestRequest.Deactivate
    def __init__(self, hub_id: _Optional[str] = ..., activate: _Optional[_Union[DeviceCommandSetWalkTestRequest.Activate, _Mapping]] = ..., deactivate: _Optional[_Union[DeviceCommandSetWalkTestRequest.Deactivate, _Mapping]] = ...) -> None: ...
