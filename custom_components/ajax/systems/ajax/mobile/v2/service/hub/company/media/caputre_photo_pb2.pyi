from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CapturePhotoOnDemandRequest(_message.Message):
    __slots__ = ("hub_id", "device_id", "device_type")
    class DeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_DEVICE_TYPE_INFO: _ClassVar[CapturePhotoOnDemandRequest.DeviceType]
        MOTION_CAM: _ClassVar[CapturePhotoOnDemandRequest.DeviceType]
        MOTION_CAM_OUTDOOR: _ClassVar[CapturePhotoOnDemandRequest.DeviceType]
        MOTION_CAM_FIBRA_BASE: _ClassVar[CapturePhotoOnDemandRequest.DeviceType]
    NO_DEVICE_TYPE_INFO: CapturePhotoOnDemandRequest.DeviceType
    MOTION_CAM: CapturePhotoOnDemandRequest.DeviceType
    MOTION_CAM_OUTDOOR: CapturePhotoOnDemandRequest.DeviceType
    MOTION_CAM_FIBRA_BASE: CapturePhotoOnDemandRequest.DeviceType
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    device_id: str
    device_type: CapturePhotoOnDemandRequest.DeviceType
    def __init__(self, hub_id: _Optional[str] = ..., device_id: _Optional[str] = ..., device_type: _Optional[_Union[CapturePhotoOnDemandRequest.DeviceType, str]] = ...) -> None: ...

class CapturePhotoOnDemandResponse(_message.Message):
    __slots__ = ("success", "error")
    class Error(_message.Message):
        __slots__ = ("request_already_sent", "internal_error", "company_on_hub_not_found_error", "permission_denied_error", "deadline_exceeded_error", "wrong_device_state", "hub_busy_error")
        REQUEST_ALREADY_SENT_FIELD_NUMBER: _ClassVar[int]
        INTERNAL_ERROR_FIELD_NUMBER: _ClassVar[int]
        COMPANY_ON_HUB_NOT_FOUND_ERROR_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_ERROR_FIELD_NUMBER: _ClassVar[int]
        DEADLINE_EXCEEDED_ERROR_FIELD_NUMBER: _ClassVar[int]
        WRONG_DEVICE_STATE_FIELD_NUMBER: _ClassVar[int]
        HUB_BUSY_ERROR_FIELD_NUMBER: _ClassVar[int]
        request_already_sent: _response_pb2.IllegalStateError
        internal_error: _response_pb2.InternalError
        company_on_hub_not_found_error: _response_pb2.CompanyOnHubNotFoundError
        permission_denied_error: _response_pb2.PermissionDeniedError
        deadline_exceeded_error: _response_pb2.DeadlineExceededError
        wrong_device_state: _response_pb2.IllegalStateError
        hub_busy_error: _response_pb2.HubBusyError
        def __init__(self, request_already_sent: _Optional[_Union[_response_pb2.IllegalStateError, _Mapping]] = ..., internal_error: _Optional[_Union[_response_pb2.InternalError, _Mapping]] = ..., company_on_hub_not_found_error: _Optional[_Union[_response_pb2.CompanyOnHubNotFoundError, _Mapping]] = ..., permission_denied_error: _Optional[_Union[_response_pb2.PermissionDeniedError, _Mapping]] = ..., deadline_exceeded_error: _Optional[_Union[_response_pb2.DeadlineExceededError, _Mapping]] = ..., wrong_device_state: _Optional[_Union[_response_pb2.IllegalStateError, _Mapping]] = ..., hub_busy_error: _Optional[_Union[_response_pb2.HubBusyError, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    error: CapturePhotoOnDemandResponse.Error
    def __init__(self, success: _Optional[_Union[_response_pb2.Success, _Mapping]] = ..., error: _Optional[_Union[CapturePhotoOnDemandResponse.Error, _Mapping]] = ...) -> None: ...
