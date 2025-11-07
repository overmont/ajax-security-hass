from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import object_type_pb2 as _object_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApplyCompanyTemplateRequest(_message.Message):
    __slots__ = ("template_id", "hub_id", "objects")
    class HubObject(_message.Message):
        __slots__ = ("id", "type")
        ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        id: str
        type: _object_type_pb2.ObjectType
        def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[_object_type_pb2.ObjectType, _Mapping]] = ...) -> None: ...
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    hub_id: str
    objects: _containers.RepeatedCompositeFieldContainer[ApplyCompanyTemplateRequest.HubObject]
    def __init__(self, template_id: _Optional[str] = ..., hub_id: _Optional[str] = ..., objects: _Optional[_Iterable[_Union[ApplyCompanyTemplateRequest.HubObject, _Mapping]]] = ...) -> None: ...
