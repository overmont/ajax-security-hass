from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrivacyAccessList(_message.Message):
    __slots__ = ("hub_id", "privacy_access")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_ACCESS_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    privacy_access: _containers.RepeatedCompositeFieldContainer[PrivacyAccess]
    def __init__(self, hub_id: _Optional[str] = ..., privacy_access: _Optional[_Iterable[_Union[PrivacyAccess, _Mapping]]] = ...) -> None: ...

class PrivacyAccess(_message.Message):
    __slots__ = ("userHexId", "target_object_type", "target_device_hex_id", "pod_access_mode", "permission_active")
    class PodAccessMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_POD_ACCESS_MODE_INFO: _ClassVar[PrivacyAccess.PodAccessMode]
        ALWAYS: _ClassVar[PrivacyAccess.PodAccessMode]
        ARMED: _ClassVar[PrivacyAccess.PodAccessMode]
    NO_POD_ACCESS_MODE_INFO: PrivacyAccess.PodAccessMode
    ALWAYS: PrivacyAccess.PodAccessMode
    ARMED: PrivacyAccess.PodAccessMode
    class TargetObjectType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_TARGET_OBJECT_TYPE_INFO: _ClassVar[PrivacyAccess.TargetObjectType]
        MOTION_CAM: _ClassVar[PrivacyAccess.TargetObjectType]
        MOTION_CAM_OUTDOOR: _ClassVar[PrivacyAccess.TargetObjectType]
        STREAMING_CAMERA: _ClassVar[PrivacyAccess.TargetObjectType]
    NO_TARGET_OBJECT_TYPE_INFO: PrivacyAccess.TargetObjectType
    MOTION_CAM: PrivacyAccess.TargetObjectType
    MOTION_CAM_OUTDOOR: PrivacyAccess.TargetObjectType
    STREAMING_CAMERA: PrivacyAccess.TargetObjectType
    USERHEXID_FIELD_NUMBER: _ClassVar[int]
    TARGET_OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_DEVICE_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    POD_ACCESS_MODE_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    userHexId: str
    target_object_type: PrivacyAccess.TargetObjectType
    target_device_hex_id: str
    pod_access_mode: PrivacyAccess.PodAccessMode
    permission_active: bool
    def __init__(self, userHexId: _Optional[str] = ..., target_object_type: _Optional[_Union[PrivacyAccess.TargetObjectType, str]] = ..., target_device_hex_id: _Optional[str] = ..., pod_access_mode: _Optional[_Union[PrivacyAccess.PodAccessMode, str]] = ..., permission_active: bool = ...) -> None: ...
