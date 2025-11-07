from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SimCardStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIM_CARD_STATUS_UNSPECIFIED: _ClassVar[SimCardStatus]
    SIM_CARD_STATUS_OK: _ClassVar[SimCardStatus]
    SIM_CARD_STATUS_MISSING: _ClassVar[SimCardStatus]
    SIM_CARD_STATUS_MALFUNCTION: _ClassVar[SimCardStatus]
    SIM_CARD_STATUS_LOCKED: _ClassVar[SimCardStatus]
    SIM_CARD_STATUS_UNKNOWN: _ClassVar[SimCardStatus]
SIM_CARD_STATUS_UNSPECIFIED: SimCardStatus
SIM_CARD_STATUS_OK: SimCardStatus
SIM_CARD_STATUS_MISSING: SimCardStatus
SIM_CARD_STATUS_MALFUNCTION: SimCardStatus
SIM_CARD_STATUS_LOCKED: SimCardStatus
SIM_CARD_STATUS_UNKNOWN: SimCardStatus
