from v3.mobilegwsvc.commonmodels.space.device.light import light_device_profile_pb2 as _light_device_profile_pb2
from v3.mobilegwsvc.commonmodels.device.light.properties import smart_lock_control_pb2 as _smart_lock_control_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LightSmartLock(_message.Message):
    __slots__ = ("profile", "spread_properties")
    class SmartLockSpreadProperty(_message.Message):
        __slots__ = ("smart_lock_control",)
        SMART_LOCK_CONTROL_FIELD_NUMBER: _ClassVar[int]
        smart_lock_control: _smart_lock_control_pb2.SmartLockControl
        def __init__(self, smart_lock_control: _Optional[_Union[_smart_lock_control_pb2.SmartLockControl, _Mapping]] = ...) -> None: ...
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    SPREAD_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    profile: _light_device_profile_pb2.LightDeviceProfile
    spread_properties: _containers.RepeatedCompositeFieldContainer[LightSmartLock.SmartLockSpreadProperty]
    def __init__(self, profile: _Optional[_Union[_light_device_profile_pb2.LightDeviceProfile, _Mapping]] = ..., spread_properties: _Optional[_Iterable[_Union[LightSmartLock.SmartLockSpreadProperty, _Mapping]]] = ...) -> None: ...
