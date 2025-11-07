from systems.ajax.api.mobile.v2.common.accounting import service_state_pb2 as _service_state_pb2
from systems.ajax.api.mobile.v2.common.hub import hub_box_type_pb2 as _hub_box_type_pb2
from systems.ajax.api.mobile.v2.common.hub import hub_feature_pb2 as _hub_feature_pb2
from systems.ajax.api.mobile.v2.common.space.device import device_color_pb2 as _device_color_pb2
from systems.ajax.api.mobile.v2.common.space.device import device_constraints_pb2 as _device_constraints_pb2
from systems.ajax.api.mobile.v2.common.space import displayed_chime_status_pb2 as _displayed_chime_status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Hub(_message.Message):
    __slots__ = ("id", "room_id", "service_state", "device_color", "box_type", "constraints", "hub_features", "chime_status")
    ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_STATE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_COLOR_FIELD_NUMBER: _ClassVar[int]
    BOX_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    HUB_FEATURES_FIELD_NUMBER: _ClassVar[int]
    CHIME_STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    room_id: str
    service_state: _service_state_pb2.ServiceState
    device_color: _device_color_pb2.DeviceColor
    box_type: _hub_box_type_pb2.HubBoxType
    constraints: _device_constraints_pb2.DeviceConstraints
    hub_features: _hub_feature_pb2.HubFeatures
    chime_status: _displayed_chime_status_pb2.DisplayedChimeStatus
    def __init__(self, id: _Optional[str] = ..., room_id: _Optional[str] = ..., service_state: _Optional[_Union[_service_state_pb2.ServiceState, str]] = ..., device_color: _Optional[_Union[_device_color_pb2.DeviceColor, str]] = ..., box_type: _Optional[_Union[_hub_box_type_pb2.HubBoxType, str]] = ..., constraints: _Optional[_Union[_device_constraints_pb2.DeviceConstraints, _Mapping]] = ..., hub_features: _Optional[_Union[_hub_feature_pb2.HubFeatures, _Mapping]] = ..., chime_status: _Optional[_Union[_displayed_chime_status_pb2.DisplayedChimeStatus, str]] = ...) -> None: ...
