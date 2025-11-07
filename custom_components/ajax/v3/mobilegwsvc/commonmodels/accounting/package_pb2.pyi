from systems.ajax.api.mobile.v2.common.accounting import feature_target_pb2 as _feature_target_pb2
from systems.ajax.api.mobile.v2.common.accounting import category_pb2 as _category_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Package(_message.Message):
    __slots__ = ("id", "name", "name_lokalise_key", "description", "description_lokalise_key", "feature_target", "category", "service_lokalise_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_LOKALISE_KEY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_LOKALISE_KEY_FIELD_NUMBER: _ClassVar[int]
    FEATURE_TARGET_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SERVICE_LOKALISE_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    name_lokalise_key: str
    description: str
    description_lokalise_key: str
    feature_target: _feature_target_pb2.FeatureTarget
    category: _category_pb2.Category
    service_lokalise_id: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., name_lokalise_key: _Optional[str] = ..., description: _Optional[str] = ..., description_lokalise_key: _Optional[str] = ..., feature_target: _Optional[_Union[_feature_target_pb2.FeatureTarget, str]] = ..., category: _Optional[_Union[_category_pb2.Category, str]] = ..., service_lokalise_id: _Optional[str] = ...) -> None: ...
