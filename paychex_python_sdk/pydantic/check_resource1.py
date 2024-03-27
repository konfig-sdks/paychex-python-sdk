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

from paychex_python_sdk.pydantic.pay_component_resource1 import PayComponentResource1

class CheckResource1(BaseModel):
    # The id assigned to the worker
    worker_id: typing.Optional[str] = Field(None, alias='workerId')

    # The id of a single check that a workers has.
    paycheck_id: typing.Optional[str] = Field(None, alias='paycheckId')

    # The id for the unprocessed payperiod.
    pay_period_id: typing.Optional[str] = Field(None, alias='payPeriodId')

    # Id that you define which is used for error handling/responses. This is not required when sending a single check.
    check_correlation_id: typing.Optional[str] = Field(None, alias='checkCorrelationId')

    # This is used optionally for blocking the auto distribution of the earnings on the workers if they are setup for auto distribution.
    block_auto_distribution: typing.Optional[Literal[True, False]] = Field(None, alias='blockAutoDistribution')

    # The earnings to apply to the check.Each earning needs to define as one of the following:1 .payHours: Will use the default hourly rate defined on the worker to apply the hours against. 2. payHours and payRate: Will allow you to define the monetary rate that the hours will be applied against. 3. payHours and payRateId: Will allow you to define which workers predefined pay rate the hours will be applied against. 4. payUnits: Will use the default hourly rate defined on the worker to apply the units against. 5. payUnits and payRate: Will allow you to define the monetary rate that the units will be applied against. 6. payUnits and payRateId: Will allow you to define which workers predefined pay rate the units will be applied against. 7. payAmount: Will allow you to define straight monetary amount.
    earnings: typing.Optional[typing.List[PayComponentResource1]] = Field(None, alias='earnings')

    # Deduction pay components on the check.
    deductions: typing.Optional[typing.List[PayComponentResource1]] = Field(None, alias='deductions')

    # Informational pay components on the check.
    informational: typing.Optional[typing.List[PayComponentResource1]] = Field(None, alias='informational')

    # Tax pay components on the check.
    taxes: typing.Optional[typing.List[PayComponentResource1]] = Field(None, alias='taxes')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
