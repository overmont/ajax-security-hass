from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TemporaryVideoAccessDeniedForProData(_message.Message):
    __slots__ = ("requester_member_id", "requester_name", "requester_email", "request_id")
    REQUESTER_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTER_NAME_FIELD_NUMBER: _ClassVar[int]
    REQUESTER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    requester_member_id: str
    requester_name: str
    requester_email: str
    request_id: str
    def __init__(self, requester_member_id: _Optional[str] = ..., requester_name: _Optional[str] = ..., requester_email: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...
