from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class En54DisablementEndpoints(_message.Message):
    __slots__ = ("endpoints", "endpoint_data")
    class Endpoint(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENDPOINT_UNSPECIFIED: _ClassVar[En54DisablementEndpoints.Endpoint]
        ENDPOINT_SMOKE: _ClassVar[En54DisablementEndpoints.Endpoint]
        ENDPOINT_TEMP: _ClassVar[En54DisablementEndpoints.Endpoint]
        ENDPOINT_TEMP_RAPID_RISE: _ClassVar[En54DisablementEndpoints.Endpoint]
        ENDPOINT_SOUNDER: _ClassVar[En54DisablementEndpoints.Endpoint]
        ENDPOINT_VAD: _ClassVar[En54DisablementEndpoints.Endpoint]
        ENDPOINT_OUTPUT_1: _ClassVar[En54DisablementEndpoints.Endpoint]
        ENDPOINT_OUTPUT_2: _ClassVar[En54DisablementEndpoints.Endpoint]
        ENDPOINT_OUTPUTS: _ClassVar[En54DisablementEndpoints.Endpoint]
        ENDPOINT_INPUT: _ClassVar[En54DisablementEndpoints.Endpoint]
        ENDPOINT_MCP: _ClassVar[En54DisablementEndpoints.Endpoint]
    ENDPOINT_UNSPECIFIED: En54DisablementEndpoints.Endpoint
    ENDPOINT_SMOKE: En54DisablementEndpoints.Endpoint
    ENDPOINT_TEMP: En54DisablementEndpoints.Endpoint
    ENDPOINT_TEMP_RAPID_RISE: En54DisablementEndpoints.Endpoint
    ENDPOINT_SOUNDER: En54DisablementEndpoints.Endpoint
    ENDPOINT_VAD: En54DisablementEndpoints.Endpoint
    ENDPOINT_OUTPUT_1: En54DisablementEndpoints.Endpoint
    ENDPOINT_OUTPUT_2: En54DisablementEndpoints.Endpoint
    ENDPOINT_OUTPUTS: En54DisablementEndpoints.Endpoint
    ENDPOINT_INPUT: En54DisablementEndpoints.Endpoint
    ENDPOINT_MCP: En54DisablementEndpoints.Endpoint
    class EndpointData(_message.Message):
        __slots__ = ("endpoint", "name")
        ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        endpoint: En54DisablementEndpoints.Endpoint
        name: str
        def __init__(self, endpoint: _Optional[_Union[En54DisablementEndpoints.Endpoint, str]] = ..., name: _Optional[str] = ...) -> None: ...
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_DATA_FIELD_NUMBER: _ClassVar[int]
    endpoints: _containers.RepeatedScalarFieldContainer[En54DisablementEndpoints.Endpoint]
    endpoint_data: _containers.RepeatedCompositeFieldContainer[En54DisablementEndpoints.EndpointData]
    def __init__(self, endpoints: _Optional[_Iterable[_Union[En54DisablementEndpoints.Endpoint, str]]] = ..., endpoint_data: _Optional[_Iterable[_Union[En54DisablementEndpoints.EndpointData, _Mapping]]] = ...) -> None: ...
