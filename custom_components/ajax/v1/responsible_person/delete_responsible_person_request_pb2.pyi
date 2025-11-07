from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteResponsiblePersonRequest(_message.Message):
    __slots__ = ("facility_id", "facility_responsible_person_id")
    FACILITY_ID_FIELD_NUMBER: _ClassVar[int]
    FACILITY_RESPONSIBLE_PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    facility_id: str
    facility_responsible_person_id: str
    def __init__(self, facility_id: _Optional[str] = ..., facility_responsible_person_id: _Optional[str] = ...) -> None: ...
