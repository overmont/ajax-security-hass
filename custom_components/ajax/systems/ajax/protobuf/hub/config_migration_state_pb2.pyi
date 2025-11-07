from systems.ajax.protobuf.hub import object_type_pb2 as _object_type_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigMigrationState(_message.Message):
    __slots__ = ("data_transfer_state", "migration_frame_devices_state", "migration_button_devices_state", "migration_result", "object_type", "id")
    class DataTransferState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_TRANSFER_UNKNOWN_STATE: _ClassVar[ConfigMigrationState.DataTransferState]
        DATA_TRANSFER_IN_PROGRESS: _ClassVar[ConfigMigrationState.DataTransferState]
        DATA_TRANSFER_FINISHED: _ClassVar[ConfigMigrationState.DataTransferState]
    DATA_TRANSFER_UNKNOWN_STATE: ConfigMigrationState.DataTransferState
    DATA_TRANSFER_IN_PROGRESS: ConfigMigrationState.DataTransferState
    DATA_TRANSFER_FINISHED: ConfigMigrationState.DataTransferState
    class MigrationFrameDevicesState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MIGRATION_FRAME_DEVICES_UNKNOWN_STATE: _ClassVar[ConfigMigrationState.MigrationFrameDevicesState]
        MIGRATION_FRAME_DEVICES_NOT_AVAILABLE: _ClassVar[ConfigMigrationState.MigrationFrameDevicesState]
        MIGRATION_FRAME_DEVICES_WAITING_FOR_START: _ClassVar[ConfigMigrationState.MigrationFrameDevicesState]
        MIGRATION_FRAME_DEVICES_IN_PROGRESS: _ClassVar[ConfigMigrationState.MigrationFrameDevicesState]
        MIGRATION_FRAME_DEVICES_FINISHED: _ClassVar[ConfigMigrationState.MigrationFrameDevicesState]
    MIGRATION_FRAME_DEVICES_UNKNOWN_STATE: ConfigMigrationState.MigrationFrameDevicesState
    MIGRATION_FRAME_DEVICES_NOT_AVAILABLE: ConfigMigrationState.MigrationFrameDevicesState
    MIGRATION_FRAME_DEVICES_WAITING_FOR_START: ConfigMigrationState.MigrationFrameDevicesState
    MIGRATION_FRAME_DEVICES_IN_PROGRESS: ConfigMigrationState.MigrationFrameDevicesState
    MIGRATION_FRAME_DEVICES_FINISHED: ConfigMigrationState.MigrationFrameDevicesState
    class MigrationButtonDevicesState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MIGRATION_BUTTON_DEVICES_UNKNOWN_STATE: _ClassVar[ConfigMigrationState.MigrationButtonDevicesState]
        MIGRATION_BUTTON_DEVICES_NOT_AVAILABLE: _ClassVar[ConfigMigrationState.MigrationButtonDevicesState]
        MIGRATION_BUTTON_DEVICES_WAITING_FOR_START: _ClassVar[ConfigMigrationState.MigrationButtonDevicesState]
        MIGRATION_BUTTON_DEVICES_IN_PROGRESS: _ClassVar[ConfigMigrationState.MigrationButtonDevicesState]
        MIGRATION_BUTTON_DEVICES_FINISHED: _ClassVar[ConfigMigrationState.MigrationButtonDevicesState]
    MIGRATION_BUTTON_DEVICES_UNKNOWN_STATE: ConfigMigrationState.MigrationButtonDevicesState
    MIGRATION_BUTTON_DEVICES_NOT_AVAILABLE: ConfigMigrationState.MigrationButtonDevicesState
    MIGRATION_BUTTON_DEVICES_WAITING_FOR_START: ConfigMigrationState.MigrationButtonDevicesState
    MIGRATION_BUTTON_DEVICES_IN_PROGRESS: ConfigMigrationState.MigrationButtonDevicesState
    MIGRATION_BUTTON_DEVICES_FINISHED: ConfigMigrationState.MigrationButtonDevicesState
    class MigrationResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MIGRATION_RESULT_IN_PROGRESS: _ClassVar[ConfigMigrationState.MigrationResult]
        MIGRATION_RESULT_SERVER_TIMED_OUT: _ClassVar[ConfigMigrationState.MigrationResult]
        MIGRATION_RESULT_FINISHED_OK: _ClassVar[ConfigMigrationState.MigrationResult]
        MIGRATION_RESULT_MIGRATION_FAILED: _ClassVar[ConfigMigrationState.MigrationResult]
    MIGRATION_RESULT_IN_PROGRESS: ConfigMigrationState.MigrationResult
    MIGRATION_RESULT_SERVER_TIMED_OUT: ConfigMigrationState.MigrationResult
    MIGRATION_RESULT_FINISHED_OK: ConfigMigrationState.MigrationResult
    MIGRATION_RESULT_MIGRATION_FAILED: ConfigMigrationState.MigrationResult
    DATA_TRANSFER_STATE_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_FRAME_DEVICES_STATE_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_BUTTON_DEVICES_STATE_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    data_transfer_state: ConfigMigrationState.DataTransferState
    migration_frame_devices_state: ConfigMigrationState.MigrationFrameDevicesState
    migration_button_devices_state: ConfigMigrationState.MigrationButtonDevicesState
    migration_result: ConfigMigrationState.MigrationResult
    object_type: _object_type_pb2.ObjectType
    id: str
    def __init__(self, data_transfer_state: _Optional[_Union[ConfigMigrationState.DataTransferState, str]] = ..., migration_frame_devices_state: _Optional[_Union[ConfigMigrationState.MigrationFrameDevicesState, str]] = ..., migration_button_devices_state: _Optional[_Union[ConfigMigrationState.MigrationButtonDevicesState, str]] = ..., migration_result: _Optional[_Union[ConfigMigrationState.MigrationResult, str]] = ..., object_type: _Optional[_Union[_object_type_pb2.ObjectType, str]] = ..., id: _Optional[str] = ...) -> None: ...
