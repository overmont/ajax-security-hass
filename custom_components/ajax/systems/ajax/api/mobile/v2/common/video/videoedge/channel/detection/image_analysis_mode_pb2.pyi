from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ImageAnalysisMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IMAGE_ANALYSIS_MODE_UNSPECIFIED: _ClassVar[ImageAnalysisMode]
    IMAGE_ANALYSIS_MODE_BY_FRAME: _ClassVar[ImageAnalysisMode]
    IMAGE_ANALYSIS_MODE_BY_CAMERA_ALGORITHM: _ClassVar[ImageAnalysisMode]
IMAGE_ANALYSIS_MODE_UNSPECIFIED: ImageAnalysisMode
IMAGE_ANALYSIS_MODE_BY_FRAME: ImageAnalysisMode
IMAGE_ANALYSIS_MODE_BY_CAMERA_ALGORITHM: ImageAnalysisMode
