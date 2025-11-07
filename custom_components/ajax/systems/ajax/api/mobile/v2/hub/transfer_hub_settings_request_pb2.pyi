from systems.ajax.api.mobile.v2.common.space import space_locator_pb2 as _space_locator_pb2
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransferHubSettingsRequest(_message.Message):
    __slots__ = ("space_locator", "donor_hub_id", "target_hub_qr_code", "accept_snatch_hub")
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    DONOR_HUB_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_HUB_QR_CODE_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_SNATCH_HUB_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    donor_hub_id: str
    target_hub_qr_code: str
    accept_snatch_hub: bool
    def __init__(self, space_locator: _Optional[_Union[_space_locator_pb2.SpaceLocator, _Mapping]] = ..., donor_hub_id: _Optional[str] = ..., target_hub_qr_code: _Optional[str] = ..., accept_snatch_hub: bool = ...) -> None: ...

class TransferHubSettingsResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_not_found", "space_locked", "passive_hubs_limit_exceeded", "hub_in_use", "hub_already_in_space", "target_hub_not_found", "hub_qr_code_invalid", "hub_claim_error", "hub_not_empty", "hub_error", "hub_wrong_state", "hub_busy", "member_not_support_add_fibra_and_hybrid_hub", "member_not_authorized_add_hub", "member_not_authorized_add_fibra_and_hybrid_hub", "hub_locked_by_another_company", "target_hub_space_on_monitoring", "transfer_hub_settings_validation_errors", "donor_hub_has_active_subscriptions", "donor_hub_has_active_subscriptions_for_member", "target_hub_has_active_subscriptions", "target_hub_has_active_subscriptions_for_member", "illegal_donor_hub_service_state")
        class TransferHubSettingsValidationErrors(_message.Message):
            __slots__ = ("error",)
            class TransferHubSettingsValidationError(_message.Message):
                __slots__ = ("target_permission_denied", "target_armed", "target_state_fetch_failed", "target_offline", "target_in_migration", "target_firmware_lower_minimal", "target_firmware_lower_donor", "target_users_limit_exceeded", "donor_permission_denied", "donor_state_fetch_failed", "donor_target_incompatible_types", "donor_firmware_lower_minimal", "donor_in_migration", "donor_online")
                TARGET_PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
                TARGET_ARMED_FIELD_NUMBER: _ClassVar[int]
                TARGET_STATE_FETCH_FAILED_FIELD_NUMBER: _ClassVar[int]
                TARGET_OFFLINE_FIELD_NUMBER: _ClassVar[int]
                TARGET_IN_MIGRATION_FIELD_NUMBER: _ClassVar[int]
                TARGET_FIRMWARE_LOWER_MINIMAL_FIELD_NUMBER: _ClassVar[int]
                TARGET_FIRMWARE_LOWER_DONOR_FIELD_NUMBER: _ClassVar[int]
                TARGET_USERS_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
                DONOR_PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
                DONOR_STATE_FETCH_FAILED_FIELD_NUMBER: _ClassVar[int]
                DONOR_TARGET_INCOMPATIBLE_TYPES_FIELD_NUMBER: _ClassVar[int]
                DONOR_FIRMWARE_LOWER_MINIMAL_FIELD_NUMBER: _ClassVar[int]
                DONOR_IN_MIGRATION_FIELD_NUMBER: _ClassVar[int]
                DONOR_ONLINE_FIELD_NUMBER: _ClassVar[int]
                target_permission_denied: _response_pb2.DefaultError
                target_armed: _response_pb2.DefaultError
                target_state_fetch_failed: _response_pb2.DefaultError
                target_offline: _response_pb2.DefaultError
                target_in_migration: _response_pb2.DefaultError
                target_firmware_lower_minimal: _response_pb2.DefaultError
                target_firmware_lower_donor: _response_pb2.DefaultError
                target_users_limit_exceeded: _response_pb2.DefaultError
                donor_permission_denied: _response_pb2.DefaultError
                donor_state_fetch_failed: _response_pb2.DefaultError
                donor_target_incompatible_types: _response_pb2.DefaultError
                donor_firmware_lower_minimal: _response_pb2.DefaultError
                donor_in_migration: _response_pb2.DefaultError
                donor_online: _response_pb2.DefaultError
                def __init__(self, target_permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., target_armed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., target_state_fetch_failed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., target_offline: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., target_in_migration: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., target_firmware_lower_minimal: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., target_firmware_lower_donor: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., target_users_limit_exceeded: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., donor_permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., donor_state_fetch_failed: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., donor_target_incompatible_types: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., donor_firmware_lower_minimal: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., donor_in_migration: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., donor_online: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
            ERROR_FIELD_NUMBER: _ClassVar[int]
            error: _containers.RepeatedCompositeFieldContainer[TransferHubSettingsResponse.Failure.TransferHubSettingsValidationErrors.TransferHubSettingsValidationError]
            def __init__(self, error: _Optional[_Iterable[_Union[TransferHubSettingsResponse.Failure.TransferHubSettingsValidationErrors.TransferHubSettingsValidationError, _Mapping]]] = ...) -> None: ...
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        PASSIVE_HUBS_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
        HUB_IN_USE_FIELD_NUMBER: _ClassVar[int]
        HUB_ALREADY_IN_SPACE_FIELD_NUMBER: _ClassVar[int]
        TARGET_HUB_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        HUB_QR_CODE_INVALID_FIELD_NUMBER: _ClassVar[int]
        HUB_CLAIM_ERROR_FIELD_NUMBER: _ClassVar[int]
        HUB_NOT_EMPTY_FIELD_NUMBER: _ClassVar[int]
        HUB_ERROR_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        HUB_BUSY_FIELD_NUMBER: _ClassVar[int]
        MEMBER_NOT_SUPPORT_ADD_FIBRA_AND_HYBRID_HUB_FIELD_NUMBER: _ClassVar[int]
        MEMBER_NOT_AUTHORIZED_ADD_HUB_FIELD_NUMBER: _ClassVar[int]
        MEMBER_NOT_AUTHORIZED_ADD_FIBRA_AND_HYBRID_HUB_FIELD_NUMBER: _ClassVar[int]
        HUB_LOCKED_BY_ANOTHER_COMPANY_FIELD_NUMBER: _ClassVar[int]
        TARGET_HUB_SPACE_ON_MONITORING_FIELD_NUMBER: _ClassVar[int]
        TRANSFER_HUB_SETTINGS_VALIDATION_ERRORS_FIELD_NUMBER: _ClassVar[int]
        DONOR_HUB_HAS_ACTIVE_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
        DONOR_HUB_HAS_ACTIVE_SUBSCRIPTIONS_FOR_MEMBER_FIELD_NUMBER: _ClassVar[int]
        TARGET_HUB_HAS_ACTIVE_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
        TARGET_HUB_HAS_ACTIVE_SUBSCRIPTIONS_FOR_MEMBER_FIELD_NUMBER: _ClassVar[int]
        ILLEGAL_DONOR_HUB_SERVICE_STATE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        space_locked: _response_pb2.SpaceLockedError
        passive_hubs_limit_exceeded: _response_pb2.LimitExceededError
        hub_in_use: _response_pb2.DefaultError
        hub_already_in_space: _response_pb2.DefaultError
        target_hub_not_found: _response_pb2.DefaultError
        hub_qr_code_invalid: _response_pb2.DefaultError
        hub_claim_error: _response_pb2.DefaultError
        hub_not_empty: _response_pb2.DefaultError
        hub_error: _response_pb2.DefaultError
        hub_wrong_state: _response_pb2.DefaultError
        hub_busy: _response_pb2.HubBusyError
        member_not_support_add_fibra_and_hybrid_hub: _response_pb2.DefaultError
        member_not_authorized_add_hub: _response_pb2.DefaultError
        member_not_authorized_add_fibra_and_hybrid_hub: _response_pb2.DefaultError
        hub_locked_by_another_company: _response_pb2.DefaultError
        target_hub_space_on_monitoring: _response_pb2.DefaultError
        transfer_hub_settings_validation_errors: TransferHubSettingsResponse.Failure.TransferHubSettingsValidationErrors
        donor_hub_has_active_subscriptions: _response_pb2.DefaultError
        donor_hub_has_active_subscriptions_for_member: _response_pb2.DefaultError
        target_hub_has_active_subscriptions: _response_pb2.DefaultError
        target_hub_has_active_subscriptions_for_member: _response_pb2.DefaultError
        illegal_donor_hub_service_state: _response_pb2.DefaultError
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., space_locked: _Optional[_Union[_response_pb2.SpaceLockedError, _Mapping]] = ..., passive_hubs_limit_exceeded: _Optional[_Union[_response_pb2.LimitExceededError, _Mapping]] = ..., hub_in_use: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_already_in_space: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., target_hub_not_found: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_qr_code_invalid: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_claim_error: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_not_empty: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_error: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_wrong_state: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_busy: _Optional[_Union[_response_pb2.HubBusyError, _Mapping]] = ..., member_not_support_add_fibra_and_hybrid_hub: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., member_not_authorized_add_hub: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., member_not_authorized_add_fibra_and_hybrid_hub: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_locked_by_another_company: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., target_hub_space_on_monitoring: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., transfer_hub_settings_validation_errors: _Optional[_Union[TransferHubSettingsResponse.Failure.TransferHubSettingsValidationErrors, _Mapping]] = ..., donor_hub_has_active_subscriptions: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., donor_hub_has_active_subscriptions_for_member: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., target_hub_has_active_subscriptions: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., target_hub_has_active_subscriptions_for_member: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., illegal_donor_hub_service_state: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: TransferHubSettingsResponse.Failure
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., failure: _Optional[_Union[TransferHubSettingsResponse.Failure, _Mapping]] = ...) -> None: ...
