from v3.mobilegwsvc.commonmodels.company.templates import device_settings_locator_pb2 as _device_settings_locator_pb2
from v3.mobilegwsvc.commonmodels.space.device.light import light_device_id_pb2 as _light_device_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApplyCompanyTemplateV2Request(_message.Message):
    __slots__ = ("device_settings_locator", "space_id", "device_ids")
    DEVICE_SETTINGS_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    device_settings_locator: _device_settings_locator_pb2.DeviceSettingsLocator
    space_id: str
    device_ids: _containers.RepeatedCompositeFieldContainer[_light_device_id_pb2.LightDeviceId]
    def __init__(self, device_settings_locator: _Optional[_Union[_device_settings_locator_pb2.DeviceSettingsLocator, _Mapping]] = ..., space_id: _Optional[str] = ..., device_ids: _Optional[_Iterable[_Union[_light_device_id_pb2.LightDeviceId, _Mapping]]] = ...) -> None: ...
