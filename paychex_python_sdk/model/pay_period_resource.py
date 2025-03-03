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


class PayPeriodResource(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The representational state of pay periods.
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            payPeriodId = schemas.StrSchema
            
            
            class intervalCode(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ANNUAL": "ANNUAL",
                        "BI_WEEKLY": "BI_WEEKLY",
                        "MONTHLY": "MONTHLY",
                        "QUARTERLY": "QUARTERLY",
                        "SEMI_ANNUAL": "SEMI_ANNUAL",
                        "SEMI_MONTHLY": "SEMI_MONTHLY",
                        "WEEKLY": "WEEKLY",
                    }
                
                @schemas.classproperty
                def ANNUAL(cls):
                    return cls("ANNUAL")
                
                @schemas.classproperty
                def BI_WEEKLY(cls):
                    return cls("BI_WEEKLY")
                
                @schemas.classproperty
                def MONTHLY(cls):
                    return cls("MONTHLY")
                
                @schemas.classproperty
                def QUARTERLY(cls):
                    return cls("QUARTERLY")
                
                @schemas.classproperty
                def SEMI_ANNUAL(cls):
                    return cls("SEMI_ANNUAL")
                
                @schemas.classproperty
                def SEMI_MONTHLY(cls):
                    return cls("SEMI_MONTHLY")
                
                @schemas.classproperty
                def WEEKLY(cls):
                    return cls("WEEKLY")
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "COMPLETED": "COMPLETED",
                        "COMPLETED_BY_MEC": "COMPLETED_BY_MEC",
                        "ENTRY": "ENTRY",
                        "INITIAL": "INITIAL",
                        "PROCESSING": "PROCESSING",
                        "REISSUED": "REISSUED",
                        "RELEASED": "RELEASED",
                        "REVERSED": "REVERSED",
                    }
                
                @schemas.classproperty
                def COMPLETED(cls):
                    return cls("COMPLETED")
                
                @schemas.classproperty
                def COMPLETED_BY_MEC(cls):
                    return cls("COMPLETED_BY_MEC")
                
                @schemas.classproperty
                def ENTRY(cls):
                    return cls("ENTRY")
                
                @schemas.classproperty
                def INITIAL(cls):
                    return cls("INITIAL")
                
                @schemas.classproperty
                def PROCESSING(cls):
                    return cls("PROCESSING")
                
                @schemas.classproperty
                def REISSUED(cls):
                    return cls("REISSUED")
                
                @schemas.classproperty
                def RELEASED(cls):
                    return cls("RELEASED")
                
                @schemas.classproperty
                def REVERSED(cls):
                    return cls("REVERSED")
            startDate = schemas.DateTimeSchema
            endDate = schemas.DateTimeSchema
            submitByDate = schemas.DateTimeSchema
            checkDate = schemas.DateTimeSchema
            checkCount = schemas.Int32Schema
            
            
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
                "description": description,
                "payPeriodId": payPeriodId,
                "intervalCode": intervalCode,
                "status": status,
                "startDate": startDate,
                "endDate": endDate,
                "submitByDate": submitByDate,
                "checkDate": checkDate,
                "checkCount": checkCount,
                "links": links,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payPeriodId"]) -> MetaOapg.properties.payPeriodId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["intervalCode"]) -> MetaOapg.properties.intervalCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["submitByDate"]) -> MetaOapg.properties.submitByDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["checkDate"]) -> MetaOapg.properties.checkDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["checkCount"]) -> MetaOapg.properties.checkCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> MetaOapg.properties.links: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "payPeriodId", "intervalCode", "status", "startDate", "endDate", "submitByDate", "checkDate", "checkCount", "links", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payPeriodId"]) -> typing.Union[MetaOapg.properties.payPeriodId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["intervalCode"]) -> typing.Union[MetaOapg.properties.intervalCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDate"]) -> typing.Union[MetaOapg.properties.startDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endDate"]) -> typing.Union[MetaOapg.properties.endDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["submitByDate"]) -> typing.Union[MetaOapg.properties.submitByDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["checkDate"]) -> typing.Union[MetaOapg.properties.checkDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["checkCount"]) -> typing.Union[MetaOapg.properties.checkCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union[MetaOapg.properties.links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "payPeriodId", "intervalCode", "status", "startDate", "endDate", "submitByDate", "checkDate", "checkCount", "links", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        payPeriodId: typing.Union[MetaOapg.properties.payPeriodId, str, schemas.Unset] = schemas.unset,
        intervalCode: typing.Union[MetaOapg.properties.intervalCode, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        startDate: typing.Union[MetaOapg.properties.startDate, str, datetime, schemas.Unset] = schemas.unset,
        endDate: typing.Union[MetaOapg.properties.endDate, str, datetime, schemas.Unset] = schemas.unset,
        submitByDate: typing.Union[MetaOapg.properties.submitByDate, str, datetime, schemas.Unset] = schemas.unset,
        checkDate: typing.Union[MetaOapg.properties.checkDate, str, datetime, schemas.Unset] = schemas.unset,
        checkCount: typing.Union[MetaOapg.properties.checkCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        links: typing.Union[MetaOapg.properties.links, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PayPeriodResource':
        return super().__new__(
            cls,
            *args,
            description=description,
            payPeriodId=payPeriodId,
            intervalCode=intervalCode,
            status=status,
            startDate=startDate,
            endDate=endDate,
            submitByDate=submitByDate,
            checkDate=checkDate,
            checkCount=checkCount,
            links=links,
            _configuration=_configuration,
            **kwargs,
        )

from paychex_python_sdk.model.link import Link
