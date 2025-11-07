from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class HubBoxType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HUB_BOX_TYPE_UNSPECIFIED: _ClassVar[HubBoxType]
    HUB_BOX_TYPE_PCB: _ClassVar[HubBoxType]
    HUB_BOX_TYPE_CASE_WITH_EXTERNAL_LED: _ClassVar[HubBoxType]
    HUB_BOX_TYPE_CASE_C: _ClassVar[HubBoxType]
    HUB_BOX_TYPE_CASE_D: _ClassVar[HubBoxType]
HUB_BOX_TYPE_UNSPECIFIED: HubBoxType
HUB_BOX_TYPE_PCB: HubBoxType
HUB_BOX_TYPE_CASE_WITH_EXTERNAL_LED: HubBoxType
HUB_BOX_TYPE_CASE_C: HubBoxType
HUB_BOX_TYPE_CASE_D: HubBoxType
