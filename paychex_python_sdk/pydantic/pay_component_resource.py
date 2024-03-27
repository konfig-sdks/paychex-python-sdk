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

from paychex_python_sdk.pydantic.link import Link
from paychex_python_sdk.pydantic.pay_component_resource_applies_to_worker_types import PayComponentResourceAppliesToWorkerTypes

class PayComponentResource(BaseModel):
    # The description of the Pay Component.
    description: typing.Optional[str] = Field(None, alias='description')

    # The unique identifier used to identify a pay component.
    component_id: typing.Optional[str] = Field(None, alias='componentId')

    # The unique identifier associated for the pay component on this check.
    check_component_id: typing.Optional[str] = Field(None, alias='checkComponentId')

    # The Paychex standard code number for the Pay Component, can be two digit.
    code: typing.Optional[str] = Field(None, alias='code')

    # Name given to the pay component.
    name: typing.Optional[str] = Field(None, alias='name')

    # The category that this component falls into.
    classification_type: typing.Optional[str] = Field(None, alias='classificationType')

    # The effect that the pay component will have on the check amount.
    effect_on_pay: typing.Optional[Literal["ADDITION", "ADDITION_WITH_IN_OUT", "EMPLOYER_INFORMATIONAL", "REDUCTION"]] = Field(None, alias='effectOnPay')

    # The date that the pay component is able to be applied on a check.
    start_date: typing.Optional[datetime] = Field(None, alias='startDate')

    # The date that the pay component is not available to be applied on a check moving forward.
    end_date: typing.Optional[datetime] = Field(None, alias='endDate')

    applies_to_worker_types: typing.Optional[PayComponentResourceAppliesToWorkerTypes] = Field(None, alias='appliesToWorkerTypes')

    # This is used optionally for overriding a job when it needs to be different than the workers default. This option is only available when the client has job costing.
    job_id: typing.Optional[str] = Field(None, alias='jobId')

    # This is used optionally for overriding a labor assignment when it needs to be different than the workers assignment distribution. This option is only available when the client has labor assignment.
    labor_assignment_id: typing.Optional[str] = Field(None, alias='laborAssignmentId')

    # Unique identifier for this workers pay rate **This ID will change if this is created for an IN_PROGRESS worker that is later completed within Flex**
    pay_rate_id: typing.Optional[str] = Field(None, alias='payRateId')

    # The rate amount that will be applied for this component. Used in conjunction with Hours or Units.
    pay_rate: typing.Optional[str] = Field(None, alias='payRate')

    # The number of hours that will be applied for this component. Used in conjunction with rate.
    pay_hours: typing.Optional[str] = Field(None, alias='payHours')

    # The number of units that will be applied for this component. Used in conjunction with rate.
    pay_units: typing.Optional[str] = Field(None, alias='payUnits')

    # The flat amount to be applied for this component. Not used with Rate, Hours, or Units.
    pay_amount: typing.Optional[str] = Field(None, alias='payAmount')

    # This is used optionally for specifying a date that the pay component was generated on.
    line_date: typing.Optional[datetime] = Field(None, alias='lineDate')

    # This is used optionally for memoing the payHours or payUnits so that they are informational when using a payAmount.
    memoed: typing.Optional[bool] = Field(None, alias='memoed')

    links: typing.Optional[typing.List[Link]] = Field(None, alias='links')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
