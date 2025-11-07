from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CloudArchiveGetMetadataFragmentsDataRequest(_message.Message):
    __slots__ = ("session_id", "tag", "entries")
    class Entry(_message.Message):
        __slots__ = ("fragment_id",)
        FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
        fragment_id: int
        def __init__(self, fragment_id: _Optional[int] = ...) -> None: ...
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    tag: str
    entries: _containers.RepeatedCompositeFieldContainer[CloudArchiveGetMetadataFragmentsDataRequest.Entry]
    def __init__(self, session_id: _Optional[str] = ..., tag: _Optional[str] = ..., entries: _Optional[_Iterable[_Union[CloudArchiveGetMetadataFragmentsDataRequest.Entry, _Mapping]]] = ...) -> None: ...
