from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import source_type_pb2 as _source_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActionSourceObject(_message.Message):
    __slots__ = ("type", "hex_id", "object_name")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    HEX_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    type: _source_type_pb2.HubNotificationSourceType
    hex_id: str
    object_name: str
    def __init__(self, type: _Optional[_Union[_source_type_pb2.HubNotificationSourceType, str]] = ..., hex_id: _Optional[str] = ..., object_name: _Optional[str] = ...) -> None: ...
