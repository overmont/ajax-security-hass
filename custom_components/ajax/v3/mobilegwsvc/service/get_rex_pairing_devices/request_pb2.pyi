from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import object_type_pb2 as _object_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetRexPairingDevicesRequest(_message.Message):
    __slots__ = ("hub_id", "rex_id", "rex_type")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    REX_ID_FIELD_NUMBER: _ClassVar[int]
    REX_TYPE_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    rex_id: str
    rex_type: _object_type_pb2.ObjectType
    def __init__(self, hub_id: _Optional[str] = ..., rex_id: _Optional[str] = ..., rex_type: _Optional[_Union[_object_type_pb2.ObjectType, _Mapping]] = ...) -> None: ...
