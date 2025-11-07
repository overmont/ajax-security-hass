from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChangeArmingStateAction(_message.Message):
    __slots__ = ("targets", "action_type")
    class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTION_TYPE_UNSPECIFIED: _ClassVar[ChangeArmingStateAction.ActionType]
        ACTION_TYPE_DISARM: _ClassVar[ChangeArmingStateAction.ActionType]
        ACTION_TYPE_ARM: _ClassVar[ChangeArmingStateAction.ActionType]
    ACTION_TYPE_UNSPECIFIED: ChangeArmingStateAction.ActionType
    ACTION_TYPE_DISARM: ChangeArmingStateAction.ActionType
    ACTION_TYPE_ARM: ChangeArmingStateAction.ActionType
    class Target(_message.Message):
        __slots__ = ("space", "group")
        class Space(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Group(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        SPACE_FIELD_NUMBER: _ClassVar[int]
        GROUP_FIELD_NUMBER: _ClassVar[int]
        space: ChangeArmingStateAction.Target.Space
        group: ChangeArmingStateAction.Target.Group
        def __init__(self, space: _Optional[_Union[ChangeArmingStateAction.Target.Space, _Mapping]] = ..., group: _Optional[_Union[ChangeArmingStateAction.Target.Group, _Mapping]] = ...) -> None: ...
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    targets: _containers.RepeatedCompositeFieldContainer[ChangeArmingStateAction.Target]
    action_type: ChangeArmingStateAction.ActionType
    def __init__(self, targets: _Optional[_Iterable[_Union[ChangeArmingStateAction.Target, _Mapping]]] = ..., action_type: _Optional[_Union[ChangeArmingStateAction.ActionType, str]] = ...) -> None: ...
