from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import wire_input_alarm_type_pb2 as _wire_input_alarm_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CustomAlarmTypeInfo(_message.Message):
    __slots__ = ("custom_alarm_type",)
    CUSTOM_ALARM_TYPE_FIELD_NUMBER: _ClassVar[int]
    custom_alarm_type: _wire_input_alarm_type_pb2.CustomAlarmType
    def __init__(self, custom_alarm_type: _Optional[_Union[_wire_input_alarm_type_pb2.CustomAlarmType, str]] = ...) -> None: ...
