from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PhotoOnDemand(_message.Message):
    __slots__ = ("estimated_arming_state",)
    class EstimatedArmingState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ESTIMATED_ARMING_STATE_UNSPECIFIED: _ClassVar[PhotoOnDemand.EstimatedArmingState]
        ESTIMATED_ARMING_STATE_DISARMED: _ClassVar[PhotoOnDemand.EstimatedArmingState]
        ESTIMATED_ARMING_STATE_ARMED: _ClassVar[PhotoOnDemand.EstimatedArmingState]
        ESTIMATED_ARMING_STATE_N_A: _ClassVar[PhotoOnDemand.EstimatedArmingState]
    ESTIMATED_ARMING_STATE_UNSPECIFIED: PhotoOnDemand.EstimatedArmingState
    ESTIMATED_ARMING_STATE_DISARMED: PhotoOnDemand.EstimatedArmingState
    ESTIMATED_ARMING_STATE_ARMED: PhotoOnDemand.EstimatedArmingState
    ESTIMATED_ARMING_STATE_N_A: PhotoOnDemand.EstimatedArmingState
    ESTIMATED_ARMING_STATE_FIELD_NUMBER: _ClassVar[int]
    estimated_arming_state: PhotoOnDemand.EstimatedArmingState
    def __init__(self, estimated_arming_state: _Optional[_Union[PhotoOnDemand.EstimatedArmingState, str]] = ...) -> None: ...
