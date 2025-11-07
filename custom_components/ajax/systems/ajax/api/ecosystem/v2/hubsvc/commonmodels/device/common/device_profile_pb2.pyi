from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_color_pb2 as _device_color_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_label_pb2 as _device_label_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_firmware_update_part_pb2 as _device_firmware_update_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_firmware_version_pb2 as _device_firmware_version_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_appearance_pb2 as _device_appearance_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceProfile(_message.Message):
    __slots__ = ("id", "name", "device_color", "device_label", "displayed_id", "device_profile_settings", "device_appearance", "marketing_device_index", "room_id", "group_id", "device_firmware_version", "device_firmware_update", "device_location")
    class DeviceProfileSettings(_message.Message):
        __slots__ = ("name", "device_location")
        NAME_FIELD_NUMBER: _ClassVar[int]
        DEVICE_LOCATION_FIELD_NUMBER: _ClassVar[int]
        name: str
        device_location: str
        def __init__(self, name: _Optional[str] = ..., device_location: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_COLOR_FIELD_NUMBER: _ClassVar[int]
    DEVICE_LABEL_FIELD_NUMBER: _ClassVar[int]
    DISPLAYED_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_PROFILE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_APPEARANCE_FIELD_NUMBER: _ClassVar[int]
    MARKETING_DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIRMWARE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    device_color: _device_color_pb2.DeviceColor
    device_label: _device_label_pb2.DeviceLabel
    displayed_id: str
    device_profile_settings: DeviceProfile.DeviceProfileSettings
    device_appearance: _device_appearance_pb2.DeviceAppearance
    marketing_device_index: int
    room_id: str
    group_id: str
    device_firmware_version: _device_firmware_version_pb2.DeviceFirmwareVersion
    device_firmware_update: _device_firmware_update_part_pb2.DeviceFirmwareUpdatePart
    device_location: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., device_color: _Optional[_Union[_device_color_pb2.DeviceColor, str]] = ..., device_label: _Optional[_Union[_device_label_pb2.DeviceLabel, str]] = ..., displayed_id: _Optional[str] = ..., device_profile_settings: _Optional[_Union[DeviceProfile.DeviceProfileSettings, _Mapping]] = ..., device_appearance: _Optional[_Union[_device_appearance_pb2.DeviceAppearance, _Mapping]] = ..., marketing_device_index: _Optional[int] = ..., room_id: _Optional[str] = ..., group_id: _Optional[str] = ..., device_firmware_version: _Optional[_Union[_device_firmware_version_pb2.DeviceFirmwareVersion, _Mapping]] = ..., device_firmware_update: _Optional[_Union[_device_firmware_update_part_pb2.DeviceFirmwareUpdatePart, _Mapping]] = ..., device_location: _Optional[str] = ...) -> None: ...
