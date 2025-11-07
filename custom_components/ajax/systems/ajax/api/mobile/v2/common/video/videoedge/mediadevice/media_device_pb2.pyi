from systems.ajax.api.mobile.v2.common.video.videoedge.mediadevice import media_device_capabilities_pb2 as _media_device_capabilities_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.mediadevice import media_device_settings_pb2 as _media_device_settings_pb2
from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MediaDeviceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DS_NONE: _ClassVar[MediaDeviceState]
    CONNECTING: _ClassVar[MediaDeviceState]
    CONNECTED: _ClassVar[MediaDeviceState]
    CONNECTION_FAILED: _ClassVar[MediaDeviceState]
    INVALID_LOGIN: _ClassVar[MediaDeviceState]
    BAD_MODEL: _ClassVar[MediaDeviceState]
    SETTING_UP: _ClassVar[MediaDeviceState]
    RESOLVE_FAILED: _ClassVar[MediaDeviceState]
    FINGERPRINT_MISMATCH: _ClassVar[MediaDeviceState]

class MediaDeviceProtocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    P_NONE: _ClassVar[MediaDeviceProtocol]
    P_ONVIF: _ClassVar[MediaDeviceProtocol]
DS_NONE: MediaDeviceState
CONNECTING: MediaDeviceState
CONNECTED: MediaDeviceState
CONNECTION_FAILED: MediaDeviceState
INVALID_LOGIN: MediaDeviceState
BAD_MODEL: MediaDeviceState
SETTING_UP: MediaDeviceState
RESOLVE_FAILED: MediaDeviceState
FINGERPRINT_MISMATCH: MediaDeviceState
P_NONE: MediaDeviceProtocol
P_ONVIF: MediaDeviceProtocol

class MediaDevice(_message.Message):
    __slots__ = ("guid", "family", "model", "enabled", "info", "state", "connection_settings", "capabilities", "device_settings", "permanent")
    GUID_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    DEVICE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    PERMANENT_FIELD_NUMBER: _ClassVar[int]
    guid: str
    family: str
    model: str
    enabled: bool
    info: MediaDeviceInfo
    state: _containers.RepeatedScalarFieldContainer[MediaDeviceState]
    connection_settings: _media_device_settings_pb2.ConnectionSettings
    capabilities: _media_device_capabilities_pb2.MediaDeviceCapabilities
    device_settings: _media_device_settings_pb2.MediaDeviceSettings
    permanent: bool
    def __init__(self, guid: _Optional[str] = ..., family: _Optional[str] = ..., model: _Optional[str] = ..., enabled: bool = ..., info: _Optional[_Union[MediaDeviceInfo, _Mapping]] = ..., state: _Optional[_Iterable[_Union[MediaDeviceState, str]]] = ..., connection_settings: _Optional[_Union[_media_device_settings_pb2.ConnectionSettings, _Mapping]] = ..., capabilities: _Optional[_Union[_media_device_capabilities_pb2.MediaDeviceCapabilities, _Mapping]] = ..., device_settings: _Optional[_Union[_media_device_settings_pb2.MediaDeviceSettings, _Mapping]] = ..., permanent: bool = ...) -> None: ...

class MediaDeviceInfo(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
