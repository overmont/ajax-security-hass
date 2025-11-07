from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import object_type_pb2 as _object_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterWireInputToHubRequest(_message.Message):
    __slots__ = ("hub_id", "room_id", "group_id", "wire_input_name", "wire_input_index", "parent_id", "parent_type", "fire_zone_id", "device_location")
    class ParentType(_message.Message):
        __slots__ = ("transmitter_fibra_two_channels", "transmitter_fibra_four_channels_two_relays_two_logical", "multi_transmitter", "multi_transmitter_fibra", "en54_io_module_base", "en54_io_module_two_in_two_out", "multi_transmitter_g3")
        TRANSMITTER_FIBRA_TWO_CHANNELS_FIELD_NUMBER: _ClassVar[int]
        TRANSMITTER_FIBRA_FOUR_CHANNELS_TWO_RELAYS_TWO_LOGICAL_FIELD_NUMBER: _ClassVar[int]
        MULTI_TRANSMITTER_FIELD_NUMBER: _ClassVar[int]
        MULTI_TRANSMITTER_FIBRA_FIELD_NUMBER: _ClassVar[int]
        EN54_IO_MODULE_BASE_FIELD_NUMBER: _ClassVar[int]
        EN54_IO_MODULE_TWO_IN_TWO_OUT_FIELD_NUMBER: _ClassVar[int]
        MULTI_TRANSMITTER_G3_FIELD_NUMBER: _ClassVar[int]
        transmitter_fibra_two_channels: _object_type_pb2.TransmitterFibraTwoChannels
        transmitter_fibra_four_channels_two_relays_two_logical: _object_type_pb2.TransmitterFibraFourChannelsTwoRelaysTwoLogical
        multi_transmitter: _object_type_pb2.MultiTransmitter
        multi_transmitter_fibra: _object_type_pb2.MultiTransmitterFibra
        en54_io_module_base: _object_type_pb2.En54IoModuleBase
        en54_io_module_two_in_two_out: _object_type_pb2.En54IoModuleTwoInTwoOut
        multi_transmitter_g3: _object_type_pb2.MultiTransmitterG3
        def __init__(self, transmitter_fibra_two_channels: _Optional[_Union[_object_type_pb2.TransmitterFibraTwoChannels, _Mapping]] = ..., transmitter_fibra_four_channels_two_relays_two_logical: _Optional[_Union[_object_type_pb2.TransmitterFibraFourChannelsTwoRelaysTwoLogical, _Mapping]] = ..., multi_transmitter: _Optional[_Union[_object_type_pb2.MultiTransmitter, _Mapping]] = ..., multi_transmitter_fibra: _Optional[_Union[_object_type_pb2.MultiTransmitterFibra, _Mapping]] = ..., en54_io_module_base: _Optional[_Union[_object_type_pb2.En54IoModuleBase, _Mapping]] = ..., en54_io_module_two_in_two_out: _Optional[_Union[_object_type_pb2.En54IoModuleTwoInTwoOut, _Mapping]] = ..., multi_transmitter_g3: _Optional[_Union[_object_type_pb2.MultiTransmitterG3, _Mapping]] = ...) -> None: ...
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    WIRE_INPUT_NAME_FIELD_NUMBER: _ClassVar[int]
    WIRE_INPUT_INDEX_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIRE_ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    room_id: str
    group_id: str
    wire_input_name: str
    wire_input_index: int
    parent_id: str
    parent_type: RegisterWireInputToHubRequest.ParentType
    fire_zone_id: str
    device_location: str
    def __init__(self, hub_id: _Optional[str] = ..., room_id: _Optional[str] = ..., group_id: _Optional[str] = ..., wire_input_name: _Optional[str] = ..., wire_input_index: _Optional[int] = ..., parent_id: _Optional[str] = ..., parent_type: _Optional[_Union[RegisterWireInputToHubRequest.ParentType, _Mapping]] = ..., fire_zone_id: _Optional[str] = ..., device_location: _Optional[str] = ...) -> None: ...
