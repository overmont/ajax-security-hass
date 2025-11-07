from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommonDeviceNotificationsPart(_message.Message):
    __slots__ = ("device_notifications",)
    class NotificationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOTIFICATION_TYPE_UNSPECIFIED: _ClassVar[CommonDeviceNotificationsPart.NotificationType]
        NOTIFICATION_TYPE_INCORRECT_DEVICE_INSTALLATION: _ClassVar[CommonDeviceNotificationsPart.NotificationType]
        NOTIFICATION_TYPE_BATTERY_FAILED_CHARGE: _ClassVar[CommonDeviceNotificationsPart.NotificationType]
        NOTIFICATION_TYPE_BATTERY_FAILED_LOAD_TEST: _ClassVar[CommonDeviceNotificationsPart.NotificationType]
    NOTIFICATION_TYPE_UNSPECIFIED: CommonDeviceNotificationsPart.NotificationType
    NOTIFICATION_TYPE_INCORRECT_DEVICE_INSTALLATION: CommonDeviceNotificationsPart.NotificationType
    NOTIFICATION_TYPE_BATTERY_FAILED_CHARGE: CommonDeviceNotificationsPart.NotificationType
    NOTIFICATION_TYPE_BATTERY_FAILED_LOAD_TEST: CommonDeviceNotificationsPart.NotificationType
    class IsEnabled(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IS_ENABLED_UNSPECIFIED: _ClassVar[CommonDeviceNotificationsPart.IsEnabled]
        IS_ENABLED_DISABLED: _ClassVar[CommonDeviceNotificationsPart.IsEnabled]
        IS_ENABLED_ENABLED: _ClassVar[CommonDeviceNotificationsPart.IsEnabled]
    IS_ENABLED_UNSPECIFIED: CommonDeviceNotificationsPart.IsEnabled
    IS_ENABLED_DISABLED: CommonDeviceNotificationsPart.IsEnabled
    IS_ENABLED_ENABLED: CommonDeviceNotificationsPart.IsEnabled
    class DeviceNotificationsPartSettings(_message.Message):
        __slots__ = ("device_notifications",)
        DEVICE_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
        device_notifications: _containers.RepeatedCompositeFieldContainer[CommonDeviceNotificationsPart.Notification]
        def __init__(self, device_notifications: _Optional[_Iterable[_Union[CommonDeviceNotificationsPart.Notification, _Mapping]]] = ...) -> None: ...
    class Notification(_message.Message):
        __slots__ = ("notification_type", "is_enabled")
        NOTIFICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
        IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        notification_type: CommonDeviceNotificationsPart.NotificationType
        is_enabled: CommonDeviceNotificationsPart.IsEnabled
        def __init__(self, notification_type: _Optional[_Union[CommonDeviceNotificationsPart.NotificationType, str]] = ..., is_enabled: _Optional[_Union[CommonDeviceNotificationsPart.IsEnabled, str]] = ...) -> None: ...
    DEVICE_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    device_notifications: _containers.RepeatedCompositeFieldContainer[CommonDeviceNotificationsPart.Notification]
    def __init__(self, device_notifications: _Optional[_Iterable[_Union[CommonDeviceNotificationsPart.Notification, _Mapping]]] = ...) -> None: ...
