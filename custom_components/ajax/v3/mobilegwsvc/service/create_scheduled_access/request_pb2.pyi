from v3.mobilegwsvc.commonmodels.scheduled_acesss import scheduled_access_pb2 as _scheduled_access_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateScheduledAccessRequest(_message.Message):
    __slots__ = ("scheduled_access", "hub_id")
    SCHEDULED_ACCESS_FIELD_NUMBER: _ClassVar[int]
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    scheduled_access: _scheduled_access_pb2.ScheduledAccess
    hub_id: str
    def __init__(self, scheduled_access: _Optional[_Union[_scheduled_access_pb2.ScheduledAccess, _Mapping]] = ..., hub_id: _Optional[str] = ...) -> None: ...
