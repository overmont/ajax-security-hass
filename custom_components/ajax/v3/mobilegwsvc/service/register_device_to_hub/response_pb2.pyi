from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import object_type_pb2 as _object_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterDeviceToHubResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("device_added", "waiting_for_action", "search_started", "cancel_registration")
        class WaitingForAction(_message.Message):
            __slots__ = ("object_type",)
            OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
            object_type: _object_type_pb2.ObjectType
            def __init__(self, object_type: _Optional[_Union[_object_type_pb2.ObjectType, _Mapping]] = ...) -> None: ...
        class DeviceAdded(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class SearchStarted(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class CancelRegistration(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        DEVICE_ADDED_FIELD_NUMBER: _ClassVar[int]
        WAITING_FOR_ACTION_FIELD_NUMBER: _ClassVar[int]
        SEARCH_STARTED_FIELD_NUMBER: _ClassVar[int]
        CANCEL_REGISTRATION_FIELD_NUMBER: _ClassVar[int]
        device_added: RegisterDeviceToHubResponse.Success.DeviceAdded
        waiting_for_action: RegisterDeviceToHubResponse.Success.WaitingForAction
        search_started: RegisterDeviceToHubResponse.Success.SearchStarted
        cancel_registration: RegisterDeviceToHubResponse.Success.CancelRegistration
        def __init__(self, device_added: _Optional[_Union[RegisterDeviceToHubResponse.Success.DeviceAdded, _Mapping]] = ..., waiting_for_action: _Optional[_Union[RegisterDeviceToHubResponse.Success.WaitingForAction, _Mapping]] = ..., search_started: _Optional[_Union[RegisterDeviceToHubResponse.Success.SearchStarted, _Mapping]] = ..., cancel_registration: _Optional[_Union[RegisterDeviceToHubResponse.Success.CancelRegistration, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "hub_request_already_performed", "hub_wrong_state", "permission_denied", "hub_busy", "hub_offline", "device_search_timeout", "unknown_device", "hub_type_not_supported", "hub_firmware_not_supported", "s_line_insufficient_access", "s_line_unsupported_role", "device_registration_restricted", "limit_exceeded_on_fibra_line", "limit_exceeded_of_one_byte_devices", "switch_load_failed", "objects_limit_exceeded")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        HUB_REQUEST_ALREADY_PERFORMED_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        HUB_BUSY_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        DEVICE_SEARCH_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN_DEVICE_FIELD_NUMBER: _ClassVar[int]
        HUB_TYPE_NOT_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
        HUB_FIRMWARE_NOT_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
        S_LINE_INSUFFICIENT_ACCESS_FIELD_NUMBER: _ClassVar[int]
        S_LINE_UNSUPPORTED_ROLE_FIELD_NUMBER: _ClassVar[int]
        DEVICE_REGISTRATION_RESTRICTED_FIELD_NUMBER: _ClassVar[int]
        LIMIT_EXCEEDED_ON_FIBRA_LINE_FIELD_NUMBER: _ClassVar[int]
        LIMIT_EXCEEDED_OF_ONE_BYTE_DEVICES_FIELD_NUMBER: _ClassVar[int]
        SWITCH_LOAD_FAILED_FIELD_NUMBER: _ClassVar[int]
        OBJECTS_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        hub_request_already_performed: _response_pb2.Error
        hub_wrong_state: _response_pb2.HubWrongStateError
        permission_denied: _response_pb2.Error
        hub_busy: _response_pb2.HubBusyError
        hub_offline: _response_pb2.Error
        device_search_timeout: _response_pb2.Error
        unknown_device: RegisterDeviceToHubResponse.UnknownDeviceError
        hub_type_not_supported: _response_pb2.Error
        hub_firmware_not_supported: RegisterDeviceToHubResponse.HubFirmwareNotSupportedError
        s_line_insufficient_access: _response_pb2.Error
        s_line_unsupported_role: _response_pb2.Error
        device_registration_restricted: _response_pb2.Error
        limit_exceeded_on_fibra_line: _response_pb2.Error
        limit_exceeded_of_one_byte_devices: _response_pb2.Error
        switch_load_failed: _response_pb2.Error
        objects_limit_exceeded: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_request_already_performed: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_wrong_state: _Optional[_Union[_response_pb2.HubWrongStateError, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_busy: _Optional[_Union[_response_pb2.HubBusyError, _Mapping]] = ..., hub_offline: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., device_search_timeout: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., unknown_device: _Optional[_Union[RegisterDeviceToHubResponse.UnknownDeviceError, _Mapping]] = ..., hub_type_not_supported: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_firmware_not_supported: _Optional[_Union[RegisterDeviceToHubResponse.HubFirmwareNotSupportedError, _Mapping]] = ..., s_line_insufficient_access: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., s_line_unsupported_role: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., device_registration_restricted: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., limit_exceeded_on_fibra_line: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., limit_exceeded_of_one_byte_devices: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., switch_load_failed: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., objects_limit_exceeded: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    class UnknownDeviceError(_message.Message):
        __slots__ = ("available_fw_update",)
        class AvailableFwUpdate(_message.Message):
            __slots__ = ("firmware_version", "firmware_version_raw")
            FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
            FIRMWARE_VERSION_RAW_FIELD_NUMBER: _ClassVar[int]
            firmware_version: str
            firmware_version_raw: int
            def __init__(self, firmware_version: _Optional[str] = ..., firmware_version_raw: _Optional[int] = ...) -> None: ...
        AVAILABLE_FW_UPDATE_FIELD_NUMBER: _ClassVar[int]
        available_fw_update: RegisterDeviceToHubResponse.UnknownDeviceError.AvailableFwUpdate
        def __init__(self, available_fw_update: _Optional[_Union[RegisterDeviceToHubResponse.UnknownDeviceError.AvailableFwUpdate, _Mapping]] = ...) -> None: ...
    class HubFirmwareNotSupportedError(_message.Message):
        __slots__ = ("available_fw_update",)
        class AvailableFwUpdate(_message.Message):
            __slots__ = ("firmware_version", "firmware_version_raw")
            FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
            FIRMWARE_VERSION_RAW_FIELD_NUMBER: _ClassVar[int]
            firmware_version: str
            firmware_version_raw: int
            def __init__(self, firmware_version: _Optional[str] = ..., firmware_version_raw: _Optional[int] = ...) -> None: ...
        AVAILABLE_FW_UPDATE_FIELD_NUMBER: _ClassVar[int]
        available_fw_update: RegisterDeviceToHubResponse.HubFirmwareNotSupportedError.AvailableFwUpdate
        def __init__(self, available_fw_update: _Optional[_Union[RegisterDeviceToHubResponse.HubFirmwareNotSupportedError.AvailableFwUpdate, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: RegisterDeviceToHubResponse.Success
    failure: RegisterDeviceToHubResponse.Failure
    def __init__(self, success: _Optional[_Union[RegisterDeviceToHubResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[RegisterDeviceToHubResponse.Failure, _Mapping]] = ...) -> None: ...
