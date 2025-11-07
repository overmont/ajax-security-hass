from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.space import source_pb2 as _source_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.event.space import qualifier_pb2 as _qualifier_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import source_pb2 as _source_pb2_1
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceNotificationContent(_message.Message):
    __slots__ = ("qualifier", "space_source", "hub_source")
    QUALIFIER_FIELD_NUMBER: _ClassVar[int]
    SPACE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    HUB_SOURCE_FIELD_NUMBER: _ClassVar[int]
    qualifier: _qualifier_pb2.SpaceEventQualifier
    space_source: _source_pb2.SpaceNotificationSource
    hub_source: _source_pb2_1.HubNotificationSource
    def __init__(self, qualifier: _Optional[_Union[_qualifier_pb2.SpaceEventQualifier, _Mapping]] = ..., space_source: _Optional[_Union[_source_pb2.SpaceNotificationSource, _Mapping]] = ..., hub_source: _Optional[_Union[_source_pb2_1.HubNotificationSource, _Mapping]] = ...) -> None: ...
