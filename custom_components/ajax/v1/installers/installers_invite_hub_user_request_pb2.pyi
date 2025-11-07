from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class InstallersInviteHubUserRequest(_message.Message):
    __slots__ = ("hub_user_id", "hub_hex_id")
    HUB_USER_ID_FIELD_NUMBER: _ClassVar[int]
    HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    hub_user_id: str
    hub_hex_id: str
    def __init__(self, hub_user_id: _Optional[str] = ..., hub_hex_id: _Optional[str] = ...) -> None: ...
