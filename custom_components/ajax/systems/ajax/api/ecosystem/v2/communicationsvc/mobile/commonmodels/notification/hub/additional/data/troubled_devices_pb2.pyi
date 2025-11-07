from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.event.hub import qualifier_pb2 as _qualifier_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import device_color_pb2 as _device_color_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import device_label_pb2 as _device_label_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import hub_box_type_pb2 as _hub_box_type_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import hub_type_pb2 as _hub_type_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import source_pb2 as _source_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import source_image_info_pb2 as _source_image_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TroubledDevices(_message.Message):
    __slots__ = ("troubled_devices", "hub_info", "troubled_followed_groups")
    class TroubledDevice(_message.Message):
        __slots__ = ("device", "troubled_alarm")
        DEVICE_FIELD_NUMBER: _ClassVar[int]
        TROUBLED_ALARM_FIELD_NUMBER: _ClassVar[int]
        device: _source_pb2.HubNotificationSource
        troubled_alarm: _qualifier_pb2.HubEventQualifier
        def __init__(self, device: _Optional[_Union[_source_pb2.HubNotificationSource, _Mapping]] = ..., troubled_alarm: _Optional[_Union[_qualifier_pb2.HubEventQualifier, _Mapping]] = ...) -> None: ...
    class TroubledFollowedGroup(_message.Message):
        __slots__ = ("id", "name", "image_info")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        IMAGE_INFO_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        image_info: _source_image_info_pb2.SourceImageInfo
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., image_info: _Optional[_Union[_source_image_info_pb2.SourceImageInfo, _Mapping]] = ...) -> None: ...
    class HubInfo(_message.Message):
        __slots__ = ("hex_id", "name", "color", "type", "box_type", "label")
        HEX_ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        COLOR_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        BOX_TYPE_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        hex_id: str
        name: str
        color: _device_color_pb2.DeviceColor
        type: _hub_type_pb2.HubType
        box_type: _hub_box_type_pb2.HubBoxType
        label: _device_label_pb2.DeviceLabel
        def __init__(self, hex_id: _Optional[str] = ..., name: _Optional[str] = ..., color: _Optional[_Union[_device_color_pb2.DeviceColor, str]] = ..., type: _Optional[_Union[_hub_type_pb2.HubType, str]] = ..., box_type: _Optional[_Union[_hub_box_type_pb2.HubBoxType, str]] = ..., label: _Optional[_Union[_device_label_pb2.DeviceLabel, str]] = ...) -> None: ...
    TROUBLED_DEVICES_FIELD_NUMBER: _ClassVar[int]
    HUB_INFO_FIELD_NUMBER: _ClassVar[int]
    TROUBLED_FOLLOWED_GROUPS_FIELD_NUMBER: _ClassVar[int]
    troubled_devices: _containers.RepeatedCompositeFieldContainer[TroubledDevices.TroubledDevice]
    hub_info: TroubledDevices.HubInfo
    troubled_followed_groups: _containers.RepeatedCompositeFieldContainer[TroubledDevices.TroubledFollowedGroup]
    def __init__(self, troubled_devices: _Optional[_Iterable[_Union[TroubledDevices.TroubledDevice, _Mapping]]] = ..., hub_info: _Optional[_Union[TroubledDevices.HubInfo, _Mapping]] = ..., troubled_followed_groups: _Optional[_Iterable[_Union[TroubledDevices.TroubledFollowedGroup, _Mapping]]] = ...) -> None: ...
