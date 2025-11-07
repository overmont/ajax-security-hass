from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HubAccessResponse(_message.Message):
    __slots__ = ("profi_mail", "user_id", "pro_name", "access_level", "access_time", "is_request_declined")
    PROFI_MAIL_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PRO_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_REQUEST_DECLINED_FIELD_NUMBER: _ClassVar[int]
    profi_mail: str
    user_id: str
    pro_name: str
    access_level: int
    access_time: int
    is_request_declined: bool
    def __init__(self, profi_mail: _Optional[str] = ..., user_id: _Optional[str] = ..., pro_name: _Optional[str] = ..., access_level: _Optional[int] = ..., access_time: _Optional[int] = ..., is_request_declined: bool = ...) -> None: ...
