from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SmartLockType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SMART_LOCK_TYPE_UNSPECIFIED: _ClassVar[SmartLockType]
    SMART_LOCK_TYPE_ASSA_ABLOY: _ClassVar[SmartLockType]
    SMART_LOCK_TYPE_ASSA_ABLOY_NA: _ClassVar[SmartLockType]
SMART_LOCK_TYPE_UNSPECIFIED: SmartLockType
SMART_LOCK_TYPE_ASSA_ABLOY: SmartLockType
SMART_LOCK_TYPE_ASSA_ABLOY_NA: SmartLockType

class SmartLock(_message.Message):
    __slots__ = ("id", "external_id", "type", "owner_space_member_id", "name", "status", "feature", "serial_number")
    ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    OWNER_SPACE_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FEATURE_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    id: str
    external_id: str
    type: SmartLockType
    owner_space_member_id: str
    name: str
    status: SmartLockStatus
    feature: SmartLockFeature
    serial_number: str
    def __init__(self, id: _Optional[str] = ..., external_id: _Optional[str] = ..., type: _Optional[_Union[SmartLockType, str]] = ..., owner_space_member_id: _Optional[str] = ..., name: _Optional[str] = ..., status: _Optional[_Union[SmartLockStatus, _Mapping]] = ..., feature: _Optional[_Union[SmartLockFeature, _Mapping]] = ..., serial_number: _Optional[str] = ...) -> None: ...

class ExternalSmartLock(_message.Message):
    __slots__ = ("external_id", "type", "name", "status", "feature", "serial_number")
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FEATURE_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    external_id: str
    type: SmartLockType
    name: str
    status: SmartLockStatus
    feature: SmartLockFeature
    serial_number: str
    def __init__(self, external_id: _Optional[str] = ..., type: _Optional[_Union[SmartLockType, str]] = ..., name: _Optional[str] = ..., status: _Optional[_Union[SmartLockStatus, _Mapping]] = ..., feature: _Optional[_Union[SmartLockFeature, _Mapping]] = ..., serial_number: _Optional[str] = ...) -> None: ...

class SmartLockStatus(_message.Message):
    __slots__ = ("lock_status", "connection_status", "battery_status", "authorization_status")
    class LockStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOCK_STATUS_UNSPECIFIED: _ClassVar[SmartLockStatus.LockStatus]
        LOCK_STATUS_UNLOCKED: _ClassVar[SmartLockStatus.LockStatus]
        LOCK_STATUS_LOCKED: _ClassVar[SmartLockStatus.LockStatus]
        LOCK_STATUS_UNLATCHED: _ClassVar[SmartLockStatus.LockStatus]
    LOCK_STATUS_UNSPECIFIED: SmartLockStatus.LockStatus
    LOCK_STATUS_UNLOCKED: SmartLockStatus.LockStatus
    LOCK_STATUS_LOCKED: SmartLockStatus.LockStatus
    LOCK_STATUS_UNLATCHED: SmartLockStatus.LockStatus
    class ConnectionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONNECTION_STATUS_UNSPECIFIED: _ClassVar[SmartLockStatus.ConnectionStatus]
        CONNECTION_STATUS_OFFLINE: _ClassVar[SmartLockStatus.ConnectionStatus]
        CONNECTION_STATUS_ONLINE: _ClassVar[SmartLockStatus.ConnectionStatus]
    CONNECTION_STATUS_UNSPECIFIED: SmartLockStatus.ConnectionStatus
    CONNECTION_STATUS_OFFLINE: SmartLockStatus.ConnectionStatus
    CONNECTION_STATUS_ONLINE: SmartLockStatus.ConnectionStatus
    class AuthorizationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AUTHORIZATION_STATUS_UNSPECIFIED: _ClassVar[SmartLockStatus.AuthorizationStatus]
        AUTHORIZATION_STATUS_UNAUTHORIZED: _ClassVar[SmartLockStatus.AuthorizationStatus]
        AUTHORIZATION_STATUS_AUTHORIZED: _ClassVar[SmartLockStatus.AuthorizationStatus]
    AUTHORIZATION_STATUS_UNSPECIFIED: SmartLockStatus.AuthorizationStatus
    AUTHORIZATION_STATUS_UNAUTHORIZED: SmartLockStatus.AuthorizationStatus
    AUTHORIZATION_STATUS_AUTHORIZED: SmartLockStatus.AuthorizationStatus
    class BatteryStatus(_message.Message):
        __slots__ = ("level", "warning")
        class Warning(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            WARNING_UNSPECIFIED: _ClassVar[SmartLockStatus.BatteryStatus.Warning]
            WARNING_NONE: _ClassVar[SmartLockStatus.BatteryStatus.Warning]
            WARNING_LOW_CHARGE: _ClassVar[SmartLockStatus.BatteryStatus.Warning]
        WARNING_UNSPECIFIED: SmartLockStatus.BatteryStatus.Warning
        WARNING_NONE: SmartLockStatus.BatteryStatus.Warning
        WARNING_LOW_CHARGE: SmartLockStatus.BatteryStatus.Warning
        LEVEL_FIELD_NUMBER: _ClassVar[int]
        WARNING_FIELD_NUMBER: _ClassVar[int]
        level: int
        warning: SmartLockStatus.BatteryStatus.Warning
        def __init__(self, level: _Optional[int] = ..., warning: _Optional[_Union[SmartLockStatus.BatteryStatus.Warning, str]] = ...) -> None: ...
    LOCK_STATUS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    BATTERY_STATUS_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    lock_status: SmartLockStatus.LockStatus
    connection_status: SmartLockStatus.ConnectionStatus
    battery_status: SmartLockStatus.BatteryStatus
    authorization_status: SmartLockStatus.AuthorizationStatus
    def __init__(self, lock_status: _Optional[_Union[SmartLockStatus.LockStatus, str]] = ..., connection_status: _Optional[_Union[SmartLockStatus.ConnectionStatus, str]] = ..., battery_status: _Optional[_Union[SmartLockStatus.BatteryStatus, _Mapping]] = ..., authorization_status: _Optional[_Union[SmartLockStatus.AuthorizationStatus, str]] = ...) -> None: ...

class SmartLockFeature(_message.Message):
    __slots__ = ("embedded_doorbell", "bridge", "latch_control")
    class LatchControl(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class EmbeddedDoorbell(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Bridge(_message.Message):
        __slots__ = ("connection_status",)
        class ConnectionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CONNECTION_STATUS_UNSPECIFIED: _ClassVar[SmartLockFeature.Bridge.ConnectionStatus]
            CONNECTION_STATUS_OFFLINE: _ClassVar[SmartLockFeature.Bridge.ConnectionStatus]
            CONNECTION_STATUS_ONLINE: _ClassVar[SmartLockFeature.Bridge.ConnectionStatus]
        CONNECTION_STATUS_UNSPECIFIED: SmartLockFeature.Bridge.ConnectionStatus
        CONNECTION_STATUS_OFFLINE: SmartLockFeature.Bridge.ConnectionStatus
        CONNECTION_STATUS_ONLINE: SmartLockFeature.Bridge.ConnectionStatus
        CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
        connection_status: SmartLockFeature.Bridge.ConnectionStatus
        def __init__(self, connection_status: _Optional[_Union[SmartLockFeature.Bridge.ConnectionStatus, str]] = ...) -> None: ...
    EMBEDDED_DOORBELL_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_FIELD_NUMBER: _ClassVar[int]
    LATCH_CONTROL_FIELD_NUMBER: _ClassVar[int]
    embedded_doorbell: SmartLockFeature.EmbeddedDoorbell
    bridge: SmartLockFeature.Bridge
    latch_control: SmartLockFeature.LatchControl
    def __init__(self, embedded_doorbell: _Optional[_Union[SmartLockFeature.EmbeddedDoorbell, _Mapping]] = ..., bridge: _Optional[_Union[SmartLockFeature.Bridge, _Mapping]] = ..., latch_control: _Optional[_Union[SmartLockFeature.LatchControl, _Mapping]] = ...) -> None: ...

class SmartLockUpdate(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class SmartLockAvailableToAdd(_message.Message):
    __slots__ = ("smart_lock", "addition_status")
    class AdditionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ADDITION_STATUS_UNSPECIFIED: _ClassVar[SmartLockAvailableToAdd.AdditionStatus]
        ADDITION_STATUS_ALREADY_ADDED: _ClassVar[SmartLockAvailableToAdd.AdditionStatus]
        ADDITION_STATUS_AVAILABLE_TO_ADD: _ClassVar[SmartLockAvailableToAdd.AdditionStatus]
    ADDITION_STATUS_UNSPECIFIED: SmartLockAvailableToAdd.AdditionStatus
    ADDITION_STATUS_ALREADY_ADDED: SmartLockAvailableToAdd.AdditionStatus
    ADDITION_STATUS_AVAILABLE_TO_ADD: SmartLockAvailableToAdd.AdditionStatus
    SMART_LOCK_FIELD_NUMBER: _ClassVar[int]
    ADDITION_STATUS_FIELD_NUMBER: _ClassVar[int]
    smart_lock: ExternalSmartLock
    addition_status: SmartLockAvailableToAdd.AdditionStatus
    def __init__(self, smart_lock: _Optional[_Union[ExternalSmartLock, _Mapping]] = ..., addition_status: _Optional[_Union[SmartLockAvailableToAdd.AdditionStatus, str]] = ...) -> None: ...
