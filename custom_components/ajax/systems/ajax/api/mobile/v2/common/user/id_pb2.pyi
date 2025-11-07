from systems.ajax.api.mobile.v2.common.user import type_pb2 as _type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserId(_message.Message):
    __slots__ = ("hex_id", "type")
    HEX_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    hex_id: str
    type: _type_pb2.UserType
    def __init__(self, hex_id: _Optional[str] = ..., type: _Optional[_Union[_type_pb2.UserType, str]] = ...) -> None: ...
