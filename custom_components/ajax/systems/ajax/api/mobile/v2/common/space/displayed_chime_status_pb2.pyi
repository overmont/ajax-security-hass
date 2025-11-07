from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DisplayedChimeStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DISPLAYED_CHIME_STATUS_UNSPECIFIED: _ClassVar[DisplayedChimeStatus]
    DISPLAYED_CHIME_STATUS_ENABLED: _ClassVar[DisplayedChimeStatus]
    DISPLAYED_CHIME_STATUS_CAN_BE_ENABLED: _ClassVar[DisplayedChimeStatus]
    DISPLAYED_CHIME_STATUS_MALFUNCTION: _ClassVar[DisplayedChimeStatus]
    DISPLAYED_CHIME_STATUS_DISABLED: _ClassVar[DisplayedChimeStatus]
DISPLAYED_CHIME_STATUS_UNSPECIFIED: DisplayedChimeStatus
DISPLAYED_CHIME_STATUS_ENABLED: DisplayedChimeStatus
DISPLAYED_CHIME_STATUS_CAN_BE_ENABLED: DisplayedChimeStatus
DISPLAYED_CHIME_STATUS_MALFUNCTION: DisplayedChimeStatus
DISPLAYED_CHIME_STATUS_DISABLED: DisplayedChimeStatus
