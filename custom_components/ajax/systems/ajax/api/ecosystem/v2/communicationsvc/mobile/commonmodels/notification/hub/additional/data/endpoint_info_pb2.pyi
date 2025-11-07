from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EndpointInfo(_message.Message):
    __slots__ = ("target", "name")
    class Endpoint(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENDPOINT_UNSPECIFIED: _ClassVar[EndpointInfo.Endpoint]
        LIGHT_SWITCH_BUTTON_1: _ClassVar[EndpointInfo.Endpoint]
        LIGHT_SWITCH_BUTTON_2: _ClassVar[EndpointInfo.Endpoint]
        FOUR_CHANNELS_RELAY_FIBRA_CHANNEL_1: _ClassVar[EndpointInfo.Endpoint]
        FOUR_CHANNELS_RELAY_FIBRA_CHANNEL_2: _ClassVar[EndpointInfo.Endpoint]
        FOUR_CHANNELS_RELAY_FIBRA_CHANNEL_3: _ClassVar[EndpointInfo.Endpoint]
        FOUR_CHANNELS_RELAY_FIBRA_CHANNEL_4: _ClassVar[EndpointInfo.Endpoint]
        TRANSMITTER_FIBRA_FOUR_CHANNELS_CHANNEL_1: _ClassVar[EndpointInfo.Endpoint]
        TRANSMITTER_FIBRA_FOUR_CHANNELS_CHANNEL_2: _ClassVar[EndpointInfo.Endpoint]
        TRANSMITTER_FIBRA_FOUR_CHANNELS_CHANNEL_3: _ClassVar[EndpointInfo.Endpoint]
        TRANSMITTER_FIBRA_FOUR_CHANNELS_CHANNEL_4: _ClassVar[EndpointInfo.Endpoint]
        EN54_IO_MODULE_OUTPUT_1: _ClassVar[EndpointInfo.Endpoint]
        EN54_IO_MODULE_OUTPUT_2: _ClassVar[EndpointInfo.Endpoint]
    ENDPOINT_UNSPECIFIED: EndpointInfo.Endpoint
    LIGHT_SWITCH_BUTTON_1: EndpointInfo.Endpoint
    LIGHT_SWITCH_BUTTON_2: EndpointInfo.Endpoint
    FOUR_CHANNELS_RELAY_FIBRA_CHANNEL_1: EndpointInfo.Endpoint
    FOUR_CHANNELS_RELAY_FIBRA_CHANNEL_2: EndpointInfo.Endpoint
    FOUR_CHANNELS_RELAY_FIBRA_CHANNEL_3: EndpointInfo.Endpoint
    FOUR_CHANNELS_RELAY_FIBRA_CHANNEL_4: EndpointInfo.Endpoint
    TRANSMITTER_FIBRA_FOUR_CHANNELS_CHANNEL_1: EndpointInfo.Endpoint
    TRANSMITTER_FIBRA_FOUR_CHANNELS_CHANNEL_2: EndpointInfo.Endpoint
    TRANSMITTER_FIBRA_FOUR_CHANNELS_CHANNEL_3: EndpointInfo.Endpoint
    TRANSMITTER_FIBRA_FOUR_CHANNELS_CHANNEL_4: EndpointInfo.Endpoint
    EN54_IO_MODULE_OUTPUT_1: EndpointInfo.Endpoint
    EN54_IO_MODULE_OUTPUT_2: EndpointInfo.Endpoint
    TARGET_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    target: EndpointInfo.Endpoint
    name: str
    def __init__(self, target: _Optional[_Union[EndpointInfo.Endpoint, str]] = ..., name: _Optional[str] = ...) -> None: ...
