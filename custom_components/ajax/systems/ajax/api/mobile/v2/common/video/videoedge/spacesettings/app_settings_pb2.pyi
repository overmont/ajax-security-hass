from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HideShortDisconnectsOnTimeline(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HIDE_SHORT_DISCONNECTS_ON_TIMELINE_UNSPECIFIED: _ClassVar[HideShortDisconnectsOnTimeline]
    HIDE_SHORT_DISCONNECTS_ON_TIMELINE_ENABLED: _ClassVar[HideShortDisconnectsOnTimeline]
    HIDE_SHORT_DISCONNECTS_ON_TIMELINE_DISABLED: _ClassVar[HideShortDisconnectsOnTimeline]
HIDE_SHORT_DISCONNECTS_ON_TIMELINE_UNSPECIFIED: HideShortDisconnectsOnTimeline
HIDE_SHORT_DISCONNECTS_ON_TIMELINE_ENABLED: HideShortDisconnectsOnTimeline
HIDE_SHORT_DISCONNECTS_ON_TIMELINE_DISABLED: HideShortDisconnectsOnTimeline

class AppSettings(_message.Message):
    __slots__ = ("hide_short_disconnects_on_timeline",)
    HIDE_SHORT_DISCONNECTS_ON_TIMELINE_FIELD_NUMBER: _ClassVar[int]
    hide_short_disconnects_on_timeline: HideShortDisconnectsOnTimeline
    def __init__(self, hide_short_disconnects_on_timeline: _Optional[_Union[HideShortDisconnectsOnTimeline, str]] = ...) -> None: ...
