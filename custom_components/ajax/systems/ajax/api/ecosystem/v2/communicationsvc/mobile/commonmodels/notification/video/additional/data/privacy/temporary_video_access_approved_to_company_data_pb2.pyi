from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TemporaryVideoAccessApprovedToCompanyData(_message.Message):
    __slots__ = ("company_id", "company_name", "company_email", "request_id", "duration")
    COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPANY_EMAIL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    company_id: str
    company_name: str
    company_email: str
    request_id: str
    duration: _duration_pb2.Duration
    def __init__(self, company_id: _Optional[str] = ..., company_name: _Optional[str] = ..., company_email: _Optional[str] = ..., request_id: _Optional[str] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
