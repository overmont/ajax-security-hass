from systems.ajax.api.mobile.v2.common.accounting import feature_target_pb2 as _feature_target_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActivateServicesRequest(_message.Message):
    __slots__ = ("feature_target_id", "feature_target", "service_to_activate", "reseller_id", "agreement_version")
    class ServiceToActivate(_message.Message):
        __slots__ = ("feature_id", "package_id")
        FEATURE_ID_FIELD_NUMBER: _ClassVar[int]
        PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
        feature_id: str
        package_id: str
        def __init__(self, feature_id: _Optional[str] = ..., package_id: _Optional[str] = ...) -> None: ...
    FEATURE_TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    FEATURE_TARGET_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TO_ACTIVATE_FIELD_NUMBER: _ClassVar[int]
    RESELLER_ID_FIELD_NUMBER: _ClassVar[int]
    AGREEMENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    feature_target_id: _containers.RepeatedScalarFieldContainer[str]
    feature_target: _feature_target_pb2.FeatureTarget
    service_to_activate: _containers.RepeatedCompositeFieldContainer[ActivateServicesRequest.ServiceToActivate]
    reseller_id: str
    agreement_version: str
    def __init__(self, feature_target_id: _Optional[_Iterable[str]] = ..., feature_target: _Optional[_Union[_feature_target_pb2.FeatureTarget, str]] = ..., service_to_activate: _Optional[_Iterable[_Union[ActivateServicesRequest.ServiceToActivate, _Mapping]]] = ..., reseller_id: _Optional[str] = ..., agreement_version: _Optional[str] = ...) -> None: ...
