from v3.mobilegwsvc.commonmodels.hub.object import hub_object_type_with_index_pb2 as _hub_object_type_with_index_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateHubObjectIndexRequest(_message.Message):
    __slots__ = ("hub_id", "hub_object_type_with_index", "object_id", "index")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    HUB_OBJECT_TYPE_WITH_INDEX_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    hub_object_type_with_index: _hub_object_type_with_index_pb2.HubObjectTypeWithIndex
    object_id: str
    index: int
    def __init__(self, hub_id: _Optional[str] = ..., hub_object_type_with_index: _Optional[_Union[_hub_object_type_with_index_pb2.HubObjectTypeWithIndex, str]] = ..., object_id: _Optional[str] = ..., index: _Optional[int] = ...) -> None: ...
