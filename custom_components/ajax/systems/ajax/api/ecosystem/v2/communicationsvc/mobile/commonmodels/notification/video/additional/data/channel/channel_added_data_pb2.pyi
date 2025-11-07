from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChannelAddedData(_message.Message):
    __slots__ = ("channel_id", "channel_name")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    channel_name: str
    def __init__(self, channel_id: _Optional[str] = ..., channel_name: _Optional[str] = ...) -> None: ...
