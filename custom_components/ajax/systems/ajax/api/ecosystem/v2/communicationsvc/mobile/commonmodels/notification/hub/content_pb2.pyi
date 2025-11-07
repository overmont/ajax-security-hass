from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.event.hub import qualifier_pb2 as _qualifier_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import source_pb2 as _source_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import origin_pb2 as _origin_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HubNotificationContent(_message.Message):
    __slots__ = ("origin", "qualifier", "source")
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    QUALIFIER_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    origin: _origin_pb2.HubOrigin
    qualifier: _qualifier_pb2.HubEventQualifier
    source: _source_pb2.HubNotificationSource
    def __init__(self, origin: _Optional[_Union[_origin_pb2.HubOrigin, _Mapping]] = ..., qualifier: _Optional[_Union[_qualifier_pb2.HubEventQualifier, _Mapping]] = ..., source: _Optional[_Union[_source_pb2.HubNotificationSource, _Mapping]] = ...) -> None: ...
