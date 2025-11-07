from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import origin_id_pb2 as _origin_id_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import folder_pb2 as _folder_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationsFilter(_message.Message):
    __slots__ = ("origin", "folder")
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    FOLDER_FIELD_NUMBER: _ClassVar[int]
    origin: _origin_id_pb2.NotificationOriginId
    folder: _folder_pb2.NotificationFolder
    def __init__(self, origin: _Optional[_Union[_origin_id_pb2.NotificationOriginId, _Mapping]] = ..., folder: _Optional[_Union[_folder_pb2.NotificationFolder, str]] = ...) -> None: ...
