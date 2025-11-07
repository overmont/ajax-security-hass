from v1.facility import facility_pb2 as _facility_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FacilityStreamNotesResponse(_message.Message):
    __slots__ = ("notes",)
    NOTES_FIELD_NUMBER: _ClassVar[int]
    notes: _containers.RepeatedCompositeFieldContainer[_facility_pb2.Facility.Note]
    def __init__(self, notes: _Optional[_Iterable[_Union[_facility_pb2.Facility.Note, _Mapping]]] = ...) -> None: ...
