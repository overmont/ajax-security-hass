from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RadioInterferenceDetectionPart(_message.Message):
    __slots__ = ("radio_interference_level", "radio_interference_detection", "radio_interference_detection_beep", "capabilities")
    class RadioInterferenceLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RADIO_INTERFERENCE_LEVEL_UNSPECIFIED: _ClassVar[RadioInterferenceDetectionPart.RadioInterferenceLevel]
        RADIO_INTERFERENCE_LEVEL_HIGH: _ClassVar[RadioInterferenceDetectionPart.RadioInterferenceLevel]
        RADIO_INTERFERENCE_LEVEL_OK: _ClassVar[RadioInterferenceDetectionPart.RadioInterferenceLevel]
        RADIO_INTERFERENCE_LEVEL_NOT_APPLICABLE: _ClassVar[RadioInterferenceDetectionPart.RadioInterferenceLevel]
    RADIO_INTERFERENCE_LEVEL_UNSPECIFIED: RadioInterferenceDetectionPart.RadioInterferenceLevel
    RADIO_INTERFERENCE_LEVEL_HIGH: RadioInterferenceDetectionPart.RadioInterferenceLevel
    RADIO_INTERFERENCE_LEVEL_OK: RadioInterferenceDetectionPart.RadioInterferenceLevel
    RADIO_INTERFERENCE_LEVEL_NOT_APPLICABLE: RadioInterferenceDetectionPart.RadioInterferenceLevel
    class RadioInterferenceDetection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RADIO_INTERFERENCE_DETECTION_UNSPECIFIED: _ClassVar[RadioInterferenceDetectionPart.RadioInterferenceDetection]
        RADIO_INTERFERENCE_DETECTION_DISABLED: _ClassVar[RadioInterferenceDetectionPart.RadioInterferenceDetection]
        RADIO_INTERFERENCE_DETECTION_ENABLED: _ClassVar[RadioInterferenceDetectionPart.RadioInterferenceDetection]
    RADIO_INTERFERENCE_DETECTION_UNSPECIFIED: RadioInterferenceDetectionPart.RadioInterferenceDetection
    RADIO_INTERFERENCE_DETECTION_DISABLED: RadioInterferenceDetectionPart.RadioInterferenceDetection
    RADIO_INTERFERENCE_DETECTION_ENABLED: RadioInterferenceDetectionPart.RadioInterferenceDetection
    class RadioInterferenceDetectionBeep(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RADIO_INTERFERENCE_DETECTION_BEEP_UNSPECIFIED: _ClassVar[RadioInterferenceDetectionPart.RadioInterferenceDetectionBeep]
        RADIO_INTERFERENCE_DETECTION_BEEP_DISABLED: _ClassVar[RadioInterferenceDetectionPart.RadioInterferenceDetectionBeep]
        RADIO_INTERFERENCE_DETECTION_BEEP_ENABLED: _ClassVar[RadioInterferenceDetectionPart.RadioInterferenceDetectionBeep]
    RADIO_INTERFERENCE_DETECTION_BEEP_UNSPECIFIED: RadioInterferenceDetectionPart.RadioInterferenceDetectionBeep
    RADIO_INTERFERENCE_DETECTION_BEEP_DISABLED: RadioInterferenceDetectionPart.RadioInterferenceDetectionBeep
    RADIO_INTERFERENCE_DETECTION_BEEP_ENABLED: RadioInterferenceDetectionPart.RadioInterferenceDetectionBeep
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[RadioInterferenceDetectionPart.Capability]
        CAPABILITY_INTERFERENCE_DETECTION: _ClassVar[RadioInterferenceDetectionPart.Capability]
    CAPABILITY_UNSPECIFIED: RadioInterferenceDetectionPart.Capability
    CAPABILITY_INTERFERENCE_DETECTION: RadioInterferenceDetectionPart.Capability
    class RadioInterferenceDetectionSettings(_message.Message):
        __slots__ = ("radio_interference_detection", "radio_interference_detection_beep")
        RADIO_INTERFERENCE_DETECTION_FIELD_NUMBER: _ClassVar[int]
        RADIO_INTERFERENCE_DETECTION_BEEP_FIELD_NUMBER: _ClassVar[int]
        radio_interference_detection: RadioInterferenceDetectionPart.RadioInterferenceDetection
        radio_interference_detection_beep: RadioInterferenceDetectionPart.RadioInterferenceDetectionBeep
        def __init__(self, radio_interference_detection: _Optional[_Union[RadioInterferenceDetectionPart.RadioInterferenceDetection, str]] = ..., radio_interference_detection_beep: _Optional[_Union[RadioInterferenceDetectionPart.RadioInterferenceDetectionBeep, str]] = ...) -> None: ...
    RADIO_INTERFERENCE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    RADIO_INTERFERENCE_DETECTION_FIELD_NUMBER: _ClassVar[int]
    RADIO_INTERFERENCE_DETECTION_BEEP_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    radio_interference_level: RadioInterferenceDetectionPart.RadioInterferenceLevel
    radio_interference_detection: RadioInterferenceDetectionPart.RadioInterferenceDetection
    radio_interference_detection_beep: RadioInterferenceDetectionPart.RadioInterferenceDetectionBeep
    capabilities: _containers.RepeatedScalarFieldContainer[RadioInterferenceDetectionPart.Capability]
    def __init__(self, radio_interference_level: _Optional[_Union[RadioInterferenceDetectionPart.RadioInterferenceLevel, str]] = ..., radio_interference_detection: _Optional[_Union[RadioInterferenceDetectionPart.RadioInterferenceDetection, str]] = ..., radio_interference_detection_beep: _Optional[_Union[RadioInterferenceDetectionPart.RadioInterferenceDetectionBeep, str]] = ..., capabilities: _Optional[_Iterable[_Union[RadioInterferenceDetectionPart.Capability, str]]] = ...) -> None: ...
