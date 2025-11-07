from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.smartlock import source_type_pb2 as _source_type_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SmartLockNotificationSource(_message.Message):
    __slots__ = ("type", "id", "name", "room_hex_id", "room_name")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROOM_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    type: _source_type_pb2.SmartLockNotificationSourceType
    id: str
    name: str
    room_hex_id: str
    room_name: str
    def __init__(self, type: _Optional[_Union[_source_type_pb2.SmartLockNotificationSourceType, str]] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., room_hex_id: _Optional[str] = ..., room_name: _Optional[str] = ...) -> None: ...
