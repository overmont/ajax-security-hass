from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StreamHubDeviceRequest(_message.Message):
    __slots__ = ("hub_id", "hub_device_id")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    HUB_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    hub_device_id: str
    def __init__(self, hub_id: _Optional[str] = ..., hub_device_id: _Optional[str] = ...) -> None: ...
