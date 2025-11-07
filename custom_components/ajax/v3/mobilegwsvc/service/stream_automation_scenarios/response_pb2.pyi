from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.scheduled_acesss import scheduled_access_pb2 as _scheduled_access_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamHubAutomationScenariosResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("snapshot", "created", "updated", "deleted")
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        CREATED_FIELD_NUMBER: _ClassVar[int]
        UPDATED_FIELD_NUMBER: _ClassVar[int]
        DELETED_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamHubAutomationScenariosResponse.Snapshot
        created: StreamHubAutomationScenariosResponse.Created
        updated: StreamHubAutomationScenariosResponse.Updated
        deleted: StreamHubAutomationScenariosResponse.Deleted
        def __init__(self, snapshot: _Optional[_Union[StreamHubAutomationScenariosResponse.Snapshot, _Mapping]] = ..., created: _Optional[_Union[StreamHubAutomationScenariosResponse.Created, _Mapping]] = ..., updated: _Optional[_Union[StreamHubAutomationScenariosResponse.Updated, _Mapping]] = ..., deleted: _Optional[_Union[StreamHubAutomationScenariosResponse.Deleted, _Mapping]] = ...) -> None: ...
    class Snapshot(_message.Message):
        __slots__ = ("automation_scenarios",)
        AUTOMATION_SCENARIOS_FIELD_NUMBER: _ClassVar[int]
        automation_scenarios: _containers.RepeatedCompositeFieldContainer[StreamHubAutomationScenariosResponse.AutomationScenarioObject]
        def __init__(self, automation_scenarios: _Optional[_Iterable[_Union[StreamHubAutomationScenariosResponse.AutomationScenarioObject, _Mapping]]] = ...) -> None: ...
    class Created(_message.Message):
        __slots__ = ("automation_scenario",)
        AUTOMATION_SCENARIO_FIELD_NUMBER: _ClassVar[int]
        automation_scenario: StreamHubAutomationScenariosResponse.AutomationScenarioObject
        def __init__(self, automation_scenario: _Optional[_Union[StreamHubAutomationScenariosResponse.AutomationScenarioObject, _Mapping]] = ...) -> None: ...
    class Updated(_message.Message):
        __slots__ = ("automation_scenario",)
        AUTOMATION_SCENARIO_FIELD_NUMBER: _ClassVar[int]
        automation_scenario: StreamHubAutomationScenariosResponse.AutomationScenarioObject
        def __init__(self, automation_scenario: _Optional[_Union[StreamHubAutomationScenariosResponse.AutomationScenarioObject, _Mapping]] = ...) -> None: ...
    class Deleted(_message.Message):
        __slots__ = ("scheduled_access_id",)
        SCHEDULED_ACCESS_ID_FIELD_NUMBER: _ClassVar[int]
        scheduled_access_id: int
        def __init__(self, scheduled_access_id: _Optional[int] = ...) -> None: ...
    class AutomationScenarioObject(_message.Message):
        __slots__ = ("scheduled_access",)
        SCHEDULED_ACCESS_FIELD_NUMBER: _ClassVar[int]
        scheduled_access: _scheduled_access_pb2.ScheduledAccess
        def __init__(self, scheduled_access: _Optional[_Union[_scheduled_access_pb2.ScheduledAccess, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("bad_request", "hub_not_found", "request_timeout", "permission_denied")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        HUB_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        REQUEST_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        hub_not_found: _response_pb2.Error
        request_timeout: _response_pb2.Error
        permission_denied: _response_pb2.Error
        def __init__(self, bad_request: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., hub_not_found: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., request_timeout: _Optional[_Union[_response_pb2.Error, _Mapping]] = ..., permission_denied: _Optional[_Union[_response_pb2.Error, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamHubAutomationScenariosResponse.Success
    failure: StreamHubAutomationScenariosResponse.Failure
    def __init__(self, success: _Optional[_Union[StreamHubAutomationScenariosResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[StreamHubAutomationScenariosResponse.Failure, _Mapping]] = ...) -> None: ...
