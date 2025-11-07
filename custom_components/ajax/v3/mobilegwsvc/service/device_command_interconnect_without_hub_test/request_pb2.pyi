from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import object_type_pb2 as _object_type_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceCommandInterconnectWithoutHubTestRequest(_message.Message):
    __slots__ = ("hub_id", "device_id", "object_type", "iwh_test_command")
    class IWHTestCommand(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IWH_TEST_COMMAND_UNSPECIFIED: _ClassVar[DeviceCommandInterconnectWithoutHubTestRequest.IWHTestCommand]
        IWH_TEST_COMMAND_START: _ClassVar[DeviceCommandInterconnectWithoutHubTestRequest.IWHTestCommand]
        IWH_TEST_COMMAND_STOP: _ClassVar[DeviceCommandInterconnectWithoutHubTestRequest.IWHTestCommand]
    IWH_TEST_COMMAND_UNSPECIFIED: DeviceCommandInterconnectWithoutHubTestRequest.IWHTestCommand
    IWH_TEST_COMMAND_START: DeviceCommandInterconnectWithoutHubTestRequest.IWHTestCommand
    IWH_TEST_COMMAND_STOP: DeviceCommandInterconnectWithoutHubTestRequest.IWHTestCommand
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    IWH_TEST_COMMAND_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    device_id: str
    object_type: _object_type_pb2.ObjectType
    iwh_test_command: DeviceCommandInterconnectWithoutHubTestRequest.IWHTestCommand
    def __init__(self, hub_id: _Optional[str] = ..., device_id: _Optional[str] = ..., object_type: _Optional[_Union[_object_type_pb2.ObjectType, _Mapping]] = ..., iwh_test_command: _Optional[_Union[DeviceCommandInterconnectWithoutHubTestRequest.IWHTestCommand, str]] = ...) -> None: ...
