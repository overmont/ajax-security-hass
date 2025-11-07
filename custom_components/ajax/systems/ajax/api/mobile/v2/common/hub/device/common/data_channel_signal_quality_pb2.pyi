from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DataChannelSignalQuality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATA_CHANNEL_SIGNAL_QUALITY_UNSPECIFIED: _ClassVar[DataChannelSignalQuality]
    DATA_CHANNEL_SIGNAL_QUALITY_NO: _ClassVar[DataChannelSignalQuality]
    DATA_CHANNEL_SIGNAL_QUALITY_WEAK: _ClassVar[DataChannelSignalQuality]
    DATA_CHANNEL_SIGNAL_QUALITY_NORMAL: _ClassVar[DataChannelSignalQuality]
    DATA_CHANNEL_SIGNAL_QUALITY_STRONG: _ClassVar[DataChannelSignalQuality]
DATA_CHANNEL_SIGNAL_QUALITY_UNSPECIFIED: DataChannelSignalQuality
DATA_CHANNEL_SIGNAL_QUALITY_NO: DataChannelSignalQuality
DATA_CHANNEL_SIGNAL_QUALITY_WEAK: DataChannelSignalQuality
DATA_CHANNEL_SIGNAL_QUALITY_NORMAL: DataChannelSignalQuality
DATA_CHANNEL_SIGNAL_QUALITY_STRONG: DataChannelSignalQuality
