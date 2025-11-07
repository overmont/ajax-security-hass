from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VideoEdgeChannelMediaDataInfo(_message.Message):
    __slots__ = ("channel_id", "allowed_member_ids")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    allowed_member_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, channel_id: _Optional[str] = ..., allowed_member_ids: _Optional[_Iterable[str]] = ...) -> None: ...
