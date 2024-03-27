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


class WorkerResource1(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            workerId = schemas.StrSchema
            employeeId = schemas.StrSchema
            
            
            class workerType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def EMPLOYEE(cls):
                    return cls("EMPLOYEE")
                
                @schemas.classproperty
                def CONTRACTOR(cls):
                    return cls("CONTRACTOR")
                
                @schemas.classproperty
                def INDEPENDENT_CONTRACTOR(cls):
                    return cls("INDEPENDENT_CONTRACTOR")
            
            
            class employmentType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def FULL_TIME(cls):
                    return cls("FULL_TIME")
                
                @schemas.classproperty
                def PART_TIME(cls):
                    return cls("PART_TIME")
            
            
            class exemptionType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def EXEMPT(cls):
                    return cls("EXEMPT")
                
                @schemas.classproperty
                def NON_EXEMPT(cls):
                    return cls("NON_EXEMPT")
            birthDate = schemas.DateTimeSchema
            
            
            class sex(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def MALE(cls):
                    return cls("MALE")
                
                @schemas.classproperty
                def FEMALE(cls):
                    return cls("FEMALE")
                
                @schemas.classproperty
                def NOT_SPECIFIED(cls):
                    return cls("NOT_SPECIFIED")
            ethnicityCode = schemas.StrSchema
            hireDate = schemas.DateTimeSchema
            clockId = schemas.StrSchema
        
            @staticmethod
            def name() -> typing.Type['NameResource1']:
                return NameResource1
        
            @staticmethod
            def legalId() -> typing.Type['LegalIdResource1']:
                return LegalIdResource1
            laborAssignmentId = schemas.StrSchema
            locationId = schemas.StrSchema
            jobId = schemas.StrSchema
        
            @staticmethod
            def job() -> typing.Type['JobTitleResource1']:
                return JobTitleResource1
        
            @staticmethod
            def organization() -> typing.Type['OrganizationResource1']:
                return OrganizationResource1
        
            @staticmethod
            def supervisor() -> typing.Type['SupervisorResource1']:
                return SupervisorResource1
        
            @staticmethod
            def currentStatus() -> typing.Type['Status1']:
                return Status1
            
            
            class communications(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CommunicationResource1']:
                        return CommunicationResource1
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CommunicationResource1'], typing.List['CommunicationResource1']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'communications':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CommunicationResource1':
                    return super().__getitem__(i)
            
            
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
            workerCorrelationId = schemas.StrSchema
            __annotations__ = {
                "workerId": workerId,
                "employeeId": employeeId,
                "workerType": workerType,
                "employmentType": employmentType,
                "exemptionType": exemptionType,
                "birthDate": birthDate,
                "sex": sex,
                "ethnicityCode": ethnicityCode,
                "hireDate": hireDate,
                "clockId": clockId,
                "name": name,
                "legalId": legalId,
                "laborAssignmentId": laborAssignmentId,
                "locationId": locationId,
                "jobId": jobId,
                "job": job,
                "organization": organization,
                "supervisor": supervisor,
                "currentStatus": currentStatus,
                "communications": communications,
                "links": links,
                "workerCorrelationId": workerCorrelationId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workerId"]) -> MetaOapg.properties.workerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeId"]) -> MetaOapg.properties.employeeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workerType"]) -> MetaOapg.properties.workerType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employmentType"]) -> MetaOapg.properties.employmentType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exemptionType"]) -> MetaOapg.properties.exemptionType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["birthDate"]) -> MetaOapg.properties.birthDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sex"]) -> MetaOapg.properties.sex: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ethnicityCode"]) -> MetaOapg.properties.ethnicityCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hireDate"]) -> MetaOapg.properties.hireDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clockId"]) -> MetaOapg.properties.clockId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> 'NameResource1': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legalId"]) -> 'LegalIdResource1': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["laborAssignmentId"]) -> MetaOapg.properties.laborAssignmentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locationId"]) -> MetaOapg.properties.locationId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobId"]) -> MetaOapg.properties.jobId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["job"]) -> 'JobTitleResource1': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization"]) -> 'OrganizationResource1': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supervisor"]) -> 'SupervisorResource1': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentStatus"]) -> 'Status1': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["communications"]) -> MetaOapg.properties.communications: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> MetaOapg.properties.links: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workerCorrelationId"]) -> MetaOapg.properties.workerCorrelationId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["workerId", "employeeId", "workerType", "employmentType", "exemptionType", "birthDate", "sex", "ethnicityCode", "hireDate", "clockId", "name", "legalId", "laborAssignmentId", "locationId", "jobId", "job", "organization", "supervisor", "currentStatus", "communications", "links", "workerCorrelationId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workerId"]) -> typing.Union[MetaOapg.properties.workerId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeId"]) -> typing.Union[MetaOapg.properties.employeeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workerType"]) -> typing.Union[MetaOapg.properties.workerType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employmentType"]) -> typing.Union[MetaOapg.properties.employmentType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exemptionType"]) -> typing.Union[MetaOapg.properties.exemptionType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["birthDate"]) -> typing.Union[MetaOapg.properties.birthDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sex"]) -> typing.Union[MetaOapg.properties.sex, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ethnicityCode"]) -> typing.Union[MetaOapg.properties.ethnicityCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hireDate"]) -> typing.Union[MetaOapg.properties.hireDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clockId"]) -> typing.Union[MetaOapg.properties.clockId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union['NameResource1', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legalId"]) -> typing.Union['LegalIdResource1', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["laborAssignmentId"]) -> typing.Union[MetaOapg.properties.laborAssignmentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locationId"]) -> typing.Union[MetaOapg.properties.locationId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobId"]) -> typing.Union[MetaOapg.properties.jobId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["job"]) -> typing.Union['JobTitleResource1', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization"]) -> typing.Union['OrganizationResource1', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supervisor"]) -> typing.Union['SupervisorResource1', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentStatus"]) -> typing.Union['Status1', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["communications"]) -> typing.Union[MetaOapg.properties.communications, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union[MetaOapg.properties.links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workerCorrelationId"]) -> typing.Union[MetaOapg.properties.workerCorrelationId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["workerId", "employeeId", "workerType", "employmentType", "exemptionType", "birthDate", "sex", "ethnicityCode", "hireDate", "clockId", "name", "legalId", "laborAssignmentId", "locationId", "jobId", "job", "organization", "supervisor", "currentStatus", "communications", "links", "workerCorrelationId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        workerId: typing.Union[MetaOapg.properties.workerId, str, schemas.Unset] = schemas.unset,
        employeeId: typing.Union[MetaOapg.properties.employeeId, str, schemas.Unset] = schemas.unset,
        workerType: typing.Union[MetaOapg.properties.workerType, str, schemas.Unset] = schemas.unset,
        employmentType: typing.Union[MetaOapg.properties.employmentType, str, schemas.Unset] = schemas.unset,
        exemptionType: typing.Union[MetaOapg.properties.exemptionType, str, schemas.Unset] = schemas.unset,
        birthDate: typing.Union[MetaOapg.properties.birthDate, str, datetime, schemas.Unset] = schemas.unset,
        sex: typing.Union[MetaOapg.properties.sex, str, schemas.Unset] = schemas.unset,
        ethnicityCode: typing.Union[MetaOapg.properties.ethnicityCode, str, schemas.Unset] = schemas.unset,
        hireDate: typing.Union[MetaOapg.properties.hireDate, str, datetime, schemas.Unset] = schemas.unset,
        clockId: typing.Union[MetaOapg.properties.clockId, str, schemas.Unset] = schemas.unset,
        name: typing.Union['NameResource1', schemas.Unset] = schemas.unset,
        legalId: typing.Union['LegalIdResource1', schemas.Unset] = schemas.unset,
        laborAssignmentId: typing.Union[MetaOapg.properties.laborAssignmentId, str, schemas.Unset] = schemas.unset,
        locationId: typing.Union[MetaOapg.properties.locationId, str, schemas.Unset] = schemas.unset,
        jobId: typing.Union[MetaOapg.properties.jobId, str, schemas.Unset] = schemas.unset,
        job: typing.Union['JobTitleResource1', schemas.Unset] = schemas.unset,
        organization: typing.Union['OrganizationResource1', schemas.Unset] = schemas.unset,
        supervisor: typing.Union['SupervisorResource1', schemas.Unset] = schemas.unset,
        currentStatus: typing.Union['Status1', schemas.Unset] = schemas.unset,
        communications: typing.Union[MetaOapg.properties.communications, list, tuple, schemas.Unset] = schemas.unset,
        links: typing.Union[MetaOapg.properties.links, list, tuple, schemas.Unset] = schemas.unset,
        workerCorrelationId: typing.Union[MetaOapg.properties.workerCorrelationId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WorkerResource1':
        return super().__new__(
            cls,
            *args,
            workerId=workerId,
            employeeId=employeeId,
            workerType=workerType,
            employmentType=employmentType,
            exemptionType=exemptionType,
            birthDate=birthDate,
            sex=sex,
            ethnicityCode=ethnicityCode,
            hireDate=hireDate,
            clockId=clockId,
            name=name,
            legalId=legalId,
            laborAssignmentId=laborAssignmentId,
            locationId=locationId,
            jobId=jobId,
            job=job,
            organization=organization,
            supervisor=supervisor,
            currentStatus=currentStatus,
            communications=communications,
            links=links,
            workerCorrelationId=workerCorrelationId,
            _configuration=_configuration,
            **kwargs,
        )

from paychex_python_sdk.model.communication_resource1 import CommunicationResource1
from paychex_python_sdk.model.job_title_resource1 import JobTitleResource1
from paychex_python_sdk.model.legal_id_resource1 import LegalIdResource1
from paychex_python_sdk.model.link import Link
from paychex_python_sdk.model.name_resource1 import NameResource1
from paychex_python_sdk.model.organization_resource1 import OrganizationResource1
from paychex_python_sdk.model.status1 import Status1
from paychex_python_sdk.model.supervisor_resource1 import SupervisorResource1
