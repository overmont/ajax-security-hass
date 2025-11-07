from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import source_image_info_pb2 as _source_image_info_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.space import source_type_pb2 as _source_type_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import member_type_pb2 as _member_type_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceNotificationSource(_message.Message):
    __slots__ = ("type", "id", "name", "room_id", "room_name", "member_type", "image_info")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    MEMBER_TYPE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_INFO_FIELD_NUMBER: _ClassVar[int]
    type: _source_type_pb2.SpaceNotificationSourceType
    id: str
    name: str
    room_id: str
    room_name: str
    member_type: _member_type_pb2.MemberType
    image_info: _source_image_info_pb2.SourceImageInfo
    def __init__(self, type: _Optional[_Union[_source_type_pb2.SpaceNotificationSourceType, str]] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., room_id: _Optional[str] = ..., room_name: _Optional[str] = ..., member_type: _Optional[_Union[_member_type_pb2.MemberType, str]] = ..., image_info: _Optional[_Union[_source_image_info_pb2.SourceImageInfo, _Mapping]] = ...) -> None: ...
