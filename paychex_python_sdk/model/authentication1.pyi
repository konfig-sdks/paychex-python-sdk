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


class Authentication1(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Required Authentication object is going to be different based on each authType. <br />* NO_AUTH doesn't have any other fields in authentication object <br />* BASIC_AUTH needs 2 fields: username and password <br />* APIKEY requires the field: apiKey <br />* OAUTH2 requires 5 fields:  tokenUrl, clientId, clientSecret, grantType, contentType <br />* OAUTH2_BASIC requires 5 fields:  tokenUrl, clientId, clientSecret, grantType, contentType
    """


    class MetaOapg:
        required = {
            "authType",
        }
        
        class properties:
            
            
            class authType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def NO_AUTH(cls):
                    return cls("NO_AUTH")
                
                @schemas.classproperty
                def BASIC_AUTH(cls):
                    return cls("BASIC_AUTH")
                
                @schemas.classproperty
                def API_KEY(cls):
                    return cls("API_KEY")
                
                @schemas.classproperty
                def OAUTH2(cls):
                    return cls("OAUTH2")
                
                @schemas.classproperty
                def OAUTH2_BASIC(cls):
                    return cls("OAUTH2_BASIC")
            apiKey = schemas.StrSchema
            username = schemas.StrSchema
            password = schemas.StrSchema
            tokenUrl = schemas.StrSchema
            clientId = schemas.StrSchema
            clientSecret = schemas.StrSchema
            grantType = schemas.StrSchema
            contentType = schemas.StrSchema
            __annotations__ = {
                "authType": authType,
                "apiKey": apiKey,
                "username": username,
                "password": password,
                "tokenUrl": tokenUrl,
                "clientId": clientId,
                "clientSecret": clientSecret,
                "grantType": grantType,
                "contentType": contentType,
            }
    
    authType: MetaOapg.properties.authType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authType"]) -> MetaOapg.properties.authType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apiKey"]) -> MetaOapg.properties.apiKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tokenUrl"]) -> MetaOapg.properties.tokenUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clientId"]) -> MetaOapg.properties.clientId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clientSecret"]) -> MetaOapg.properties.clientSecret: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["grantType"]) -> MetaOapg.properties.grantType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contentType"]) -> MetaOapg.properties.contentType: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["authType", "apiKey", "username", "password", "tokenUrl", "clientId", "clientSecret", "grantType", "contentType", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authType"]) -> MetaOapg.properties.authType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apiKey"]) -> typing.Union[MetaOapg.properties.apiKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> typing.Union[MetaOapg.properties.username, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> typing.Union[MetaOapg.properties.password, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tokenUrl"]) -> typing.Union[MetaOapg.properties.tokenUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clientId"]) -> typing.Union[MetaOapg.properties.clientId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clientSecret"]) -> typing.Union[MetaOapg.properties.clientSecret, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["grantType"]) -> typing.Union[MetaOapg.properties.grantType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contentType"]) -> typing.Union[MetaOapg.properties.contentType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["authType", "apiKey", "username", "password", "tokenUrl", "clientId", "clientSecret", "grantType", "contentType", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        authType: typing.Union[MetaOapg.properties.authType, str, ],
        apiKey: typing.Union[MetaOapg.properties.apiKey, str, schemas.Unset] = schemas.unset,
        username: typing.Union[MetaOapg.properties.username, str, schemas.Unset] = schemas.unset,
        password: typing.Union[MetaOapg.properties.password, str, schemas.Unset] = schemas.unset,
        tokenUrl: typing.Union[MetaOapg.properties.tokenUrl, str, schemas.Unset] = schemas.unset,
        clientId: typing.Union[MetaOapg.properties.clientId, str, schemas.Unset] = schemas.unset,
        clientSecret: typing.Union[MetaOapg.properties.clientSecret, str, schemas.Unset] = schemas.unset,
        grantType: typing.Union[MetaOapg.properties.grantType, str, schemas.Unset] = schemas.unset,
        contentType: typing.Union[MetaOapg.properties.contentType, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Authentication1':
        return super().__new__(
            cls,
            *args,
            authType=authType,
            apiKey=apiKey,
            username=username,
            password=password,
            tokenUrl=tokenUrl,
            clientId=clientId,
            clientSecret=clientSecret,
            grantType=grantType,
            contentType=contentType,
            _configuration=_configuration,
            **kwargs,
        )
