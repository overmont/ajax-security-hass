from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamDetectionZoneTestRequest(_message.Message):
    __slots__ = ("hub_detection_zone_test", "device_detection_zone_test")
    class HubDetectionZoneTest(_message.Message):
        __slots__ = ("hub_id",)
        HUB_ID_FIELD_NUMBER: _ClassVar[int]
        hub_id: str
        def __init__(self, hub_id: _Optional[str] = ...) -> None: ...
    class DeviceDetectionZoneTest(_message.Message):
        __slots__ = ("hub_id", "device_id")
        HUB_ID_FIELD_NUMBER: _ClassVar[int]
        DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
        hub_id: str
        device_id: str
        def __init__(self, hub_id: _Optional[str] = ..., device_id: _Optional[str] = ...) -> None: ...
    HUB_DETECTION_ZONE_TEST_FIELD_NUMBER: _ClassVar[int]
    DEVICE_DETECTION_ZONE_TEST_FIELD_NUMBER: _ClassVar[int]
    hub_detection_zone_test: StreamDetectionZoneTestRequest.HubDetectionZoneTest
    device_detection_zone_test: StreamDetectionZoneTestRequest.DeviceDetectionZoneTest
    def __init__(self, hub_detection_zone_test: _Optional[_Union[StreamDetectionZoneTestRequest.HubDetectionZoneTest, _Mapping]] = ..., device_detection_zone_test: _Optional[_Union[StreamDetectionZoneTestRequest.DeviceDetectionZoneTest, _Mapping]] = ...) -> None: ...
