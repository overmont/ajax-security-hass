from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class FeatureTarget(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FEATURE_TARGET_NO_INFO: _ClassVar[FeatureTarget]
    FEATURE_TARGET_HUB: _ClassVar[FeatureTarget]
    FEATURE_TARGET_VIDEO_EDGE_CHANNEL: _ClassVar[FeatureTarget]
    FEATURE_TARGET_VIDEO_EDGE: _ClassVar[FeatureTarget]
FEATURE_TARGET_NO_INFO: FeatureTarget
FEATURE_TARGET_HUB: FeatureTarget
FEATURE_TARGET_VIDEO_EDGE_CHANNEL: FeatureTarget
FEATURE_TARGET_VIDEO_EDGE: FeatureTarget
