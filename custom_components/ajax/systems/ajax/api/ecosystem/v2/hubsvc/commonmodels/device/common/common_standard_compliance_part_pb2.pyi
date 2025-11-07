from systems.ajax.api.ecosystem.v2.commonmodels.device.common import security_standart_pb2 as _security_standart_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommonStandardCompliancePart(_message.Message):
    __slots__ = ("current_standard", "pd_compliance", "en_compliance", "sia_cp_compliance")
    class ComplianceInfo(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPLIANCE_INFO_UNSPECIFIED: _ClassVar[CommonStandardCompliancePart.ComplianceInfo]
        COMPLIANCE_INFO_COMPLIANT: _ClassVar[CommonStandardCompliancePart.ComplianceInfo]
        COMPLIANCE_INFO_WARNING: _ClassVar[CommonStandardCompliancePart.ComplianceInfo]
    COMPLIANCE_INFO_UNSPECIFIED: CommonStandardCompliancePart.ComplianceInfo
    COMPLIANCE_INFO_COMPLIANT: CommonStandardCompliancePart.ComplianceInfo
    COMPLIANCE_INFO_WARNING: CommonStandardCompliancePart.ComplianceInfo
    CURRENT_STANDARD_FIELD_NUMBER: _ClassVar[int]
    PD_COMPLIANCE_FIELD_NUMBER: _ClassVar[int]
    EN_COMPLIANCE_FIELD_NUMBER: _ClassVar[int]
    SIA_CP_COMPLIANCE_FIELD_NUMBER: _ClassVar[int]
    current_standard: _security_standart_pb2.SecurityStandard
    pd_compliance: CommonStandardCompliancePart.ComplianceInfo
    en_compliance: CommonStandardCompliancePart.ComplianceInfo
    sia_cp_compliance: CommonStandardCompliancePart.ComplianceInfo
    def __init__(self, current_standard: _Optional[_Union[_security_standart_pb2.SecurityStandard, str]] = ..., pd_compliance: _Optional[_Union[CommonStandardCompliancePart.ComplianceInfo, str]] = ..., en_compliance: _Optional[_Union[CommonStandardCompliancePart.ComplianceInfo, str]] = ..., sia_cp_compliance: _Optional[_Union[CommonStandardCompliancePart.ComplianceInfo, str]] = ...) -> None: ...
