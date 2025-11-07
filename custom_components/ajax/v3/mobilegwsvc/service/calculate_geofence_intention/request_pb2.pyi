from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CalculateGeofenceIntentionRequest(_message.Message):
    __slots__ = ("hub_id", "desired_state")
    class DesiredState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DESIRED_STATE_UNSPECIFIED: _ClassVar[CalculateGeofenceIntentionRequest.DesiredState]
        DESIRED_STATE_ARMED: _ClassVar[CalculateGeofenceIntentionRequest.DesiredState]
        DESIRED_STATE_DISARMED: _ClassVar[CalculateGeofenceIntentionRequest.DesiredState]
    DESIRED_STATE_UNSPECIFIED: CalculateGeofenceIntentionRequest.DesiredState
    DESIRED_STATE_ARMED: CalculateGeofenceIntentionRequest.DesiredState
    DESIRED_STATE_DISARMED: CalculateGeofenceIntentionRequest.DesiredState
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DESIRED_STATE_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    desired_state: CalculateGeofenceIntentionRequest.DesiredState
    def __init__(self, hub_id: _Optional[str] = ..., desired_state: _Optional[_Union[CalculateGeofenceIntentionRequest.DesiredState, str]] = ...) -> None: ...
