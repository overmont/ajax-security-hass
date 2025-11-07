from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Country(_message.Message):
    __slots__ = ("code", "name")
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    code: str
    name: str
    def __init__(self, code: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class GetCountriesRequest(_message.Message):
    __slots__ = ("locale",)
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    locale: str
    def __init__(self, locale: _Optional[str] = ...) -> None: ...

class GetCountriesResponse(_message.Message):
    __slots__ = ("locale", "countries")
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    COUNTRIES_FIELD_NUMBER: _ClassVar[int]
    locale: str
    countries: _containers.RepeatedCompositeFieldContainer[Country]
    def __init__(self, locale: _Optional[str] = ..., countries: _Optional[_Iterable[_Union[Country, _Mapping]]] = ...) -> None: ...
