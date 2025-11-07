from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.space.device.light import light_device_id_pb2 as _light_device_id_pb2
from v3.mobilegwsvc.commonmodels.company.templates import company_template_type_pb2 as _company_template_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamDevicePresetApplicationResponse(_message.Message):
    __slots__ = ("success", "failure")
    class SettingsApplyStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SETTINGS_APPLY_STATUS_UNSPECIFIED: _ClassVar[StreamDevicePresetApplicationResponse.SettingsApplyStatus]
        SETTINGS_APPLY_STATUS_SUCCESS: _ClassVar[StreamDevicePresetApplicationResponse.SettingsApplyStatus]
        SETTINGS_APPLY_STATUS_FAILURE: _ClassVar[StreamDevicePresetApplicationResponse.SettingsApplyStatus]
        SETTINGS_APPLY_STATUS_FAILED_TO_START: _ClassVar[StreamDevicePresetApplicationResponse.SettingsApplyStatus]
    SETTINGS_APPLY_STATUS_UNSPECIFIED: StreamDevicePresetApplicationResponse.SettingsApplyStatus
    SETTINGS_APPLY_STATUS_SUCCESS: StreamDevicePresetApplicationResponse.SettingsApplyStatus
    SETTINGS_APPLY_STATUS_FAILURE: StreamDevicePresetApplicationResponse.SettingsApplyStatus
    SETTINGS_APPLY_STATUS_FAILED_TO_START: StreamDevicePresetApplicationResponse.SettingsApplyStatus
    class Success(_message.Message):
        __slots__ = ("snapshot", "update")
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        UPDATE_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamDevicePresetApplicationResponse.Snapshot
        update: StreamDevicePresetApplicationResponse.Update
        def __init__(self, snapshot: _Optional[_Union[StreamDevicePresetApplicationResponse.Snapshot, _Mapping]] = ..., update: _Optional[_Union[StreamDevicePresetApplicationResponse.Update, _Mapping]] = ...) -> None: ...
    class Snapshot(_message.Message):
        __slots__ = ("total_num_of_targets", "total_processed", "errors", "company_template_metadata")
        TOTAL_NUM_OF_TARGETS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_PROCESSED_FIELD_NUMBER: _ClassVar[int]
        ERRORS_FIELD_NUMBER: _ClassVar[int]
        COMPANY_TEMPLATE_METADATA_FIELD_NUMBER: _ClassVar[int]
        total_num_of_targets: int
        total_processed: int
        errors: _containers.RepeatedCompositeFieldContainer[StreamDevicePresetApplicationResponse.SettingsApplyResultOnTarget]
        company_template_metadata: StreamDevicePresetApplicationResponse.TemplateMetadata
        def __init__(self, total_num_of_targets: _Optional[int] = ..., total_processed: _Optional[int] = ..., errors: _Optional[_Iterable[_Union[StreamDevicePresetApplicationResponse.SettingsApplyResultOnTarget, _Mapping]]] = ..., company_template_metadata: _Optional[_Union[StreamDevicePresetApplicationResponse.TemplateMetadata, _Mapping]] = ...) -> None: ...
    class TemplateMetadata(_message.Message):
        __slots__ = ("company_template_name", "company_template_type")
        COMPANY_TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
        COMPANY_TEMPLATE_TYPE_FIELD_NUMBER: _ClassVar[int]
        company_template_name: str
        company_template_type: _company_template_type_pb2.CompanyTemplateType
        def __init__(self, company_template_name: _Optional[str] = ..., company_template_type: _Optional[_Union[_company_template_type_pb2.CompanyTemplateType, str]] = ...) -> None: ...
    class Update(_message.Message):
        __slots__ = ("application_result",)
        APPLICATION_RESULT_FIELD_NUMBER: _ClassVar[int]
        application_result: StreamDevicePresetApplicationResponse.SettingsApplyResultOnTarget
        def __init__(self, application_result: _Optional[_Union[StreamDevicePresetApplicationResponse.SettingsApplyResultOnTarget, _Mapping]] = ...) -> None: ...
    class SettingsApplyResultOnTarget(_message.Message):
        __slots__ = ("target", "apply_status")
        TARGET_FIELD_NUMBER: _ClassVar[int]
        APPLY_STATUS_FIELD_NUMBER: _ClassVar[int]
        target: StreamDevicePresetApplicationResponse.SettingTarget
        apply_status: StreamDevicePresetApplicationResponse.SettingsApplyStatus
        def __init__(self, target: _Optional[_Union[StreamDevicePresetApplicationResponse.SettingTarget, _Mapping]] = ..., apply_status: _Optional[_Union[StreamDevicePresetApplicationResponse.SettingsApplyStatus, str]] = ...) -> None: ...
    class SettingTarget(_message.Message):
        __slots__ = ("light_device_id",)
        LIGHT_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
        light_device_id: _light_device_id_pb2.LightDeviceId
        def __init__(self, light_device_id: _Optional[_Union[_light_device_id_pb2.LightDeviceId, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("illegal_argument", "permission_denied")
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        illegal_argument: _response_pb2.Error
        permission_denied: _response_pb2.Error
        def __init__(self, illegal_argument: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamDevicePresetApplicationResponse.Success
    failure: StreamDevicePresetApplicationResponse.Failure
    def __init__(self, success: _Optional[_Union[StreamDevicePresetApplicationResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[StreamDevicePresetApplicationResponse.Failure, _Mapping]] = ...) -> None: ...
