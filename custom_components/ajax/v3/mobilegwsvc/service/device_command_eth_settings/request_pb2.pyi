from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import object_type_pb2 as _object_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceCommandEthernetSettingsRequest(_message.Message):
    __slots__ = ("hub_id", "device_id", "device_type", "dhcp", "ip", "mask", "gate", "dns")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DHCP_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    GATE_FIELD_NUMBER: _ClassVar[int]
    DNS_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    device_id: str
    device_type: _object_type_pb2.ObjectType
    dhcp: bool
    ip: str
    mask: str
    gate: str
    dns: str
    def __init__(self, hub_id: _Optional[str] = ..., device_id: _Optional[str] = ..., device_type: _Optional[_Union[_object_type_pb2.ObjectType, _Mapping]] = ..., dhcp: bool = ..., ip: _Optional[str] = ..., mask: _Optional[str] = ..., gate: _Optional[str] = ..., dns: _Optional[str] = ...) -> None: ...
