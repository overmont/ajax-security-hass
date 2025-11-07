from systems.ajax.protobuf.hub import name_pb2 as _name_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccessKey(_message.Message):
    __slots__ = ("id", "name", "access_key_id", "associated_group_id", "associated_user_id", "cms_device_index")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CMS_DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _name_pb2.Name
    access_key_id: str
    associated_group_id: str
    associated_user_id: str
    cms_device_index: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[_Union[_name_pb2.Name, _Mapping]] = ..., access_key_id: _Optional[str] = ..., associated_group_id: _Optional[str] = ..., associated_user_id: _Optional[str] = ..., cms_device_index: _Optional[int] = ...) -> None: ...
