from systems.ajax.api.mobile.v2.common.hub.device.common import battery_charged_state_pb2 as _battery_charged_state_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.backupchannel import backup_channel_info_pb2 as _backup_channel_info_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.mcu import chime_pb2 as _chime_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.mcu import operating_mode_pb2 as _operating_mode_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.mcu.spacesettings import backup_channel_space_settings_pb2 as _backup_channel_space_settings_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Mcu(_message.Message):
    __slots__ = ("battery_status", "external_power_state", "mcu_state", "backup_channel_info", "backup_channel_space_settings", "operating_mode", "battery_state", "battery_charged_state", "chime", "assigned_extender_device_index", "battery_temperature_state", "pir_motion_led_indication", "ring_button_bell_state", "capabilities")
    class ExternalPowerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXTERNAL_POWER_STATE_UNSPECIFIED: _ClassVar[Mcu.ExternalPowerState]
        EXTERNAL_POWER_STATE_CONNECTED: _ClassVar[Mcu.ExternalPowerState]
        EXTERNAL_POWER_STATE_DISCONNECTED: _ClassVar[Mcu.ExternalPowerState]
    EXTERNAL_POWER_STATE_UNSPECIFIED: Mcu.ExternalPowerState
    EXTERNAL_POWER_STATE_CONNECTED: Mcu.ExternalPowerState
    EXTERNAL_POWER_STATE_DISCONNECTED: Mcu.ExternalPowerState
    class BatteryState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BATTERY_STATE_UNSPECIFIED: _ClassVar[Mcu.BatteryState]
        BATTERY_STATE_BROKEN: _ClassVar[Mcu.BatteryState]
        BATTERY_STATE_OK: _ClassVar[Mcu.BatteryState]
    BATTERY_STATE_UNSPECIFIED: Mcu.BatteryState
    BATTERY_STATE_BROKEN: Mcu.BatteryState
    BATTERY_STATE_OK: Mcu.BatteryState
    class McuState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MCU_STATE_UNSPECIFIED: _ClassVar[Mcu.McuState]
        MCU_STATE_FIRMWARE_UPGRADE_IN_PROGRESS: _ClassVar[Mcu.McuState]
        MCU_STATE_OK: _ClassVar[Mcu.McuState]
        MCU_STATE_FAILED: _ClassVar[Mcu.McuState]
    MCU_STATE_UNSPECIFIED: Mcu.McuState
    MCU_STATE_FIRMWARE_UPGRADE_IN_PROGRESS: Mcu.McuState
    MCU_STATE_OK: Mcu.McuState
    MCU_STATE_FAILED: Mcu.McuState
    class BatteryTemperatureState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BATTERY_TEMPERATURE_STATE_UNSPECIFIED: _ClassVar[Mcu.BatteryTemperatureState]
        BATTERY_TEMPERATURE_STATE_OK: _ClassVar[Mcu.BatteryTemperatureState]
        BATTERY_TEMPERATURE_STATE_OUT_OF_RANGE: _ClassVar[Mcu.BatteryTemperatureState]
    BATTERY_TEMPERATURE_STATE_UNSPECIFIED: Mcu.BatteryTemperatureState
    BATTERY_TEMPERATURE_STATE_OK: Mcu.BatteryTemperatureState
    BATTERY_TEMPERATURE_STATE_OUT_OF_RANGE: Mcu.BatteryTemperatureState
    class PirMotionLedIndication(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PIR_MOTION_LED_INDICATION_UNSPECIFIED: _ClassVar[Mcu.PirMotionLedIndication]
        PIR_MOTION_LED_INDICATION_ENABLED: _ClassVar[Mcu.PirMotionLedIndication]
        PIR_MOTION_LED_INDICATION_DISABLED: _ClassVar[Mcu.PirMotionLedIndication]
    PIR_MOTION_LED_INDICATION_UNSPECIFIED: Mcu.PirMotionLedIndication
    PIR_MOTION_LED_INDICATION_ENABLED: Mcu.PirMotionLedIndication
    PIR_MOTION_LED_INDICATION_DISABLED: Mcu.PirMotionLedIndication
    class RingButtonBellState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RING_BUTTON_BELL_STATE_UNSPECIFIED: _ClassVar[Mcu.RingButtonBellState]
        RING_BUTTON_BELL_STATE_ENABLED: _ClassVar[Mcu.RingButtonBellState]
        RING_BUTTON_BELL_STATE_DISABLED: _ClassVar[Mcu.RingButtonBellState]
    RING_BUTTON_BELL_STATE_UNSPECIFIED: Mcu.RingButtonBellState
    RING_BUTTON_BELL_STATE_ENABLED: Mcu.RingButtonBellState
    RING_BUTTON_BELL_STATE_DISABLED: Mcu.RingButtonBellState
    class BatteryStatus(_message.Message):
        __slots__ = ("battery_state", "battery_charged_state")
        BATTERY_STATE_FIELD_NUMBER: _ClassVar[int]
        BATTERY_CHARGED_STATE_FIELD_NUMBER: _ClassVar[int]
        battery_state: Mcu.BatteryState
        battery_charged_state: _battery_charged_state_pb2.BatteryChargedState
        def __init__(self, battery_state: _Optional[_Union[Mcu.BatteryState, str]] = ..., battery_charged_state: _Optional[_Union[_battery_charged_state_pb2.BatteryChargedState, str]] = ...) -> None: ...
    class Capabilities(_message.Message):
        __slots__ = ("flags",)
        class Flag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            FLAG_UNSPECIFIED: _ClassVar[Mcu.Capabilities.Flag]
            FLAG_HAVE_BATTERY: _ClassVar[Mcu.Capabilities.Flag]
            FLAG_SUPPORTS_INTRUSION: _ClassVar[Mcu.Capabilities.Flag]
            FLAG_HAVE_CHIME: _ClassVar[Mcu.Capabilities.Flag]
            FLAG_HAVE_RING_BUTTON: _ClassVar[Mcu.Capabilities.Flag]
            FLAG_HAVE_PIR_MOTION_LED_INDICATION: _ClassVar[Mcu.Capabilities.Flag]
        FLAG_UNSPECIFIED: Mcu.Capabilities.Flag
        FLAG_HAVE_BATTERY: Mcu.Capabilities.Flag
        FLAG_SUPPORTS_INTRUSION: Mcu.Capabilities.Flag
        FLAG_HAVE_CHIME: Mcu.Capabilities.Flag
        FLAG_HAVE_RING_BUTTON: Mcu.Capabilities.Flag
        FLAG_HAVE_PIR_MOTION_LED_INDICATION: Mcu.Capabilities.Flag
        FLAGS_FIELD_NUMBER: _ClassVar[int]
        flags: _containers.RepeatedScalarFieldContainer[Mcu.Capabilities.Flag]
        def __init__(self, flags: _Optional[_Iterable[_Union[Mcu.Capabilities.Flag, str]]] = ...) -> None: ...
    BATTERY_STATUS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_POWER_STATE_FIELD_NUMBER: _ClassVar[int]
    MCU_STATE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_CHANNEL_INFO_FIELD_NUMBER: _ClassVar[int]
    BACKUP_CHANNEL_SPACE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    OPERATING_MODE_FIELD_NUMBER: _ClassVar[int]
    BATTERY_STATE_FIELD_NUMBER: _ClassVar[int]
    BATTERY_CHARGED_STATE_FIELD_NUMBER: _ClassVar[int]
    CHIME_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_EXTENDER_DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
    BATTERY_TEMPERATURE_STATE_FIELD_NUMBER: _ClassVar[int]
    PIR_MOTION_LED_INDICATION_FIELD_NUMBER: _ClassVar[int]
    RING_BUTTON_BELL_STATE_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    battery_status: Mcu.BatteryStatus
    external_power_state: Mcu.ExternalPowerState
    mcu_state: Mcu.McuState
    backup_channel_info: _backup_channel_info_pb2.BackupChannelInfo
    backup_channel_space_settings: _backup_channel_space_settings_pb2.BackupChannelSpaceSettings
    operating_mode: _operating_mode_pb2.OperatingMode
    battery_state: Mcu.BatteryState
    battery_charged_state: _battery_charged_state_pb2.BatteryChargedState
    chime: _chime_pb2.Chime
    assigned_extender_device_index: int
    battery_temperature_state: Mcu.BatteryTemperatureState
    pir_motion_led_indication: Mcu.PirMotionLedIndication
    ring_button_bell_state: Mcu.RingButtonBellState
    capabilities: Mcu.Capabilities
    def __init__(self, battery_status: _Optional[_Union[Mcu.BatteryStatus, _Mapping]] = ..., external_power_state: _Optional[_Union[Mcu.ExternalPowerState, str]] = ..., mcu_state: _Optional[_Union[Mcu.McuState, str]] = ..., backup_channel_info: _Optional[_Union[_backup_channel_info_pb2.BackupChannelInfo, _Mapping]] = ..., backup_channel_space_settings: _Optional[_Union[_backup_channel_space_settings_pb2.BackupChannelSpaceSettings, _Mapping]] = ..., operating_mode: _Optional[_Union[_operating_mode_pb2.OperatingMode, str]] = ..., battery_state: _Optional[_Union[Mcu.BatteryState, str]] = ..., battery_charged_state: _Optional[_Union[_battery_charged_state_pb2.BatteryChargedState, str]] = ..., chime: _Optional[_Union[_chime_pb2.Chime, _Mapping]] = ..., assigned_extender_device_index: _Optional[int] = ..., battery_temperature_state: _Optional[_Union[Mcu.BatteryTemperatureState, str]] = ..., pir_motion_led_indication: _Optional[_Union[Mcu.PirMotionLedIndication, str]] = ..., ring_button_bell_state: _Optional[_Union[Mcu.RingButtonBellState, str]] = ..., capabilities: _Optional[_Union[Mcu.Capabilities, _Mapping]] = ...) -> None: ...
