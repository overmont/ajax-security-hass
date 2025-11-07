from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TemporaryVideoAccessDeniedForCompanyData(_message.Message):
    __slots__ = ("company_id", "company_name", "company_email", "request_id")
    COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPANY_EMAIL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    company_id: str
    company_name: str
    company_email: str
    request_id: str
    def __init__(self, company_id: _Optional[str] = ..., company_name: _Optional[str] = ..., company_email: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...
