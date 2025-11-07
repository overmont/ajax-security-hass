from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class TwoStageArmingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TWO_STAGE_ARMING_MODE_UNSPECIFIED: _ClassVar[TwoStageArmingMode]
    TWO_STAGE_ARMING_MODE_ENABLED: _ClassVar[TwoStageArmingMode]
    TWO_STAGE_ARMING_MODE_DISABLED: _ClassVar[TwoStageArmingMode]
TWO_STAGE_ARMING_MODE_UNSPECIFIED: TwoStageArmingMode
TWO_STAGE_ARMING_MODE_ENABLED: TwoStageArmingMode
TWO_STAGE_ARMING_MODE_DISABLED: TwoStageArmingMode
