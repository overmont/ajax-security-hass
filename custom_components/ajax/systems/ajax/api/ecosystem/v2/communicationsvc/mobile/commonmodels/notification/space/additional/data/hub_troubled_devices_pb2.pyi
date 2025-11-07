from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import troubled_devices_pb2 as _troubled_devices_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HubInSpaceTroubledDevices(_message.Message):
    __slots__ = ("troubled_devices",)
    TROUBLED_DEVICES_FIELD_NUMBER: _ClassVar[int]
    troubled_devices: _troubled_devices_pb2.TroubledDevices
    def __init__(self, troubled_devices: _Optional[_Union[_troubled_devices_pb2.TroubledDevices, _Mapping]] = ...) -> None: ...
