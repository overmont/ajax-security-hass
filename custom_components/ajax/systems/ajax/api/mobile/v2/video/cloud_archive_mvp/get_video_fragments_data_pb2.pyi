from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CloudArchiveGetVideoFragmentsDataRequest(_message.Message):
    __slots__ = ("session_id", "tag", "entries")
    class Entry(_message.Message):
        __slots__ = ("fragment_id", "fragment_part")
        FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
        FRAGMENT_PART_FIELD_NUMBER: _ClassVar[int]
        fragment_id: int
        fragment_part: CloudArchiveGetVideoFragmentsDataRequest.FragmentPart
        def __init__(self, fragment_id: _Optional[int] = ..., fragment_part: _Optional[_Union[CloudArchiveGetVideoFragmentsDataRequest.FragmentPart, _Mapping]] = ...) -> None: ...
    class FragmentPart(_message.Message):
        __slots__ = ("fragment_id", "offset")
        FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        fragment_id: int
        offset: int
        def __init__(self, fragment_id: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    tag: str
    entries: _containers.RepeatedCompositeFieldContainer[CloudArchiveGetVideoFragmentsDataRequest.Entry]
    def __init__(self, session_id: _Optional[str] = ..., tag: _Optional[str] = ..., entries: _Optional[_Iterable[_Union[CloudArchiveGetVideoFragmentsDataRequest.Entry, _Mapping]]] = ...) -> None: ...
