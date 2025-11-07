from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PhotoOnDemandDevicePermissions(_message.Message):
    __slots__ = ("device_permission",)
    class DevicePermission(_message.Message):
        __slots__ = ("device_id", "not_allowed", "allowed_always", "when_armed", "after_alarm")
        DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
        NOT_ALLOWED_FIELD_NUMBER: _ClassVar[int]
        ALLOWED_ALWAYS_FIELD_NUMBER: _ClassVar[int]
        WHEN_ARMED_FIELD_NUMBER: _ClassVar[int]
        AFTER_ALARM_FIELD_NUMBER: _ClassVar[int]
        device_id: str
        not_allowed: PhotoOnDemandDevicePermissions.NotAllowed
        allowed_always: PhotoOnDemandDevicePermissions.AllowedAlways
        when_armed: PhotoOnDemandDevicePermissions.WhenArmed
        after_alarm: PhotoOnDemandDevicePermissions.AfterAlarm
        def __init__(self, device_id: _Optional[str] = ..., not_allowed: _Optional[_Union[PhotoOnDemandDevicePermissions.NotAllowed, _Mapping]] = ..., allowed_always: _Optional[_Union[PhotoOnDemandDevicePermissions.AllowedAlways, _Mapping]] = ..., when_armed: _Optional[_Union[PhotoOnDemandDevicePermissions.WhenArmed, _Mapping]] = ..., after_alarm: _Optional[_Union[PhotoOnDemandDevicePermissions.AfterAlarm, _Mapping]] = ...) -> None: ...
    class NotAllowed(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class AllowedAlways(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class WhenArmed(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class AfterAlarm(_message.Message):
        __slots__ = ("capture_photo_available_until", "configured_time_to_capture_photo_minutes")
        CAPTURE_PHOTO_AVAILABLE_UNTIL_FIELD_NUMBER: _ClassVar[int]
        CONFIGURED_TIME_TO_CAPTURE_PHOTO_MINUTES_FIELD_NUMBER: _ClassVar[int]
        capture_photo_available_until: _timestamp_pb2.Timestamp
        configured_time_to_capture_photo_minutes: int
        def __init__(self, capture_photo_available_until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., configured_time_to_capture_photo_minutes: _Optional[int] = ...) -> None: ...
    DEVICE_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    device_permission: PhotoOnDemandDevicePermissions.DevicePermission
    def __init__(self, device_permission: _Optional[_Union[PhotoOnDemandDevicePermissions.DevicePermission, _Mapping]] = ...) -> None: ...
