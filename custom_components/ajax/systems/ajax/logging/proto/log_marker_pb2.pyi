from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LogMarker(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOG_MARKER_UNSPECIFIED: _ClassVar[LogMarker]
    LOG_MARKER_VIDEO_EDGE_ID: _ClassVar[LogMarker]
    LOG_MARKER_SPACE_ID: _ClassVar[LogMarker]
    LOG_MARKER_COMPANY_ID: _ClassVar[LogMarker]
    LOG_MARKER_SPACE_MEMBER_ID: _ClassVar[LogMarker]
    LOG_MARKER_HUB_ID: _ClassVar[LogMarker]
    LOG_MARKER_USER_ID: _ClassVar[LogMarker]
    LOG_MARKER_EMPLOYEE_ID: _ClassVar[LogMarker]
    LOG_MARKER_WEBRTC_SESSION_ID: _ClassVar[LogMarker]
LOG_MARKER_UNSPECIFIED: LogMarker
LOG_MARKER_VIDEO_EDGE_ID: LogMarker
LOG_MARKER_SPACE_ID: LogMarker
LOG_MARKER_COMPANY_ID: LogMarker
LOG_MARKER_SPACE_MEMBER_ID: LogMarker
LOG_MARKER_HUB_ID: LogMarker
LOG_MARKER_USER_ID: LogMarker
LOG_MARKER_EMPLOYEE_ID: LogMarker
LOG_MARKER_WEBRTC_SESSION_ID: LogMarker
LOG_MARKER_FIELD_NUMBER: _ClassVar[int]
log_marker: _descriptor.FieldDescriptor
LOG_MARKER_KEY_FIELD_NUMBER: _ClassVar[int]
log_marker_key: _descriptor.FieldDescriptor

class LogMarkerKey(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...
