from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HubCommandEthernetSettingsRequest(_message.Message):
    __slots__ = ("hub_id", "dhcp", "ip", "mask", "gate", "dns")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DHCP_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    GATE_FIELD_NUMBER: _ClassVar[int]
    DNS_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    dhcp: bool
    ip: str
    mask: str
    gate: str
    dns: str
    def __init__(self, hub_id: _Optional[str] = ..., dhcp: bool = ..., ip: _Optional[str] = ..., mask: _Optional[str] = ..., gate: _Optional[str] = ..., dns: _Optional[str] = ...) -> None: ...
