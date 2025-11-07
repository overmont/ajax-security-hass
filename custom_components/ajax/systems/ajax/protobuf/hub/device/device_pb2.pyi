from systems.ajax.protobuf.hub.device import door_protect_pb2 as _door_protect_pb2
from systems.ajax.protobuf.hub.device import motion_protect_pb2 as _motion_protect_pb2
from systems.ajax.protobuf.hub.device import fire_protect_pb2 as _fire_protect_pb2
from systems.ajax.protobuf.hub.device import glass_protect_pb2 as _glass_protect_pb2
from systems.ajax.protobuf.hub.device import leaks_protect_pb2 as _leaks_protect_pb2
from systems.ajax.protobuf.hub.device import motion_protect_curtain_pb2 as _motion_protect_curtain_pb2
from systems.ajax.protobuf.hub.device import range_extender_pb2 as _range_extender_pb2
from systems.ajax.protobuf.hub.device import combi_protect_pb2 as _combi_protect_pb2
from systems.ajax.protobuf.hub.device import fire_protect_plus_pb2 as _fire_protect_plus_pb2
from systems.ajax.protobuf.hub.device import keypad_pb2 as _keypad_pb2
from systems.ajax.protobuf.hub.device import space_control_pb2 as _space_control_pb2
from systems.ajax.protobuf.hub.device import button_pb2 as _button_pb2
from systems.ajax.protobuf.hub.device import double_button_pb2 as _double_button_pb2
from systems.ajax.protobuf.hub.device import motion_cam_pb2 as _motion_cam_pb2
from systems.ajax.protobuf.hub.device import motion_protect_plus_pb2 as _motion_protect_plus_pb2
from systems.ajax.protobuf.hub.device import door_protect_plus_pb2 as _door_protect_plus_pb2
from systems.ajax.protobuf.hub.device import transmitter_pb2 as _transmitter_pb2
from systems.ajax.protobuf.hub.device import relay_pb2 as _relay_pb2
from systems.ajax.protobuf.hub.device import motion_protect_outdoor_pb2 as _motion_protect_outdoor_pb2
from systems.ajax.protobuf.hub.device import street_siren_pb2 as _street_siren_pb2
from systems.ajax.protobuf.hub.device import street_siren_double_deck_pb2 as _street_siren_double_deck_pb2
from systems.ajax.protobuf.hub.device import home_siren_pb2 as _home_siren_pb2
from systems.ajax.protobuf.hub.device import keypad_plus_pb2 as _keypad_plus_pb2
from systems.ajax.protobuf.hub.device import socket_pb2 as _socket_pb2
from systems.ajax.protobuf.hub.device import wall_switch_pb2 as _wall_switch_pb2
from systems.ajax.protobuf.hub.device import universal_device_pb2 as _universal_device_pb2
from systems.ajax.protobuf.hub.device import wire_input_pb2 as _wire_input_pb2
from systems.ajax.protobuf.hub.device import wire_siren_pb2 as _wire_siren_pb2
from systems.ajax.protobuf.hub.device import yavir_access_control_pb2 as _yavir_access_control_pb2
from systems.ajax.protobuf.hub.device import access_key_pb2 as _access_key_pb2
from systems.ajax.protobuf.hub.device import multi_transmitter_pb2 as _multi_transmitter_pb2
from systems.ajax.protobuf.hub.device import wire_input_mt_pb2 as _wire_input_mt_pb2
from systems.ajax.protobuf.hub.device import keypad_combi_pb2 as _keypad_combi_pb2
from systems.ajax.protobuf.hub.device import dual_curtain_outdoor_pb2 as _dual_curtain_outdoor_pb2
from systems.ajax.protobuf.hub.device import access_card_pb2 as _access_card_pb2
from systems.ajax.protobuf.hub.device import motion_cam_outdoor_pb2 as _motion_cam_outdoor_pb2
from systems.ajax.protobuf.hub.device import door_protect_fibra_pb2 as _door_protect_fibra_pb2
from systems.ajax.protobuf.hub.device import motion_protect_fibra_pb2 as _motion_protect_fibra_pb2
from systems.ajax.protobuf.hub.device import glass_protect_fibra_pb2 as _glass_protect_fibra_pb2
from systems.ajax.protobuf.hub.device import combi_protect_fibra_pb2 as _combi_protect_fibra_pb2
from systems.ajax.protobuf.hub.device import keypad_fibra_pb2 as _keypad_fibra_pb2
from systems.ajax.protobuf.hub.device import motion_protect_plus_fibra_pb2 as _motion_protect_plus_fibra_pb2
from systems.ajax.protobuf.hub.device import door_protect_plus_fibra_pb2 as _door_protect_plus_fibra_pb2
from systems.ajax.protobuf.hub.device import street_siren_fibra_pb2 as _street_siren_fibra_pb2
from systems.ajax.protobuf.hub.device import home_siren_fibra_pb2 as _home_siren_fibra_pb2
from systems.ajax.protobuf.hub.device import street_siren_double_deck_fibra_pb2 as _street_siren_double_deck_fibra_pb2
from systems.ajax.protobuf.hub.device import range_extender2_pb2 as _range_extender2_pb2
from systems.ajax.protobuf.hub.device import vhf_bridge_pb2 as _vhf_bridge_pb2
from systems.ajax.protobuf.hub.device import socket_base_pb2 as _socket_base_pb2
from systems.ajax.protobuf.hub.device import hub_device_pb2 as _hub_device_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Device(_message.Message):
    __slots__ = ("door_protect", "motion_protect", "fire_protect", "glass_protect", "leak_protect", "motion_protect_curtain", "range_extender", "combi_protect", "fire_protect_plus", "keypad", "space_control", "button", "motion_cam", "motion_protect_plus", "door_protect_plus", "universal_device", "transmitter", "relay", "motion_protect_outdoor", "street_siren", "home_siren", "motion_cam_outdoor", "keypad_plus", "dual_curtain_outdoor", "street_siren_double_deck", "multi_transmitter", "wire_input_mt", "socket", "wall_switch", "wire_input", "wire_siren", "yavir_access_control", "access_key", "access_card", "hub", "double_button", "keypad_combi", "vhf_bridge", "range_extender2", "socket_base", "door_protect_fibra", "motion_protect_fibra", "glass_protect_fibra", "combi_protect_fibra", "keypad_fibra", "motion_protect_plus_fibra", "door_protect_plus_fibra", "street_siren_fibra", "home_siren_fibra", "street_siren_double_deck_fibra")
    DOOR_PROTECT_FIELD_NUMBER: _ClassVar[int]
    MOTION_PROTECT_FIELD_NUMBER: _ClassVar[int]
    FIRE_PROTECT_FIELD_NUMBER: _ClassVar[int]
    GLASS_PROTECT_FIELD_NUMBER: _ClassVar[int]
    LEAK_PROTECT_FIELD_NUMBER: _ClassVar[int]
    MOTION_PROTECT_CURTAIN_FIELD_NUMBER: _ClassVar[int]
    RANGE_EXTENDER_FIELD_NUMBER: _ClassVar[int]
    COMBI_PROTECT_FIELD_NUMBER: _ClassVar[int]
    FIRE_PROTECT_PLUS_FIELD_NUMBER: _ClassVar[int]
    KEYPAD_FIELD_NUMBER: _ClassVar[int]
    SPACE_CONTROL_FIELD_NUMBER: _ClassVar[int]
    BUTTON_FIELD_NUMBER: _ClassVar[int]
    MOTION_CAM_FIELD_NUMBER: _ClassVar[int]
    MOTION_PROTECT_PLUS_FIELD_NUMBER: _ClassVar[int]
    DOOR_PROTECT_PLUS_FIELD_NUMBER: _ClassVar[int]
    UNIVERSAL_DEVICE_FIELD_NUMBER: _ClassVar[int]
    TRANSMITTER_FIELD_NUMBER: _ClassVar[int]
    RELAY_FIELD_NUMBER: _ClassVar[int]
    MOTION_PROTECT_OUTDOOR_FIELD_NUMBER: _ClassVar[int]
    STREET_SIREN_FIELD_NUMBER: _ClassVar[int]
    HOME_SIREN_FIELD_NUMBER: _ClassVar[int]
    MOTION_CAM_OUTDOOR_FIELD_NUMBER: _ClassVar[int]
    KEYPAD_PLUS_FIELD_NUMBER: _ClassVar[int]
    DUAL_CURTAIN_OUTDOOR_FIELD_NUMBER: _ClassVar[int]
    STREET_SIREN_DOUBLE_DECK_FIELD_NUMBER: _ClassVar[int]
    MULTI_TRANSMITTER_FIELD_NUMBER: _ClassVar[int]
    WIRE_INPUT_MT_FIELD_NUMBER: _ClassVar[int]
    SOCKET_FIELD_NUMBER: _ClassVar[int]
    WALL_SWITCH_FIELD_NUMBER: _ClassVar[int]
    WIRE_INPUT_FIELD_NUMBER: _ClassVar[int]
    WIRE_SIREN_FIELD_NUMBER: _ClassVar[int]
    YAVIR_ACCESS_CONTROL_FIELD_NUMBER: _ClassVar[int]
    ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    ACCESS_CARD_FIELD_NUMBER: _ClassVar[int]
    HUB_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_BUTTON_FIELD_NUMBER: _ClassVar[int]
    KEYPAD_COMBI_FIELD_NUMBER: _ClassVar[int]
    VHF_BRIDGE_FIELD_NUMBER: _ClassVar[int]
    RANGE_EXTENDER2_FIELD_NUMBER: _ClassVar[int]
    SOCKET_BASE_FIELD_NUMBER: _ClassVar[int]
    DOOR_PROTECT_FIBRA_FIELD_NUMBER: _ClassVar[int]
    MOTION_PROTECT_FIBRA_FIELD_NUMBER: _ClassVar[int]
    GLASS_PROTECT_FIBRA_FIELD_NUMBER: _ClassVar[int]
    COMBI_PROTECT_FIBRA_FIELD_NUMBER: _ClassVar[int]
    KEYPAD_FIBRA_FIELD_NUMBER: _ClassVar[int]
    MOTION_PROTECT_PLUS_FIBRA_FIELD_NUMBER: _ClassVar[int]
    DOOR_PROTECT_PLUS_FIBRA_FIELD_NUMBER: _ClassVar[int]
    STREET_SIREN_FIBRA_FIELD_NUMBER: _ClassVar[int]
    HOME_SIREN_FIBRA_FIELD_NUMBER: _ClassVar[int]
    STREET_SIREN_DOUBLE_DECK_FIBRA_FIELD_NUMBER: _ClassVar[int]
    door_protect: _door_protect_pb2.DoorProtect
    motion_protect: _motion_protect_pb2.MotionProtect
    fire_protect: _fire_protect_pb2.FireProtect
    glass_protect: _glass_protect_pb2.GlassProtect
    leak_protect: _leaks_protect_pb2.LeaksProtect
    motion_protect_curtain: _motion_protect_curtain_pb2.MotionProtectCurtain
    range_extender: _range_extender_pb2.RangeExtender
    combi_protect: _combi_protect_pb2.CombiProtect
    fire_protect_plus: _fire_protect_plus_pb2.FireProtectPlus
    keypad: _keypad_pb2.Keypad
    space_control: _space_control_pb2.SpaceControl
    button: _button_pb2.Button
    motion_cam: _motion_cam_pb2.MotionCam
    motion_protect_plus: _motion_protect_plus_pb2.MotionProtectPlus
    door_protect_plus: _door_protect_plus_pb2.DoorProtectPlus
    universal_device: _universal_device_pb2.UniversalDevice
    transmitter: _transmitter_pb2.Transmitter
    relay: _relay_pb2.Relay
    motion_protect_outdoor: _motion_protect_outdoor_pb2.MotionProtectOutdoor
    street_siren: _street_siren_pb2.StreetSiren
    home_siren: _home_siren_pb2.HomeSiren
    motion_cam_outdoor: _motion_cam_outdoor_pb2.MotionCamOutdoor
    keypad_plus: _keypad_plus_pb2.KeypadPlus
    dual_curtain_outdoor: _dual_curtain_outdoor_pb2.DualCurtainOutdoor
    street_siren_double_deck: _street_siren_double_deck_pb2.StreetSirenDoubleDeck
    multi_transmitter: _multi_transmitter_pb2.MultiTransmitter
    wire_input_mt: _wire_input_mt_pb2.WireInputMt
    socket: _socket_pb2.Socket
    wall_switch: _wall_switch_pb2.WallSwitch
    wire_input: _wire_input_pb2.WireInput
    wire_siren: _wire_siren_pb2.WireSiren
    yavir_access_control: _yavir_access_control_pb2.YavirAccessControl
    access_key: _access_key_pb2.AccessKey
    access_card: _access_card_pb2.AccessCard
    hub: _hub_device_pb2.HubDevice
    double_button: _double_button_pb2.DoubleButton
    keypad_combi: _keypad_combi_pb2.KeypadCombi
    vhf_bridge: _vhf_bridge_pb2.VhfBridge
    range_extender2: _range_extender2_pb2.RangeExtender2
    socket_base: _socket_base_pb2.SocketBase
    door_protect_fibra: _door_protect_fibra_pb2.DoorProtectFibra
    motion_protect_fibra: _motion_protect_fibra_pb2.MotionProtectFibra
    glass_protect_fibra: _glass_protect_fibra_pb2.GlassProtectFibra
    combi_protect_fibra: _combi_protect_fibra_pb2.CombiProtectFibra
    keypad_fibra: _keypad_fibra_pb2.KeypadFibra
    motion_protect_plus_fibra: _motion_protect_plus_fibra_pb2.MotionProtectPlusFibra
    door_protect_plus_fibra: _door_protect_plus_fibra_pb2.DoorProtectPlusFibra
    street_siren_fibra: _street_siren_fibra_pb2.StreetSirenFibra
    home_siren_fibra: _home_siren_fibra_pb2.HomeSirenFibra
    street_siren_double_deck_fibra: _street_siren_double_deck_fibra_pb2.StreetSirenDoubleDeckFibra
    def __init__(self, door_protect: _Optional[_Union[_door_protect_pb2.DoorProtect, _Mapping]] = ..., motion_protect: _Optional[_Union[_motion_protect_pb2.MotionProtect, _Mapping]] = ..., fire_protect: _Optional[_Union[_fire_protect_pb2.FireProtect, _Mapping]] = ..., glass_protect: _Optional[_Union[_glass_protect_pb2.GlassProtect, _Mapping]] = ..., leak_protect: _Optional[_Union[_leaks_protect_pb2.LeaksProtect, _Mapping]] = ..., motion_protect_curtain: _Optional[_Union[_motion_protect_curtain_pb2.MotionProtectCurtain, _Mapping]] = ..., range_extender: _Optional[_Union[_range_extender_pb2.RangeExtender, _Mapping]] = ..., combi_protect: _Optional[_Union[_combi_protect_pb2.CombiProtect, _Mapping]] = ..., fire_protect_plus: _Optional[_Union[_fire_protect_plus_pb2.FireProtectPlus, _Mapping]] = ..., keypad: _Optional[_Union[_keypad_pb2.Keypad, _Mapping]] = ..., space_control: _Optional[_Union[_space_control_pb2.SpaceControl, _Mapping]] = ..., button: _Optional[_Union[_button_pb2.Button, _Mapping]] = ..., motion_cam: _Optional[_Union[_motion_cam_pb2.MotionCam, _Mapping]] = ..., motion_protect_plus: _Optional[_Union[_motion_protect_plus_pb2.MotionProtectPlus, _Mapping]] = ..., door_protect_plus: _Optional[_Union[_door_protect_plus_pb2.DoorProtectPlus, _Mapping]] = ..., universal_device: _Optional[_Union[_universal_device_pb2.UniversalDevice, _Mapping]] = ..., transmitter: _Optional[_Union[_transmitter_pb2.Transmitter, _Mapping]] = ..., relay: _Optional[_Union[_relay_pb2.Relay, _Mapping]] = ..., motion_protect_outdoor: _Optional[_Union[_motion_protect_outdoor_pb2.MotionProtectOutdoor, _Mapping]] = ..., street_siren: _Optional[_Union[_street_siren_pb2.StreetSiren, _Mapping]] = ..., home_siren: _Optional[_Union[_home_siren_pb2.HomeSiren, _Mapping]] = ..., motion_cam_outdoor: _Optional[_Union[_motion_cam_outdoor_pb2.MotionCamOutdoor, _Mapping]] = ..., keypad_plus: _Optional[_Union[_keypad_plus_pb2.KeypadPlus, _Mapping]] = ..., dual_curtain_outdoor: _Optional[_Union[_dual_curtain_outdoor_pb2.DualCurtainOutdoor, _Mapping]] = ..., street_siren_double_deck: _Optional[_Union[_street_siren_double_deck_pb2.StreetSirenDoubleDeck, _Mapping]] = ..., multi_transmitter: _Optional[_Union[_multi_transmitter_pb2.MultiTransmitter, _Mapping]] = ..., wire_input_mt: _Optional[_Union[_wire_input_mt_pb2.WireInputMt, _Mapping]] = ..., socket: _Optional[_Union[_socket_pb2.Socket, _Mapping]] = ..., wall_switch: _Optional[_Union[_wall_switch_pb2.WallSwitch, _Mapping]] = ..., wire_input: _Optional[_Union[_wire_input_pb2.WireInput, _Mapping]] = ..., wire_siren: _Optional[_Union[_wire_siren_pb2.WireSiren, _Mapping]] = ..., yavir_access_control: _Optional[_Union[_yavir_access_control_pb2.YavirAccessControl, _Mapping]] = ..., access_key: _Optional[_Union[_access_key_pb2.AccessKey, _Mapping]] = ..., access_card: _Optional[_Union[_access_card_pb2.AccessCard, _Mapping]] = ..., hub: _Optional[_Union[_hub_device_pb2.HubDevice, _Mapping]] = ..., double_button: _Optional[_Union[_double_button_pb2.DoubleButton, _Mapping]] = ..., keypad_combi: _Optional[_Union[_keypad_combi_pb2.KeypadCombi, _Mapping]] = ..., vhf_bridge: _Optional[_Union[_vhf_bridge_pb2.VhfBridge, _Mapping]] = ..., range_extender2: _Optional[_Union[_range_extender2_pb2.RangeExtender2, _Mapping]] = ..., socket_base: _Optional[_Union[_socket_base_pb2.SocketBase, _Mapping]] = ..., door_protect_fibra: _Optional[_Union[_door_protect_fibra_pb2.DoorProtectFibra, _Mapping]] = ..., motion_protect_fibra: _Optional[_Union[_motion_protect_fibra_pb2.MotionProtectFibra, _Mapping]] = ..., glass_protect_fibra: _Optional[_Union[_glass_protect_fibra_pb2.GlassProtectFibra, _Mapping]] = ..., combi_protect_fibra: _Optional[_Union[_combi_protect_fibra_pb2.CombiProtectFibra, _Mapping]] = ..., keypad_fibra: _Optional[_Union[_keypad_fibra_pb2.KeypadFibra, _Mapping]] = ..., motion_protect_plus_fibra: _Optional[_Union[_motion_protect_plus_fibra_pb2.MotionProtectPlusFibra, _Mapping]] = ..., door_protect_plus_fibra: _Optional[_Union[_door_protect_plus_fibra_pb2.DoorProtectPlusFibra, _Mapping]] = ..., street_siren_fibra: _Optional[_Union[_street_siren_fibra_pb2.StreetSirenFibra, _Mapping]] = ..., home_siren_fibra: _Optional[_Union[_home_siren_fibra_pb2.HomeSirenFibra, _Mapping]] = ..., street_siren_double_deck_fibra: _Optional[_Union[_street_siren_double_deck_fibra_pb2.StreetSirenDoubleDeckFibra, _Mapping]] = ...) -> None: ...
