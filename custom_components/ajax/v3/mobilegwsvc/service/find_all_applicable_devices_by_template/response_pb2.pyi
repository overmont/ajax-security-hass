from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.space.device.light import light_device_id_pb2 as _light_device_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FindAllApplicableDevicesByTemplateResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("device_ids",)
        DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
        device_ids: _containers.RepeatedCompositeFieldContainer[_light_device_id_pb2.LightDeviceId]
        def __init__(self, device_ids: _Optional[_Iterable[_Union[_light_device_id_pb2.LightDeviceId, _Mapping]]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("illegal_argument", "permission_denied", "space_not_found")
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        illegal_argument: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_not_found: _response_pb2.Error
        def __init__(self, illegal_argument: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., space_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: FindAllApplicableDevicesByTemplateResponse.Success
    failure: FindAllApplicableDevicesByTemplateResponse.Failure
    def __init__(self, success: _Optional[_Union[FindAllApplicableDevicesByTemplateResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[FindAllApplicableDevicesByTemplateResponse.Failure, _Mapping]] = ...) -> None: ...
