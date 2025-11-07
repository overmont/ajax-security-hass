from systems.ajax.api.mobile.v2.common.space.device import hub_device_pb2 as _hub_device_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FireZone(_message.Message):
    __slots__ = ("id", "name", "included_devices")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_DEVICES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    included_devices: _containers.RepeatedCompositeFieldContainer[_hub_device_pb2.HubDevice]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., included_devices: _Optional[_Iterable[_Union[_hub_device_pb2.HubDevice, _Mapping]]] = ...) -> None: ...
