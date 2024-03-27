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


class LegalIdResource1(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The workers legal tax identification information. This data field cannot be PATCHED for ACTIVE workers.
    """


    class MetaOapg:
        
        class properties:
            
            
            class legalIdType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SSN(cls):
                    return cls("SSN")
                
                @schemas.classproperty
                def FEIN(cls):
                    return cls("FEIN")
            legalIdValue = schemas.StrSchema
            __annotations__ = {
                "legalIdType": legalIdType,
                "legalIdValue": legalIdValue,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legalIdType"]) -> MetaOapg.properties.legalIdType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legalIdValue"]) -> MetaOapg.properties.legalIdValue: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["legalIdType", "legalIdValue", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legalIdType"]) -> typing.Union[MetaOapg.properties.legalIdType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legalIdValue"]) -> typing.Union[MetaOapg.properties.legalIdValue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["legalIdType", "legalIdValue", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        legalIdType: typing.Union[MetaOapg.properties.legalIdType, str, schemas.Unset] = schemas.unset,
        legalIdValue: typing.Union[MetaOapg.properties.legalIdValue, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LegalIdResource1':
        return super().__new__(
            cls,
            *args,
            legalIdType=legalIdType,
            legalIdValue=legalIdValue,
            _configuration=_configuration,
            **kwargs,
        )
