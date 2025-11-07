from systems.ajax.api.mobile.v2.common.space.smartlock import smart_lock_space_settings_pb2 as _smart_lock_space_settings_pb2
from systems.ajax.api.mobile.v2.common.space.smartlock import smart_lock_pb2 as _smart_lock_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SmartLockInSpace(_message.Message):
    __slots__ = ("id", "details", "space_settings")
    ID_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    SPACE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    details: _smart_lock_pb2.SmartLock
    space_settings: _smart_lock_space_settings_pb2.SmartLockSpaceSettings
    def __init__(self, id: _Optional[str] = ..., details: _Optional[_Union[_smart_lock_pb2.SmartLock, _Mapping]] = ..., space_settings: _Optional[_Union[_smart_lock_space_settings_pb2.SmartLockSpaceSettings, _Mapping]] = ...) -> None: ...
