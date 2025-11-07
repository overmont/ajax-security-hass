from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.company.templates import lightweight_company_template_pb2 as _lightweight_company_template_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FindAllLightweightCompanyTemplatesResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("templates",)
        TEMPLATES_FIELD_NUMBER: _ClassVar[int]
        templates: _containers.RepeatedCompositeFieldContainer[_lightweight_company_template_pb2.LightweightCompanyTemplate]
        def __init__(self, templates: _Optional[_Iterable[_Union[_lightweight_company_template_pb2.LightweightCompanyTemplate, _Mapping]]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("illegal_argument", "permission_denied")
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        illegal_argument: _response_pb2.Error
        permission_denied: _response_pb2.Error
        def __init__(self, illegal_argument: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: FindAllLightweightCompanyTemplatesResponse.Success
    failure: FindAllLightweightCompanyTemplatesResponse.Failure
    def __init__(self, success: _Optional[_Union[FindAllLightweightCompanyTemplatesResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[FindAllLightweightCompanyTemplatesResponse.Failure, _Mapping]] = ...) -> None: ...
