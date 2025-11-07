from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ImageStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IMAGE_STATUS_UNSPECIFIED: _ClassVar[ImageStatus]
    IMAGE_STATUS_IN_PROGRESS: _ClassVar[ImageStatus]
    IMAGE_STATUS_READY: _ClassVar[ImageStatus]
    IMAGE_STATUS_FAILED: _ClassVar[ImageStatus]
IMAGE_STATUS_UNSPECIFIED: ImageStatus
IMAGE_STATUS_IN_PROGRESS: ImageStatus
IMAGE_STATUS_READY: ImageStatus
IMAGE_STATUS_FAILED: ImageStatus
