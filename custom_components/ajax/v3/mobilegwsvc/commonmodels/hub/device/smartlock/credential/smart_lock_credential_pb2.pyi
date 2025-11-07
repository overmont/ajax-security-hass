from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SmartLockCredential(_message.Message):
    __slots__ = ("id", "name", "enabled", "entry_code", "contactless_key")
    class EntryCode(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class ContactlessKey(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ENTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    CONTACTLESS_KEY_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    enabled: bool
    entry_code: SmartLockCredential.EntryCode
    contactless_key: SmartLockCredential.ContactlessKey
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., enabled: bool = ..., entry_code: _Optional[_Union[SmartLockCredential.EntryCode, _Mapping]] = ..., contactless_key: _Optional[_Union[SmartLockCredential.ContactlessKey, _Mapping]] = ...) -> None: ...
