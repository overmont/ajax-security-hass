from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.validation import validation_by_pb2 as _validation_by_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResendConfirmationCodesResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("expected_token_length", "validation_by_sms", "validation_by_call")
        EXPECTED_TOKEN_LENGTH_FIELD_NUMBER: _ClassVar[int]
        VALIDATION_BY_SMS_FIELD_NUMBER: _ClassVar[int]
        VALIDATION_BY_CALL_FIELD_NUMBER: _ClassVar[int]
        expected_token_length: int
        validation_by_sms: _validation_by_pb2.ValidationBySms
        validation_by_call: _validation_by_pb2.ValidationByCall
        def __init__(self, expected_token_length: _Optional[int] = ..., validation_by_sms: _Optional[_Union[_validation_by_pb2.ValidationBySms, _Mapping]] = ..., validation_by_call: _Optional[_Union[_validation_by_pb2.ValidationByCall, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "email_validation_failed", "phone_validation_failed", "cannot_request_confirmation_codes", "cannot_send_confirmation_codes")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        EMAIL_VALIDATION_FAILED_FIELD_NUMBER: _ClassVar[int]
        PHONE_VALIDATION_FAILED_FIELD_NUMBER: _ClassVar[int]
        CANNOT_REQUEST_CONFIRMATION_CODES_FIELD_NUMBER: _ClassVar[int]
        CANNOT_SEND_CONFIRMATION_CODES_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        email_validation_failed: _response_pb2.Error
        phone_validation_failed: _response_pb2.Error
        cannot_request_confirmation_codes: _response_pb2.Error
        cannot_send_confirmation_codes: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., email_validation_failed: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., phone_validation_failed: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., cannot_request_confirmation_codes: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., cannot_send_confirmation_codes: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: ResendConfirmationCodesResponse.Success
    failure: ResendConfirmationCodesResponse.Failure
    def __init__(self, success: _Optional[_Union[ResendConfirmationCodesResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[ResendConfirmationCodesResponse.Failure, _Mapping]] = ...) -> None: ...
