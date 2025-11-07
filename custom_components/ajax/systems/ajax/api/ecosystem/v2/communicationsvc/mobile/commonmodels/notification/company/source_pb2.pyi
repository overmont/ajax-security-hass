from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import source_image_info_pb2 as _source_image_info_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.company import source_type_pb2 as _source_type_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import member_type_pb2 as _member_type_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompanyNotificationSource(_message.Message):
    __slots__ = ("type", "id", "name", "image_info", "member_type")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_INFO_FIELD_NUMBER: _ClassVar[int]
    MEMBER_TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _source_type_pb2.CompanyNotificationSourceType
    id: str
    name: str
    image_info: _source_image_info_pb2.SourceImageInfo
    member_type: _member_type_pb2.MemberType
    def __init__(self, type: _Optional[_Union[_source_type_pb2.CompanyNotificationSourceType, str]] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., image_info: _Optional[_Union[_source_image_info_pb2.SourceImageInfo, _Mapping]] = ..., member_type: _Optional[_Union[_member_type_pb2.MemberType, str]] = ...) -> None: ...
