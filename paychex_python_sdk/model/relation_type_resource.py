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


class RelationTypeResource(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            relationshipTypeId = schemas.StrSchema
            relationshipTypeName = schemas.StrSchema
            __annotations__ = {
                "relationshipTypeId": relationshipTypeId,
                "relationshipTypeName": relationshipTypeName,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relationshipTypeId"]) -> MetaOapg.properties.relationshipTypeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relationshipTypeName"]) -> MetaOapg.properties.relationshipTypeName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["relationshipTypeId", "relationshipTypeName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relationshipTypeId"]) -> typing.Union[MetaOapg.properties.relationshipTypeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relationshipTypeName"]) -> typing.Union[MetaOapg.properties.relationshipTypeName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["relationshipTypeId", "relationshipTypeName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        relationshipTypeId: typing.Union[MetaOapg.properties.relationshipTypeId, str, schemas.Unset] = schemas.unset,
        relationshipTypeName: typing.Union[MetaOapg.properties.relationshipTypeName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RelationTypeResource':
        return super().__new__(
            cls,
            *args,
            relationshipTypeId=relationshipTypeId,
            relationshipTypeName=relationshipTypeName,
            _configuration=_configuration,
            **kwargs,
        )
