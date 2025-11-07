from google.protobuf import timestamp_pb2 as _timestamp_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import space_pb2 as _space_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import folder_pb2 as _folder_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import importance_pb2 as _importance_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import content_pb2 as _content_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import additional_data_pb2 as _additional_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Notification(_message.Message):
    __slots__ = ("id", "universal_token", "space", "server_timestamp", "folder", "importance", "content", "read_by_user", "additional_data")
    ID_FIELD_NUMBER: _ClassVar[int]
    UNIVERSAL_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SPACE_FIELD_NUMBER: _ClassVar[int]
    SERVER_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    FOLDER_FIELD_NUMBER: _ClassVar[int]
    IMPORTANCE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    READ_BY_USER_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_DATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    universal_token: str
    space: _space_pb2.NotificationSpace
    server_timestamp: _timestamp_pb2.Timestamp
    folder: _folder_pb2.NotificationFolder
    importance: _importance_pb2.NotificationImportance
    content: _content_pb2.NotificationContent
    read_by_user: bool
    additional_data: _containers.RepeatedCompositeFieldContainer[_additional_data_pb2.NotificationAdditionalData]
    def __init__(self, id: _Optional[str] = ..., universal_token: _Optional[str] = ..., space: _Optional[_Union[_space_pb2.NotificationSpace, _Mapping]] = ..., server_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., folder: _Optional[_Union[_folder_pb2.NotificationFolder, str]] = ..., importance: _Optional[_Union[_importance_pb2.NotificationImportance, str]] = ..., content: _Optional[_Union[_content_pb2.NotificationContent, _Mapping]] = ..., read_by_user: bool = ..., additional_data: _Optional[_Iterable[_Union[_additional_data_pb2.NotificationAdditionalData, _Mapping]]] = ...) -> None: ...
