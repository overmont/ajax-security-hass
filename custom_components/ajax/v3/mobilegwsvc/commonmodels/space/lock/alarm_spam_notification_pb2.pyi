from v3.mobilegwsvc.commonmodels.hub.device import hub_device_view_source_pb2 as _hub_device_view_source_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AlarmSpamNotification(_message.Message):
    __slots__ = ("spam_objects",)
    SPAM_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    spam_objects: _containers.RepeatedCompositeFieldContainer[SpamObject]
    def __init__(self, spam_objects: _Optional[_Iterable[_Union[SpamObject, _Mapping]]] = ...) -> None: ...

class SpamObject(_message.Message):
    __slots__ = ("hub_device",)
    HUB_DEVICE_FIELD_NUMBER: _ClassVar[int]
    hub_device: _hub_device_view_source_pb2.HubDeviceViewSource
    def __init__(self, hub_device: _Optional[_Union[_hub_device_view_source_pb2.HubDeviceViewSource, _Mapping]] = ...) -> None: ...
