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


class PayComponentResource1(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Tax pay components on the check.
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            componentId = schemas.StrSchema
            checkComponentId = schemas.StrSchema
            name = schemas.StrSchema
            classificationType = schemas.StrSchema
            
            
            class effectOnPay(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ADDITION": "ADDITION",
                        "ADDITION_WITH_IN_OUT": "ADDITION_WITH_IN_OUT",
                        "EMPLOYER_INFORMATIONAL": "EMPLOYER_INFORMATIONAL",
                        "REDUCTION": "REDUCTION",
                    }
                
                @schemas.classproperty
                def ADDITION(cls):
                    return cls("ADDITION")
                
                @schemas.classproperty
                def ADDITION_WITH_IN_OUT(cls):
                    return cls("ADDITION_WITH_IN_OUT")
                
                @schemas.classproperty
                def EMPLOYER_INFORMATIONAL(cls):
                    return cls("EMPLOYER_INFORMATIONAL")
                
                @schemas.classproperty
                def REDUCTION(cls):
                    return cls("REDUCTION")
            startDate = schemas.DateTimeSchema
            endDate = schemas.DateTimeSchema
            jobId = schemas.StrSchema
            laborAssignmentId = schemas.StrSchema
            payRateId = schemas.StrSchema
            payRate = schemas.StrSchema
            payHours = schemas.StrSchema
            payUnits = schemas.StrSchema
            payAmount = schemas.StrSchema
            lineDate = schemas.DateTimeSchema
            memoed = schemas.BoolSchema
            __annotations__ = {
                "description": description,
                "componentId": componentId,
                "checkComponentId": checkComponentId,
                "name": name,
                "classificationType": classificationType,
                "effectOnPay": effectOnPay,
                "startDate": startDate,
                "endDate": endDate,
                "jobId": jobId,
                "laborAssignmentId": laborAssignmentId,
                "payRateId": payRateId,
                "payRate": payRate,
                "payHours": payHours,
                "payUnits": payUnits,
                "payAmount": payAmount,
                "lineDate": lineDate,
                "memoed": memoed,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["componentId"]) -> MetaOapg.properties.componentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["checkComponentId"]) -> MetaOapg.properties.checkComponentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["classificationType"]) -> MetaOapg.properties.classificationType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["effectOnPay"]) -> MetaOapg.properties.effectOnPay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobId"]) -> MetaOapg.properties.jobId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["laborAssignmentId"]) -> MetaOapg.properties.laborAssignmentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payRateId"]) -> MetaOapg.properties.payRateId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payRate"]) -> MetaOapg.properties.payRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payHours"]) -> MetaOapg.properties.payHours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payUnits"]) -> MetaOapg.properties.payUnits: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payAmount"]) -> MetaOapg.properties.payAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lineDate"]) -> MetaOapg.properties.lineDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["memoed"]) -> MetaOapg.properties.memoed: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "componentId", "checkComponentId", "name", "classificationType", "effectOnPay", "startDate", "endDate", "jobId", "laborAssignmentId", "payRateId", "payRate", "payHours", "payUnits", "payAmount", "lineDate", "memoed", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["componentId"]) -> typing.Union[MetaOapg.properties.componentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["checkComponentId"]) -> typing.Union[MetaOapg.properties.checkComponentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["classificationType"]) -> typing.Union[MetaOapg.properties.classificationType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["effectOnPay"]) -> typing.Union[MetaOapg.properties.effectOnPay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDate"]) -> typing.Union[MetaOapg.properties.startDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endDate"]) -> typing.Union[MetaOapg.properties.endDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobId"]) -> typing.Union[MetaOapg.properties.jobId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["laborAssignmentId"]) -> typing.Union[MetaOapg.properties.laborAssignmentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payRateId"]) -> typing.Union[MetaOapg.properties.payRateId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payRate"]) -> typing.Union[MetaOapg.properties.payRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payHours"]) -> typing.Union[MetaOapg.properties.payHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payUnits"]) -> typing.Union[MetaOapg.properties.payUnits, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payAmount"]) -> typing.Union[MetaOapg.properties.payAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lineDate"]) -> typing.Union[MetaOapg.properties.lineDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["memoed"]) -> typing.Union[MetaOapg.properties.memoed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "componentId", "checkComponentId", "name", "classificationType", "effectOnPay", "startDate", "endDate", "jobId", "laborAssignmentId", "payRateId", "payRate", "payHours", "payUnits", "payAmount", "lineDate", "memoed", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        componentId: typing.Union[MetaOapg.properties.componentId, str, schemas.Unset] = schemas.unset,
        checkComponentId: typing.Union[MetaOapg.properties.checkComponentId, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        classificationType: typing.Union[MetaOapg.properties.classificationType, str, schemas.Unset] = schemas.unset,
        effectOnPay: typing.Union[MetaOapg.properties.effectOnPay, str, schemas.Unset] = schemas.unset,
        startDate: typing.Union[MetaOapg.properties.startDate, str, datetime, schemas.Unset] = schemas.unset,
        endDate: typing.Union[MetaOapg.properties.endDate, str, datetime, schemas.Unset] = schemas.unset,
        jobId: typing.Union[MetaOapg.properties.jobId, str, schemas.Unset] = schemas.unset,
        laborAssignmentId: typing.Union[MetaOapg.properties.laborAssignmentId, str, schemas.Unset] = schemas.unset,
        payRateId: typing.Union[MetaOapg.properties.payRateId, str, schemas.Unset] = schemas.unset,
        payRate: typing.Union[MetaOapg.properties.payRate, str, schemas.Unset] = schemas.unset,
        payHours: typing.Union[MetaOapg.properties.payHours, str, schemas.Unset] = schemas.unset,
        payUnits: typing.Union[MetaOapg.properties.payUnits, str, schemas.Unset] = schemas.unset,
        payAmount: typing.Union[MetaOapg.properties.payAmount, str, schemas.Unset] = schemas.unset,
        lineDate: typing.Union[MetaOapg.properties.lineDate, str, datetime, schemas.Unset] = schemas.unset,
        memoed: typing.Union[MetaOapg.properties.memoed, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PayComponentResource1':
        return super().__new__(
            cls,
            *args,
            description=description,
            componentId=componentId,
            checkComponentId=checkComponentId,
            name=name,
            classificationType=classificationType,
            effectOnPay=effectOnPay,
            startDate=startDate,
            endDate=endDate,
            jobId=jobId,
            laborAssignmentId=laborAssignmentId,
            payRateId=payRateId,
            payRate=payRate,
            payHours=payHours,
            payUnits=payUnits,
            payAmount=payAmount,
            lineDate=lineDate,
            memoed=memoed,
            _configuration=_configuration,
            **kwargs,
        )
