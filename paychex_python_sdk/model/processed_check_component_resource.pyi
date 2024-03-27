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


class ProcessedCheckComponentResource(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            componentId = schemas.StrSchema
            checkComponentId = schemas.StrSchema
            name = schemas.StrSchema
            classificationType = schemas.StrSchema
            
            
            class effectOnPay(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
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
            memoed = schemas.BoolSchema
            laborAssignmentId = schemas.StrSchema
        
            @staticmethod
            def organization() -> typing.Type['OrganizationResource2']:
                return OrganizationResource2
            jobName = schemas.StrSchema
            jobId = schemas.StrSchema
            paidBy = schemas.StrSchema
            lineDate = schemas.DateTimeSchema
            amount = schemas.StrSchema
            rate = schemas.StrSchema
            hours = schemas.StrSchema
            units = schemas.StrSchema
            __annotations__ = {
                "componentId": componentId,
                "checkComponentId": checkComponentId,
                "name": name,
                "classificationType": classificationType,
                "effectOnPay": effectOnPay,
                "memoed": memoed,
                "laborAssignmentId": laborAssignmentId,
                "organization": organization,
                "jobName": jobName,
                "jobId": jobId,
                "paidBy": paidBy,
                "lineDate": lineDate,
                "amount": amount,
                "rate": rate,
                "hours": hours,
                "units": units,
            }
    
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
    def __getitem__(self, name: typing_extensions.Literal["memoed"]) -> MetaOapg.properties.memoed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["laborAssignmentId"]) -> MetaOapg.properties.laborAssignmentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization"]) -> 'OrganizationResource2': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobName"]) -> MetaOapg.properties.jobName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobId"]) -> MetaOapg.properties.jobId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paidBy"]) -> MetaOapg.properties.paidBy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lineDate"]) -> MetaOapg.properties.lineDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rate"]) -> MetaOapg.properties.rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hours"]) -> MetaOapg.properties.hours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["units"]) -> MetaOapg.properties.units: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["componentId", "checkComponentId", "name", "classificationType", "effectOnPay", "memoed", "laborAssignmentId", "organization", "jobName", "jobId", "paidBy", "lineDate", "amount", "rate", "hours", "units", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
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
    def get_item_oapg(self, name: typing_extensions.Literal["memoed"]) -> typing.Union[MetaOapg.properties.memoed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["laborAssignmentId"]) -> typing.Union[MetaOapg.properties.laborAssignmentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization"]) -> typing.Union['OrganizationResource2', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobName"]) -> typing.Union[MetaOapg.properties.jobName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobId"]) -> typing.Union[MetaOapg.properties.jobId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paidBy"]) -> typing.Union[MetaOapg.properties.paidBy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lineDate"]) -> typing.Union[MetaOapg.properties.lineDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rate"]) -> typing.Union[MetaOapg.properties.rate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hours"]) -> typing.Union[MetaOapg.properties.hours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["units"]) -> typing.Union[MetaOapg.properties.units, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["componentId", "checkComponentId", "name", "classificationType", "effectOnPay", "memoed", "laborAssignmentId", "organization", "jobName", "jobId", "paidBy", "lineDate", "amount", "rate", "hours", "units", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        componentId: typing.Union[MetaOapg.properties.componentId, str, schemas.Unset] = schemas.unset,
        checkComponentId: typing.Union[MetaOapg.properties.checkComponentId, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        classificationType: typing.Union[MetaOapg.properties.classificationType, str, schemas.Unset] = schemas.unset,
        effectOnPay: typing.Union[MetaOapg.properties.effectOnPay, str, schemas.Unset] = schemas.unset,
        memoed: typing.Union[MetaOapg.properties.memoed, bool, schemas.Unset] = schemas.unset,
        laborAssignmentId: typing.Union[MetaOapg.properties.laborAssignmentId, str, schemas.Unset] = schemas.unset,
        organization: typing.Union['OrganizationResource2', schemas.Unset] = schemas.unset,
        jobName: typing.Union[MetaOapg.properties.jobName, str, schemas.Unset] = schemas.unset,
        jobId: typing.Union[MetaOapg.properties.jobId, str, schemas.Unset] = schemas.unset,
        paidBy: typing.Union[MetaOapg.properties.paidBy, str, schemas.Unset] = schemas.unset,
        lineDate: typing.Union[MetaOapg.properties.lineDate, str, datetime, schemas.Unset] = schemas.unset,
        amount: typing.Union[MetaOapg.properties.amount, str, schemas.Unset] = schemas.unset,
        rate: typing.Union[MetaOapg.properties.rate, str, schemas.Unset] = schemas.unset,
        hours: typing.Union[MetaOapg.properties.hours, str, schemas.Unset] = schemas.unset,
        units: typing.Union[MetaOapg.properties.units, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProcessedCheckComponentResource':
        return super().__new__(
            cls,
            *args,
            componentId=componentId,
            checkComponentId=checkComponentId,
            name=name,
            classificationType=classificationType,
            effectOnPay=effectOnPay,
            memoed=memoed,
            laborAssignmentId=laborAssignmentId,
            organization=organization,
            jobName=jobName,
            jobId=jobId,
            paidBy=paidBy,
            lineDate=lineDate,
            amount=amount,
            rate=rate,
            hours=hours,
            units=units,
            _configuration=_configuration,
            **kwargs,
        )

from paychex_python_sdk.model.organization_resource2 import OrganizationResource2
