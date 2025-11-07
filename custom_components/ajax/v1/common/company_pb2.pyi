from v1.common import role_pb2 as _role_pb2
from v1.common import image_pb2 as _image_pb2
from v1.common import email_address_pb2 as _email_address_pb2
from v1.common import permission_pb2 as _permission_pb2
from v1.common import restore_permission_pb2 as _restore_permission_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Company(_message.Message):
    __slots__ = ("hex_id", "name", "status", "roles", "logo", "emails", "phones", "web_page_url", "permissions", "restore_permissions", "object_id", "privacy_override_management_authorization_status", "service_type", "enabled_features")
    class ServiceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SERVICE_TYPE_NO_INFO: _ClassVar[Company.ServiceType]
        SERVICE_TYPE_DEALER: _ClassVar[Company.ServiceType]
        SERVICE_TYPE_RESELLER: _ClassVar[Company.ServiceType]
    SERVICE_TYPE_NO_INFO: Company.ServiceType
    SERVICE_TYPE_DEALER: Company.ServiceType
    SERVICE_TYPE_RESELLER: Company.ServiceType
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACCEPTED: _ClassVar[Company.Status]
        REJECTED: _ClassVar[Company.Status]
        WAITING_FOR_VERIFICATION: _ClassVar[Company.Status]
    ACCEPTED: Company.Status
    REJECTED: Company.Status
    WAITING_FOR_VERIFICATION: Company.Status
    class PrivacyOverrideManagementAuthorizationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRIVACY_OVERRIDE_MANAGEMENT_AUTHORIZATION_STATUS_UNSPECIFIED: _ClassVar[Company.PrivacyOverrideManagementAuthorizationStatus]
        PRIVACY_OVERRIDE_MANAGEMENT_AUTHORIZATION_STATUS_AUTHORIZED: _ClassVar[Company.PrivacyOverrideManagementAuthorizationStatus]
        PRIVACY_OVERRIDE_MANAGEMENT_AUTHORIZATION_STATUS_UNAUTHORIZED: _ClassVar[Company.PrivacyOverrideManagementAuthorizationStatus]
    PRIVACY_OVERRIDE_MANAGEMENT_AUTHORIZATION_STATUS_UNSPECIFIED: Company.PrivacyOverrideManagementAuthorizationStatus
    PRIVACY_OVERRIDE_MANAGEMENT_AUTHORIZATION_STATUS_AUTHORIZED: Company.PrivacyOverrideManagementAuthorizationStatus
    PRIVACY_OVERRIDE_MANAGEMENT_AUTHORIZATION_STATUS_UNAUTHORIZED: Company.PrivacyOverrideManagementAuthorizationStatus
    class Feature(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FEATURE_UNSPECIFIED: _ClassVar[Company.Feature]
        FEATURE_HIDE_FACILITIES_ON_SEARCH: _ClassVar[Company.Feature]
    FEATURE_UNSPECIFIED: Company.Feature
    FEATURE_HIDE_FACILITIES_ON_SEARCH: Company.Feature
    class Logo(_message.Message):
        __slots__ = ("image_id", "images")
        IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
        IMAGES_FIELD_NUMBER: _ClassVar[int]
        image_id: str
        images: _containers.RepeatedCompositeFieldContainer[_image_pb2.Image]
        def __init__(self, image_id: _Optional[str] = ..., images: _Optional[_Iterable[_Union[_image_pb2.Image, _Mapping]]] = ...) -> None: ...
    class Phone(_message.Message):
        __slots__ = ("number", "description")
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        number: str
        description: str
        def __init__(self, number: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
    HEX_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    EMAILS_FIELD_NUMBER: _ClassVar[int]
    PHONES_FIELD_NUMBER: _ClassVar[int]
    WEB_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_OVERRIDE_MANAGEMENT_AUTHORIZATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FEATURES_FIELD_NUMBER: _ClassVar[int]
    hex_id: str
    name: str
    status: Company.Status
    roles: _containers.RepeatedScalarFieldContainer[_role_pb2.Role]
    logo: Company.Logo
    emails: _containers.RepeatedCompositeFieldContainer[_email_address_pb2.EmailAddress]
    phones: _containers.RepeatedCompositeFieldContainer[Company.Phone]
    web_page_url: str
    permissions: _containers.RepeatedScalarFieldContainer[_permission_pb2.Permission]
    restore_permissions: _containers.RepeatedScalarFieldContainer[_restore_permission_pb2.RestorePermission]
    object_id: str
    privacy_override_management_authorization_status: Company.PrivacyOverrideManagementAuthorizationStatus
    service_type: Company.ServiceType
    enabled_features: _containers.RepeatedScalarFieldContainer[Company.Feature]
    def __init__(self, hex_id: _Optional[str] = ..., name: _Optional[str] = ..., status: _Optional[_Union[Company.Status, str]] = ..., roles: _Optional[_Iterable[_Union[_role_pb2.Role, str]]] = ..., logo: _Optional[_Union[Company.Logo, _Mapping]] = ..., emails: _Optional[_Iterable[_Union[_email_address_pb2.EmailAddress, _Mapping]]] = ..., phones: _Optional[_Iterable[_Union[Company.Phone, _Mapping]]] = ..., web_page_url: _Optional[str] = ..., permissions: _Optional[_Iterable[_Union[_permission_pb2.Permission, str]]] = ..., restore_permissions: _Optional[_Iterable[_Union[_restore_permission_pb2.RestorePermission, str]]] = ..., object_id: _Optional[str] = ..., privacy_override_management_authorization_status: _Optional[_Union[Company.PrivacyOverrideManagementAuthorizationStatus, str]] = ..., service_type: _Optional[_Union[Company.ServiceType, str]] = ..., enabled_features: _Optional[_Iterable[_Union[Company.Feature, str]]] = ...) -> None: ...
