from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import space_lite_pb2 as _space_lite_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JoinSpaceRequest(_message.Message):
    __slots__ = ("hub_qr",)
    HUB_QR_FIELD_NUMBER: _ClassVar[int]
    hub_qr: str
    def __init__(self, hub_qr: _Optional[str] = ...) -> None: ...

class JoinSpaceResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("lite_space",)
        LITE_SPACE_FIELD_NUMBER: _ClassVar[int]
        lite_space: _space_lite_pb2.LiteSpace
        def __init__(self, lite_space: _Optional[_Union[_space_lite_pb2.LiteSpace, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("hub_error",)
        class HubError(_message.Message):
            __slots__ = ("bad_request", "space_not_found", "hub_not_found", "hub_qr_code_invalid", "hub_claim_error", "hub_claim_forbidden_by_company_error", "hub_offline")
            BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
            SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
            HUB_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
            HUB_QR_CODE_INVALID_FIELD_NUMBER: _ClassVar[int]
            HUB_CLAIM_ERROR_FIELD_NUMBER: _ClassVar[int]
            HUB_CLAIM_FORBIDDEN_BY_COMPANY_ERROR_FIELD_NUMBER: _ClassVar[int]
            HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
            bad_request: _response_pb2.DefaultError
            space_not_found: _response_pb2.DefaultError
            hub_not_found: _response_pb2.DefaultError
            hub_qr_code_invalid: _response_pb2.DefaultError
            hub_claim_error: _response_pb2.DefaultError
            hub_claim_forbidden_by_company_error: _response_pb2.DefaultError
            hub_offline: _response_pb2.DefaultError
            def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_qr_code_invalid: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_claim_error: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_claim_forbidden_by_company_error: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_offline: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
        HUB_ERROR_FIELD_NUMBER: _ClassVar[int]
        hub_error: JoinSpaceResponse.Failure.HubError
        def __init__(self, hub_error: _Optional[_Union[JoinSpaceResponse.Failure.HubError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: JoinSpaceResponse.Success
    failure: JoinSpaceResponse.Failure
    def __init__(self, success: _Optional[_Union[JoinSpaceResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[JoinSpaceResponse.Failure, _Mapping]] = ...) -> None: ...
