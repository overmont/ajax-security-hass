from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.meta import meta_pb2 as _meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ArmingRestrictionsPart(_message.Message):
    __slots__ = ("integrity_checks",)
    class IntegrityCheckType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INTEGRITY_CHECK_TYPE_UNSPECIFIED: _ClassVar[ArmingRestrictionsPart.IntegrityCheckType]
        INTEGRITY_CHECK_TYPE_TAMPER: _ClassVar[ArmingRestrictionsPart.IntegrityCheckType]
    INTEGRITY_CHECK_TYPE_UNSPECIFIED: ArmingRestrictionsPart.IntegrityCheckType
    INTEGRITY_CHECK_TYPE_TAMPER: ArmingRestrictionsPart.IntegrityCheckType
    class IsEnabled(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IS_ENABLED_UNSPECIFIED: _ClassVar[ArmingRestrictionsPart.IsEnabled]
        IS_ENABLED_DISABLED: _ClassVar[ArmingRestrictionsPart.IsEnabled]
        IS_ENABLED_ENABLED: _ClassVar[ArmingRestrictionsPart.IsEnabled]
    IS_ENABLED_UNSPECIFIED: ArmingRestrictionsPart.IsEnabled
    IS_ENABLED_DISABLED: ArmingRestrictionsPart.IsEnabled
    IS_ENABLED_ENABLED: ArmingRestrictionsPart.IsEnabled
    class ArmingRestrictionsPartSettings(_message.Message):
        __slots__ = ("integrity_checks",)
        INTEGRITY_CHECKS_FIELD_NUMBER: _ClassVar[int]
        integrity_checks: _containers.RepeatedCompositeFieldContainer[ArmingRestrictionsPart.IntegrityCheck]
        def __init__(self, integrity_checks: _Optional[_Iterable[_Union[ArmingRestrictionsPart.IntegrityCheck, _Mapping]]] = ...) -> None: ...
    class IntegrityCheck(_message.Message):
        __slots__ = ("integrity_check_type", "is_enabled")
        INTEGRITY_CHECK_TYPE_FIELD_NUMBER: _ClassVar[int]
        IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        integrity_check_type: ArmingRestrictionsPart.IntegrityCheckType
        is_enabled: ArmingRestrictionsPart.IsEnabled
        def __init__(self, integrity_check_type: _Optional[_Union[ArmingRestrictionsPart.IntegrityCheckType, str]] = ..., is_enabled: _Optional[_Union[ArmingRestrictionsPart.IsEnabled, str]] = ...) -> None: ...
    INTEGRITY_CHECKS_FIELD_NUMBER: _ClassVar[int]
    integrity_checks: _containers.RepeatedCompositeFieldContainer[ArmingRestrictionsPart.IntegrityCheck]
    def __init__(self, integrity_checks: _Optional[_Iterable[_Union[ArmingRestrictionsPart.IntegrityCheck, _Mapping]]] = ...) -> None: ...
