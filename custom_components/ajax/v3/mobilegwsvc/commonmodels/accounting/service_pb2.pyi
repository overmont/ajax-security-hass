from systems.ajax.api.mobile.v2.common.accounting import feature_pb2 as _feature_pb2
from v3.mobilegwsvc.commonmodels.accounting import package_pb2 as _package_pb2
from v3.mobilegwsvc.commonmodels.accounting import current_service_agreement_pb2 as _current_service_agreement_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Service(_message.Message):
    __slots__ = ("feature", "package", "current_service_agreement", "max_target_count_to_assign")
    FEATURE_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SERVICE_AGREEMENT_FIELD_NUMBER: _ClassVar[int]
    MAX_TARGET_COUNT_TO_ASSIGN_FIELD_NUMBER: _ClassVar[int]
    feature: _feature_pb2.Feature
    package: _package_pb2.Package
    current_service_agreement: _current_service_agreement_pb2.CurrentServiceAgreement
    max_target_count_to_assign: int
    def __init__(self, feature: _Optional[_Union[_feature_pb2.Feature, _Mapping]] = ..., package: _Optional[_Union[_package_pb2.Package, _Mapping]] = ..., current_service_agreement: _Optional[_Union[_current_service_agreement_pb2.CurrentServiceAgreement, _Mapping]] = ..., max_target_count_to_assign: _Optional[int] = ...) -> None: ...
