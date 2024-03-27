# coding: utf-8

"""
    External API

      # Developer Resources  Refer [Developer Resources](https://developer.paychex.com/resources/overview/) for more details on API specification 

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from paychex_python_sdk import schemas  # noqa: F401


class PersonResource(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The person associated with this relationship. The relationship must have either a person or entity.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def name() -> typing.Type['NameResource1']:
                return NameResource1
        
            @staticmethod
            def communication() -> typing.Type['PersonCommunicationResource']:
                return PersonCommunicationResource
            __annotations__ = {
                "name": name,
                "communication": communication,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> 'NameResource1': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["communication"]) -> 'PersonCommunicationResource': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "communication", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union['NameResource1', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["communication"]) -> typing.Union['PersonCommunicationResource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "communication", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union['NameResource1', schemas.Unset] = schemas.unset,
        communication: typing.Union['PersonCommunicationResource', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PersonResource':
        return super().__new__(
            cls,
            *args,
            name=name,
            communication=communication,
            _configuration=_configuration,
            **kwargs,
        )

from paychex_python_sdk.model.name_resource1 import NameResource1
from paychex_python_sdk.model.person_communication_resource import PersonCommunicationResource
