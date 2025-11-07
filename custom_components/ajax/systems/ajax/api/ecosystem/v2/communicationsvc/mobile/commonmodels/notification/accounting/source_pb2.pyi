from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import source_image_info_pb2 as _source_image_info_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.accounting import source_type_pb2 as _source_type_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.accounting import source_info_pb2 as _source_info_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccountingNotificationSource(_message.Message):
    __slots__ = ("type", "id", "name", "source_info", "image_info")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
    IMAGE_INFO_FIELD_NUMBER: _ClassVar[int]
    type: _source_type_pb2.AccountingNotificationSourceType
    id: str
    name: str
    source_info: _source_info_pb2.AccountingNotificationSourceInfo
    image_info: _source_image_info_pb2.SourceImageInfo
    def __init__(self, type: _Optional[_Union[_source_type_pb2.AccountingNotificationSourceType, str]] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., source_info: _Optional[_Union[_source_info_pb2.AccountingNotificationSourceInfo, _Mapping]] = ..., image_info: _Optional[_Union[_source_image_info_pb2.SourceImageInfo, _Mapping]] = ...) -> None: ...
