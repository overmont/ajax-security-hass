from v1.responsible_person import responsible_person_pb2 as _responsible_person_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamResponsiblePersonsResponse(_message.Message):
    __slots__ = ("responsible_persons",)
    RESPONSIBLE_PERSONS_FIELD_NUMBER: _ClassVar[int]
    responsible_persons: _containers.RepeatedCompositeFieldContainer[_responsible_person_pb2.ResponsiblePerson]
    def __init__(self, responsible_persons: _Optional[_Iterable[_Union[_responsible_person_pb2.ResponsiblePerson, _Mapping]]] = ...) -> None: ...
