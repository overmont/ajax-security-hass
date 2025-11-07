from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.company import lite_space_company_pb2 as _lite_space_company_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamLiteSpaceCompaniesResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("snapshot", "update")
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        UPDATE_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamLiteSpaceCompaniesResponse.Snapshot
        update: StreamLiteSpaceCompaniesResponse.Update
        def __init__(self, snapshot: _Optional[_Union[StreamLiteSpaceCompaniesResponse.Snapshot, _Mapping]] = ..., update: _Optional[_Union[StreamLiteSpaceCompaniesResponse.Update, _Mapping]] = ...) -> None: ...
    class Snapshot(_message.Message):
        __slots__ = ("lite_space_companies",)
        LITE_SPACE_COMPANIES_FIELD_NUMBER: _ClassVar[int]
        lite_space_companies: StreamLiteSpaceCompaniesResponse.LiteSpaceCompanies
        def __init__(self, lite_space_companies: _Optional[_Union[StreamLiteSpaceCompaniesResponse.LiteSpaceCompanies, _Mapping]] = ...) -> None: ...
    class Update(_message.Message):
        __slots__ = ("lite_space_company", "update_type")
        class UpdateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UPDATE_TYPE_UNSPECIFIED: _ClassVar[StreamLiteSpaceCompaniesResponse.Update.UpdateType]
            UPDATE_TYPE_ADD: _ClassVar[StreamLiteSpaceCompaniesResponse.Update.UpdateType]
            UPDATE_TYPE_UPDATE: _ClassVar[StreamLiteSpaceCompaniesResponse.Update.UpdateType]
            UPDATE_TYPE_REMOVE: _ClassVar[StreamLiteSpaceCompaniesResponse.Update.UpdateType]
        UPDATE_TYPE_UNSPECIFIED: StreamLiteSpaceCompaniesResponse.Update.UpdateType
        UPDATE_TYPE_ADD: StreamLiteSpaceCompaniesResponse.Update.UpdateType
        UPDATE_TYPE_UPDATE: StreamLiteSpaceCompaniesResponse.Update.UpdateType
        UPDATE_TYPE_REMOVE: StreamLiteSpaceCompaniesResponse.Update.UpdateType
        LITE_SPACE_COMPANY_FIELD_NUMBER: _ClassVar[int]
        UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
        lite_space_company: _lite_space_company_pb2.LiteSpaceCompany
        update_type: StreamLiteSpaceCompaniesResponse.Update.UpdateType
        def __init__(self, lite_space_company: _Optional[_Union[_lite_space_company_pb2.LiteSpaceCompany, _Mapping]] = ..., update_type: _Optional[_Union[StreamLiteSpaceCompaniesResponse.Update.UpdateType, str]] = ...) -> None: ...
    class LiteSpaceCompanies(_message.Message):
        __slots__ = ("lite_space_company",)
        LITE_SPACE_COMPANY_FIELD_NUMBER: _ClassVar[int]
        lite_space_company: _containers.RepeatedCompositeFieldContainer[_lite_space_company_pb2.LiteSpaceCompany]
        def __init__(self, lite_space_company: _Optional[_Iterable[_Union[_lite_space_company_pb2.LiteSpaceCompany, _Mapping]]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamLiteSpaceCompaniesResponse.Success
    failure: StreamLiteSpaceCompaniesResponse.Failure
    def __init__(self, success: _Optional[_Union[StreamLiteSpaceCompaniesResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[StreamLiteSpaceCompaniesResponse.Failure, _Mapping]] = ...) -> None: ...
