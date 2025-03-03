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


class CheckSummaryResource(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            payPeriodId = schemas.StrSchema
            checkDate = schemas.DateTimeSchema
            payRunDate = schemas.DateTimeSchema
            totalHrs = schemas.StrSchema
            checkNumber = schemas.StrSchema
            totalEarnings = schemas.StrSchema
            totalWithholdings = schemas.StrSchema
            totalDeductions = schemas.StrSchema
            netPay = schemas.StrSchema
            checkType = schemas.StrSchema
            grossYTD = schemas.StrSchema
            netYTD = schemas.StrSchema
            
            
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
                "payPeriodId": payPeriodId,
                "checkDate": checkDate,
                "payRunDate": payRunDate,
                "totalHrs": totalHrs,
                "checkNumber": checkNumber,
                "totalEarnings": totalEarnings,
                "totalWithholdings": totalWithholdings,
                "totalDeductions": totalDeductions,
                "netPay": netPay,
                "checkType": checkType,
                "grossYTD": grossYTD,
                "netYTD": netYTD,
                "links": links,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payPeriodId"]) -> MetaOapg.properties.payPeriodId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["checkDate"]) -> MetaOapg.properties.checkDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payRunDate"]) -> MetaOapg.properties.payRunDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalHrs"]) -> MetaOapg.properties.totalHrs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["checkNumber"]) -> MetaOapg.properties.checkNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalEarnings"]) -> MetaOapg.properties.totalEarnings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalWithholdings"]) -> MetaOapg.properties.totalWithholdings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalDeductions"]) -> MetaOapg.properties.totalDeductions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["netPay"]) -> MetaOapg.properties.netPay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["checkType"]) -> MetaOapg.properties.checkType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["grossYTD"]) -> MetaOapg.properties.grossYTD: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["netYTD"]) -> MetaOapg.properties.netYTD: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> MetaOapg.properties.links: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["payPeriodId", "checkDate", "payRunDate", "totalHrs", "checkNumber", "totalEarnings", "totalWithholdings", "totalDeductions", "netPay", "checkType", "grossYTD", "netYTD", "links", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payPeriodId"]) -> typing.Union[MetaOapg.properties.payPeriodId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["checkDate"]) -> typing.Union[MetaOapg.properties.checkDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payRunDate"]) -> typing.Union[MetaOapg.properties.payRunDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalHrs"]) -> typing.Union[MetaOapg.properties.totalHrs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["checkNumber"]) -> typing.Union[MetaOapg.properties.checkNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalEarnings"]) -> typing.Union[MetaOapg.properties.totalEarnings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalWithholdings"]) -> typing.Union[MetaOapg.properties.totalWithholdings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalDeductions"]) -> typing.Union[MetaOapg.properties.totalDeductions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["netPay"]) -> typing.Union[MetaOapg.properties.netPay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["checkType"]) -> typing.Union[MetaOapg.properties.checkType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["grossYTD"]) -> typing.Union[MetaOapg.properties.grossYTD, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["netYTD"]) -> typing.Union[MetaOapg.properties.netYTD, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union[MetaOapg.properties.links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["payPeriodId", "checkDate", "payRunDate", "totalHrs", "checkNumber", "totalEarnings", "totalWithholdings", "totalDeductions", "netPay", "checkType", "grossYTD", "netYTD", "links", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        payPeriodId: typing.Union[MetaOapg.properties.payPeriodId, str, schemas.Unset] = schemas.unset,
        checkDate: typing.Union[MetaOapg.properties.checkDate, str, datetime, schemas.Unset] = schemas.unset,
        payRunDate: typing.Union[MetaOapg.properties.payRunDate, str, datetime, schemas.Unset] = schemas.unset,
        totalHrs: typing.Union[MetaOapg.properties.totalHrs, str, schemas.Unset] = schemas.unset,
        checkNumber: typing.Union[MetaOapg.properties.checkNumber, str, schemas.Unset] = schemas.unset,
        totalEarnings: typing.Union[MetaOapg.properties.totalEarnings, str, schemas.Unset] = schemas.unset,
        totalWithholdings: typing.Union[MetaOapg.properties.totalWithholdings, str, schemas.Unset] = schemas.unset,
        totalDeductions: typing.Union[MetaOapg.properties.totalDeductions, str, schemas.Unset] = schemas.unset,
        netPay: typing.Union[MetaOapg.properties.netPay, str, schemas.Unset] = schemas.unset,
        checkType: typing.Union[MetaOapg.properties.checkType, str, schemas.Unset] = schemas.unset,
        grossYTD: typing.Union[MetaOapg.properties.grossYTD, str, schemas.Unset] = schemas.unset,
        netYTD: typing.Union[MetaOapg.properties.netYTD, str, schemas.Unset] = schemas.unset,
        links: typing.Union[MetaOapg.properties.links, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CheckSummaryResource':
        return super().__new__(
            cls,
            *args,
            payPeriodId=payPeriodId,
            checkDate=checkDate,
            payRunDate=payRunDate,
            totalHrs=totalHrs,
            checkNumber=checkNumber,
            totalEarnings=totalEarnings,
            totalWithholdings=totalWithholdings,
            totalDeductions=totalDeductions,
            netPay=netPay,
            checkType=checkType,
            grossYTD=grossYTD,
            netYTD=netYTD,
            links=links,
            _configuration=_configuration,
            **kwargs,
        )

from paychex_python_sdk.model.link import Link
