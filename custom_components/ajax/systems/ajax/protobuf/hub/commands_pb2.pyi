from google.protobuf import wrappers_pb2 as _wrappers_pb2
from systems.ajax.protobuf.hub import hub_pb2 as _hub_pb2
from systems.ajax.protobuf.hub import user_pb2 as _user_pb2
from systems.ajax.protobuf.hub import update_pb2 as _update_pb2
from systems.ajax.protobuf.hub import camera_pb2 as _camera_pb2
from systems.ajax.protobuf.hub.device import hub_device_pb2 as _hub_device_pb2
from systems.ajax.protobuf.hub import object_type_pb2 as _object_type_pb2
from systems.ajax.protobuf.hub import scenario_pb2 as _scenario_pb2
from systems.ajax.protobuf.gw import error_pb2 as _error_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from systems.ajax.protobuf.hub.device import device_pb2 as _device_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HubCommand(_message.Message):
    __slots__ = ("hub_id", "arming", "panic", "drop_cache", "cancel_search", "start_firmware_update", "update_groups_mode", "reset_sim_traffic_counter", "mute_fire_detectors", "reset_alarm_condition", "delay_interconnect", "update_card_state", "group_arming", "drop_logs", "invite_users", "revoke_user_invite", "profi_hub_access_request", "detach_user", "change_user_role", "change_user_permissions", "request_arming_reset", "engineer_attendance_required", "create_new_room", "delete_room", "create_new_group", "delete_group", "link_camera", "unlink_camera", "edit_stream_data", "link_device", "unlink_device", "device_command", "scan_fibra_devices", "get_scanned_fibra_devices", "create_security_company_binding", "delete_security_company_binding", "cancel_delete_security_company_binding", "update_network_channel_state", "update_ethernet_settings", "update_wifi_settings", "update_gsm_sim_card_settings", "update_gsm_sim_card_balance_number", "get_gsm_sim_card_balance", "scan_wifi_networks", "join_wifi_network", "join_wifi_network_advanced", "forget_wifi_network", "apply_update", "create_scenario", "update_scenario", "delete_scenario", "apply_updates", "start_migration", "stop_migration", "add_access_card", "delete_access_card", "erase_access_card", "exit_card_mode", "cancel_access_key_search", "register_access_key", "delete_access_key")
    class Answer(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[HubCommand.Answer]
        DELIVERED: _ClassVar[HubCommand.Answer]
        DELIVERED_COMMAND_PERFORMED: _ClassVar[HubCommand.Answer]
        DELIVERED_COMMAND_NOT_PERFORMED: _ClassVar[HubCommand.Answer]
        MODE_FINISHED: _ClassVar[HubCommand.Answer]
        FAILED_INSUFFICIENT_ACCESS: _ClassVar[HubCommand.Answer]
        FAILED_UNKNOWN_COMMAND: _ClassVar[HubCommand.Answer]
        UNDELIVERED_RECEIVER_OFFLINE: _ClassVar[HubCommand.Answer]
        UNDELIVERED_WRONG_RECEIVER: _ClassVar[HubCommand.Answer]
        DELIVERED_WAS_ALREADY_PERFORMED: _ClassVar[HubCommand.Answer]
        FAILED_WRONG_PARAMETERS: _ClassVar[HubCommand.Answer]
        FAILED_WRONG_MESSAGE_TYPE: _ClassVar[HubCommand.Answer]
        TRANSPORT_EXCEPTION: _ClassVar[HubCommand.Answer]
        SERVER_ERROR: _ClassVar[HubCommand.Answer]
        REQUEST_DELIVERED: _ClassVar[HubCommand.Answer]
        BUSY: _ClassVar[HubCommand.Answer]
        HUB_ERROR: _ClassVar[HubCommand.Answer]
        WRONG_STATE: _ClassVar[HubCommand.Answer]
        OBJECTS_LIMIT: _ClassVar[HubCommand.Answer]
        PARAMS_APPLICATION_FAILURE: _ClassVar[HubCommand.Answer]
        PARTITION_NOT_EMPTY: _ClassVar[HubCommand.Answer]
        OBJECT_NOT_FOUND: _ClassVar[HubCommand.Answer]
        HUB_BLOCKED_BY_SERVICE_PROVIDER: _ClassVar[HubCommand.Answer]
        NO_DATA: _ClassVar[HubCommand.Answer]
        ALARM_RESET_NEEDED: _ClassVar[HubCommand.Answer]
    SUCCESS: HubCommand.Answer
    DELIVERED: HubCommand.Answer
    DELIVERED_COMMAND_PERFORMED: HubCommand.Answer
    DELIVERED_COMMAND_NOT_PERFORMED: HubCommand.Answer
    MODE_FINISHED: HubCommand.Answer
    FAILED_INSUFFICIENT_ACCESS: HubCommand.Answer
    FAILED_UNKNOWN_COMMAND: HubCommand.Answer
    UNDELIVERED_RECEIVER_OFFLINE: HubCommand.Answer
    UNDELIVERED_WRONG_RECEIVER: HubCommand.Answer
    DELIVERED_WAS_ALREADY_PERFORMED: HubCommand.Answer
    FAILED_WRONG_PARAMETERS: HubCommand.Answer
    FAILED_WRONG_MESSAGE_TYPE: HubCommand.Answer
    TRANSPORT_EXCEPTION: HubCommand.Answer
    SERVER_ERROR: HubCommand.Answer
    REQUEST_DELIVERED: HubCommand.Answer
    BUSY: HubCommand.Answer
    HUB_ERROR: HubCommand.Answer
    WRONG_STATE: HubCommand.Answer
    OBJECTS_LIMIT: HubCommand.Answer
    PARAMS_APPLICATION_FAILURE: HubCommand.Answer
    PARTITION_NOT_EMPTY: HubCommand.Answer
    OBJECT_NOT_FOUND: HubCommand.Answer
    HUB_BLOCKED_BY_SERVICE_PROVIDER: HubCommand.Answer
    NO_DATA: HubCommand.Answer
    ALARM_RESET_NEEDED: HubCommand.Answer
    class NetworkSettingsStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_NETWORK_SETTINGS_STATUS_INFO: _ClassVar[HubCommand.NetworkSettingsStatus]
        NETWORK_SET_OK: _ClassVar[HubCommand.NetworkSettingsStatus]
        NETWORK_SET_ERROR: _ClassVar[HubCommand.NetworkSettingsStatus]
    NO_NETWORK_SETTINGS_STATUS_INFO: HubCommand.NetworkSettingsStatus
    NETWORK_SET_OK: HubCommand.NetworkSettingsStatus
    NETWORK_SET_ERROR: HubCommand.NetworkSettingsStatus
    class WifiNetworkJoinStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_WIFI_NETWORK_JOIN_STATUS_INO: _ClassVar[HubCommand.WifiNetworkJoinStatus]
        JOIN_SUCCESS: _ClassVar[HubCommand.WifiNetworkJoinStatus]
        JOIN_ERROR: _ClassVar[HubCommand.WifiNetworkJoinStatus]
    NO_WIFI_NETWORK_JOIN_STATUS_INO: HubCommand.WifiNetworkJoinStatus
    JOIN_SUCCESS: HubCommand.WifiNetworkJoinStatus
    JOIN_ERROR: HubCommand.WifiNetworkJoinStatus
    class Arming(_message.Message):
        __slots__ = ("type", "ignore_problems")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ARM: _ClassVar[HubCommand.Arming.Type]
            DISARM: _ClassVar[HubCommand.Arming.Type]
            NIGHT_MODE_ON: _ClassVar[HubCommand.Arming.Type]
            NIGHT_MODE_OFF: _ClassVar[HubCommand.Arming.Type]
        ARM: HubCommand.Arming.Type
        DISARM: HubCommand.Arming.Type
        NIGHT_MODE_ON: HubCommand.Arming.Type
        NIGHT_MODE_OFF: HubCommand.Arming.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        IGNORE_PROBLEMS_FIELD_NUMBER: _ClassVar[int]
        type: HubCommand.Arming.Type
        ignore_problems: bool
        def __init__(self, type: _Optional[_Union[HubCommand.Arming.Type, str]] = ..., ignore_problems: bool = ...) -> None: ...
    class Panic(_message.Message):
        __slots__ = ("panic_location",)
        class PanicLocation(_message.Message):
            __slots__ = ("latitude", "longitude", "accuracy", "speed", "timestamp")
            LATITUDE_FIELD_NUMBER: _ClassVar[int]
            LONGITUDE_FIELD_NUMBER: _ClassVar[int]
            ACCURACY_FIELD_NUMBER: _ClassVar[int]
            SPEED_FIELD_NUMBER: _ClassVar[int]
            TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
            latitude: float
            longitude: float
            accuracy: float
            speed: float
            timestamp: int
            def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., accuracy: _Optional[float] = ..., speed: _Optional[float] = ..., timestamp: _Optional[int] = ...) -> None: ...
        PANIC_LOCATION_FIELD_NUMBER: _ClassVar[int]
        panic_location: HubCommand.Panic.PanicLocation
        def __init__(self, panic_location: _Optional[_Union[HubCommand.Panic.PanicLocation, _Mapping]] = ...) -> None: ...
    class DropCache(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class CancelSearch(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class StartFirmwareUpdate(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class UpdateGroupsMode(_message.Message):
        __slots__ = ("groups_mode",)
        class GroupsMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            OFF: _ClassVar[HubCommand.UpdateGroupsMode.GroupsMode]
            ON: _ClassVar[HubCommand.UpdateGroupsMode.GroupsMode]
        OFF: HubCommand.UpdateGroupsMode.GroupsMode
        ON: HubCommand.UpdateGroupsMode.GroupsMode
        GROUPS_MODE_FIELD_NUMBER: _ClassVar[int]
        groups_mode: HubCommand.UpdateGroupsMode.GroupsMode
        def __init__(self, groups_mode: _Optional[_Union[HubCommand.UpdateGroupsMode.GroupsMode, str]] = ...) -> None: ...
    class ResetSimTrafficCounter(_message.Message):
        __slots__ = ("sim_card_index",)
        SIM_CARD_INDEX_FIELD_NUMBER: _ClassVar[int]
        sim_card_index: int
        def __init__(self, sim_card_index: _Optional[int] = ...) -> None: ...
    class MuteFireDetectors(_message.Message):
        __slots__ = ("mute_type",)
        class MuteType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ALL_FIRE_DETECTORS: _ClassVar[HubCommand.MuteFireDetectors.MuteType]
            ALL_FIRE_DETECTORS_EXCEPT_TRIGGERED: _ClassVar[HubCommand.MuteFireDetectors.MuteType]
        ALL_FIRE_DETECTORS: HubCommand.MuteFireDetectors.MuteType
        ALL_FIRE_DETECTORS_EXCEPT_TRIGGERED: HubCommand.MuteFireDetectors.MuteType
        MUTE_TYPE_FIELD_NUMBER: _ClassVar[int]
        mute_type: HubCommand.MuteFireDetectors.MuteType
        def __init__(self, mute_type: _Optional[_Union[HubCommand.MuteFireDetectors.MuteType, str]] = ...) -> None: ...
    class ResetAlarmCondition(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class DelayInterconnect(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class UpdateCardState(_message.Message):
        __slots__ = ("card_state", "card_id")
        class CardState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            OFF: _ClassVar[HubCommand.UpdateCardState.CardState]
            ON: _ClassVar[HubCommand.UpdateCardState.CardState]
        OFF: HubCommand.UpdateCardState.CardState
        ON: HubCommand.UpdateCardState.CardState
        CARD_STATE_FIELD_NUMBER: _ClassVar[int]
        CARD_ID_FIELD_NUMBER: _ClassVar[int]
        card_state: HubCommand.UpdateCardState.CardState
        card_id: str
        def __init__(self, card_state: _Optional[_Union[HubCommand.UpdateCardState.CardState, str]] = ..., card_id: _Optional[str] = ...) -> None: ...
    class GroupArming(_message.Message):
        __slots__ = ("group_id", "type", "ignore_problems")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ARM: _ClassVar[HubCommand.GroupArming.Type]
            DISARM: _ClassVar[HubCommand.GroupArming.Type]
        ARM: HubCommand.GroupArming.Type
        DISARM: HubCommand.GroupArming.Type
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        IGNORE_PROBLEMS_FIELD_NUMBER: _ClassVar[int]
        group_id: str
        type: HubCommand.GroupArming.Type
        ignore_problems: bool
        def __init__(self, group_id: _Optional[str] = ..., type: _Optional[_Union[HubCommand.GroupArming.Type, str]] = ..., ignore_problems: bool = ...) -> None: ...
    class DropLogs(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class InviteUsers(_message.Message):
        __slots__ = ("emails", "role")
        class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            USER: _ClassVar[HubCommand.InviteUsers.Role]
            PRO: _ClassVar[HubCommand.InviteUsers.Role]
        USER: HubCommand.InviteUsers.Role
        PRO: HubCommand.InviteUsers.Role
        EMAILS_FIELD_NUMBER: _ClassVar[int]
        ROLE_FIELD_NUMBER: _ClassVar[int]
        emails: _containers.RepeatedScalarFieldContainer[str]
        role: HubCommand.InviteUsers.Role
        def __init__(self, emails: _Optional[_Iterable[str]] = ..., role: _Optional[_Union[HubCommand.InviteUsers.Role, str]] = ...) -> None: ...
    class RevokeUserInvite(_message.Message):
        __slots__ = ("email",)
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        email: str
        def __init__(self, email: _Optional[str] = ...) -> None: ...
    class ProfiHubAccessRequest(_message.Message):
        __slots__ = ("user_id", "user_email", "user_name", "permissions", "time_of_access_in_hours")
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
        USER_NAME_FIELD_NUMBER: _ClassVar[int]
        PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        TIME_OF_ACCESS_IN_HOURS_FIELD_NUMBER: _ClassVar[int]
        user_id: str
        user_email: str
        user_name: str
        permissions: _containers.RepeatedScalarFieldContainer[_user_pb2.User.Permission]
        time_of_access_in_hours: int
        def __init__(self, user_id: _Optional[str] = ..., user_email: _Optional[str] = ..., user_name: _Optional[str] = ..., permissions: _Optional[_Iterable[_Union[_user_pb2.User.Permission, str]]] = ..., time_of_access_in_hours: _Optional[int] = ...) -> None: ...
    class DetachUser(_message.Message):
        __slots__ = ("user_id",)
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        user_id: str
        def __init__(self, user_id: _Optional[str] = ...) -> None: ...
    class CreateNewRoom(_message.Message):
        __slots__ = ("room_name",)
        ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
        room_name: str
        def __init__(self, room_name: _Optional[str] = ...) -> None: ...
    class DeleteRoom(_message.Message):
        __slots__ = ("room_id",)
        ROOM_ID_FIELD_NUMBER: _ClassVar[int]
        room_id: str
        def __init__(self, room_id: _Optional[str] = ...) -> None: ...
    class CreateNewGroup(_message.Message):
        __slots__ = ("group_name",)
        GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
        group_name: str
        def __init__(self, group_name: _Optional[str] = ...) -> None: ...
    class DeleteGroup(_message.Message):
        __slots__ = ("group_id",)
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        group_id: str
        def __init__(self, group_id: _Optional[str] = ...) -> None: ...
    class LinkCamera(_message.Message):
        __slots__ = ("room_id", "camera_name", "service_type", "stream_data_url", "dvr", "parent_camera_id")
        ROOM_ID_FIELD_NUMBER: _ClassVar[int]
        CAMERA_NAME_FIELD_NUMBER: _ClassVar[int]
        SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        STREAM_DATA_URL_FIELD_NUMBER: _ClassVar[int]
        DVR_FIELD_NUMBER: _ClassVar[int]
        PARENT_CAMERA_ID_FIELD_NUMBER: _ClassVar[int]
        room_id: str
        camera_name: str
        service_type: _camera_pb2.Camera.ServiceType
        stream_data_url: str
        dvr: bool
        parent_camera_id: str
        def __init__(self, room_id: _Optional[str] = ..., camera_name: _Optional[str] = ..., service_type: _Optional[_Union[_camera_pb2.Camera.ServiceType, str]] = ..., stream_data_url: _Optional[str] = ..., dvr: bool = ..., parent_camera_id: _Optional[str] = ...) -> None: ...
    class UnlinkCamera(_message.Message):
        __slots__ = ("camera_id", "service_id")
        CAMERA_ID_FIELD_NUMBER: _ClassVar[int]
        SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
        camera_id: str
        service_id: str
        def __init__(self, camera_id: _Optional[str] = ..., service_id: _Optional[str] = ...) -> None: ...
    class EditStreamData(_message.Message):
        __slots__ = ("service_id", "camera_id", "service_type", "stream_data_url", "hikvision_or_safire_settings", "dahua_or_uniview_settings")
        SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
        CAMERA_ID_FIELD_NUMBER: _ClassVar[int]
        SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        STREAM_DATA_URL_FIELD_NUMBER: _ClassVar[int]
        HIKVISION_OR_SAFIRE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        DAHUA_OR_UNIVIEW_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        service_id: str
        camera_id: str
        service_type: _camera_pb2.Camera.ServiceType
        stream_data_url: str
        hikvision_or_safire_settings: _camera_pb2.Camera.HikvisionOrSafireSettings
        dahua_or_uniview_settings: _camera_pb2.Camera.DahuaOrUniviewSettings
        def __init__(self, service_id: _Optional[str] = ..., camera_id: _Optional[str] = ..., service_type: _Optional[_Union[_camera_pb2.Camera.ServiceType, str]] = ..., stream_data_url: _Optional[str] = ..., hikvision_or_safire_settings: _Optional[_Union[_camera_pb2.Camera.HikvisionOrSafireSettings, _Mapping]] = ..., dahua_or_uniview_settings: _Optional[_Union[_camera_pb2.Camera.DahuaOrUniviewSettings, _Mapping]] = ...) -> None: ...
    class LinkDevice(_message.Message):
        __slots__ = ("room_id", "group_id", "device_qr_code", "wire_input_multi_transmitter_id", "device_name")
        ROOM_ID_FIELD_NUMBER: _ClassVar[int]
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        DEVICE_QR_CODE_FIELD_NUMBER: _ClassVar[int]
        WIRE_INPUT_MULTI_TRANSMITTER_ID_FIELD_NUMBER: _ClassVar[int]
        DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        room_id: str
        group_id: str
        device_qr_code: str
        wire_input_multi_transmitter_id: HubCommand.WireInputMultiTransmitterId
        device_name: str
        def __init__(self, room_id: _Optional[str] = ..., group_id: _Optional[str] = ..., device_qr_code: _Optional[str] = ..., wire_input_multi_transmitter_id: _Optional[_Union[HubCommand.WireInputMultiTransmitterId, _Mapping]] = ..., device_name: _Optional[str] = ...) -> None: ...
    class WireInputMultiTransmitterId(_message.Message):
        __slots__ = ("multi_transmitter_id", "wire_input_index")
        MULTI_TRANSMITTER_ID_FIELD_NUMBER: _ClassVar[int]
        WIRE_INPUT_INDEX_FIELD_NUMBER: _ClassVar[int]
        multi_transmitter_id: str
        wire_input_index: int
        def __init__(self, multi_transmitter_id: _Optional[str] = ..., wire_input_index: _Optional[int] = ...) -> None: ...
    class UnlinkDevice(_message.Message):
        __slots__ = ("device_id",)
        DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
        device_id: str
        def __init__(self, device_id: _Optional[str] = ...) -> None: ...
    class ScanFibraDevices(_message.Message):
        __slots__ = ("action",)
        class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NO_ACTION_INFO: _ClassVar[HubCommand.ScanFibraDevices.Action]
            START: _ClassVar[HubCommand.ScanFibraDevices.Action]
            STOP: _ClassVar[HubCommand.ScanFibraDevices.Action]
        NO_ACTION_INFO: HubCommand.ScanFibraDevices.Action
        START: HubCommand.ScanFibraDevices.Action
        STOP: HubCommand.ScanFibraDevices.Action
        ACTION_FIELD_NUMBER: _ClassVar[int]
        action: HubCommand.ScanFibraDevices.Action
        def __init__(self, action: _Optional[_Union[HubCommand.ScanFibraDevices.Action, str]] = ...) -> None: ...
    class GetScannedFibraDevices(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class CreateSecurityCompanyBinding(_message.Message):
        __slots__ = ("company_id",)
        COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
        company_id: str
        def __init__(self, company_id: _Optional[str] = ...) -> None: ...
    class DeleteSecurityCompanyBinding(_message.Message):
        __slots__ = ("company_id",)
        COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
        company_id: str
        def __init__(self, company_id: _Optional[str] = ...) -> None: ...
    class CancelDeleteSecurityCompanyBinding(_message.Message):
        __slots__ = ("company_id",)
        COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
        company_id: str
        def __init__(self, company_id: _Optional[str] = ...) -> None: ...
    class UpdateNetworkChannelState(_message.Message):
        __slots__ = ("channel", "state")
        class Channel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NO_CHANNEL_INFO: _ClassVar[HubCommand.UpdateNetworkChannelState.Channel]
            ETHERNET: _ClassVar[HubCommand.UpdateNetworkChannelState.Channel]
            GSM: _ClassVar[HubCommand.UpdateNetworkChannelState.Channel]
            WIFI: _ClassVar[HubCommand.UpdateNetworkChannelState.Channel]
        NO_CHANNEL_INFO: HubCommand.UpdateNetworkChannelState.Channel
        ETHERNET: HubCommand.UpdateNetworkChannelState.Channel
        GSM: HubCommand.UpdateNetworkChannelState.Channel
        WIFI: HubCommand.UpdateNetworkChannelState.Channel
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NO_STATE_INFO: _ClassVar[HubCommand.UpdateNetworkChannelState.State]
            ON: _ClassVar[HubCommand.UpdateNetworkChannelState.State]
            OFF: _ClassVar[HubCommand.UpdateNetworkChannelState.State]
        NO_STATE_INFO: HubCommand.UpdateNetworkChannelState.State
        ON: HubCommand.UpdateNetworkChannelState.State
        OFF: HubCommand.UpdateNetworkChannelState.State
        CHANNEL_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        channel: HubCommand.UpdateNetworkChannelState.Channel
        state: HubCommand.UpdateNetworkChannelState.State
        def __init__(self, channel: _Optional[_Union[HubCommand.UpdateNetworkChannelState.Channel, str]] = ..., state: _Optional[_Union[HubCommand.UpdateNetworkChannelState.State, str]] = ...) -> None: ...
    class UpdateEthernetSettings(_message.Message):
        __slots__ = ("dhcp", "ip", "mask", "gate", "dns")
        DHCP_FIELD_NUMBER: _ClassVar[int]
        IP_FIELD_NUMBER: _ClassVar[int]
        MASK_FIELD_NUMBER: _ClassVar[int]
        GATE_FIELD_NUMBER: _ClassVar[int]
        DNS_FIELD_NUMBER: _ClassVar[int]
        dhcp: bool
        ip: str
        mask: str
        gate: str
        dns: str
        def __init__(self, dhcp: bool = ..., ip: _Optional[str] = ..., mask: _Optional[str] = ..., gate: _Optional[str] = ..., dns: _Optional[str] = ...) -> None: ...
    class UpdateWifiSettings(_message.Message):
        __slots__ = ("dhcp", "ip", "mask", "gate", "dns")
        DHCP_FIELD_NUMBER: _ClassVar[int]
        IP_FIELD_NUMBER: _ClassVar[int]
        MASK_FIELD_NUMBER: _ClassVar[int]
        GATE_FIELD_NUMBER: _ClassVar[int]
        DNS_FIELD_NUMBER: _ClassVar[int]
        dhcp: bool
        ip: str
        mask: str
        gate: str
        dns: str
        def __init__(self, dhcp: bool = ..., ip: _Optional[str] = ..., mask: _Optional[str] = ..., gate: _Optional[str] = ..., dns: _Optional[str] = ...) -> None: ...
    class UpdateGsmSimCardSettings(_message.Message):
        __slots__ = ("apn", "username", "password", "sim_card_index")
        APN_FIELD_NUMBER: _ClassVar[int]
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        SIM_CARD_INDEX_FIELD_NUMBER: _ClassVar[int]
        apn: str
        username: str
        password: str
        sim_card_index: int
        def __init__(self, apn: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., sim_card_index: _Optional[int] = ...) -> None: ...
    class UpdateGsmSimCardBalanceNumber(_message.Message):
        __slots__ = ("balance_number", "sim_card_index")
        BALANCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        SIM_CARD_INDEX_FIELD_NUMBER: _ClassVar[int]
        balance_number: str
        sim_card_index: int
        def __init__(self, balance_number: _Optional[str] = ..., sim_card_index: _Optional[int] = ...) -> None: ...
    class GetGsmSimCardBalance(_message.Message):
        __slots__ = ("sim_card_index",)
        SIM_CARD_INDEX_FIELD_NUMBER: _ClassVar[int]
        sim_card_index: int
        def __init__(self, sim_card_index: _Optional[int] = ...) -> None: ...
    class ScanWifiNetworks(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class JoinWifiNetwork(_message.Message):
        __slots__ = ("ssid", "security_protocol", "password")
        SSID_FIELD_NUMBER: _ClassVar[int]
        SECURITY_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        ssid: str
        security_protocol: _hub_device_pb2.HubDevice.Wifi.SecurityProtocol
        password: str
        def __init__(self, ssid: _Optional[str] = ..., security_protocol: _Optional[_Union[_hub_device_pb2.HubDevice.Wifi.SecurityProtocol, str]] = ..., password: _Optional[str] = ...) -> None: ...
    class JoinWifiNetworkAdvanced(_message.Message):
        __slots__ = ("ssid", "security_protocol", "password", "dhcp", "channel", "ip", "gate", "dns", "mask")
        SSID_FIELD_NUMBER: _ClassVar[int]
        SECURITY_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        DHCP_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_FIELD_NUMBER: _ClassVar[int]
        IP_FIELD_NUMBER: _ClassVar[int]
        GATE_FIELD_NUMBER: _ClassVar[int]
        DNS_FIELD_NUMBER: _ClassVar[int]
        MASK_FIELD_NUMBER: _ClassVar[int]
        ssid: str
        security_protocol: _hub_device_pb2.HubDevice.Wifi.SecurityProtocol
        password: str
        dhcp: bool
        channel: int
        ip: str
        gate: str
        dns: str
        mask: str
        def __init__(self, ssid: _Optional[str] = ..., security_protocol: _Optional[_Union[_hub_device_pb2.HubDevice.Wifi.SecurityProtocol, str]] = ..., password: _Optional[str] = ..., dhcp: bool = ..., channel: _Optional[int] = ..., ip: _Optional[str] = ..., gate: _Optional[str] = ..., dns: _Optional[str] = ..., mask: _Optional[str] = ...) -> None: ...
    class ForgetWifiNetwork(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class ApplyUpdate(_message.Message):
        __slots__ = ("update",)
        UPDATE_FIELD_NUMBER: _ClassVar[int]
        update: _update_pb2.Update
        def __init__(self, update: _Optional[_Union[_update_pb2.Update, _Mapping]] = ...) -> None: ...
    class ApplyUpdates(_message.Message):
        __slots__ = ("updates",)
        UPDATES_FIELD_NUMBER: _ClassVar[int]
        updates: _containers.RepeatedCompositeFieldContainer[_update_pb2.Update]
        def __init__(self, updates: _Optional[_Iterable[_Union[_update_pb2.Update, _Mapping]]] = ...) -> None: ...
    class Result(_message.Message):
        __slots__ = ("answer", "network_settings_status", "wifi_network_join_status", "arming_error_details", "invite_users_response_details", "link_device_response_details", "gsm_sim_card_balance_response_details", "scan_wifi_networks_response_details", "migration_error_details", "create_unit_response_details", "register_access_key_error_details", "engineer_attendance_required_error_details", "scanned_fibra_devices_details")
        class ArmingErrorDetails(_message.Message):
            __slots__ = ("arm_prevent_objects",)
            class ArmPreventObject(_message.Message):
                __slots__ = ("code", "source_id", "source_type", "source_name", "source_room", "source_room_id", "text", "hub_name")
                CODE_FIELD_NUMBER: _ClassVar[int]
                SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
                SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
                SOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
                SOURCE_ROOM_FIELD_NUMBER: _ClassVar[int]
                SOURCE_ROOM_ID_FIELD_NUMBER: _ClassVar[int]
                TEXT_FIELD_NUMBER: _ClassVar[int]
                HUB_NAME_FIELD_NUMBER: _ClassVar[int]
                code: str
                source_id: str
                source_type: _object_type_pb2.ObjectType
                source_name: str
                source_room: str
                source_room_id: str
                text: str
                hub_name: str
                def __init__(self, code: _Optional[str] = ..., source_id: _Optional[str] = ..., source_type: _Optional[_Union[_object_type_pb2.ObjectType, str]] = ..., source_name: _Optional[str] = ..., source_room: _Optional[str] = ..., source_room_id: _Optional[str] = ..., text: _Optional[str] = ..., hub_name: _Optional[str] = ...) -> None: ...
            ARM_PREVENT_OBJECTS_FIELD_NUMBER: _ClassVar[int]
            arm_prevent_objects: _containers.RepeatedCompositeFieldContainer[HubCommand.Result.ArmingErrorDetails.ArmPreventObject]
            def __init__(self, arm_prevent_objects: _Optional[_Iterable[_Union[HubCommand.Result.ArmingErrorDetails.ArmPreventObject, _Mapping]]] = ...) -> None: ...
        class MigrationErrorDetails(_message.Message):
            __slots__ = ("errors",)
            class MigrationError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                UNKNOWN_ERROR: _ClassVar[HubCommand.Result.MigrationErrorDetails.MigrationError]
                NO_RIGHTS_ON_TARGET: _ClassVar[HubCommand.Result.MigrationErrorDetails.MigrationError]
                NO_RIGHTS_ON_DONOR: _ClassVar[HubCommand.Result.MigrationErrorDetails.MigrationError]
                TARGET_ARMED: _ClassVar[HubCommand.Result.MigrationErrorDetails.MigrationError]
                TARGET_OFFLINE: _ClassVar[HubCommand.Result.MigrationErrorDetails.MigrationError]
                DONOR_ONLINE: _ClassVar[HubCommand.Result.MigrationErrorDetails.MigrationError]
                TARGET_FW_LOWER_MINIMAL: _ClassVar[HubCommand.Result.MigrationErrorDetails.MigrationError]
                DONOR_FW_LOWER_MINIMAL: _ClassVar[HubCommand.Result.MigrationErrorDetails.MigrationError]
                TARGET_FW_LOWER_DONOR: _ClassVar[HubCommand.Result.MigrationErrorDetails.MigrationError]
                TARGET_STATE_FETCH_FAILED: _ClassVar[HubCommand.Result.MigrationErrorDetails.MigrationError]
                DONOR_STATE_FETCH_FAILED: _ClassVar[HubCommand.Result.MigrationErrorDetails.MigrationError]
                DONOR_TARGET_INCOMPATIBLE_TYPES: _ClassVar[HubCommand.Result.MigrationErrorDetails.MigrationError]
                TARGET_IS_ALREADY_IN_MIGRATION: _ClassVar[HubCommand.Result.MigrationErrorDetails.MigrationError]
                DONOR_IS_ALREADY_IN_MIGRATION: _ClassVar[HubCommand.Result.MigrationErrorDetails.MigrationError]
            UNKNOWN_ERROR: HubCommand.Result.MigrationErrorDetails.MigrationError
            NO_RIGHTS_ON_TARGET: HubCommand.Result.MigrationErrorDetails.MigrationError
            NO_RIGHTS_ON_DONOR: HubCommand.Result.MigrationErrorDetails.MigrationError
            TARGET_ARMED: HubCommand.Result.MigrationErrorDetails.MigrationError
            TARGET_OFFLINE: HubCommand.Result.MigrationErrorDetails.MigrationError
            DONOR_ONLINE: HubCommand.Result.MigrationErrorDetails.MigrationError
            TARGET_FW_LOWER_MINIMAL: HubCommand.Result.MigrationErrorDetails.MigrationError
            DONOR_FW_LOWER_MINIMAL: HubCommand.Result.MigrationErrorDetails.MigrationError
            TARGET_FW_LOWER_DONOR: HubCommand.Result.MigrationErrorDetails.MigrationError
            TARGET_STATE_FETCH_FAILED: HubCommand.Result.MigrationErrorDetails.MigrationError
            DONOR_STATE_FETCH_FAILED: HubCommand.Result.MigrationErrorDetails.MigrationError
            DONOR_TARGET_INCOMPATIBLE_TYPES: HubCommand.Result.MigrationErrorDetails.MigrationError
            TARGET_IS_ALREADY_IN_MIGRATION: HubCommand.Result.MigrationErrorDetails.MigrationError
            DONOR_IS_ALREADY_IN_MIGRATION: HubCommand.Result.MigrationErrorDetails.MigrationError
            ERRORS_FIELD_NUMBER: _ClassVar[int]
            errors: _containers.RepeatedScalarFieldContainer[HubCommand.Result.MigrationErrorDetails.MigrationError]
            def __init__(self, errors: _Optional[_Iterable[_Union[HubCommand.Result.MigrationErrorDetails.MigrationError, str]]] = ...) -> None: ...
        class InviteUsersResponseDetails(_message.Message):
            __slots__ = ("invite_statuses",)
            class InviteStatus(_message.Message):
                __slots__ = ("email", "status")
                class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    NO_INVITE_STATUS_INFO: _ClassVar[HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status]
                    USER_BOUND: _ClassVar[HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status]
                    USER_INVITED: _ClassVar[HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status]
                    INVALID_OR_NON_EXISTING_USER_EMAIL: _ClassVar[HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status]
                    OBJECTS_LIMIT_EXCEEDED: _ClassVar[HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status]
                    INVALID_OR_NON_EXISTING_PRO_EMAIL: _ClassVar[HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status]
                    ALREADY_BOUND: _ClassVar[HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status]
                NO_INVITE_STATUS_INFO: HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status
                USER_BOUND: HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status
                USER_INVITED: HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status
                INVALID_OR_NON_EXISTING_USER_EMAIL: HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status
                OBJECTS_LIMIT_EXCEEDED: HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status
                INVALID_OR_NON_EXISTING_PRO_EMAIL: HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status
                ALREADY_BOUND: HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status
                EMAIL_FIELD_NUMBER: _ClassVar[int]
                STATUS_FIELD_NUMBER: _ClassVar[int]
                email: str
                status: HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status
                def __init__(self, email: _Optional[str] = ..., status: _Optional[_Union[HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status, str]] = ...) -> None: ...
            INVITE_STATUSES_FIELD_NUMBER: _ClassVar[int]
            invite_statuses: _containers.RepeatedCompositeFieldContainer[HubCommand.Result.InviteUsersResponseDetails.InviteStatus]
            def __init__(self, invite_statuses: _Optional[_Iterable[_Union[HubCommand.Result.InviteUsersResponseDetails.InviteStatus, _Mapping]]] = ...) -> None: ...
        class LinkDeviceResponseDetails(_message.Message):
            __slots__ = ("status", "fail_device_type", "fail_reason")
            class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                NO_STATUS_INFO: _ClassVar[HubCommand.Result.LinkDeviceResponseDetails.Status]
                SUCCESS: _ClassVar[HubCommand.Result.LinkDeviceResponseDetails.Status]
                SEARCH_TIMEOUT: _ClassVar[HubCommand.Result.LinkDeviceResponseDetails.Status]
                REGISTRATION_FAILED: _ClassVar[HubCommand.Result.LinkDeviceResponseDetails.Status]
                REGISTRATION_STEP: _ClassVar[HubCommand.Result.LinkDeviceResponseDetails.Status]
            NO_STATUS_INFO: HubCommand.Result.LinkDeviceResponseDetails.Status
            SUCCESS: HubCommand.Result.LinkDeviceResponseDetails.Status
            SEARCH_TIMEOUT: HubCommand.Result.LinkDeviceResponseDetails.Status
            REGISTRATION_FAILED: HubCommand.Result.LinkDeviceResponseDetails.Status
            REGISTRATION_STEP: HubCommand.Result.LinkDeviceResponseDetails.Status
            STATUS_FIELD_NUMBER: _ClassVar[int]
            FAIL_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
            FAIL_REASON_FIELD_NUMBER: _ClassVar[int]
            status: HubCommand.Result.LinkDeviceResponseDetails.Status
            fail_device_type: str
            fail_reason: int
            def __init__(self, status: _Optional[_Union[HubCommand.Result.LinkDeviceResponseDetails.Status, str]] = ..., fail_device_type: _Optional[str] = ..., fail_reason: _Optional[int] = ...) -> None: ...
        class GsmSimCardBalanceResponseDetails(_message.Message):
            __slots__ = ("balance",)
            BALANCE_FIELD_NUMBER: _ClassVar[int]
            balance: str
            def __init__(self, balance: _Optional[str] = ...) -> None: ...
        class ScanWifiNetworksResponseDetails(_message.Message):
            __slots__ = ("available_networks",)
            class WifiNetwork(_message.Message):
                __slots__ = ("ssid", "security_protocol", "signal_level")
                SSID_FIELD_NUMBER: _ClassVar[int]
                SECURITY_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
                SIGNAL_LEVEL_FIELD_NUMBER: _ClassVar[int]
                ssid: str
                security_protocol: _hub_device_pb2.HubDevice.Wifi.SecurityProtocol
                signal_level: _hub_device_pb2.HubDevice.Wifi.SignalLevel
                def __init__(self, ssid: _Optional[str] = ..., security_protocol: _Optional[_Union[_hub_device_pb2.HubDevice.Wifi.SecurityProtocol, str]] = ..., signal_level: _Optional[_Union[_hub_device_pb2.HubDevice.Wifi.SignalLevel, str]] = ...) -> None: ...
            AVAILABLE_NETWORKS_FIELD_NUMBER: _ClassVar[int]
            available_networks: _containers.RepeatedCompositeFieldContainer[HubCommand.Result.ScanWifiNetworksResponseDetails.WifiNetwork]
            def __init__(self, available_networks: _Optional[_Iterable[_Union[HubCommand.Result.ScanWifiNetworksResponseDetails.WifiNetwork, _Mapping]]] = ...) -> None: ...
        class CreateUnitResponseDetails(_message.Message):
            __slots__ = ("room_id", "group_id")
            ROOM_ID_FIELD_NUMBER: _ClassVar[int]
            GROUP_ID_FIELD_NUMBER: _ClassVar[int]
            room_id: str
            group_id: str
            def __init__(self, room_id: _Optional[str] = ..., group_id: _Optional[str] = ...) -> None: ...
        class RegisterAccessKeyErrorDetails(_message.Message):
            __slots__ = ("fail_reason",)
            class FailReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                NO_FAIL_REASON_INFO: _ClassVar[HubCommand.Result.RegisterAccessKeyErrorDetails.FailReason]
                KEY_ALREADY_IN_USE: _ClassVar[HubCommand.Result.RegisterAccessKeyErrorDetails.FailReason]
                NO_AVAILABLE_READERS: _ClassVar[HubCommand.Result.RegisterAccessKeyErrorDetails.FailReason]
                USER_NOT_FOUND: _ClassVar[HubCommand.Result.RegisterAccessKeyErrorDetails.FailReason]
            NO_FAIL_REASON_INFO: HubCommand.Result.RegisterAccessKeyErrorDetails.FailReason
            KEY_ALREADY_IN_USE: HubCommand.Result.RegisterAccessKeyErrorDetails.FailReason
            NO_AVAILABLE_READERS: HubCommand.Result.RegisterAccessKeyErrorDetails.FailReason
            USER_NOT_FOUND: HubCommand.Result.RegisterAccessKeyErrorDetails.FailReason
            FAIL_REASON_FIELD_NUMBER: _ClassVar[int]
            fail_reason: HubCommand.Result.RegisterAccessKeyErrorDetails.FailReason
            def __init__(self, fail_reason: _Optional[_Union[HubCommand.Result.RegisterAccessKeyErrorDetails.FailReason, str]] = ...) -> None: ...
        class EngineerAttendanceRequiredErrorDetails(_message.Message):
            __slots__ = ("fail_reason",)
            class FailReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                NO_FAIL_REASON_INFO: _ClassVar[HubCommand.Result.EngineerAttendanceRequiredErrorDetails.FailReason]
                WRONG_OR_INACTIVE_REQUEST_ID: _ClassVar[HubCommand.Result.EngineerAttendanceRequiredErrorDetails.FailReason]
            NO_FAIL_REASON_INFO: HubCommand.Result.EngineerAttendanceRequiredErrorDetails.FailReason
            WRONG_OR_INACTIVE_REQUEST_ID: HubCommand.Result.EngineerAttendanceRequiredErrorDetails.FailReason
            FAIL_REASON_FIELD_NUMBER: _ClassVar[int]
            fail_reason: HubCommand.Result.EngineerAttendanceRequiredErrorDetails.FailReason
            def __init__(self, fail_reason: _Optional[_Union[HubCommand.Result.EngineerAttendanceRequiredErrorDetails.FailReason, str]] = ...) -> None: ...
        class ScannedFibraDevicesDetails(_message.Message):
            __slots__ = ("devices",)
            DEVICES_FIELD_NUMBER: _ClassVar[int]
            devices: _containers.RepeatedCompositeFieldContainer[_device_pb2.Device]
            def __init__(self, devices: _Optional[_Iterable[_Union[_device_pb2.Device, _Mapping]]] = ...) -> None: ...
        ANSWER_FIELD_NUMBER: _ClassVar[int]
        NETWORK_SETTINGS_STATUS_FIELD_NUMBER: _ClassVar[int]
        WIFI_NETWORK_JOIN_STATUS_FIELD_NUMBER: _ClassVar[int]
        ARMING_ERROR_DETAILS_FIELD_NUMBER: _ClassVar[int]
        INVITE_USERS_RESPONSE_DETAILS_FIELD_NUMBER: _ClassVar[int]
        LINK_DEVICE_RESPONSE_DETAILS_FIELD_NUMBER: _ClassVar[int]
        GSM_SIM_CARD_BALANCE_RESPONSE_DETAILS_FIELD_NUMBER: _ClassVar[int]
        SCAN_WIFI_NETWORKS_RESPONSE_DETAILS_FIELD_NUMBER: _ClassVar[int]
        MIGRATION_ERROR_DETAILS_FIELD_NUMBER: _ClassVar[int]
        CREATE_UNIT_RESPONSE_DETAILS_FIELD_NUMBER: _ClassVar[int]
        REGISTER_ACCESS_KEY_ERROR_DETAILS_FIELD_NUMBER: _ClassVar[int]
        ENGINEER_ATTENDANCE_REQUIRED_ERROR_DETAILS_FIELD_NUMBER: _ClassVar[int]
        SCANNED_FIBRA_DEVICES_DETAILS_FIELD_NUMBER: _ClassVar[int]
        answer: HubCommand.Answer
        network_settings_status: HubCommand.NetworkSettingsStatus
        wifi_network_join_status: HubCommand.WifiNetworkJoinStatus
        arming_error_details: HubCommand.Result.ArmingErrorDetails
        invite_users_response_details: HubCommand.Result.InviteUsersResponseDetails
        link_device_response_details: HubCommand.Result.LinkDeviceResponseDetails
        gsm_sim_card_balance_response_details: HubCommand.Result.GsmSimCardBalanceResponseDetails
        scan_wifi_networks_response_details: HubCommand.Result.ScanWifiNetworksResponseDetails
        migration_error_details: HubCommand.Result.MigrationErrorDetails
        create_unit_response_details: HubCommand.Result.CreateUnitResponseDetails
        register_access_key_error_details: HubCommand.Result.RegisterAccessKeyErrorDetails
        engineer_attendance_required_error_details: HubCommand.Result.EngineerAttendanceRequiredErrorDetails
        scanned_fibra_devices_details: HubCommand.Result.ScannedFibraDevicesDetails
        def __init__(self, answer: _Optional[_Union[HubCommand.Answer, str]] = ..., network_settings_status: _Optional[_Union[HubCommand.NetworkSettingsStatus, str]] = ..., wifi_network_join_status: _Optional[_Union[HubCommand.WifiNetworkJoinStatus, str]] = ..., arming_error_details: _Optional[_Union[HubCommand.Result.ArmingErrorDetails, _Mapping]] = ..., invite_users_response_details: _Optional[_Union[HubCommand.Result.InviteUsersResponseDetails, _Mapping]] = ..., link_device_response_details: _Optional[_Union[HubCommand.Result.LinkDeviceResponseDetails, _Mapping]] = ..., gsm_sim_card_balance_response_details: _Optional[_Union[HubCommand.Result.GsmSimCardBalanceResponseDetails, _Mapping]] = ..., scan_wifi_networks_response_details: _Optional[_Union[HubCommand.Result.ScanWifiNetworksResponseDetails, _Mapping]] = ..., migration_error_details: _Optional[_Union[HubCommand.Result.MigrationErrorDetails, _Mapping]] = ..., create_unit_response_details: _Optional[_Union[HubCommand.Result.CreateUnitResponseDetails, _Mapping]] = ..., register_access_key_error_details: _Optional[_Union[HubCommand.Result.RegisterAccessKeyErrorDetails, _Mapping]] = ..., engineer_attendance_required_error_details: _Optional[_Union[HubCommand.Result.EngineerAttendanceRequiredErrorDetails, _Mapping]] = ..., scanned_fibra_devices_details: _Optional[_Union[HubCommand.Result.ScannedFibraDevicesDetails, _Mapping]] = ...) -> None: ...
    class CreateScenario(_message.Message):
        __slots__ = ("scenario", "field_mask")
        SCENARIO_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        scenario: _scenario_pb2.Scenario
        field_mask: _field_mask_pb2.FieldMask
        def __init__(self, scenario: _Optional[_Union[_scenario_pb2.Scenario, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...
    class UpdateScenario(_message.Message):
        __slots__ = ("scenario", "field_mask")
        SCENARIO_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        scenario: _scenario_pb2.Scenario
        field_mask: _field_mask_pb2.FieldMask
        def __init__(self, scenario: _Optional[_Union[_scenario_pb2.Scenario, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...
    class DeleteScenario(_message.Message):
        __slots__ = ("id", "field_mask")
        ID_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        id: str
        field_mask: _field_mask_pb2.FieldMask
        def __init__(self, id: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...
    class StartMigration(_message.Message):
        __slots__ = ("donor_id",)
        DONOR_ID_FIELD_NUMBER: _ClassVar[int]
        donor_id: str
        def __init__(self, donor_id: _Optional[str] = ...) -> None: ...
    class StopMigration(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class RequestArmingReset(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class EngineerAttendanceRequired(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class AddAccessCard(_message.Message):
        __slots__ = ("name", "color", "type", "user_id")
        class Color(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            WHITE: _ClassVar[HubCommand.AddAccessCard.Color]
            BLACK: _ClassVar[HubCommand.AddAccessCard.Color]
        WHITE: HubCommand.AddAccessCard.Color
        BLACK: HubCommand.AddAccessCard.Color
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CARD: _ClassVar[HubCommand.AddAccessCard.Type]
            TAG: _ClassVar[HubCommand.AddAccessCard.Type]
        CARD: HubCommand.AddAccessCard.Type
        TAG: HubCommand.AddAccessCard.Type
        NAME_FIELD_NUMBER: _ClassVar[int]
        COLOR_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        name: str
        color: HubCommand.AddAccessCard.Color
        type: HubCommand.AddAccessCard.Type
        user_id: str
        def __init__(self, name: _Optional[str] = ..., color: _Optional[_Union[HubCommand.AddAccessCard.Color, str]] = ..., type: _Optional[_Union[HubCommand.AddAccessCard.Type, str]] = ..., user_id: _Optional[str] = ...) -> None: ...
    class DeleteAccessCard(_message.Message):
        __slots__ = ("id", "delete_mode")
        class DeleteMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            WITHOUT_CARD: _ClassVar[HubCommand.DeleteAccessCard.DeleteMode]
            WITH_CARD: _ClassVar[HubCommand.DeleteAccessCard.DeleteMode]
        WITHOUT_CARD: HubCommand.DeleteAccessCard.DeleteMode
        WITH_CARD: HubCommand.DeleteAccessCard.DeleteMode
        ID_FIELD_NUMBER: _ClassVar[int]
        DELETE_MODE_FIELD_NUMBER: _ClassVar[int]
        id: str
        delete_mode: HubCommand.DeleteAccessCard.DeleteMode
        def __init__(self, id: _Optional[str] = ..., delete_mode: _Optional[_Union[HubCommand.DeleteAccessCard.DeleteMode, str]] = ...) -> None: ...
    class EraseAccessCard(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class ExitCardMode(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class CancelAccessKeySearch(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class RegisterAccessKey(_message.Message):
        __slots__ = ("key_name",)
        KEY_NAME_FIELD_NUMBER: _ClassVar[int]
        key_name: str
        def __init__(self, key_name: _Optional[str] = ...) -> None: ...
    class DeleteAccessKey(_message.Message):
        __slots__ = ("key_id",)
        KEY_ID_FIELD_NUMBER: _ClassVar[int]
        key_id: str
        def __init__(self, key_id: _Optional[str] = ...) -> None: ...
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    ARMING_FIELD_NUMBER: _ClassVar[int]
    PANIC_FIELD_NUMBER: _ClassVar[int]
    DROP_CACHE_FIELD_NUMBER: _ClassVar[int]
    CANCEL_SEARCH_FIELD_NUMBER: _ClassVar[int]
    START_FIRMWARE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_GROUPS_MODE_FIELD_NUMBER: _ClassVar[int]
    RESET_SIM_TRAFFIC_COUNTER_FIELD_NUMBER: _ClassVar[int]
    MUTE_FIRE_DETECTORS_FIELD_NUMBER: _ClassVar[int]
    RESET_ALARM_CONDITION_FIELD_NUMBER: _ClassVar[int]
    DELAY_INTERCONNECT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_CARD_STATE_FIELD_NUMBER: _ClassVar[int]
    GROUP_ARMING_FIELD_NUMBER: _ClassVar[int]
    DROP_LOGS_FIELD_NUMBER: _ClassVar[int]
    INVITE_USERS_FIELD_NUMBER: _ClassVar[int]
    REVOKE_USER_INVITE_FIELD_NUMBER: _ClassVar[int]
    PROFI_HUB_ACCESS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DETACH_USER_FIELD_NUMBER: _ClassVar[int]
    CHANGE_USER_ROLE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_USER_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ARMING_RESET_FIELD_NUMBER: _ClassVar[int]
    ENGINEER_ATTENDANCE_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    CREATE_NEW_ROOM_FIELD_NUMBER: _ClassVar[int]
    DELETE_ROOM_FIELD_NUMBER: _ClassVar[int]
    CREATE_NEW_GROUP_FIELD_NUMBER: _ClassVar[int]
    DELETE_GROUP_FIELD_NUMBER: _ClassVar[int]
    LINK_CAMERA_FIELD_NUMBER: _ClassVar[int]
    UNLINK_CAMERA_FIELD_NUMBER: _ClassVar[int]
    EDIT_STREAM_DATA_FIELD_NUMBER: _ClassVar[int]
    LINK_DEVICE_FIELD_NUMBER: _ClassVar[int]
    UNLINK_DEVICE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_COMMAND_FIELD_NUMBER: _ClassVar[int]
    SCAN_FIBRA_DEVICES_FIELD_NUMBER: _ClassVar[int]
    GET_SCANNED_FIBRA_DEVICES_FIELD_NUMBER: _ClassVar[int]
    CREATE_SECURITY_COMPANY_BINDING_FIELD_NUMBER: _ClassVar[int]
    DELETE_SECURITY_COMPANY_BINDING_FIELD_NUMBER: _ClassVar[int]
    CANCEL_DELETE_SECURITY_COMPANY_BINDING_FIELD_NUMBER: _ClassVar[int]
    UPDATE_NETWORK_CHANNEL_STATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_ETHERNET_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_WIFI_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_GSM_SIM_CARD_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_GSM_SIM_CARD_BALANCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    GET_GSM_SIM_CARD_BALANCE_FIELD_NUMBER: _ClassVar[int]
    SCAN_WIFI_NETWORKS_FIELD_NUMBER: _ClassVar[int]
    JOIN_WIFI_NETWORK_FIELD_NUMBER: _ClassVar[int]
    JOIN_WIFI_NETWORK_ADVANCED_FIELD_NUMBER: _ClassVar[int]
    FORGET_WIFI_NETWORK_FIELD_NUMBER: _ClassVar[int]
    APPLY_UPDATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_SCENARIO_FIELD_NUMBER: _ClassVar[int]
    UPDATE_SCENARIO_FIELD_NUMBER: _ClassVar[int]
    DELETE_SCENARIO_FIELD_NUMBER: _ClassVar[int]
    APPLY_UPDATES_FIELD_NUMBER: _ClassVar[int]
    START_MIGRATION_FIELD_NUMBER: _ClassVar[int]
    STOP_MIGRATION_FIELD_NUMBER: _ClassVar[int]
    ADD_ACCESS_CARD_FIELD_NUMBER: _ClassVar[int]
    DELETE_ACCESS_CARD_FIELD_NUMBER: _ClassVar[int]
    ERASE_ACCESS_CARD_FIELD_NUMBER: _ClassVar[int]
    EXIT_CARD_MODE_FIELD_NUMBER: _ClassVar[int]
    CANCEL_ACCESS_KEY_SEARCH_FIELD_NUMBER: _ClassVar[int]
    REGISTER_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    DELETE_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    arming: HubCommand.Arming
    panic: HubCommand.Panic
    drop_cache: HubCommand.DropCache
    cancel_search: HubCommand.CancelSearch
    start_firmware_update: HubCommand.StartFirmwareUpdate
    update_groups_mode: HubCommand.UpdateGroupsMode
    reset_sim_traffic_counter: HubCommand.ResetSimTrafficCounter
    mute_fire_detectors: HubCommand.MuteFireDetectors
    reset_alarm_condition: HubCommand.ResetAlarmCondition
    delay_interconnect: HubCommand.DelayInterconnect
    update_card_state: HubCommand.UpdateCardState
    group_arming: HubCommand.GroupArming
    drop_logs: HubCommand.DropLogs
    invite_users: HubCommand.InviteUsers
    revoke_user_invite: HubCommand.RevokeUserInvite
    profi_hub_access_request: HubCommand.ProfiHubAccessRequest
    detach_user: HubCommand.DetachUser
    change_user_role: ChangeUserRole
    change_user_permissions: ChangeUserPermissions
    request_arming_reset: HubCommand.RequestArmingReset
    engineer_attendance_required: HubCommand.EngineerAttendanceRequired
    create_new_room: HubCommand.CreateNewRoom
    delete_room: HubCommand.DeleteRoom
    create_new_group: HubCommand.CreateNewGroup
    delete_group: HubCommand.DeleteGroup
    link_camera: HubCommand.LinkCamera
    unlink_camera: HubCommand.UnlinkCamera
    edit_stream_data: HubCommand.EditStreamData
    link_device: HubCommand.LinkDevice
    unlink_device: HubCommand.UnlinkDevice
    device_command: DeviceCommand
    scan_fibra_devices: HubCommand.ScanFibraDevices
    get_scanned_fibra_devices: HubCommand.GetScannedFibraDevices
    create_security_company_binding: HubCommand.CreateSecurityCompanyBinding
    delete_security_company_binding: HubCommand.DeleteSecurityCompanyBinding
    cancel_delete_security_company_binding: HubCommand.CancelDeleteSecurityCompanyBinding
    update_network_channel_state: HubCommand.UpdateNetworkChannelState
    update_ethernet_settings: HubCommand.UpdateEthernetSettings
    update_wifi_settings: HubCommand.UpdateWifiSettings
    update_gsm_sim_card_settings: HubCommand.UpdateGsmSimCardSettings
    update_gsm_sim_card_balance_number: HubCommand.UpdateGsmSimCardBalanceNumber
    get_gsm_sim_card_balance: HubCommand.GetGsmSimCardBalance
    scan_wifi_networks: HubCommand.ScanWifiNetworks
    join_wifi_network: HubCommand.JoinWifiNetwork
    join_wifi_network_advanced: HubCommand.JoinWifiNetworkAdvanced
    forget_wifi_network: HubCommand.ForgetWifiNetwork
    apply_update: HubCommand.ApplyUpdate
    create_scenario: HubCommand.CreateScenario
    update_scenario: HubCommand.UpdateScenario
    delete_scenario: HubCommand.DeleteScenario
    apply_updates: HubCommand.ApplyUpdates
    start_migration: HubCommand.StartMigration
    stop_migration: HubCommand.StopMigration
    add_access_card: HubCommand.AddAccessCard
    delete_access_card: HubCommand.DeleteAccessCard
    erase_access_card: HubCommand.EraseAccessCard
    exit_card_mode: HubCommand.ExitCardMode
    cancel_access_key_search: HubCommand.CancelAccessKeySearch
    register_access_key: HubCommand.RegisterAccessKey
    delete_access_key: HubCommand.DeleteAccessKey
    def __init__(self, hub_id: _Optional[str] = ..., arming: _Optional[_Union[HubCommand.Arming, _Mapping]] = ..., panic: _Optional[_Union[HubCommand.Panic, _Mapping]] = ..., drop_cache: _Optional[_Union[HubCommand.DropCache, _Mapping]] = ..., cancel_search: _Optional[_Union[HubCommand.CancelSearch, _Mapping]] = ..., start_firmware_update: _Optional[_Union[HubCommand.StartFirmwareUpdate, _Mapping]] = ..., update_groups_mode: _Optional[_Union[HubCommand.UpdateGroupsMode, _Mapping]] = ..., reset_sim_traffic_counter: _Optional[_Union[HubCommand.ResetSimTrafficCounter, _Mapping]] = ..., mute_fire_detectors: _Optional[_Union[HubCommand.MuteFireDetectors, _Mapping]] = ..., reset_alarm_condition: _Optional[_Union[HubCommand.ResetAlarmCondition, _Mapping]] = ..., delay_interconnect: _Optional[_Union[HubCommand.DelayInterconnect, _Mapping]] = ..., update_card_state: _Optional[_Union[HubCommand.UpdateCardState, _Mapping]] = ..., group_arming: _Optional[_Union[HubCommand.GroupArming, _Mapping]] = ..., drop_logs: _Optional[_Union[HubCommand.DropLogs, _Mapping]] = ..., invite_users: _Optional[_Union[HubCommand.InviteUsers, _Mapping]] = ..., revoke_user_invite: _Optional[_Union[HubCommand.RevokeUserInvite, _Mapping]] = ..., profi_hub_access_request: _Optional[_Union[HubCommand.ProfiHubAccessRequest, _Mapping]] = ..., detach_user: _Optional[_Union[HubCommand.DetachUser, _Mapping]] = ..., change_user_role: _Optional[_Union[ChangeUserRole, _Mapping]] = ..., change_user_permissions: _Optional[_Union[ChangeUserPermissions, _Mapping]] = ..., request_arming_reset: _Optional[_Union[HubCommand.RequestArmingReset, _Mapping]] = ..., engineer_attendance_required: _Optional[_Union[HubCommand.EngineerAttendanceRequired, _Mapping]] = ..., create_new_room: _Optional[_Union[HubCommand.CreateNewRoom, _Mapping]] = ..., delete_room: _Optional[_Union[HubCommand.DeleteRoom, _Mapping]] = ..., create_new_group: _Optional[_Union[HubCommand.CreateNewGroup, _Mapping]] = ..., delete_group: _Optional[_Union[HubCommand.DeleteGroup, _Mapping]] = ..., link_camera: _Optional[_Union[HubCommand.LinkCamera, _Mapping]] = ..., unlink_camera: _Optional[_Union[HubCommand.UnlinkCamera, _Mapping]] = ..., edit_stream_data: _Optional[_Union[HubCommand.EditStreamData, _Mapping]] = ..., link_device: _Optional[_Union[HubCommand.LinkDevice, _Mapping]] = ..., unlink_device: _Optional[_Union[HubCommand.UnlinkDevice, _Mapping]] = ..., device_command: _Optional[_Union[DeviceCommand, _Mapping]] = ..., scan_fibra_devices: _Optional[_Union[HubCommand.ScanFibraDevices, _Mapping]] = ..., get_scanned_fibra_devices: _Optional[_Union[HubCommand.GetScannedFibraDevices, _Mapping]] = ..., create_security_company_binding: _Optional[_Union[HubCommand.CreateSecurityCompanyBinding, _Mapping]] = ..., delete_security_company_binding: _Optional[_Union[HubCommand.DeleteSecurityCompanyBinding, _Mapping]] = ..., cancel_delete_security_company_binding: _Optional[_Union[HubCommand.CancelDeleteSecurityCompanyBinding, _Mapping]] = ..., update_network_channel_state: _Optional[_Union[HubCommand.UpdateNetworkChannelState, _Mapping]] = ..., update_ethernet_settings: _Optional[_Union[HubCommand.UpdateEthernetSettings, _Mapping]] = ..., update_wifi_settings: _Optional[_Union[HubCommand.UpdateWifiSettings, _Mapping]] = ..., update_gsm_sim_card_settings: _Optional[_Union[HubCommand.UpdateGsmSimCardSettings, _Mapping]] = ..., update_gsm_sim_card_balance_number: _Optional[_Union[HubCommand.UpdateGsmSimCardBalanceNumber, _Mapping]] = ..., get_gsm_sim_card_balance: _Optional[_Union[HubCommand.GetGsmSimCardBalance, _Mapping]] = ..., scan_wifi_networks: _Optional[_Union[HubCommand.ScanWifiNetworks, _Mapping]] = ..., join_wifi_network: _Optional[_Union[HubCommand.JoinWifiNetwork, _Mapping]] = ..., join_wifi_network_advanced: _Optional[_Union[HubCommand.JoinWifiNetworkAdvanced, _Mapping]] = ..., forget_wifi_network: _Optional[_Union[HubCommand.ForgetWifiNetwork, _Mapping]] = ..., apply_update: _Optional[_Union[HubCommand.ApplyUpdate, _Mapping]] = ..., create_scenario: _Optional[_Union[HubCommand.CreateScenario, _Mapping]] = ..., update_scenario: _Optional[_Union[HubCommand.UpdateScenario, _Mapping]] = ..., delete_scenario: _Optional[_Union[HubCommand.DeleteScenario, _Mapping]] = ..., apply_updates: _Optional[_Union[HubCommand.ApplyUpdates, _Mapping]] = ..., start_migration: _Optional[_Union[HubCommand.StartMigration, _Mapping]] = ..., stop_migration: _Optional[_Union[HubCommand.StopMigration, _Mapping]] = ..., add_access_card: _Optional[_Union[HubCommand.AddAccessCard, _Mapping]] = ..., delete_access_card: _Optional[_Union[HubCommand.DeleteAccessCard, _Mapping]] = ..., erase_access_card: _Optional[_Union[HubCommand.EraseAccessCard, _Mapping]] = ..., exit_card_mode: _Optional[_Union[HubCommand.ExitCardMode, _Mapping]] = ..., cancel_access_key_search: _Optional[_Union[HubCommand.CancelAccessKeySearch, _Mapping]] = ..., register_access_key: _Optional[_Union[HubCommand.RegisterAccessKey, _Mapping]] = ..., delete_access_key: _Optional[_Union[HubCommand.DeleteAccessKey, _Mapping]] = ...) -> None: ...

class DeviceCommand(_message.Message):
    __slots__ = ("device_id", "type", "device_type", "chimes_group_status", "chimes_status")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_DEVICE_COMMAND_TYPE_INFO: _ClassVar[DeviceCommand.Type]
        CONNECTION_TEST_START: _ClassVar[DeviceCommand.Type]
        CONNECTION_TEST_STOP: _ClassVar[DeviceCommand.Type]
        DETECTION_TEST_START: _ClassVar[DeviceCommand.Type]
        DETECTION_TEST_STOP: _ClassVar[DeviceCommand.Type]
        MUTE: _ClassVar[DeviceCommand.Type]
        SWITCH_ON: _ClassVar[DeviceCommand.Type]
        SWITCH_OFF: _ClassVar[DeviceCommand.Type]
        SOUND_TEST_START: _ClassVar[DeviceCommand.Type]
        UNLOCK_DEVICE: _ClassVar[DeviceCommand.Type]
        FIRE_SENSOR_TEST: _ClassVar[DeviceCommand.Type]
        MOTION_OUTDOOR_DETECTION_TEST_START: _ClassVar[DeviceCommand.Type]
        MOTION_OUTDOOR_UPPER_MOTION_SENSOR_DETECTION_TEST_START: _ClassVar[DeviceCommand.Type]
        MOTION_OUTDOOR_LOWER_MOTION_SENSOR_DETECTION_TEST_START: _ClassVar[DeviceCommand.Type]
        MOTION_OUTDOOR_ANTIMASKING_MOTION_SENSOR_DETECTION_TEST_START: _ClassVar[DeviceCommand.Type]
        GROUP_MODE_OFF: _ClassVar[DeviceCommand.Type]
        GROUP_MODE_ON: _ClassVar[DeviceCommand.Type]
        GSM_TRAFFIC_RESET_SIM1: _ClassVar[DeviceCommand.Type]
        GSM_TRAFFIC_RESET_SIM2: _ClassVar[DeviceCommand.Type]
        DEVICE_BYPASS_OFF: _ClassVar[DeviceCommand.Type]
        DEVICE_BYPASS_WHOLE: _ClassVar[DeviceCommand.Type]
        DEVICE_BYPASS_TAMPER: _ClassVar[DeviceCommand.Type]
        MULTI_TRANSMITTER_POWER_RESET: _ClassVar[DeviceCommand.Type]
        MOTION_CAM_FIFTH_FREQUENCY_CONNECTION_TEST_START: _ClassVar[DeviceCommand.Type]
        MOTION_CAM_ZERO_OR_FIRST_FREQUENCY_CONNECTION_TEST_START: _ClassVar[DeviceCommand.Type]
        MOTION_CAM_DATA_CHANNEL_CONNECTION_TEST_START: _ClassVar[DeviceCommand.Type]
        CHIMES_MODE: _ClassVar[DeviceCommand.Type]
        MAKE_PHOTO: _ClassVar[DeviceCommand.Type]
        INDICATION_OFF: _ClassVar[DeviceCommand.Type]
        INDICATION_ON: _ClassVar[DeviceCommand.Type]
        BUS_POWER_OFF: _ClassVar[DeviceCommand.Type]
        BUS_POWER_ON: _ClassVar[DeviceCommand.Type]
        MAX_POWER_TEST_OFF: _ClassVar[DeviceCommand.Type]
        MAX_POWER_TEST_ON: _ClassVar[DeviceCommand.Type]
    NO_DEVICE_COMMAND_TYPE_INFO: DeviceCommand.Type
    CONNECTION_TEST_START: DeviceCommand.Type
    CONNECTION_TEST_STOP: DeviceCommand.Type
    DETECTION_TEST_START: DeviceCommand.Type
    DETECTION_TEST_STOP: DeviceCommand.Type
    MUTE: DeviceCommand.Type
    SWITCH_ON: DeviceCommand.Type
    SWITCH_OFF: DeviceCommand.Type
    SOUND_TEST_START: DeviceCommand.Type
    UNLOCK_DEVICE: DeviceCommand.Type
    FIRE_SENSOR_TEST: DeviceCommand.Type
    MOTION_OUTDOOR_DETECTION_TEST_START: DeviceCommand.Type
    MOTION_OUTDOOR_UPPER_MOTION_SENSOR_DETECTION_TEST_START: DeviceCommand.Type
    MOTION_OUTDOOR_LOWER_MOTION_SENSOR_DETECTION_TEST_START: DeviceCommand.Type
    MOTION_OUTDOOR_ANTIMASKING_MOTION_SENSOR_DETECTION_TEST_START: DeviceCommand.Type
    GROUP_MODE_OFF: DeviceCommand.Type
    GROUP_MODE_ON: DeviceCommand.Type
    GSM_TRAFFIC_RESET_SIM1: DeviceCommand.Type
    GSM_TRAFFIC_RESET_SIM2: DeviceCommand.Type
    DEVICE_BYPASS_OFF: DeviceCommand.Type
    DEVICE_BYPASS_WHOLE: DeviceCommand.Type
    DEVICE_BYPASS_TAMPER: DeviceCommand.Type
    MULTI_TRANSMITTER_POWER_RESET: DeviceCommand.Type
    MOTION_CAM_FIFTH_FREQUENCY_CONNECTION_TEST_START: DeviceCommand.Type
    MOTION_CAM_ZERO_OR_FIRST_FREQUENCY_CONNECTION_TEST_START: DeviceCommand.Type
    MOTION_CAM_DATA_CHANNEL_CONNECTION_TEST_START: DeviceCommand.Type
    CHIMES_MODE: DeviceCommand.Type
    MAKE_PHOTO: DeviceCommand.Type
    INDICATION_OFF: DeviceCommand.Type
    INDICATION_ON: DeviceCommand.Type
    BUS_POWER_OFF: DeviceCommand.Type
    BUS_POWER_ON: DeviceCommand.Type
    MAX_POWER_TEST_OFF: DeviceCommand.Type
    MAX_POWER_TEST_ON: DeviceCommand.Type
    class ChimesGroupStatus(_message.Message):
        __slots__ = ("group_ids",)
        class GroupIdsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: bool
            def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
        GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
        group_ids: _containers.ScalarMap[str, bool]
        def __init__(self, group_ids: _Optional[_Mapping[str, bool]] = ...) -> None: ...
    class ChimesStatus(_message.Message):
        __slots__ = ("enabled",)
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        def __init__(self, enabled: bool = ...) -> None: ...
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHIMES_GROUP_STATUS_FIELD_NUMBER: _ClassVar[int]
    CHIMES_STATUS_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    type: DeviceCommand.Type
    device_type: _object_type_pb2.ObjectType
    chimes_group_status: DeviceCommand.ChimesGroupStatus
    chimes_status: DeviceCommand.ChimesStatus
    def __init__(self, device_id: _Optional[str] = ..., type: _Optional[_Union[DeviceCommand.Type, str]] = ..., device_type: _Optional[_Union[_object_type_pb2.ObjectType, str]] = ..., chimes_group_status: _Optional[_Union[DeviceCommand.ChimesGroupStatus, _Mapping]] = ..., chimes_status: _Optional[_Union[DeviceCommand.ChimesStatus, _Mapping]] = ...) -> None: ...

class ChangeUserRole(_message.Message):
    __slots__ = ("user_id", "user_role")
    class UserRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        USER: _ClassVar[ChangeUserRole.UserRole]
        MASTER: _ClassVar[ChangeUserRole.UserRole]
    USER: ChangeUserRole.UserRole
    MASTER: ChangeUserRole.UserRole
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ROLE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    user_role: ChangeUserRole.UserRole
    def __init__(self, user_id: _Optional[str] = ..., user_role: _Optional[_Union[ChangeUserRole.UserRole, str]] = ...) -> None: ...

class ChangeUserPermissions(_message.Message):
    __slots__ = ("user_id", "user_permission")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    user_permission: _containers.RepeatedScalarFieldContainer[_user_pb2.User.Permission]
    def __init__(self, user_id: _Optional[str] = ..., user_permission: _Optional[_Iterable[_Union[_user_pb2.User.Permission, str]]] = ...) -> None: ...
