from v3.mobilegwsvc.commonmodels.hub.device.light.properties import eol_sensor_properties_pb2 as _eol_sensor_properties_pb2
from v3.mobilegwsvc.commonmodels.hub.device.light.properties import keyarm_lock_pb2 as _keyarm_lock_pb2
from v3.mobilegwsvc.commonmodels.hub.device.light.properties import motion_cam_hdr_pb2 as _motion_cam_hdr_pb2
from v3.mobilegwsvc.commonmodels.hub.device.light.properties import relay_single_channel_custom_properties_pb2 as _relay_single_channel_custom_properties_pb2
from v3.mobilegwsvc.commonmodels.hub.device.light.properties import relay_channel_pb2 as _relay_channel_pb2
from v3.mobilegwsvc.commonmodels.hub.device.light.properties import reset_fire_alarm_wi_pb2 as _reset_fire_alarm_wi_pb2
from v3.mobilegwsvc.commonmodels.hub.device.light.properties import wire_inputs_pb2 as _wire_inputs_pb2
from v3.mobilegwsvc.commonmodels.hub.device.light.properties import fire_zone_id_pb2 as _fire_zone_id_pb2
from v3.mobilegwsvc.commonmodels.hub.device.light.properties import light_switch_channel_pb2 as _light_switch_channel_pb2
from v3.mobilegwsvc.commonmodels.hub.device.light.properties import transmitter_index_pb2 as _transmitter_index_pb2
from v3.mobilegwsvc.commonmodels.hub.device.light.properties import fire_device_action_button_pb2 as _fire_device_action_button_pb2
from v3.mobilegwsvc.commonmodels.hub.device.light import light_common_hub_device_pb2 as _light_common_hub_device_pb2
from v3.mobilegwsvc.commonmodels.hub.device.light.properties import photo_on_demand_pb2 as _photo_on_demand_pb2
from v3.mobilegwsvc.commonmodels.hub.device.light.properties import fire_zones_pb2 as _fire_zones_pb2
from v3.mobilegwsvc.commonmodels.hub.device.light.properties import download_firmware_update_pb2 as _download_firmware_update_pb2
from v3.mobilegwsvc.commonmodels.hub.device.light.properties import billing_company_pb2 as _billing_company_pb2
from v3.mobilegwsvc.commonmodels.space.device.light.properties import subscription_state_pb2 as _subscription_state_pb2
from v3.mobilegwsvc.commonmodels.hub.device.light.properties import hub_box_appearance_pb2 as _hub_box_appearance_pb2
from v3.mobilegwsvc.commonmodels.hub.device.light.properties import vhf_bridge_outputs_pb2 as _vhf_bridge_outputs_pb2
from v3.mobilegwsvc.commonmodels.hub.device.light.properties import access_devices_pb2 as _access_devices_pb2
from v3.mobilegwsvc.commonmodels.hub.device.light.properties import keypad_lock_pb2 as _keypad_lock_pb2
from v3.mobilegwsvc.commonmodels.hub.device.light.properties import socket_base_channel_pb2 as _socket_base_channel_pb2
from v3.mobilegwsvc.commonmodels.hub.device.light.properties import life_quality_info_pb2 as _life_quality_info_pb2
from v3.mobilegwsvc.commonmodels.hub.device.light.properties import water_stop_channel_pb2 as _water_stop_channel_pb2
from v3.mobilegwsvc.commonmodels.device.light.properties import smart_lock_control_pb2 as _smart_lock_control_pb2
from v3.mobilegwsvc.commonmodels.hub.device.light.properties import yavir_access_control_properties_pb2 as _yavir_access_control_properties_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LightHubDevice(_message.Message):
    __slots__ = ("common_device", "custom_properties", "spread_properties", "device_specific_properties")
    class CustomProperties(_message.Message):
        __slots__ = ("relay_single_channel_properties",)
        RELAY_SINGLE_CHANNEL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        relay_single_channel_properties: _relay_single_channel_custom_properties_pb2.RelaySingleChannelCustomProperties
        def __init__(self, relay_single_channel_properties: _Optional[_Union[_relay_single_channel_custom_properties_pb2.RelaySingleChannelCustomProperties, _Mapping]] = ...) -> None: ...
    class SpreadProperties(_message.Message):
        __slots__ = ("sort_index", "channel", "reset_fire_alarm_wi", "wire_inputs", "light_switch_channel", "keyarm_lock", "fire_device_action_button", "photo_on_demand", "fire_zones", "download_firmware_update", "billing_company", "subscription_state", "vhf_bridge_outputs", "keypad_lock", "socket_base_channel", "life_quality_info", "water_stop_channel", "smart_lock_control")
        SORT_INDEX_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_FIELD_NUMBER: _ClassVar[int]
        RESET_FIRE_ALARM_WI_FIELD_NUMBER: _ClassVar[int]
        WIRE_INPUTS_FIELD_NUMBER: _ClassVar[int]
        LIGHT_SWITCH_CHANNEL_FIELD_NUMBER: _ClassVar[int]
        KEYARM_LOCK_FIELD_NUMBER: _ClassVar[int]
        FIRE_DEVICE_ACTION_BUTTON_FIELD_NUMBER: _ClassVar[int]
        PHOTO_ON_DEMAND_FIELD_NUMBER: _ClassVar[int]
        FIRE_ZONES_FIELD_NUMBER: _ClassVar[int]
        DOWNLOAD_FIRMWARE_UPDATE_FIELD_NUMBER: _ClassVar[int]
        BILLING_COMPANY_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIPTION_STATE_FIELD_NUMBER: _ClassVar[int]
        VHF_BRIDGE_OUTPUTS_FIELD_NUMBER: _ClassVar[int]
        KEYPAD_LOCK_FIELD_NUMBER: _ClassVar[int]
        SOCKET_BASE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
        LIFE_QUALITY_INFO_FIELD_NUMBER: _ClassVar[int]
        WATER_STOP_CHANNEL_FIELD_NUMBER: _ClassVar[int]
        SMART_LOCK_CONTROL_FIELD_NUMBER: _ClassVar[int]
        sort_index: int
        channel: _relay_channel_pb2.RelayChannel
        reset_fire_alarm_wi: _reset_fire_alarm_wi_pb2.ResetFireAlarmWi
        wire_inputs: _wire_inputs_pb2.WireInputs
        light_switch_channel: _light_switch_channel_pb2.LightSwitchChannel
        keyarm_lock: _keyarm_lock_pb2.KeyarmLock
        fire_device_action_button: _fire_device_action_button_pb2.FireDeviceActionButton
        photo_on_demand: _photo_on_demand_pb2.PhotoOnDemand
        fire_zones: _fire_zones_pb2.FireZones
        download_firmware_update: _download_firmware_update_pb2.DownloadFirmwareUpdate
        billing_company: _billing_company_pb2.BillingCompany
        subscription_state: _subscription_state_pb2.SubscriptionState
        vhf_bridge_outputs: _vhf_bridge_outputs_pb2.VhfBridgeOutputs
        keypad_lock: _keypad_lock_pb2.KeypadLock
        socket_base_channel: _socket_base_channel_pb2.SocketBaseChannel
        life_quality_info: _life_quality_info_pb2.LifeQualityInfo
        water_stop_channel: _water_stop_channel_pb2.WaterStopChannel
        smart_lock_control: _smart_lock_control_pb2.SmartLockControl
        def __init__(self, sort_index: _Optional[int] = ..., channel: _Optional[_Union[_relay_channel_pb2.RelayChannel, _Mapping]] = ..., reset_fire_alarm_wi: _Optional[_Union[_reset_fire_alarm_wi_pb2.ResetFireAlarmWi, _Mapping]] = ..., wire_inputs: _Optional[_Union[_wire_inputs_pb2.WireInputs, _Mapping]] = ..., light_switch_channel: _Optional[_Union[_light_switch_channel_pb2.LightSwitchChannel, _Mapping]] = ..., keyarm_lock: _Optional[_Union[_keyarm_lock_pb2.KeyarmLock, _Mapping]] = ..., fire_device_action_button: _Optional[_Union[_fire_device_action_button_pb2.FireDeviceActionButton, _Mapping]] = ..., photo_on_demand: _Optional[_Union[_photo_on_demand_pb2.PhotoOnDemand, _Mapping]] = ..., fire_zones: _Optional[_Union[_fire_zones_pb2.FireZones, _Mapping]] = ..., download_firmware_update: _Optional[_Union[_download_firmware_update_pb2.DownloadFirmwareUpdate, _Mapping]] = ..., billing_company: _Optional[_Union[_billing_company_pb2.BillingCompany, _Mapping]] = ..., subscription_state: _Optional[_Union[_subscription_state_pb2.SubscriptionState, _Mapping]] = ..., vhf_bridge_outputs: _Optional[_Union[_vhf_bridge_outputs_pb2.VhfBridgeOutputs, _Mapping]] = ..., keypad_lock: _Optional[_Union[_keypad_lock_pb2.KeypadLock, _Mapping]] = ..., socket_base_channel: _Optional[_Union[_socket_base_channel_pb2.SocketBaseChannel, _Mapping]] = ..., life_quality_info: _Optional[_Union[_life_quality_info_pb2.LifeQualityInfo, _Mapping]] = ..., water_stop_channel: _Optional[_Union[_water_stop_channel_pb2.WaterStopChannel, _Mapping]] = ..., smart_lock_control: _Optional[_Union[_smart_lock_control_pb2.SmartLockControl, _Mapping]] = ...) -> None: ...
    class DeviceSpecificProperties(_message.Message):
        __slots__ = ("fire_zone_id", "transmitter_index", "motion_cam_hdr", "eol_sensor_properties", "hub_box_appearance", "access_devices", "yavir_access_control_properties")
        FIRE_ZONE_ID_FIELD_NUMBER: _ClassVar[int]
        TRANSMITTER_INDEX_FIELD_NUMBER: _ClassVar[int]
        MOTION_CAM_HDR_FIELD_NUMBER: _ClassVar[int]
        EOL_SENSOR_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        HUB_BOX_APPEARANCE_FIELD_NUMBER: _ClassVar[int]
        ACCESS_DEVICES_FIELD_NUMBER: _ClassVar[int]
        YAVIR_ACCESS_CONTROL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        fire_zone_id: _fire_zone_id_pb2.FireZoneId
        transmitter_index: _transmitter_index_pb2.TransmitterIndex
        motion_cam_hdr: _motion_cam_hdr_pb2.MotionCamHdr
        eol_sensor_properties: _eol_sensor_properties_pb2.EolSensorProperties
        hub_box_appearance: _hub_box_appearance_pb2.HubBoxAppearance
        access_devices: _access_devices_pb2.AccessDevices
        yavir_access_control_properties: _yavir_access_control_properties_pb2.YavirAccessControlProperties
        def __init__(self, fire_zone_id: _Optional[_Union[_fire_zone_id_pb2.FireZoneId, _Mapping]] = ..., transmitter_index: _Optional[_Union[_transmitter_index_pb2.TransmitterIndex, _Mapping]] = ..., motion_cam_hdr: _Optional[_Union[_motion_cam_hdr_pb2.MotionCamHdr, _Mapping]] = ..., eol_sensor_properties: _Optional[_Union[_eol_sensor_properties_pb2.EolSensorProperties, _Mapping]] = ..., hub_box_appearance: _Optional[_Union[_hub_box_appearance_pb2.HubBoxAppearance, _Mapping]] = ..., access_devices: _Optional[_Union[_access_devices_pb2.AccessDevices, _Mapping]] = ..., yavir_access_control_properties: _Optional[_Union[_yavir_access_control_properties_pb2.YavirAccessControlProperties, _Mapping]] = ...) -> None: ...
    COMMON_DEVICE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    SPREAD_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    DEVICE_SPECIFIC_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    common_device: _light_common_hub_device_pb2.LightCommonHubDevice
    custom_properties: LightHubDevice.CustomProperties
    spread_properties: _containers.RepeatedCompositeFieldContainer[LightHubDevice.SpreadProperties]
    device_specific_properties: _containers.RepeatedCompositeFieldContainer[LightHubDevice.DeviceSpecificProperties]
    def __init__(self, common_device: _Optional[_Union[_light_common_hub_device_pb2.LightCommonHubDevice, _Mapping]] = ..., custom_properties: _Optional[_Union[LightHubDevice.CustomProperties, _Mapping]] = ..., spread_properties: _Optional[_Iterable[_Union[LightHubDevice.SpreadProperties, _Mapping]]] = ..., device_specific_properties: _Optional[_Iterable[_Union[LightHubDevice.DeviceSpecificProperties, _Mapping]]] = ...) -> None: ...
