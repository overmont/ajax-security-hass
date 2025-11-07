from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceSecurityTransitionFailure(_message.Message):
    __slots__ = ("timed_out", "cancelled", "hub_offline", "hub_busy", "hub_blocked_by_service_provider", "hub_alarm_reset_required", "hub_detected_malfunctions")
    TIMED_OUT_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_FIELD_NUMBER: _ClassVar[int]
    HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
    HUB_BUSY_FIELD_NUMBER: _ClassVar[int]
    HUB_BLOCKED_BY_SERVICE_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    HUB_ALARM_RESET_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    HUB_DETECTED_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    timed_out: _response_pb2.DefaultError
    cancelled: _response_pb2.DefaultError
    hub_offline: _response_pb2.DefaultError
    hub_busy: _response_pb2.DefaultError
    hub_blocked_by_service_provider: _response_pb2.DefaultError
    hub_alarm_reset_required: _response_pb2.DefaultError
    hub_detected_malfunctions: _response_pb2.HubDetectedMalfunctionsError
    def __init__(self, timed_out: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., cancelled: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_offline: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_busy: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_blocked_by_service_provider: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_alarm_reset_required: _Optional[_Union[_response_pb2.DefaultError, _Mapping]] = ..., hub_detected_malfunctions: _Optional[_Union[_response_pb2.HubDetectedMalfunctionsError, _Mapping]] = ...) -> None: ...
