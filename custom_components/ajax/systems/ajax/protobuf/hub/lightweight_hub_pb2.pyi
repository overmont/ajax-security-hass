from google.protobuf import wrappers_pb2 as _wrappers_pb2
from systems.ajax.protobuf.hub.device import hub_device_pb2 as _hub_device_pb2
from systems.ajax.protobuf.hub import image_urls_pb2 as _image_urls_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LightweightHub(_message.Message):
    __slots__ = ("id", "name", "groups_enabled", "state", "state_with_groups", "image_urls", "online", "color", "subtype", "warnings_total_count", "firmware")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GROUPS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_WITH_GROUPS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URLS_FIELD_NUMBER: _ClassVar[int]
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    groups_enabled: bool
    state: _hub_device_pb2.HubDevice.State
    state_with_groups: _hub_device_pb2.HubDevice.StateWithGroups
    image_urls: _image_urls_pb2.ImageUrls
    online: _wrappers_pb2.BoolValue
    color: _hub_device_pb2.HubDevice.Color
    subtype: _hub_device_pb2.HubDevice.Subtype
    warnings_total_count: _wrappers_pb2.Int32Value
    firmware: _hub_device_pb2.HubDevice.Firmware
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., groups_enabled: bool = ..., state: _Optional[_Union[_hub_device_pb2.HubDevice.State, str]] = ..., state_with_groups: _Optional[_Union[_hub_device_pb2.HubDevice.StateWithGroups, str]] = ..., image_urls: _Optional[_Union[_image_urls_pb2.ImageUrls, _Mapping]] = ..., online: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., color: _Optional[_Union[_hub_device_pb2.HubDevice.Color, str]] = ..., subtype: _Optional[_Union[_hub_device_pb2.HubDevice.Subtype, str]] = ..., warnings_total_count: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., firmware: _Optional[_Union[_hub_device_pb2.HubDevice.Firmware, _Mapping]] = ...) -> None: ...
