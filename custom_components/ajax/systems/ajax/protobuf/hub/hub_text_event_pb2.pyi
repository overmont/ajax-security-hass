from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HubTextEvent(_message.Message):
    __slots__ = ("parameter",)
    PARAMETER_FIELD_NUMBER: _ClassVar[int]
    parameter: _containers.RepeatedCompositeFieldContainer[HubParameter]
    def __init__(self, parameter: _Optional[_Iterable[_Union[HubParameter, _Mapping]]] = ...) -> None: ...

class HubParameter(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
