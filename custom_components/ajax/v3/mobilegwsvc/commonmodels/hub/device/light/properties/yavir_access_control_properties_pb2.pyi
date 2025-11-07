from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import yavir_access_control_type_pb2 as _yavir_access_control_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class YavirAccessControlProperties(_message.Message):
    __slots__ = ("yavir_access_control_type",)
    YAVIR_ACCESS_CONTROL_TYPE_FIELD_NUMBER: _ClassVar[int]
    yavir_access_control_type: _yavir_access_control_type_pb2.YavirAccessControlType
    def __init__(self, yavir_access_control_type: _Optional[_Union[_yavir_access_control_type_pb2.YavirAccessControlType, str]] = ...) -> None: ...
