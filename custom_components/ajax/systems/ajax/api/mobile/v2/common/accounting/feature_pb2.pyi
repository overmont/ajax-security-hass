from systems.ajax.api.mobile.v2.common.accounting import feature_target_pb2 as _feature_target_pb2
from systems.ajax.api.mobile.v2.common.accounting import category_pb2 as _category_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FeatureState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FEATURE_STATE_NO_INFO: _ClassVar[FeatureState]
    FEATURE_STATE_ACTIVE: _ClassVar[FeatureState]
    FEATURE_STATE_INACTIVE: _ClassVar[FeatureState]
FEATURE_STATE_NO_INFO: FeatureState
FEATURE_STATE_ACTIVE: FeatureState
FEATURE_STATE_INACTIVE: FeatureState

class Feature(_message.Message):
    __slots__ = ("id", "name", "description", "feature_target", "name_lokalise_key", "description_lokalise_key", "category", "service_lokalise_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FEATURE_TARGET_FIELD_NUMBER: _ClassVar[int]
    NAME_LOKALISE_KEY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_LOKALISE_KEY_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SERVICE_LOKALISE_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    feature_target: _feature_target_pb2.FeatureTarget
    name_lokalise_key: str
    description_lokalise_key: str
    category: _category_pb2.Category
    service_lokalise_id: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., feature_target: _Optional[_Union[_feature_target_pb2.FeatureTarget, str]] = ..., name_lokalise_key: _Optional[str] = ..., description_lokalise_key: _Optional[str] = ..., category: _Optional[_Union[_category_pb2.Category, str]] = ..., service_lokalise_id: _Optional[str] = ...) -> None: ...
