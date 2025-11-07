from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import masking_sensitivity_pb2 as _masking_sensitivity_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommonMaskingPart(_message.Message):
    __slots__ = ("antimasking", "is_masked_status", "masking_sensitivity", "capabilities", "icing_detect")
    class Antimasking(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ANTIMASKING_UNSPECIFIED: _ClassVar[CommonMaskingPart.Antimasking]
        ANTIMASKING_DISABLED: _ClassVar[CommonMaskingPart.Antimasking]
        ANTIMASKING_ENABLED: _ClassVar[CommonMaskingPart.Antimasking]
    ANTIMASKING_UNSPECIFIED: CommonMaskingPart.Antimasking
    ANTIMASKING_DISABLED: CommonMaskingPart.Antimasking
    ANTIMASKING_ENABLED: CommonMaskingPart.Antimasking
    class IcingDetect(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ICING_DETECT_UNSPECIFIED: _ClassVar[CommonMaskingPart.IcingDetect]
        ICING_DETECT_DISABLED: _ClassVar[CommonMaskingPart.IcingDetect]
        ICING_DETECT_ENABLED: _ClassVar[CommonMaskingPart.IcingDetect]
    ICING_DETECT_UNSPECIFIED: CommonMaskingPart.IcingDetect
    ICING_DETECT_DISABLED: CommonMaskingPart.IcingDetect
    ICING_DETECT_ENABLED: CommonMaskingPart.IcingDetect
    class IsMaskedStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IS_MASKED_STATUS_UNSPECIFIED: _ClassVar[CommonMaskingPart.IsMaskedStatus]
        IS_MASKED_STATUS_OFF: _ClassVar[CommonMaskingPart.IsMaskedStatus]
        IS_MASKED_STATUS_ON: _ClassVar[CommonMaskingPart.IsMaskedStatus]
        IS_MASKED_STATUS_ALERT: _ClassVar[CommonMaskingPart.IsMaskedStatus]
    IS_MASKED_STATUS_UNSPECIFIED: CommonMaskingPart.IsMaskedStatus
    IS_MASKED_STATUS_OFF: CommonMaskingPart.IsMaskedStatus
    IS_MASKED_STATUS_ON: CommonMaskingPart.IsMaskedStatus
    IS_MASKED_STATUS_ALERT: CommonMaskingPart.IsMaskedStatus
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[CommonMaskingPart.Capability]
        CAPABILITY_MASKING_SENSITIVITY: _ClassVar[CommonMaskingPart.Capability]
        CAPABILITY_ICING_DETECT: _ClassVar[CommonMaskingPart.Capability]
    CAPABILITY_UNSPECIFIED: CommonMaskingPart.Capability
    CAPABILITY_MASKING_SENSITIVITY: CommonMaskingPart.Capability
    CAPABILITY_ICING_DETECT: CommonMaskingPart.Capability
    class CommonMaskingPartSettings(_message.Message):
        __slots__ = ("antimasking", "masking_sensitivity", "icing_detect")
        ANTIMASKING_FIELD_NUMBER: _ClassVar[int]
        MASKING_SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
        ICING_DETECT_FIELD_NUMBER: _ClassVar[int]
        antimasking: CommonMaskingPart.Antimasking
        masking_sensitivity: _masking_sensitivity_pb2.MaskingSensitivity
        icing_detect: CommonMaskingPart.IcingDetect
        def __init__(self, antimasking: _Optional[_Union[CommonMaskingPart.Antimasking, str]] = ..., masking_sensitivity: _Optional[_Union[_masking_sensitivity_pb2.MaskingSensitivity, _Mapping]] = ..., icing_detect: _Optional[_Union[CommonMaskingPart.IcingDetect, str]] = ...) -> None: ...
    ANTIMASKING_FIELD_NUMBER: _ClassVar[int]
    IS_MASKED_STATUS_FIELD_NUMBER: _ClassVar[int]
    MASKING_SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    ICING_DETECT_FIELD_NUMBER: _ClassVar[int]
    antimasking: CommonMaskingPart.Antimasking
    is_masked_status: CommonMaskingPart.IsMaskedStatus
    masking_sensitivity: _masking_sensitivity_pb2.MaskingSensitivity
    capabilities: _containers.RepeatedScalarFieldContainer[CommonMaskingPart.Capability]
    icing_detect: CommonMaskingPart.IcingDetect
    def __init__(self, antimasking: _Optional[_Union[CommonMaskingPart.Antimasking, str]] = ..., is_masked_status: _Optional[_Union[CommonMaskingPart.IsMaskedStatus, str]] = ..., masking_sensitivity: _Optional[_Union[_masking_sensitivity_pb2.MaskingSensitivity, _Mapping]] = ..., capabilities: _Optional[_Iterable[_Union[CommonMaskingPart.Capability, str]]] = ..., icing_detect: _Optional[_Union[CommonMaskingPart.IcingDetect, str]] = ...) -> None: ...
