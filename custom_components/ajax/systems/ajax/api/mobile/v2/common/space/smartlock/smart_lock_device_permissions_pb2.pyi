from systems.ajax.api.mobile.v2.common.space.smartlock import smart_lock_permission_pb2 as _smart_lock_permission_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SmartLockPermissions(_message.Message):
    __slots__ = ("device_id", "smart_lock_permissions", "permissions")
    class PermissionState(_message.Message):
        __slots__ = ("permission", "type")
        class Type(_message.Message):
            __slots__ = ("permanent", "temporary_when_alert_received")
            class Permanent(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class TemporaryWhenAlertReceived(_message.Message):
                __slots__ = ("duration", "expired_at")
                DURATION_FIELD_NUMBER: _ClassVar[int]
                EXPIRED_AT_FIELD_NUMBER: _ClassVar[int]
                duration: _duration_pb2.Duration
                expired_at: _timestamp_pb2.Timestamp
                def __init__(self, duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., expired_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
            PERMANENT_FIELD_NUMBER: _ClassVar[int]
            TEMPORARY_WHEN_ALERT_RECEIVED_FIELD_NUMBER: _ClassVar[int]
            permanent: SmartLockPermissions.PermissionState.Type.Permanent
            temporary_when_alert_received: SmartLockPermissions.PermissionState.Type.TemporaryWhenAlertReceived
            def __init__(self, permanent: _Optional[_Union[SmartLockPermissions.PermissionState.Type.Permanent, _Mapping]] = ..., temporary_when_alert_received: _Optional[_Union[SmartLockPermissions.PermissionState.Type.TemporaryWhenAlertReceived, _Mapping]] = ...) -> None: ...
        PERMISSION_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        permission: _smart_lock_permission_pb2.SmartLockPermission
        type: SmartLockPermissions.PermissionState.Type
        def __init__(self, permission: _Optional[_Union[_smart_lock_permission_pb2.SmartLockPermission, str]] = ..., type: _Optional[_Union[SmartLockPermissions.PermissionState.Type, _Mapping]] = ...) -> None: ...
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    smart_lock_permissions: _containers.RepeatedScalarFieldContainer[_smart_lock_permission_pb2.SmartLockPermission]
    permissions: _containers.RepeatedCompositeFieldContainer[SmartLockPermissions.PermissionState]
    def __init__(self, device_id: _Optional[str] = ..., smart_lock_permissions: _Optional[_Iterable[_Union[_smart_lock_permission_pb2.SmartLockPermission, str]]] = ..., permissions: _Optional[_Iterable[_Union[SmartLockPermissions.PermissionState, _Mapping]]] = ...) -> None: ...
