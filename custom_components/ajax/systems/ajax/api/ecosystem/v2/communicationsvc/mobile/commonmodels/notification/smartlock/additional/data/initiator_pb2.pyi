from systems.ajax.logging.proto import formatting_options_pb2 as _formatting_options_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Initiator(_message.Message):
    __slots__ = ("id", "type", "name")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Initiator.Type]
        TYPE_EXTERNAL_USER: _ClassVar[Initiator.Type]
        TYPE_SPACE_MEMBER: _ClassVar[Initiator.Type]
        TYPE_SCENARIO: _ClassVar[Initiator.Type]
    TYPE_UNSPECIFIED: Initiator.Type
    TYPE_EXTERNAL_USER: Initiator.Type
    TYPE_SPACE_MEMBER: Initiator.Type
    TYPE_SCENARIO: Initiator.Type
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: Initiator.Type
    name: str
    def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[Initiator.Type, str]] = ..., name: _Optional[str] = ...) -> None: ...
