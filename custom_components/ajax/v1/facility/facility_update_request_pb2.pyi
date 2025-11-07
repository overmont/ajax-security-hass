from v1.facility import facility_pb2 as _facility_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FacilityUpdateRequest(_message.Message):
    __slots__ = ("facility", "notes")
    class FacilityUpdateModel(_message.Message):
        __slots__ = ("facility_id", "general_info", "version", "mask")
        FACILITY_ID_FIELD_NUMBER: _ClassVar[int]
        GENERAL_INFO_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        MASK_FIELD_NUMBER: _ClassVar[int]
        facility_id: str
        general_info: _facility_pb2.Facility.GeneralInfo
        version: int
        mask: _field_mask_pb2.FieldMask
        def __init__(self, facility_id: _Optional[str] = ..., general_info: _Optional[_Union[_facility_pb2.Facility.GeneralInfo, _Mapping]] = ..., version: _Optional[int] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...
    FACILITY_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    facility: FacilityUpdateRequest.FacilityUpdateModel
    notes: _containers.RepeatedCompositeFieldContainer[_facility_pb2.Facility.Note]
    def __init__(self, facility: _Optional[_Union[FacilityUpdateRequest.FacilityUpdateModel, _Mapping]] = ..., notes: _Optional[_Iterable[_Union[_facility_pb2.Facility.Note, _Mapping]]] = ...) -> None: ...
