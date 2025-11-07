from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterInfo(_message.Message):
    __slots__ = ("cluster_id", "ping_interval_seconds")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    PING_INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    ping_interval_seconds: int
    def __init__(self, cluster_id: _Optional[str] = ..., ping_interval_seconds: _Optional[int] = ...) -> None: ...
