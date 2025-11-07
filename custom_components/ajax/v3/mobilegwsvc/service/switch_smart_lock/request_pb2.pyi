from systems.ajax.logging.proto import log_marker_pb2 as _log_marker_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SwitchSmartLockRequest(_message.Message):
    __slots__ = ("space_id", "smart_lock_id", "action")
    class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTION_UNSPECIFIED: _ClassVar[SwitchSmartLockRequest.Action]
        ACTION_UNLOCK: _ClassVar[SwitchSmartLockRequest.Action]
        ACTION_LOCK: _ClassVar[SwitchSmartLockRequest.Action]
        ACTION_UNLATCH: _ClassVar[SwitchSmartLockRequest.Action]
    ACTION_UNSPECIFIED: SwitchSmartLockRequest.Action
    ACTION_UNLOCK: SwitchSmartLockRequest.Action
    ACTION_LOCK: SwitchSmartLockRequest.Action
    ACTION_UNLATCH: SwitchSmartLockRequest.Action
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    smart_lock_id: str
    action: SwitchSmartLockRequest.Action
    def __init__(self, space_id: _Optional[str] = ..., smart_lock_id: _Optional[str] = ..., action: _Optional[_Union[SwitchSmartLockRequest.Action, str]] = ...) -> None: ...
