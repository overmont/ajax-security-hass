from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.accounting import extra_service_pb2 as _extra_service_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamExtraServiceActivationResultResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("extra_service_activated", "extra_service_failed_to_activate", "extra_service_activation_in_progress")
        EXTRA_SERVICE_ACTIVATED_FIELD_NUMBER: _ClassVar[int]
        EXTRA_SERVICE_FAILED_TO_ACTIVATE_FIELD_NUMBER: _ClassVar[int]
        EXTRA_SERVICE_ACTIVATION_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
        extra_service_activated: StreamExtraServiceActivationResultResponse.ExtraServiceActivated
        extra_service_failed_to_activate: StreamExtraServiceActivationResultResponse.ExtraServiceFailedToActivate
        extra_service_activation_in_progress: StreamExtraServiceActivationResultResponse.ExtraServiceActivationInProgress
        def __init__(self, extra_service_activated: _Optional[_Union[StreamExtraServiceActivationResultResponse.ExtraServiceActivated, _Mapping]] = ..., extra_service_failed_to_activate: _Optional[_Union[StreamExtraServiceActivationResultResponse.ExtraServiceFailedToActivate, _Mapping]] = ..., extra_service_activation_in_progress: _Optional[_Union[StreamExtraServiceActivationResultResponse.ExtraServiceActivationInProgress, _Mapping]] = ...) -> None: ...
    class ExtraServiceActivated(_message.Message):
        __slots__ = ("new_extra_service",)
        NEW_EXTRA_SERVICE_FIELD_NUMBER: _ClassVar[int]
        new_extra_service: _extra_service_pb2.ExtraService
        def __init__(self, new_extra_service: _Optional[_Union[_extra_service_pb2.ExtraService, _Mapping]] = ...) -> None: ...
    class ExtraServiceFailedToActivate(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class ExtraServiceActivationInProgress(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("message", "request_timeout", "illegal_argument")
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        REQUEST_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        message: str
        request_timeout: _response_pb2.Error
        illegal_argument: _response_pb2.Error
        def __init__(self, message: _Optional[str] = ..., request_timeout: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., illegal_argument: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamExtraServiceActivationResultResponse.Success
    failure: StreamExtraServiceActivationResultResponse.Failure
    def __init__(self, success: _Optional[_Union[StreamExtraServiceActivationResultResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[StreamExtraServiceActivationResultResponse.Failure, _Mapping]] = ...) -> None: ...
