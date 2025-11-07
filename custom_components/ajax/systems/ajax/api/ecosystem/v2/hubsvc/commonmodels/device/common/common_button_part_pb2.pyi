from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import bypass_part_pb2 as _bypass_part_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import cms_device_index_pb2 as _cms_device_index_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import device_profile_pb2 as _device_profile_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommonButtonPart(_message.Message):
    __slots__ = ("device_profile", "cms_device_index", "bypass_part", "brightness", "associated_user", "alarm_if_pressed")
    class Brightness(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BRIGHTNESS_UNSPECIFIED: _ClassVar[CommonButtonPart.Brightness]
        BRIGHTNESS_OFF: _ClassVar[CommonButtonPart.Brightness]
        BRIGHTNESS_LOW: _ClassVar[CommonButtonPart.Brightness]
        BRIGHTNESS_HIGH: _ClassVar[CommonButtonPart.Brightness]
    BRIGHTNESS_UNSPECIFIED: CommonButtonPart.Brightness
    BRIGHTNESS_OFF: CommonButtonPart.Brightness
    BRIGHTNESS_LOW: CommonButtonPart.Brightness
    BRIGHTNESS_HIGH: CommonButtonPart.Brightness
    class AlarmIfPressed(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALARM_IF_PRESSED_UNSPECIFIED: _ClassVar[CommonButtonPart.AlarmIfPressed]
        ALARM_IF_PRESSED_DISABLED: _ClassVar[CommonButtonPart.AlarmIfPressed]
        ALARM_IF_PRESSED_ENABLED: _ClassVar[CommonButtonPart.AlarmIfPressed]
    ALARM_IF_PRESSED_UNSPECIFIED: CommonButtonPart.AlarmIfPressed
    ALARM_IF_PRESSED_DISABLED: CommonButtonPart.AlarmIfPressed
    ALARM_IF_PRESSED_ENABLED: CommonButtonPart.AlarmIfPressed
    class AssociatedUser(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    DEVICE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    CMS_DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
    BYPASS_PART_FIELD_NUMBER: _ClassVar[int]
    BRIGHTNESS_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_USER_FIELD_NUMBER: _ClassVar[int]
    ALARM_IF_PRESSED_FIELD_NUMBER: _ClassVar[int]
    device_profile: _device_profile_pb2.DeviceProfile
    cms_device_index: _cms_device_index_pb2.CmsDeviceIndex
    bypass_part: _bypass_part_pb2.BypassPart
    brightness: CommonButtonPart.Brightness
    associated_user: CommonButtonPart.AssociatedUser
    alarm_if_pressed: CommonButtonPart.AlarmIfPressed
    def __init__(self, device_profile: _Optional[_Union[_device_profile_pb2.DeviceProfile, _Mapping]] = ..., cms_device_index: _Optional[_Union[_cms_device_index_pb2.CmsDeviceIndex, _Mapping]] = ..., bypass_part: _Optional[_Union[_bypass_part_pb2.BypassPart, _Mapping]] = ..., brightness: _Optional[_Union[CommonButtonPart.Brightness, str]] = ..., associated_user: _Optional[_Union[CommonButtonPart.AssociatedUser, _Mapping]] = ..., alarm_if_pressed: _Optional[_Union[CommonButtonPart.AlarmIfPressed, str]] = ...) -> None: ...
