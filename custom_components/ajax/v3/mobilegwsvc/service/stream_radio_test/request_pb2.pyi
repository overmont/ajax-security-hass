from v3.mobilegwsvc.commonmodels.hub.device.common import device_radio_test_type_pb2 as _device_radio_test_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamRadioTestRequest(_message.Message):
    __slots__ = ("hub_id", "device_id", "type")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    device_id: str
    type: _device_radio_test_type_pb2.DeviceRadioTestType
    def __init__(self, hub_id: _Optional[str] = ..., device_id: _Optional[str] = ..., type: _Optional[_Union[_device_radio_test_type_pb2.DeviceRadioTestType, str]] = ...) -> None: ...
