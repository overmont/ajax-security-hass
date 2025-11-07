from v3.mobilegwsvc.commonmodels.hub.device.light.properties import relay_channel_pb2 as _relay_channel_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RelaySingleChannelCustomProperties(_message.Message):
    __slots__ = ("channel",)
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    channel: _relay_channel_pb2.RelayChannel
    def __init__(self, channel: _Optional[_Union[_relay_channel_pb2.RelayChannel, _Mapping]] = ...) -> None: ...
