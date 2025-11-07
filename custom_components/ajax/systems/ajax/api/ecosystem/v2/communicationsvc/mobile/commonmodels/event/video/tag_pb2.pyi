from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServerConnectionLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TamperOpened(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VideoScenarioTriggered(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ChannelDisconnected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StorageErrorDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StorageWriteErrorDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VideoExportPrepared(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VideoExportFailed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FWUpdateStarted(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FWUpdateFinished(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FWUpdateFailed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StoragePoweredOffOverheated(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ChannelAdded(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExternalPowerLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RingButtonPressed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PowerLow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BatteryDisconnected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HardFault(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MotionDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HumanDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PetDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CarDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LineCrossed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemporaryVideoAccessRequestFromPro(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemporaryVideoAccessRequestFromCompany(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemporaryVideoAccessDeniedForPro(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemporaryVideoAccessApprovedToCompany(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemporaryVideoAccessApprovedToPro(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemporaryVideoAccessDeniedForCompany(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DirectExportRequested(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BatteryTemperatureOutOfRange(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeviceBackupCommunicationChannelAdded(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeviceBackupCommunicationLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OnvifAuthEnabled(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeviceMoved(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeviceHit(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FanError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StorageDeviceEjected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetArchiveStorageDeviceWriteModeMirrored(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetArchiveStorageDeviceWriteModeRoundRobin(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VideoEventTag(_message.Message):
    __slots__ = ("server_connection_loss", "tamper_opened", "video_scenario_triggered", "storage_error_detected", "storage_write_error_detected", "storage_powered_off_overheated", "storage_device_ejected", "video_export_prepared", "video_export_failed", "direct_export_requested", "set_archive_storage_device_write_mode_mirrored", "set_archive_storage_device_write_mode_round_robin", "fw_update_started", "fw_update_finished", "fw_update_failed", "channel_disconnected", "channel_added", "external_power_loss", "ring_button_pressed", "power_low", "battery_disconnected", "hard_fault", "battery_temperature_out_of_range", "temporary_video_access_request_from_pro", "temporary_video_access_request_from_company", "temporary_video_access_denied_for_pro", "temporary_video_access_approved_to_company", "temporary_video_access_approved_to_pro", "temporary_video_access_denied_for_company", "motion_detected", "human_detected", "pet_detected", "car_detected", "line_crossed", "device_backup_communication_channel_added", "device_backup_communication_loss", "onvif_auth_enabled", "device_moved", "device_hit", "fan_error")
    SERVER_CONNECTION_LOSS_FIELD_NUMBER: _ClassVar[int]
    TAMPER_OPENED_FIELD_NUMBER: _ClassVar[int]
    VIDEO_SCENARIO_TRIGGERED_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ERROR_DETECTED_FIELD_NUMBER: _ClassVar[int]
    STORAGE_WRITE_ERROR_DETECTED_FIELD_NUMBER: _ClassVar[int]
    STORAGE_POWERED_OFF_OVERHEATED_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DEVICE_EJECTED_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EXPORT_PREPARED_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EXPORT_FAILED_FIELD_NUMBER: _ClassVar[int]
    DIRECT_EXPORT_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    SET_ARCHIVE_STORAGE_DEVICE_WRITE_MODE_MIRRORED_FIELD_NUMBER: _ClassVar[int]
    SET_ARCHIVE_STORAGE_DEVICE_WRITE_MODE_ROUND_ROBIN_FIELD_NUMBER: _ClassVar[int]
    FW_UPDATE_STARTED_FIELD_NUMBER: _ClassVar[int]
    FW_UPDATE_FINISHED_FIELD_NUMBER: _ClassVar[int]
    FW_UPDATE_FAILED_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_DISCONNECTED_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ADDED_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_POWER_LOSS_FIELD_NUMBER: _ClassVar[int]
    RING_BUTTON_PRESSED_FIELD_NUMBER: _ClassVar[int]
    POWER_LOW_FIELD_NUMBER: _ClassVar[int]
    BATTERY_DISCONNECTED_FIELD_NUMBER: _ClassVar[int]
    HARD_FAULT_FIELD_NUMBER: _ClassVar[int]
    BATTERY_TEMPERATURE_OUT_OF_RANGE_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_VIDEO_ACCESS_REQUEST_FROM_PRO_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_VIDEO_ACCESS_REQUEST_FROM_COMPANY_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_VIDEO_ACCESS_DENIED_FOR_PRO_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_VIDEO_ACCESS_APPROVED_TO_COMPANY_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_VIDEO_ACCESS_APPROVED_TO_PRO_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_VIDEO_ACCESS_DENIED_FOR_COMPANY_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTED_FIELD_NUMBER: _ClassVar[int]
    HUMAN_DETECTED_FIELD_NUMBER: _ClassVar[int]
    PET_DETECTED_FIELD_NUMBER: _ClassVar[int]
    CAR_DETECTED_FIELD_NUMBER: _ClassVar[int]
    LINE_CROSSED_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BACKUP_COMMUNICATION_CHANNEL_ADDED_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BACKUP_COMMUNICATION_LOSS_FIELD_NUMBER: _ClassVar[int]
    ONVIF_AUTH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DEVICE_MOVED_FIELD_NUMBER: _ClassVar[int]
    DEVICE_HIT_FIELD_NUMBER: _ClassVar[int]
    FAN_ERROR_FIELD_NUMBER: _ClassVar[int]
    server_connection_loss: ServerConnectionLoss
    tamper_opened: TamperOpened
    video_scenario_triggered: VideoScenarioTriggered
    storage_error_detected: StorageErrorDetected
    storage_write_error_detected: StorageWriteErrorDetected
    storage_powered_off_overheated: StoragePoweredOffOverheated
    storage_device_ejected: StorageDeviceEjected
    video_export_prepared: VideoExportPrepared
    video_export_failed: VideoExportFailed
    direct_export_requested: DirectExportRequested
    set_archive_storage_device_write_mode_mirrored: SetArchiveStorageDeviceWriteModeMirrored
    set_archive_storage_device_write_mode_round_robin: SetArchiveStorageDeviceWriteModeRoundRobin
    fw_update_started: FWUpdateStarted
    fw_update_finished: FWUpdateFinished
    fw_update_failed: FWUpdateFailed
    channel_disconnected: ChannelDisconnected
    channel_added: ChannelAdded
    external_power_loss: ExternalPowerLoss
    ring_button_pressed: RingButtonPressed
    power_low: PowerLow
    battery_disconnected: BatteryDisconnected
    hard_fault: HardFault
    battery_temperature_out_of_range: BatteryTemperatureOutOfRange
    temporary_video_access_request_from_pro: TemporaryVideoAccessRequestFromPro
    temporary_video_access_request_from_company: TemporaryVideoAccessRequestFromCompany
    temporary_video_access_denied_for_pro: TemporaryVideoAccessDeniedForPro
    temporary_video_access_approved_to_company: TemporaryVideoAccessApprovedToCompany
    temporary_video_access_approved_to_pro: TemporaryVideoAccessApprovedToPro
    temporary_video_access_denied_for_company: TemporaryVideoAccessDeniedForCompany
    motion_detected: MotionDetected
    human_detected: HumanDetected
    pet_detected: PetDetected
    car_detected: CarDetected
    line_crossed: LineCrossed
    device_backup_communication_channel_added: DeviceBackupCommunicationChannelAdded
    device_backup_communication_loss: DeviceBackupCommunicationLoss
    onvif_auth_enabled: OnvifAuthEnabled
    device_moved: DeviceMoved
    device_hit: DeviceHit
    fan_error: FanError
    def __init__(self, server_connection_loss: _Optional[_Union[ServerConnectionLoss, _Mapping]] = ..., tamper_opened: _Optional[_Union[TamperOpened, _Mapping]] = ..., video_scenario_triggered: _Optional[_Union[VideoScenarioTriggered, _Mapping]] = ..., storage_error_detected: _Optional[_Union[StorageErrorDetected, _Mapping]] = ..., storage_write_error_detected: _Optional[_Union[StorageWriteErrorDetected, _Mapping]] = ..., storage_powered_off_overheated: _Optional[_Union[StoragePoweredOffOverheated, _Mapping]] = ..., storage_device_ejected: _Optional[_Union[StorageDeviceEjected, _Mapping]] = ..., video_export_prepared: _Optional[_Union[VideoExportPrepared, _Mapping]] = ..., video_export_failed: _Optional[_Union[VideoExportFailed, _Mapping]] = ..., direct_export_requested: _Optional[_Union[DirectExportRequested, _Mapping]] = ..., set_archive_storage_device_write_mode_mirrored: _Optional[_Union[SetArchiveStorageDeviceWriteModeMirrored, _Mapping]] = ..., set_archive_storage_device_write_mode_round_robin: _Optional[_Union[SetArchiveStorageDeviceWriteModeRoundRobin, _Mapping]] = ..., fw_update_started: _Optional[_Union[FWUpdateStarted, _Mapping]] = ..., fw_update_finished: _Optional[_Union[FWUpdateFinished, _Mapping]] = ..., fw_update_failed: _Optional[_Union[FWUpdateFailed, _Mapping]] = ..., channel_disconnected: _Optional[_Union[ChannelDisconnected, _Mapping]] = ..., channel_added: _Optional[_Union[ChannelAdded, _Mapping]] = ..., external_power_loss: _Optional[_Union[ExternalPowerLoss, _Mapping]] = ..., ring_button_pressed: _Optional[_Union[RingButtonPressed, _Mapping]] = ..., power_low: _Optional[_Union[PowerLow, _Mapping]] = ..., battery_disconnected: _Optional[_Union[BatteryDisconnected, _Mapping]] = ..., hard_fault: _Optional[_Union[HardFault, _Mapping]] = ..., battery_temperature_out_of_range: _Optional[_Union[BatteryTemperatureOutOfRange, _Mapping]] = ..., temporary_video_access_request_from_pro: _Optional[_Union[TemporaryVideoAccessRequestFromPro, _Mapping]] = ..., temporary_video_access_request_from_company: _Optional[_Union[TemporaryVideoAccessRequestFromCompany, _Mapping]] = ..., temporary_video_access_denied_for_pro: _Optional[_Union[TemporaryVideoAccessDeniedForPro, _Mapping]] = ..., temporary_video_access_approved_to_company: _Optional[_Union[TemporaryVideoAccessApprovedToCompany, _Mapping]] = ..., temporary_video_access_approved_to_pro: _Optional[_Union[TemporaryVideoAccessApprovedToPro, _Mapping]] = ..., temporary_video_access_denied_for_company: _Optional[_Union[TemporaryVideoAccessDeniedForCompany, _Mapping]] = ..., motion_detected: _Optional[_Union[MotionDetected, _Mapping]] = ..., human_detected: _Optional[_Union[HumanDetected, _Mapping]] = ..., pet_detected: _Optional[_Union[PetDetected, _Mapping]] = ..., car_detected: _Optional[_Union[CarDetected, _Mapping]] = ..., line_crossed: _Optional[_Union[LineCrossed, _Mapping]] = ..., device_backup_communication_channel_added: _Optional[_Union[DeviceBackupCommunicationChannelAdded, _Mapping]] = ..., device_backup_communication_loss: _Optional[_Union[DeviceBackupCommunicationLoss, _Mapping]] = ..., onvif_auth_enabled: _Optional[_Union[OnvifAuthEnabled, _Mapping]] = ..., device_moved: _Optional[_Union[DeviceMoved, _Mapping]] = ..., device_hit: _Optional[_Union[DeviceHit, _Mapping]] = ..., fan_error: _Optional[_Union[FanError, _Mapping]] = ...) -> None: ...
