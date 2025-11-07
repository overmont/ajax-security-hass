from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class JewellerSignalQuality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JEWELLER_SIGNAL_QUALITY_UNSPECIFIED: _ClassVar[JewellerSignalQuality]
    JEWELLER_SIGNAL_QUALITY_NO: _ClassVar[JewellerSignalQuality]
    JEWELLER_SIGNAL_QUALITY_WEAK: _ClassVar[JewellerSignalQuality]
    JEWELLER_SIGNAL_QUALITY_NORMAL: _ClassVar[JewellerSignalQuality]
    JEWELLER_SIGNAL_QUALITY_STRONG: _ClassVar[JewellerSignalQuality]
JEWELLER_SIGNAL_QUALITY_UNSPECIFIED: JewellerSignalQuality
JEWELLER_SIGNAL_QUALITY_NO: JewellerSignalQuality
JEWELLER_SIGNAL_QUALITY_WEAK: JewellerSignalQuality
JEWELLER_SIGNAL_QUALITY_NORMAL: JewellerSignalQuality
JEWELLER_SIGNAL_QUALITY_STRONG: JewellerSignalQuality
