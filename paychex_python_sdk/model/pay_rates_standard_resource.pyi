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


class PayRatesStandardResource(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Worker Pay Rate  Standard
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def payStandards() -> typing.Type['PayStandardResource']:
                return PayStandardResource
            
            
            class payRates(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PayRateResource']:
                        return PayRateResource
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['PayRateResource'], typing.List['PayRateResource']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'payRates':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PayRateResource':
                    return super().__getitem__(i)
            __annotations__ = {
                "payStandards": payStandards,
                "payRates": payRates,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payStandards"]) -> 'PayStandardResource': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payRates"]) -> MetaOapg.properties.payRates: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["payStandards", "payRates", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payStandards"]) -> typing.Union['PayStandardResource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payRates"]) -> typing.Union[MetaOapg.properties.payRates, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["payStandards", "payRates", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        payStandards: typing.Union['PayStandardResource', schemas.Unset] = schemas.unset,
        payRates: typing.Union[MetaOapg.properties.payRates, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PayRatesStandardResource':
        return super().__new__(
            cls,
            *args,
            payStandards=payStandards,
            payRates=payRates,
            _configuration=_configuration,
            **kwargs,
        )

from paychex_python_sdk.model.pay_rate_resource import PayRateResource
from paychex_python_sdk.model.pay_standard_resource import PayStandardResource
