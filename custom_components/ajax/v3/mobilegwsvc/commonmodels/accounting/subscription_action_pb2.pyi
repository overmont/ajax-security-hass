from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUBSCRIPTION_ACTION_UNSPECIFIED: _ClassVar[SubscriptionAction]
    SUBSCRIPTION_ACTION_DEACTIVATE: _ClassVar[SubscriptionAction]
    SUBSCRIPTION_ACTION_SCHEDULE_DEACTIVATION: _ClassVar[SubscriptionAction]
    SUBSCRIPTION_ACTION_CANCEL_SCHEDULED_DEACTIVATION: _ClassVar[SubscriptionAction]
    SUBSCRIPTION_ACTION_CHANGE_PACKAGE: _ClassVar[SubscriptionAction]
    SUBSCRIPTION_ACTION_MODIFY_TARGETS: _ClassVar[SubscriptionAction]
    SUBSCRIPTION_ACTION_GET_HEALTH_CHECK_DETAILS: _ClassVar[SubscriptionAction]
SUBSCRIPTION_ACTION_UNSPECIFIED: SubscriptionAction
SUBSCRIPTION_ACTION_DEACTIVATE: SubscriptionAction
SUBSCRIPTION_ACTION_SCHEDULE_DEACTIVATION: SubscriptionAction
SUBSCRIPTION_ACTION_CANCEL_SCHEDULED_DEACTIVATION: SubscriptionAction
SUBSCRIPTION_ACTION_CHANGE_PACKAGE: SubscriptionAction
SUBSCRIPTION_ACTION_MODIFY_TARGETS: SubscriptionAction
SUBSCRIPTION_ACTION_GET_HEALTH_CHECK_DETAILS: SubscriptionAction
