from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.virtualobject import fire_zone_pb2 as _fire_zone_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamFireZoneResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("snapshot",)
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamFireZoneResponse.FireZones
        def __init__(self, snapshot: _Optional[_Union[StreamFireZoneResponse.FireZones, _Mapping]] = ...) -> None: ...
    class FireZones(_message.Message):
        __slots__ = ("fire_zones",)
        FIRE_ZONES_FIELD_NUMBER: _ClassVar[int]
        fire_zones: _containers.RepeatedCompositeFieldContainer[_fire_zone_pb2.FireZone]
        def __init__(self, fire_zones: _Optional[_Iterable[_Union[_fire_zone_pb2.FireZone, _Mapping]]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("message", "bad_request", "hub_not_found", "illegal_argument", "request_timeout")
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        HUB_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        REQUEST_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        message: str
        bad_request: _response_pb2.Error
        hub_not_found: _response_pb2.Error
        illegal_argument: _response_pb2.Error
        request_timeout: _response_pb2.Error
        def __init__(self, message: _Optional[str] = ..., bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., illegal_argument: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., request_timeout: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamFireZoneResponse.Success
    failure: StreamFireZoneResponse.Failure
    def __init__(self, success: _Optional[_Union[StreamFireZoneResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[StreamFireZoneResponse.Failure, _Mapping]] = ...) -> None: ...
