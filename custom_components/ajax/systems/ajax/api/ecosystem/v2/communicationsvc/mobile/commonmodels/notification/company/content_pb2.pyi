from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.company import source_pb2 as _source_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.event.company import qualifier_pb2 as _qualifier_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompanyNotificationContent(_message.Message):
    __slots__ = ("qualifier", "source")
    QUALIFIER_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    qualifier: _qualifier_pb2.CompanyEventQualifier
    source: _source_pb2.CompanyNotificationSource
    def __init__(self, qualifier: _Optional[_Union[_qualifier_pb2.CompanyEventQualifier, _Mapping]] = ..., source: _Optional[_Union[_source_pb2.CompanyNotificationSource, _Mapping]] = ...) -> None: ...
