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


class LaborAssignmentResource(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The state representation of Labor Assignments within a company.
    """


    class MetaOapg:
        
        class properties:
            laborAssignmentId = schemas.StrSchema
            name = schemas.StrSchema
            startDate = schemas.DateTimeSchema
            endDate = schemas.DateTimeSchema
            organizationId = schemas.StrSchema
            positionId = schemas.StrSchema
            
            
            class links(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Link']:
                        return Link
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Link'], typing.List['Link']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'links':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Link':
                    return super().__getitem__(i)
            locationId = schemas.StrSchema
            __annotations__ = {
                "laborAssignmentId": laborAssignmentId,
                "name": name,
                "startDate": startDate,
                "endDate": endDate,
                "organizationId": organizationId,
                "positionId": positionId,
                "links": links,
                "locationId": locationId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["laborAssignmentId"]) -> MetaOapg.properties.laborAssignmentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organizationId"]) -> MetaOapg.properties.organizationId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["positionId"]) -> MetaOapg.properties.positionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> MetaOapg.properties.links: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locationId"]) -> MetaOapg.properties.locationId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["laborAssignmentId", "name", "startDate", "endDate", "organizationId", "positionId", "links", "locationId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["laborAssignmentId"]) -> typing.Union[MetaOapg.properties.laborAssignmentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDate"]) -> typing.Union[MetaOapg.properties.startDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endDate"]) -> typing.Union[MetaOapg.properties.endDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organizationId"]) -> typing.Union[MetaOapg.properties.organizationId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["positionId"]) -> typing.Union[MetaOapg.properties.positionId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union[MetaOapg.properties.links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locationId"]) -> typing.Union[MetaOapg.properties.locationId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["laborAssignmentId", "name", "startDate", "endDate", "organizationId", "positionId", "links", "locationId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        laborAssignmentId: typing.Union[MetaOapg.properties.laborAssignmentId, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        startDate: typing.Union[MetaOapg.properties.startDate, str, datetime, schemas.Unset] = schemas.unset,
        endDate: typing.Union[MetaOapg.properties.endDate, str, datetime, schemas.Unset] = schemas.unset,
        organizationId: typing.Union[MetaOapg.properties.organizationId, str, schemas.Unset] = schemas.unset,
        positionId: typing.Union[MetaOapg.properties.positionId, str, schemas.Unset] = schemas.unset,
        links: typing.Union[MetaOapg.properties.links, list, tuple, schemas.Unset] = schemas.unset,
        locationId: typing.Union[MetaOapg.properties.locationId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LaborAssignmentResource':
        return super().__new__(
            cls,
            *args,
            laborAssignmentId=laborAssignmentId,
            name=name,
            startDate=startDate,
            endDate=endDate,
            organizationId=organizationId,
            positionId=positionId,
            links=links,
            locationId=locationId,
            _configuration=_configuration,
            **kwargs,
        )

from paychex_python_sdk.model.link import Link
