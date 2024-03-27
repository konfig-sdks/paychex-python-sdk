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


class WorkerStatus(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The state representation of allowed worker statuses configured for the company.
    """


    class MetaOapg:
        
        class properties:
            workerStatusId = schemas.StrSchema
            statusType = schemas.StrSchema
            statusReason = schemas.StrSchema
            
            
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
            __annotations__ = {
                "workerStatusId": workerStatusId,
                "statusType": statusType,
                "statusReason": statusReason,
                "links": links,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workerStatusId"]) -> MetaOapg.properties.workerStatusId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statusType"]) -> MetaOapg.properties.statusType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statusReason"]) -> MetaOapg.properties.statusReason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> MetaOapg.properties.links: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["workerStatusId", "statusType", "statusReason", "links", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workerStatusId"]) -> typing.Union[MetaOapg.properties.workerStatusId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statusType"]) -> typing.Union[MetaOapg.properties.statusType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statusReason"]) -> typing.Union[MetaOapg.properties.statusReason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union[MetaOapg.properties.links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["workerStatusId", "statusType", "statusReason", "links", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        workerStatusId: typing.Union[MetaOapg.properties.workerStatusId, str, schemas.Unset] = schemas.unset,
        statusType: typing.Union[MetaOapg.properties.statusType, str, schemas.Unset] = schemas.unset,
        statusReason: typing.Union[MetaOapg.properties.statusReason, str, schemas.Unset] = schemas.unset,
        links: typing.Union[MetaOapg.properties.links, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WorkerStatus':
        return super().__new__(
            cls,
            *args,
            workerStatusId=workerStatusId,
            statusType=statusType,
            statusReason=statusReason,
            links=links,
            _configuration=_configuration,
            **kwargs,
        )

from paychex_python_sdk.model.link import Link
