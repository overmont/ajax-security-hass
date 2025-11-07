from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import hub_rfm_pb2 as _hub_rfm_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceFirmwareVersion(_message.Message):
    __slots__ = ("value", "hub_rfm")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    HUB_RFM_FIELD_NUMBER: _ClassVar[int]
    value: str
    hub_rfm: _hub_rfm_pb2.HubRfm
    def __init__(self, value: _Optional[str] = ..., hub_rfm: _Optional[_Union[_hub_rfm_pb2.HubRfm, str]] = ...) -> None: ...
