from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BackupConnectionContext(_message.Message):
    __slots__ = ("hub_connection_status", "parent_notification_id")
    class HubConnectionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HUB_CONNECTION_STATUS_UNSPECIFIED: _ClassVar[BackupConnectionContext.HubConnectionStatus]
        HUB_CONNECTION_STATUS_ONLINE: _ClassVar[BackupConnectionContext.HubConnectionStatus]
        HUB_CONNECTION_STATUS_OFFLINE: _ClassVar[BackupConnectionContext.HubConnectionStatus]
    HUB_CONNECTION_STATUS_UNSPECIFIED: BackupConnectionContext.HubConnectionStatus
    HUB_CONNECTION_STATUS_ONLINE: BackupConnectionContext.HubConnectionStatus
    HUB_CONNECTION_STATUS_OFFLINE: BackupConnectionContext.HubConnectionStatus
    HUB_CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    PARENT_NOTIFICATION_ID_FIELD_NUMBER: _ClassVar[int]
    hub_connection_status: BackupConnectionContext.HubConnectionStatus
    parent_notification_id: str
    def __init__(self, hub_connection_status: _Optional[_Union[BackupConnectionContext.HubConnectionStatus, str]] = ..., parent_notification_id: _Optional[str] = ...) -> None: ...
