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


class TelecomResource(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The telecom communications for this contact.
    """


    class MetaOapg:
        
        class properties:
            communicationId = schemas.StrSchema
            dialCountry = schemas.StrSchema
            dialArea = schemas.StrSchema
            dialNumber = schemas.StrSchema
            type = schemas.StrSchema
            usageType = schemas.StrSchema
            extension = schemas.StrSchema
            __annotations__ = {
                "communicationId": communicationId,
                "dialCountry": dialCountry,
                "dialArea": dialArea,
                "dialNumber": dialNumber,
                "type": type,
                "usageType": usageType,
                "extension": extension,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["communicationId"]) -> MetaOapg.properties.communicationId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dialCountry"]) -> MetaOapg.properties.dialCountry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dialArea"]) -> MetaOapg.properties.dialArea: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dialNumber"]) -> MetaOapg.properties.dialNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["usageType"]) -> MetaOapg.properties.usageType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extension"]) -> MetaOapg.properties.extension: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["communicationId", "dialCountry", "dialArea", "dialNumber", "type", "usageType", "extension", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["communicationId"]) -> typing.Union[MetaOapg.properties.communicationId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dialCountry"]) -> typing.Union[MetaOapg.properties.dialCountry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dialArea"]) -> typing.Union[MetaOapg.properties.dialArea, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dialNumber"]) -> typing.Union[MetaOapg.properties.dialNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["usageType"]) -> typing.Union[MetaOapg.properties.usageType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extension"]) -> typing.Union[MetaOapg.properties.extension, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["communicationId", "dialCountry", "dialArea", "dialNumber", "type", "usageType", "extension", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        communicationId: typing.Union[MetaOapg.properties.communicationId, str, schemas.Unset] = schemas.unset,
        dialCountry: typing.Union[MetaOapg.properties.dialCountry, str, schemas.Unset] = schemas.unset,
        dialArea: typing.Union[MetaOapg.properties.dialArea, str, schemas.Unset] = schemas.unset,
        dialNumber: typing.Union[MetaOapg.properties.dialNumber, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        usageType: typing.Union[MetaOapg.properties.usageType, str, schemas.Unset] = schemas.unset,
        extension: typing.Union[MetaOapg.properties.extension, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TelecomResource':
        return super().__new__(
            cls,
            *args,
            communicationId=communicationId,
            dialCountry=dialCountry,
            dialArea=dialArea,
            dialNumber=dialNumber,
            type=type,
            usageType=usageType,
            extension=extension,
            _configuration=_configuration,
            **kwargs,
        )
