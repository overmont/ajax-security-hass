from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DetectorLocator(_message.Message):
    __slots__ = ("channel_id", "detection_type")
    class DetectionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DETECTION_TYPE_UNSPECIFIED: _ClassVar[DetectorLocator.DetectionType]
        DETECTION_TYPE_PIR: _ClassVar[DetectorLocator.DetectionType]
        DETECTION_TYPE_MOTION: _ClassVar[DetectorLocator.DetectionType]
        DETECTION_TYPE_OBJECT: _ClassVar[DetectorLocator.DetectionType]
    DETECTION_TYPE_UNSPECIFIED: DetectorLocator.DetectionType
    DETECTION_TYPE_PIR: DetectorLocator.DetectionType
    DETECTION_TYPE_MOTION: DetectorLocator.DetectionType
    DETECTION_TYPE_OBJECT: DetectorLocator.DetectionType
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    DETECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    detection_type: DetectorLocator.DetectionType
    def __init__(self, channel_id: _Optional[str] = ..., detection_type: _Optional[_Union[DetectorLocator.DetectionType, str]] = ...) -> None: ...
