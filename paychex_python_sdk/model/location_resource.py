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


class LocationResource(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The state representation of Locations within a company.
    """


    class MetaOapg:
        
        class properties:
            locationId = schemas.StrSchema
            name = schemas.StrSchema
        
            @staticmethod
            def address() -> typing.Type['CommunicationResource']:
                return CommunicationResource
            
            
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
            movedIn = schemas.DateTimeSchema
            movedOut = schemas.DateTimeSchema
            __annotations__ = {
                "locationId": locationId,
                "name": name,
                "address": address,
                "links": links,
                "movedIn": movedIn,
                "movedOut": movedOut,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locationId"]) -> MetaOapg.properties.locationId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> 'CommunicationResource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> MetaOapg.properties.links: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["movedIn"]) -> MetaOapg.properties.movedIn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["movedOut"]) -> MetaOapg.properties.movedOut: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["locationId", "name", "address", "links", "movedIn", "movedOut", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locationId"]) -> typing.Union[MetaOapg.properties.locationId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union['CommunicationResource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union[MetaOapg.properties.links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["movedIn"]) -> typing.Union[MetaOapg.properties.movedIn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["movedOut"]) -> typing.Union[MetaOapg.properties.movedOut, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["locationId", "name", "address", "links", "movedIn", "movedOut", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        locationId: typing.Union[MetaOapg.properties.locationId, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        address: typing.Union['CommunicationResource', schemas.Unset] = schemas.unset,
        links: typing.Union[MetaOapg.properties.links, list, tuple, schemas.Unset] = schemas.unset,
        movedIn: typing.Union[MetaOapg.properties.movedIn, str, datetime, schemas.Unset] = schemas.unset,
        movedOut: typing.Union[MetaOapg.properties.movedOut, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LocationResource':
        return super().__new__(
            cls,
            *args,
            locationId=locationId,
            name=name,
            address=address,
            links=links,
            movedIn=movedIn,
            movedOut=movedOut,
            _configuration=_configuration,
            **kwargs,
        )

from paychex_python_sdk.model.communication_resource import CommunicationResource
from paychex_python_sdk.model.link import Link
