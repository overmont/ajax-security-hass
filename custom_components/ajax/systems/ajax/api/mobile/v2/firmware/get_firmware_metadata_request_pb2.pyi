from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common import resource_id_pb2 as _resource_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetFirmwareMetadataRequest(_message.Message):
    __slots__ = ("resource_id", "language_code")
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    resource_id: _resource_id_pb2.ResourceId
    language_code: str
    def __init__(self, resource_id: _Optional[_Union[_resource_id_pb2.ResourceId, _Mapping]] = ..., language_code: _Optional[str] = ...) -> None: ...

class GetFirmwareMetadataResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("release_notes", "before_proceed_notes")
        RELEASE_NOTES_FIELD_NUMBER: _ClassVar[int]
        BEFORE_PROCEED_NOTES_FIELD_NUMBER: _ClassVar[int]
        release_notes: _containers.RepeatedScalarFieldContainer[str]
        before_proceed_notes: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, release_notes: _Optional[_Iterable[str]] = ..., before_proceed_notes: _Optional[_Iterable[str]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("message", "illegal_argument", "not_found")
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        message: str
        illegal_argument: _response_pb2.DefaultError
        not_found: _response_pb2.DefaultError
        def __init__(self, message: _Optional[str] = ..., illegal_argument: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetFirmwareMetadataResponse.Success
    failure: GetFirmwareMetadataResponse.Failure
    def __init__(self, success: _Optional[_Union[GetFirmwareMetadataResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[GetFirmwareMetadataResponse.Failure, _Mapping]] = ...) -> None: ...
