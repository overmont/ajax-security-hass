from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorResponse(_message.Message):
    __slots__ = ("message", "errors")
    class Error(_message.Message):
        __slots__ = ("resource", "property_name_path", "property_index_path", "message_template", "message_parameters", "message")
        class MessageParametersEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        RESOURCE_FIELD_NUMBER: _ClassVar[int]
        PROPERTY_NAME_PATH_FIELD_NUMBER: _ClassVar[int]
        PROPERTY_INDEX_PATH_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        resource: str
        property_name_path: str
        property_index_path: str
        message_template: str
        message_parameters: _containers.ScalarMap[str, str]
        message: str
        def __init__(self, resource: _Optional[str] = ..., property_name_path: _Optional[str] = ..., property_index_path: _Optional[str] = ..., message_template: _Optional[str] = ..., message_parameters: _Optional[_Mapping[str, str]] = ..., message: _Optional[str] = ...) -> None: ...
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    message: str
    errors: _containers.RepeatedCompositeFieldContainer[ErrorResponse.Error]
    def __init__(self, message: _Optional[str] = ..., errors: _Optional[_Iterable[_Union[ErrorResponse.Error, _Mapping]]] = ...) -> None: ...

class ErrorId(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...
