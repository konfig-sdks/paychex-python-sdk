# coding: utf-8

"""
    External API

      # Developer Resources  Refer [Developer Resources](https://developer.paychex.com/resources/overview/) for more details on API specification 

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from paychex_python_sdk.pydantic.communication_resource import CommunicationResource
from paychex_python_sdk.pydantic.job_title_resource import JobTitleResource
from paychex_python_sdk.pydantic.legal_id_resource import LegalIdResource
from paychex_python_sdk.pydantic.name_resource import NameResource
from paychex_python_sdk.pydantic.organization_resource import OrganizationResource
from paychex_python_sdk.pydantic.status import Status
from paychex_python_sdk.pydantic.supervisor_resource import SupervisorResource

class WorkerResource(BaseModel):
    # The unique identifier associated with this worker representation.
    worker_id: typing.Optional[str] = Field(None, alias='workerId')

    # The workers employee identification information.
    employee_id: typing.Optional[str] = Field(None, alias='employeeId')

    # The type of worker. This data field cannot be PATCHED.
    worker_type: typing.Optional[Literal["EMPLOYEE", "CONTRACTOR", "INDEPENDENT_CONTRACTOR"]] = Field(None, alias='workerType')

    # The type of employment for the worker.
    employment_type: typing.Optional[Literal["FULL_TIME", "PART_TIME"]] = Field(None, alias='employmentType')

    # The Overtime classification of the worker.This data field cannot be PATCHED for ACTIVE workers.
    exemption_type: typing.Optional[Literal["EXEMPT", "NON_EXEMPT"]] = Field(None, alias='exemptionType')

    # The workers date of birth. It cannot be greater than today's date.
    birth_date: typing.Optional[datetime] = Field(None, alias='birthDate')

    sex: typing.Optional[Literal["MALE", "FEMALE", "NOT_SPECIFIED"]] = Field(None, alias='sex')

    # Disclaimer:This parameter is not visible in Flex for the client. This data field cannot be PATCHED for ACTIVE workers.
    ethnicity_code: typing.Optional[Literal["(blank)", "HISPANIC_OR_LATINO", "WHITE_NOT_OF_HISPANIC_ORIGIN", "BLACK_OR_AFRICAN_AMERICAN", "NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLAND", "ASIAN", "AMERICAN_INDIAN_OR_ALASKAN_NATIVE", "TWO_OR_MORE_RACES", "Prefer not to answer"]] = Field(None, alias='ethnicityCode')

    # The date which the worker was hired. It cannot be PATCHED for ACTIVE workers.
    hire_date: typing.Optional[datetime] = Field(None, alias='hireDate')

    # The clock ID of the worker that can be an identification for other systems.
    clock_id: typing.Optional[str] = Field(None, alias='clockId')

    name: typing.Optional[NameResource] = Field(None, alias='name')

    legal_id: typing.Optional[LegalIdResource] = Field(None, alias='legalId')

    # The workers home labor assignment. This data field cannot be POSTED or PATCHED
    labor_assignment_id: typing.Optional[str] = Field(None, alias='laborAssignmentId')

    # The workers home job. This data field cannot be POSTED or PATCHED.
    job_id: typing.Optional[str] = Field(None, alias='jobId')

    # The workers location. This data field cannot be POSTED or PATCHED.
    location_id: typing.Optional[str] = Field(None, alias='locationId')

    job: typing.Optional[JobTitleResource] = Field(None, alias='job')

    organization: typing.Optional[OrganizationResource] = Field(None, alias='organization')

    supervisor: typing.Optional[SupervisorResource] = Field(None, alias='supervisor')

    current_status: typing.Optional[Status] = Field(None, alias='currentStatus')

    # Worker Communications. This data field cannot be updated for worker endpoint.
    communications: typing.Optional[typing.List[CommunicationResource]] = Field(None, alias='communications')

    # Id that you define which is used for error handling/responses.This data field is used while POSTING multiple IN_PROGRESS workers
    worker_correlation_id: typing.Optional[str] = Field(None, alias='workerCorrelationId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
