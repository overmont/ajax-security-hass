from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.accounting import feature_target_info_pb2 as _feature_target_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApplyForMonitoringRequest(_message.Message):
    __slots__ = ("company_hex_id", "space_id", "account_number")
    COMPANY_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    company_hex_id: str
    space_id: str
    account_number: str
    def __init__(self, company_hex_id: _Optional[str] = ..., space_id: _Optional[str] = ..., account_number: _Optional[str] = ...) -> None: ...

class ApplyForMonitoringResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("feature_target_info",)
        FEATURE_TARGET_INFO_FIELD_NUMBER: _ClassVar[int]
        feature_target_info: _feature_target_info_pb2.FeatureTargetInfo
        def __init__(self, feature_target_info: _Optional[_Union[_feature_target_info_pb2.FeatureTargetInfo, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "space_not_found", "space_on_monitoring_already_exists", "permission_denied", "hub_locked", "users_limit_exceed", "account_number_required", "account_number_exists", "cannot_perform_action_for_initiator", "space_armed", "space_locked")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ON_MONITORING_ALREADY_EXISTS_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        HUB_LOCKED_FIELD_NUMBER: _ClassVar[int]
        USERS_LIMIT_EXCEED_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_NUMBER_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_NUMBER_EXISTS_FIELD_NUMBER: _ClassVar[int]
        CANNOT_PERFORM_ACTION_FOR_INITIATOR_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        space_on_monitoring_already_exists: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        hub_locked: _response_pb2.DefaultError
        users_limit_exceed: _response_pb2.DefaultError
        account_number_required: _response_pb2.DefaultError
        account_number_exists: _response_pb2.DefaultError
        cannot_perform_action_for_initiator: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        space_locked: _response_pb2.SpaceLockedError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_on_monitoring_already_exists: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_locked: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., users_limit_exceed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., account_number_required: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., account_number_exists: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., cannot_perform_action_for_initiator: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_armed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_locked: _Optional[_Union[_response_pb2.SpaceLockedError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: ApplyForMonitoringResponse.Success
    failure: ApplyForMonitoringResponse.Failure
    def __init__(self, success: _Optional[_Union[ApplyForMonitoringResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[ApplyForMonitoringResponse.Failure, _Mapping]] = ...) -> None: ...
