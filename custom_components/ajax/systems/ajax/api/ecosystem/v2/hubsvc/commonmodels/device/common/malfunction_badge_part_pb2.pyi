from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MalfunctionBadgePart(_message.Message):
    __slots__ = ("malfunction_badge",)
    class MalfunctionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MALFUNCTION_TYPE_UNSPECIFIED: _ClassVar[MalfunctionBadgePart.MalfunctionType]
        MALFUNCTION_TYPE_JEWELLER_CONNECTION_LOSS: _ClassVar[MalfunctionBadgePart.MalfunctionType]
    MALFUNCTION_TYPE_UNSPECIFIED: MalfunctionBadgePart.MalfunctionType
    MALFUNCTION_TYPE_JEWELLER_CONNECTION_LOSS: MalfunctionBadgePart.MalfunctionType
    class IsEnabled(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IS_ENABLED_UNSPECIFIED: _ClassVar[MalfunctionBadgePart.IsEnabled]
        IS_ENABLED_DISABLED: _ClassVar[MalfunctionBadgePart.IsEnabled]
        IS_ENABLED_ENABLED: _ClassVar[MalfunctionBadgePart.IsEnabled]
    IS_ENABLED_UNSPECIFIED: MalfunctionBadgePart.IsEnabled
    IS_ENABLED_DISABLED: MalfunctionBadgePart.IsEnabled
    IS_ENABLED_ENABLED: MalfunctionBadgePart.IsEnabled
    class MalfunctionBadgePartSettings(_message.Message):
        __slots__ = ("malfunction_badge",)
        MALFUNCTION_BADGE_FIELD_NUMBER: _ClassVar[int]
        malfunction_badge: _containers.RepeatedCompositeFieldContainer[MalfunctionBadgePart.MalfunctionBadge]
        def __init__(self, malfunction_badge: _Optional[_Iterable[_Union[MalfunctionBadgePart.MalfunctionBadge, _Mapping]]] = ...) -> None: ...
    class MalfunctionBadge(_message.Message):
        __slots__ = ("malfunction_type", "is_enabled")
        MALFUNCTION_TYPE_FIELD_NUMBER: _ClassVar[int]
        IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        malfunction_type: MalfunctionBadgePart.MalfunctionType
        is_enabled: MalfunctionBadgePart.IsEnabled
        def __init__(self, malfunction_type: _Optional[_Union[MalfunctionBadgePart.MalfunctionType, str]] = ..., is_enabled: _Optional[_Union[MalfunctionBadgePart.IsEnabled, str]] = ...) -> None: ...
    MALFUNCTION_BADGE_FIELD_NUMBER: _ClassVar[int]
    malfunction_badge: _containers.RepeatedCompositeFieldContainer[MalfunctionBadgePart.MalfunctionBadge]
    def __init__(self, malfunction_badge: _Optional[_Iterable[_Union[MalfunctionBadgePart.MalfunctionBadge, _Mapping]]] = ...) -> None: ...
