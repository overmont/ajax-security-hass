from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FacilityEditableFields(_message.Message):
    __slots__ = ("general_info_editable_fields", "editable_sections")
    class EditableSection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MEDIA: _ClassVar[FacilityEditableFields.EditableSection]
        NOTES: _ClassVar[FacilityEditableFields.EditableSection]
        RESPONSIBLE_PERSONS: _ClassVar[FacilityEditableFields.EditableSection]
        PRIVACY_OVERRIDE: _ClassVar[FacilityEditableFields.EditableSection]
    MEDIA: FacilityEditableFields.EditableSection
    NOTES: FacilityEditableFields.EditableSection
    RESPONSIBLE_PERSONS: FacilityEditableFields.EditableSection
    PRIVACY_OVERRIDE: FacilityEditableFields.EditableSection
    GENERAL_INFO_EDITABLE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    EDITABLE_SECTIONS_FIELD_NUMBER: _ClassVar[int]
    general_info_editable_fields: _field_mask_pb2.FieldMask
    editable_sections: _containers.RepeatedScalarFieldContainer[FacilityEditableFields.EditableSection]
    def __init__(self, general_info_editable_fields: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., editable_sections: _Optional[_Iterable[_Union[FacilityEditableFields.EditableSection, str]]] = ...) -> None: ...
