from v1.responsible_person import responsible_person_pb2 as _responsible_person_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateResponsiblePersonResponse(_message.Message):
    __slots__ = ("responsible_person",)
    RESPONSIBLE_PERSON_FIELD_NUMBER: _ClassVar[int]
    responsible_person: _responsible_person_pb2.ResponsiblePerson
    def __init__(self, responsible_person: _Optional[_Union[_responsible_person_pb2.ResponsiblePerson, _Mapping]] = ...) -> None: ...
