from systems.ajax.api.mobile.v2.hubobject.model import hub_object_pb2 as _hub_object_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamHubObjectRequest(_message.Message):
    __slots__ = ("hex_id",)
    HEX_ID_FIELD_NUMBER: _ClassVar[int]
    hex_id: str
    def __init__(self, hex_id: _Optional[str] = ...) -> None: ...

class StreamHubObject(_message.Message):
    __slots__ = ("snapshot", "create", "update", "delete")
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    CREATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    DELETE_FIELD_NUMBER: _ClassVar[int]
    snapshot: _hub_object_pb2.HubObject
    create: _hub_object_pb2.HubObject
    update: _hub_object_pb2.HubObject
    delete: _hub_object_pb2.HubObject
    def __init__(self, snapshot: _Optional[_Union[_hub_object_pb2.HubObject, _Mapping]] = ..., create: _Optional[_Union[_hub_object_pb2.HubObject, _Mapping]] = ..., update: _Optional[_Union[_hub_object_pb2.HubObject, _Mapping]] = ..., delete: _Optional[_Union[_hub_object_pb2.HubObject, _Mapping]] = ...) -> None: ...
