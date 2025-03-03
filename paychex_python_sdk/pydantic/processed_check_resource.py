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
from paychex_python_sdk.pydantic.processed_check_component_resource import ProcessedCheckComponentResource

class ProcessedCheckResource(BaseModel):
    pay_period_id: typing.Optional[str] = Field(None, alias='payPeriodId')

    paycheck_id: typing.Optional[str] = Field(None, alias='paycheckId')

    worker_id: typing.Optional[str] = Field(None, alias='workerId')

    check_date: typing.Optional[datetime] = Field(None, alias='checkDate')

    net_pay: typing.Optional[str] = Field(None, alias='netPay')

    check_type: typing.Optional[str] = Field(None, alias='checkType')

    check_number: typing.Optional[str] = Field(None, alias='checkNumber')

    earnings: typing.Optional[typing.List[ProcessedCheckComponentResource]] = Field(None, alias='earnings')

    deductions: typing.Optional[typing.List[ProcessedCheckComponentResource]] = Field(None, alias='deductions')

    informational: typing.Optional[typing.List[ProcessedCheckComponentResource]] = Field(None, alias='informational')

    taxes: typing.Optional[typing.List[ProcessedCheckComponentResource]] = Field(None, alias='taxes')

    gross_earnings: typing.Optional[str] = Field(None, alias='grossEarnings')

    links: typing.Optional[typing.List[Link]] = Field(None, alias='links')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
