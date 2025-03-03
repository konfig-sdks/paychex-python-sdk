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


class RelationshipResource(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The relationship for this worker contract. Required for POST contacts.
    """


    class MetaOapg:
        
        class properties:
            relationshipId = schemas.StrSchema
            relationWeid = schemas.StrSchema
        
            @staticmethod
            def relationshipType() -> typing.Type['RelationTypeResource1']:
                return RelationTypeResource1
            primary = schemas.BoolSchema
        
            @staticmethod
            def person() -> typing.Type['PersonResource']:
                return PersonResource
        
            @staticmethod
            def entity() -> typing.Type['EntityResource']:
                return EntityResource
            __annotations__ = {
                "relationshipId": relationshipId,
                "relationWeid": relationWeid,
                "relationshipType": relationshipType,
                "primary": primary,
                "person": person,
                "entity": entity,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relationshipId"]) -> MetaOapg.properties.relationshipId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relationWeid"]) -> MetaOapg.properties.relationWeid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relationshipType"]) -> 'RelationTypeResource1': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primary"]) -> MetaOapg.properties.primary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["person"]) -> 'PersonResource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entity"]) -> 'EntityResource': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["relationshipId", "relationWeid", "relationshipType", "primary", "person", "entity", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relationshipId"]) -> typing.Union[MetaOapg.properties.relationshipId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relationWeid"]) -> typing.Union[MetaOapg.properties.relationWeid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relationshipType"]) -> typing.Union['RelationTypeResource1', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primary"]) -> typing.Union[MetaOapg.properties.primary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["person"]) -> typing.Union['PersonResource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entity"]) -> typing.Union['EntityResource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["relationshipId", "relationWeid", "relationshipType", "primary", "person", "entity", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        relationshipId: typing.Union[MetaOapg.properties.relationshipId, str, schemas.Unset] = schemas.unset,
        relationWeid: typing.Union[MetaOapg.properties.relationWeid, str, schemas.Unset] = schemas.unset,
        relationshipType: typing.Union['RelationTypeResource1', schemas.Unset] = schemas.unset,
        primary: typing.Union[MetaOapg.properties.primary, bool, schemas.Unset] = schemas.unset,
        person: typing.Union['PersonResource', schemas.Unset] = schemas.unset,
        entity: typing.Union['EntityResource', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RelationshipResource':
        return super().__new__(
            cls,
            *args,
            relationshipId=relationshipId,
            relationWeid=relationWeid,
            relationshipType=relationshipType,
            primary=primary,
            person=person,
            entity=entity,
            _configuration=_configuration,
            **kwargs,
        )

from paychex_python_sdk.model.entity_resource import EntityResource
from paychex_python_sdk.model.person_resource import PersonResource
from paychex_python_sdk.model.relation_type_resource1 import RelationTypeResource1
