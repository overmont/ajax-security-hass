from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FireZoneCommandDisablementRequest(_message.Message):
    __slots__ = ("hub_id", "device_id", "en54_disablement_endpoints")
    class En54FireZoneDisablementState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EN54_FIRE_ZONE_DISABLEMENT_STATE_UNSPECIFIED: _ClassVar[FireZoneCommandDisablementRequest.En54FireZoneDisablementState]
        EN54_FIRE_ZONE_DISABLEMENT_STATE_NOT_CHANGED: _ClassVar[FireZoneCommandDisablementRequest.En54FireZoneDisablementState]
        EN54_FIRE_ZONE_DISABLEMENT_STATE_ENABLE: _ClassVar[FireZoneCommandDisablementRequest.En54FireZoneDisablementState]
        EN54_FIRE_ZONE_DISABLEMENT_STATE_DISABLE: _ClassVar[FireZoneCommandDisablementRequest.En54FireZoneDisablementState]
    EN54_FIRE_ZONE_DISABLEMENT_STATE_UNSPECIFIED: FireZoneCommandDisablementRequest.En54FireZoneDisablementState
    EN54_FIRE_ZONE_DISABLEMENT_STATE_NOT_CHANGED: FireZoneCommandDisablementRequest.En54FireZoneDisablementState
    EN54_FIRE_ZONE_DISABLEMENT_STATE_ENABLE: FireZoneCommandDisablementRequest.En54FireZoneDisablementState
    EN54_FIRE_ZONE_DISABLEMENT_STATE_DISABLE: FireZoneCommandDisablementRequest.En54FireZoneDisablementState
    class En54DisablementEndpoint(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EN54_DISABLEMENT_ENDPOINT_UNSPECIFIED: _ClassVar[FireZoneCommandDisablementRequest.En54DisablementEndpoint]
        EN54_DISABLEMENT_ENDPOINT_SMOKE: _ClassVar[FireZoneCommandDisablementRequest.En54DisablementEndpoint]
        EN54_DISABLEMENT_ENDPOINT_TEMPERATURE: _ClassVar[FireZoneCommandDisablementRequest.En54DisablementEndpoint]
        EN54_DISABLEMENT_ENDPOINT_SOUNDER: _ClassVar[FireZoneCommandDisablementRequest.En54DisablementEndpoint]
        EN54_DISABLEMENT_ENDPOINT_VAD: _ClassVar[FireZoneCommandDisablementRequest.En54DisablementEndpoint]
        EN54_DISABLEMENT_ENDPOINT_INPUTS: _ClassVar[FireZoneCommandDisablementRequest.En54DisablementEndpoint]
        EN54_DISABLEMENT_ENDPOINT_MCP: _ClassVar[FireZoneCommandDisablementRequest.En54DisablementEndpoint]
        EN54_DISABLEMENT_ENDPOINT_OUTPUTS: _ClassVar[FireZoneCommandDisablementRequest.En54DisablementEndpoint]
    EN54_DISABLEMENT_ENDPOINT_UNSPECIFIED: FireZoneCommandDisablementRequest.En54DisablementEndpoint
    EN54_DISABLEMENT_ENDPOINT_SMOKE: FireZoneCommandDisablementRequest.En54DisablementEndpoint
    EN54_DISABLEMENT_ENDPOINT_TEMPERATURE: FireZoneCommandDisablementRequest.En54DisablementEndpoint
    EN54_DISABLEMENT_ENDPOINT_SOUNDER: FireZoneCommandDisablementRequest.En54DisablementEndpoint
    EN54_DISABLEMENT_ENDPOINT_VAD: FireZoneCommandDisablementRequest.En54DisablementEndpoint
    EN54_DISABLEMENT_ENDPOINT_INPUTS: FireZoneCommandDisablementRequest.En54DisablementEndpoint
    EN54_DISABLEMENT_ENDPOINT_MCP: FireZoneCommandDisablementRequest.En54DisablementEndpoint
    EN54_DISABLEMENT_ENDPOINT_OUTPUTS: FireZoneCommandDisablementRequest.En54DisablementEndpoint
    class DisablementEntry(_message.Message):
        __slots__ = ("en54_disablement_endpoint", "en54_fire_zone_disablement_state")
        EN54_DISABLEMENT_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        EN54_FIRE_ZONE_DISABLEMENT_STATE_FIELD_NUMBER: _ClassVar[int]
        en54_disablement_endpoint: FireZoneCommandDisablementRequest.En54DisablementEndpoint
        en54_fire_zone_disablement_state: FireZoneCommandDisablementRequest.En54FireZoneDisablementState
        def __init__(self, en54_disablement_endpoint: _Optional[_Union[FireZoneCommandDisablementRequest.En54DisablementEndpoint, str]] = ..., en54_fire_zone_disablement_state: _Optional[_Union[FireZoneCommandDisablementRequest.En54FireZoneDisablementState, str]] = ...) -> None: ...
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    EN54_DISABLEMENT_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    device_id: str
    en54_disablement_endpoints: _containers.RepeatedCompositeFieldContainer[FireZoneCommandDisablementRequest.DisablementEntry]
    def __init__(self, hub_id: _Optional[str] = ..., device_id: _Optional[str] = ..., en54_disablement_endpoints: _Optional[_Iterable[_Union[FireZoneCommandDisablementRequest.DisablementEntry, _Mapping]]] = ...) -> None: ...
