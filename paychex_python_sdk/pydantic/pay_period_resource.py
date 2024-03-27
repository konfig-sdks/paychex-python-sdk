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

class PayPeriodResource(BaseModel):
    # The description of the Pay Period.
    description: typing.Optional[str] = Field(None, alias='description')

    # The unique identifier used to identify a pay period.
    pay_period_id: typing.Optional[str] = Field(None, alias='payPeriodId')

    # Frequency of the payroll period.
    interval_code: typing.Optional[Literal["ANNUAL", "BI_WEEKLY", "MONTHLY", "QUARTERLY", "SEMI_ANNUAL", "SEMI_MONTHLY", "WEEKLY"]] = Field(None, alias='intervalCode')

    # The current state of the associated pay period.
    status: typing.Optional[Literal["COMPLETED", "COMPLETED_BY_MEC", "ENTRY", "INITIAL", "PROCESSING", "REISSUED", "RELEASED", "REVERSED"]] = Field(None, alias='status')

    # The start date associated with this pay period.
    start_date: typing.Optional[datetime] = Field(None, alias='startDate')

    # The end date associated with this pay period.
    end_date: typing.Optional[datetime] = Field(None, alias='endDate')

    # The date by which information for the pay run must be submitted in order to be guaranteed the information is included.
    submit_by_date: typing.Optional[datetime] = Field(None, alias='submitByDate')

    # The date on which the checks associated with this pay period can be cashed.
    check_date: typing.Optional[datetime] = Field(None, alias='checkDate')

    # Number of checks that are included within the pay period.
    check_count: typing.Optional[int] = Field(None, alias='checkCount')

    links: typing.Optional[typing.List[Link]] = Field(None, alias='links')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
