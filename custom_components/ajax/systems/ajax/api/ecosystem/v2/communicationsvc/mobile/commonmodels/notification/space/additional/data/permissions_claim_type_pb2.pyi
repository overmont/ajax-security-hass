from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PermissionsClaimType(_message.Message):
    __slots__ = ("permanent", "temporary")
    class Permanent(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Temporary(_message.Message):
        __slots__ = ("duration",)
        DURATION_FIELD_NUMBER: _ClassVar[int]
        duration: _duration_pb2.Duration
        def __init__(self, duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    PERMANENT_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_FIELD_NUMBER: _ClassVar[int]
    permanent: PermissionsClaimType.Permanent
    temporary: PermissionsClaimType.Temporary
    def __init__(self, permanent: _Optional[_Union[PermissionsClaimType.Permanent, _Mapping]] = ..., temporary: _Optional[_Union[PermissionsClaimType.Temporary, _Mapping]] = ...) -> None: ...
