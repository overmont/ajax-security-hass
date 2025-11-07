from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_color_pb2 as _device_color_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_label_pb2 as _device_label_pb2
from v3.mobilegwsvc.commonmodels.space.device.light import light_device_state_pb2 as _light_device_state_pb2
from v3.mobilegwsvc.commonmodels.space.device.light import light_device_status_pb2 as _light_device_status_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_appearance_pb2 as _device_appearance_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LightDeviceProfile(_message.Message):
    __slots__ = ("id", "name", "room_id", "group_id", "device_color", "device_label", "malfunctions", "states", "statuses", "sorting_key", "device_index", "marketing_device_index", "bypassed", "interaction_disabled", "device_appearance", "device_marketing_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_COLOR_FIELD_NUMBER: _ClassVar[int]
    DEVICE_LABEL_FIELD_NUMBER: _ClassVar[int]
    MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    STATES_FIELD_NUMBER: _ClassVar[int]
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    SORTING_KEY_FIELD_NUMBER: _ClassVar[int]
    DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
    MARKETING_DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
    BYPASSED_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_DISABLED_FIELD_NUMBER: _ClassVar[int]
    DEVICE_APPEARANCE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_MARKETING_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    room_id: str
    group_id: str
    device_color: _device_color_pb2.DeviceColor
    device_label: _device_label_pb2.DeviceLabel
    malfunctions: int
    states: _containers.RepeatedScalarFieldContainer[_light_device_state_pb2.LightDeviceState]
    statuses: _containers.RepeatedCompositeFieldContainer[_light_device_status_pb2.LightDeviceStatus]
    sorting_key: str
    device_index: int
    marketing_device_index: int
    bypassed: bool
    interaction_disabled: bool
    device_appearance: _device_appearance_pb2.DeviceAppearance
    device_marketing_id: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., room_id: _Optional[str] = ..., group_id: _Optional[str] = ..., device_color: _Optional[_Union[_device_color_pb2.DeviceColor, str]] = ..., device_label: _Optional[_Union[_device_label_pb2.DeviceLabel, str]] = ..., malfunctions: _Optional[int] = ..., states: _Optional[_Iterable[_Union[_light_device_state_pb2.LightDeviceState, str]]] = ..., statuses: _Optional[_Iterable[_Union[_light_device_status_pb2.LightDeviceStatus, _Mapping]]] = ..., sorting_key: _Optional[str] = ..., device_index: _Optional[int] = ..., marketing_device_index: _Optional[int] = ..., bypassed: bool = ..., interaction_disabled: bool = ..., device_appearance: _Optional[_Union[_device_appearance_pb2.DeviceAppearance, _Mapping]] = ..., device_marketing_id: _Optional[str] = ...) -> None: ...
