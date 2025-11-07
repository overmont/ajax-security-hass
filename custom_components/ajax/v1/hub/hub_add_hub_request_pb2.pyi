from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HubAddHubRequest(_message.Message):
    __slots__ = ("hub_name", "hub_qr_code")
    HUB_NAME_FIELD_NUMBER: _ClassVar[int]
    HUB_QR_CODE_FIELD_NUMBER: _ClassVar[int]
    hub_name: str
    hub_qr_code: str
    def __init__(self, hub_name: _Optional[str] = ..., hub_qr_code: _Optional[str] = ...) -> None: ...
