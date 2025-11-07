from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MotionCamVideoBase(_message.Message):
    __slots__ = ()
    class SirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SIREN_TRIGGER_UNSPECIFIED: _ClassVar[MotionCamVideoBase.SirenTrigger]
        SIREN_TRIGGER_MOTION: _ClassVar[MotionCamVideoBase.SirenTrigger]
    SIREN_TRIGGER_UNSPECIFIED: MotionCamVideoBase.SirenTrigger
    SIREN_TRIGGER_MOTION: MotionCamVideoBase.SirenTrigger
    class ChimeTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHIME_TRIGGER_UNSPECIFIED: _ClassVar[MotionCamVideoBase.ChimeTrigger]
        CHIME_TRIGGER_BUTTON: _ClassVar[MotionCamVideoBase.ChimeTrigger]
    CHIME_TRIGGER_UNSPECIFIED: MotionCamVideoBase.ChimeTrigger
    CHIME_TRIGGER_BUTTON: MotionCamVideoBase.ChimeTrigger
    def __init__(self) -> None: ...
