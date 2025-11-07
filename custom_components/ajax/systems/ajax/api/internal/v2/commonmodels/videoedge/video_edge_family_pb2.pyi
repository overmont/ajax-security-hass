from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class VideoEdgeFamily(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VIDEO_EDGE_FAMILY_UNSPECIFIED: _ClassVar[VideoEdgeFamily]
    VIDEO_EDGE_FAMILY_NVR: _ClassVar[VideoEdgeFamily]
    VIDEO_EDGE_FAMILY_CAMERA: _ClassVar[VideoEdgeFamily]
    VIDEO_EDGE_FAMILY_DOORBELL: _ClassVar[VideoEdgeFamily]
    VIDEO_EDGE_FAMILY_INDOOR_CAM: _ClassVar[VideoEdgeFamily]
VIDEO_EDGE_FAMILY_UNSPECIFIED: VideoEdgeFamily
VIDEO_EDGE_FAMILY_NVR: VideoEdgeFamily
VIDEO_EDGE_FAMILY_CAMERA: VideoEdgeFamily
VIDEO_EDGE_FAMILY_DOORBELL: VideoEdgeFamily
VIDEO_EDGE_FAMILY_INDOOR_CAM: VideoEdgeFamily
