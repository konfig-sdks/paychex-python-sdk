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


class EmailResource1(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            primaryEmail = schemas.StrSchema
            secondaryEmail = schemas.StrSchema
            connectionName = schemas.StrSchema
            displayId = schemas.StrSchema
            legalName = schemas.StrSchema
            
            
            class notificationType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "CONNECTION_ERROR": "CONNECTION_ERROR",
                        "DATA_ERROR": "DATA_ERROR",
                        "WORKER_CHECK_ERROR": "WORKER_CHECK_ERROR",
                        "MULTI_ID_SPI_REJECT": "MULTI_ID_SPI_REJECT",
                        "EMPLOYEE_OVERTIME_NOTIFICATION": "EMPLOYEE_OVERTIME_NOTIFICATION",
                        "COMPANY_PAY_PERIOD_ERROR": "COMPANY_PAY_PERIOD_ERROR",
                        "PAYROLL_CONFIRMATION": "PAYROLL_CONFIRMATION",
                        "COMPANY_JOBCODE": "COMPANY_JOBCODE",
                        "OFFBOARDING_SURVEY": "OFFBOARDING_SURVEY",
                        "OFFBOARDING_ERROR": "OFFBOARDING_ERROR",
                        "WORKER_PUNCH_OR_ADJUSTMENT_ERROR": "WORKER_PUNCH_OR_ADJUSTMENT_ERROR",
                        "WORKER_SCHEDULE_ERROR": "WORKER_SCHEDULE_ERROR",
                    }
                
                @schemas.classproperty
                def CONNECTION_ERROR(cls):
                    return cls("CONNECTION_ERROR")
                
                @schemas.classproperty
                def DATA_ERROR(cls):
                    return cls("DATA_ERROR")
                
                @schemas.classproperty
                def WORKER_CHECK_ERROR(cls):
                    return cls("WORKER_CHECK_ERROR")
                
                @schemas.classproperty
                def MULTI_ID_SPI_REJECT(cls):
                    return cls("MULTI_ID_SPI_REJECT")
                
                @schemas.classproperty
                def EMPLOYEE_OVERTIME_NOTIFICATION(cls):
                    return cls("EMPLOYEE_OVERTIME_NOTIFICATION")
                
                @schemas.classproperty
                def COMPANY_PAY_PERIOD_ERROR(cls):
                    return cls("COMPANY_PAY_PERIOD_ERROR")
                
                @schemas.classproperty
                def PAYROLL_CONFIRMATION(cls):
                    return cls("PAYROLL_CONFIRMATION")
                
                @schemas.classproperty
                def COMPANY_JOBCODE(cls):
                    return cls("COMPANY_JOBCODE")
                
                @schemas.classproperty
                def OFFBOARDING_SURVEY(cls):
                    return cls("OFFBOARDING_SURVEY")
                
                @schemas.classproperty
                def OFFBOARDING_ERROR(cls):
                    return cls("OFFBOARDING_ERROR")
                
                @schemas.classproperty
                def WORKER_PUNCH_OR_ADJUSTMENT_ERROR(cls):
                    return cls("WORKER_PUNCH_OR_ADJUSTMENT_ERROR")
                
                @schemas.classproperty
                def WORKER_SCHEDULE_ERROR(cls):
                    return cls("WORKER_SCHEDULE_ERROR")
            
            
            class workerErrors(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['WorkerErrorResource']:
                        return WorkerErrorResource
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['WorkerErrorResource'], typing.List['WorkerErrorResource']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'workerErrors':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'WorkerErrorResource':
                    return super().__getitem__(i)
            payPeriod = schemas.StrSchema
            partnerLocationId = schemas.StrSchema
            state = schemas.StrSchema
            sourceJobName = schemas.StrSchema
            bcc = schemas.StrSchema
            employeeFirstName = schemas.StrSchema
            employeeLastName = schemas.StrSchema
            linkToSurvey = schemas.StrSchema
            
            
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
                "primaryEmail": primaryEmail,
                "secondaryEmail": secondaryEmail,
                "connectionName": connectionName,
                "displayId": displayId,
                "legalName": legalName,
                "notificationType": notificationType,
                "workerErrors": workerErrors,
                "payPeriod": payPeriod,
                "partnerLocationId": partnerLocationId,
                "state": state,
                "sourceJobName": sourceJobName,
                "bcc": bcc,
                "employeeFirstName": employeeFirstName,
                "employeeLastName": employeeLastName,
                "linkToSurvey": linkToSurvey,
                "links": links,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primaryEmail"]) -> MetaOapg.properties.primaryEmail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secondaryEmail"]) -> MetaOapg.properties.secondaryEmail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connectionName"]) -> MetaOapg.properties.connectionName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayId"]) -> MetaOapg.properties.displayId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legalName"]) -> MetaOapg.properties.legalName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notificationType"]) -> MetaOapg.properties.notificationType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workerErrors"]) -> MetaOapg.properties.workerErrors: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payPeriod"]) -> MetaOapg.properties.payPeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partnerLocationId"]) -> MetaOapg.properties.partnerLocationId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceJobName"]) -> MetaOapg.properties.sourceJobName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bcc"]) -> MetaOapg.properties.bcc: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeFirstName"]) -> MetaOapg.properties.employeeFirstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeLastName"]) -> MetaOapg.properties.employeeLastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["linkToSurvey"]) -> MetaOapg.properties.linkToSurvey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> MetaOapg.properties.links: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["primaryEmail", "secondaryEmail", "connectionName", "displayId", "legalName", "notificationType", "workerErrors", "payPeriod", "partnerLocationId", "state", "sourceJobName", "bcc", "employeeFirstName", "employeeLastName", "linkToSurvey", "links", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primaryEmail"]) -> typing.Union[MetaOapg.properties.primaryEmail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secondaryEmail"]) -> typing.Union[MetaOapg.properties.secondaryEmail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connectionName"]) -> typing.Union[MetaOapg.properties.connectionName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayId"]) -> typing.Union[MetaOapg.properties.displayId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legalName"]) -> typing.Union[MetaOapg.properties.legalName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notificationType"]) -> typing.Union[MetaOapg.properties.notificationType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workerErrors"]) -> typing.Union[MetaOapg.properties.workerErrors, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payPeriod"]) -> typing.Union[MetaOapg.properties.payPeriod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partnerLocationId"]) -> typing.Union[MetaOapg.properties.partnerLocationId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceJobName"]) -> typing.Union[MetaOapg.properties.sourceJobName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bcc"]) -> typing.Union[MetaOapg.properties.bcc, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeFirstName"]) -> typing.Union[MetaOapg.properties.employeeFirstName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeLastName"]) -> typing.Union[MetaOapg.properties.employeeLastName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["linkToSurvey"]) -> typing.Union[MetaOapg.properties.linkToSurvey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union[MetaOapg.properties.links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["primaryEmail", "secondaryEmail", "connectionName", "displayId", "legalName", "notificationType", "workerErrors", "payPeriod", "partnerLocationId", "state", "sourceJobName", "bcc", "employeeFirstName", "employeeLastName", "linkToSurvey", "links", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        primaryEmail: typing.Union[MetaOapg.properties.primaryEmail, str, schemas.Unset] = schemas.unset,
        secondaryEmail: typing.Union[MetaOapg.properties.secondaryEmail, str, schemas.Unset] = schemas.unset,
        connectionName: typing.Union[MetaOapg.properties.connectionName, str, schemas.Unset] = schemas.unset,
        displayId: typing.Union[MetaOapg.properties.displayId, str, schemas.Unset] = schemas.unset,
        legalName: typing.Union[MetaOapg.properties.legalName, str, schemas.Unset] = schemas.unset,
        notificationType: typing.Union[MetaOapg.properties.notificationType, str, schemas.Unset] = schemas.unset,
        workerErrors: typing.Union[MetaOapg.properties.workerErrors, list, tuple, schemas.Unset] = schemas.unset,
        payPeriod: typing.Union[MetaOapg.properties.payPeriod, str, schemas.Unset] = schemas.unset,
        partnerLocationId: typing.Union[MetaOapg.properties.partnerLocationId, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        sourceJobName: typing.Union[MetaOapg.properties.sourceJobName, str, schemas.Unset] = schemas.unset,
        bcc: typing.Union[MetaOapg.properties.bcc, str, schemas.Unset] = schemas.unset,
        employeeFirstName: typing.Union[MetaOapg.properties.employeeFirstName, str, schemas.Unset] = schemas.unset,
        employeeLastName: typing.Union[MetaOapg.properties.employeeLastName, str, schemas.Unset] = schemas.unset,
        linkToSurvey: typing.Union[MetaOapg.properties.linkToSurvey, str, schemas.Unset] = schemas.unset,
        links: typing.Union[MetaOapg.properties.links, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmailResource1':
        return super().__new__(
            cls,
            *args,
            primaryEmail=primaryEmail,
            secondaryEmail=secondaryEmail,
            connectionName=connectionName,
            displayId=displayId,
            legalName=legalName,
            notificationType=notificationType,
            workerErrors=workerErrors,
            payPeriod=payPeriod,
            partnerLocationId=partnerLocationId,
            state=state,
            sourceJobName=sourceJobName,
            bcc=bcc,
            employeeFirstName=employeeFirstName,
            employeeLastName=employeeLastName,
            linkToSurvey=linkToSurvey,
            links=links,
            _configuration=_configuration,
            **kwargs,
        )

from paychex_python_sdk.model.link import Link
from paychex_python_sdk.model.worker_error_resource import WorkerErrorResource
