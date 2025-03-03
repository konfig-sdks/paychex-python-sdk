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


class ClientAccountRegistration(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.Int64Schema
            startDate = schemas.DateTimeSchema
            endDate = schemas.DateTimeSchema
            endReasonCode = schemas.StrSchema
            createdDate = schemas.DateTimeSchema
            createdByApplicationName = schemas.StrSchema
            createdByUserId = schemas.StrSchema
            createdByApplicationSubProcessName = schemas.StrSchema
            modifiedDate = schemas.DateTimeSchema
            modifiedByApplicationName = schemas.StrSchema
            modifiedByApplicationSubProcessName = schemas.StrSchema
            modifiedByUserId = schemas.StrSchema
        
            @staticmethod
            def client() -> typing.Type['Client']:
                return Client
        
            @staticmethod
            def clientAccount() -> typing.Type['ClientAccount']:
                return ClientAccount
            __annotations__ = {
                "id": id,
                "startDate": startDate,
                "endDate": endDate,
                "endReasonCode": endReasonCode,
                "createdDate": createdDate,
                "createdByApplicationName": createdByApplicationName,
                "createdByUserId": createdByUserId,
                "createdByApplicationSubProcessName": createdByApplicationSubProcessName,
                "modifiedDate": modifiedDate,
                "modifiedByApplicationName": modifiedByApplicationName,
                "modifiedByApplicationSubProcessName": modifiedByApplicationSubProcessName,
                "modifiedByUserId": modifiedByUserId,
                "client": client,
                "clientAccount": clientAccount,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endReasonCode"]) -> MetaOapg.properties.endReasonCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdDate"]) -> MetaOapg.properties.createdDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdByApplicationName"]) -> MetaOapg.properties.createdByApplicationName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdByUserId"]) -> MetaOapg.properties.createdByUserId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdByApplicationSubProcessName"]) -> MetaOapg.properties.createdByApplicationSubProcessName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modifiedDate"]) -> MetaOapg.properties.modifiedDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modifiedByApplicationName"]) -> MetaOapg.properties.modifiedByApplicationName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modifiedByApplicationSubProcessName"]) -> MetaOapg.properties.modifiedByApplicationSubProcessName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modifiedByUserId"]) -> MetaOapg.properties.modifiedByUserId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client"]) -> 'Client': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clientAccount"]) -> 'ClientAccount': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "startDate", "endDate", "endReasonCode", "createdDate", "createdByApplicationName", "createdByUserId", "createdByApplicationSubProcessName", "modifiedDate", "modifiedByApplicationName", "modifiedByApplicationSubProcessName", "modifiedByUserId", "client", "clientAccount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDate"]) -> typing.Union[MetaOapg.properties.startDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endDate"]) -> typing.Union[MetaOapg.properties.endDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endReasonCode"]) -> typing.Union[MetaOapg.properties.endReasonCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdDate"]) -> typing.Union[MetaOapg.properties.createdDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdByApplicationName"]) -> typing.Union[MetaOapg.properties.createdByApplicationName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdByUserId"]) -> typing.Union[MetaOapg.properties.createdByUserId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdByApplicationSubProcessName"]) -> typing.Union[MetaOapg.properties.createdByApplicationSubProcessName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modifiedDate"]) -> typing.Union[MetaOapg.properties.modifiedDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modifiedByApplicationName"]) -> typing.Union[MetaOapg.properties.modifiedByApplicationName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modifiedByApplicationSubProcessName"]) -> typing.Union[MetaOapg.properties.modifiedByApplicationSubProcessName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modifiedByUserId"]) -> typing.Union[MetaOapg.properties.modifiedByUserId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client"]) -> typing.Union['Client', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clientAccount"]) -> typing.Union['ClientAccount', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "startDate", "endDate", "endReasonCode", "createdDate", "createdByApplicationName", "createdByUserId", "createdByApplicationSubProcessName", "modifiedDate", "modifiedByApplicationName", "modifiedByApplicationSubProcessName", "modifiedByUserId", "client", "clientAccount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        startDate: typing.Union[MetaOapg.properties.startDate, str, datetime, schemas.Unset] = schemas.unset,
        endDate: typing.Union[MetaOapg.properties.endDate, str, datetime, schemas.Unset] = schemas.unset,
        endReasonCode: typing.Union[MetaOapg.properties.endReasonCode, str, schemas.Unset] = schemas.unset,
        createdDate: typing.Union[MetaOapg.properties.createdDate, str, datetime, schemas.Unset] = schemas.unset,
        createdByApplicationName: typing.Union[MetaOapg.properties.createdByApplicationName, str, schemas.Unset] = schemas.unset,
        createdByUserId: typing.Union[MetaOapg.properties.createdByUserId, str, schemas.Unset] = schemas.unset,
        createdByApplicationSubProcessName: typing.Union[MetaOapg.properties.createdByApplicationSubProcessName, str, schemas.Unset] = schemas.unset,
        modifiedDate: typing.Union[MetaOapg.properties.modifiedDate, str, datetime, schemas.Unset] = schemas.unset,
        modifiedByApplicationName: typing.Union[MetaOapg.properties.modifiedByApplicationName, str, schemas.Unset] = schemas.unset,
        modifiedByApplicationSubProcessName: typing.Union[MetaOapg.properties.modifiedByApplicationSubProcessName, str, schemas.Unset] = schemas.unset,
        modifiedByUserId: typing.Union[MetaOapg.properties.modifiedByUserId, str, schemas.Unset] = schemas.unset,
        client: typing.Union['Client', schemas.Unset] = schemas.unset,
        clientAccount: typing.Union['ClientAccount', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ClientAccountRegistration':
        return super().__new__(
            cls,
            *args,
            id=id,
            startDate=startDate,
            endDate=endDate,
            endReasonCode=endReasonCode,
            createdDate=createdDate,
            createdByApplicationName=createdByApplicationName,
            createdByUserId=createdByUserId,
            createdByApplicationSubProcessName=createdByApplicationSubProcessName,
            modifiedDate=modifiedDate,
            modifiedByApplicationName=modifiedByApplicationName,
            modifiedByApplicationSubProcessName=modifiedByApplicationSubProcessName,
            modifiedByUserId=modifiedByUserId,
            client=client,
            clientAccount=clientAccount,
            _configuration=_configuration,
            **kwargs,
        )

from paychex_python_sdk.model.client import Client
from paychex_python_sdk.model.client_account import ClientAccount
