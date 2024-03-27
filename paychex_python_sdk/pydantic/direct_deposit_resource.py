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

class DirectDepositResource(BaseModel):
    # The ID for the direct deposit item.
    direct_deposit_id: typing.Optional[str] = Field(None, alias='directDepositId')

    # The date that this direct deposit will be applied to future pay periods. This data field cannot be PATCHED.
    start_date: typing.Optional[datetime] = Field(None, alias='startDate')

    # A type of payment for the direct deposit.
    payment_type: typing.Optional[Literal["FLAT_DOLLAR_AMOUNT", "PERCENTAGE", "REMAINDER"]] = Field(None, alias='paymentType')

    # Financial institutions account type. This data field cannot be PATCHED.
    account_type: typing.Optional[Literal["CHECKING", "SAVINGS", "CREDIT_CARD"]] = Field(None, alias='accountType')

    # The amount to be applied to this direct deposit.
    value: typing.Optional[typing.Union[int, float]] = Field(None, alias='value')

    # The financial institutions routing number.This data field cannot be PATCHED.
    routing_number: typing.Optional[str] = Field(None, alias='routingNumber')

    # The financial institutions account number.This data field cannot be PATCHED.
    account_number: typing.Optional[str] = Field(None, alias='accountNumber')

    # The priority order for which the direct deposits will be performed in. When a new direct deposit is added the priority will be assigned. The priority can be modified only by swapping with a different direct deposit using the bulk PATCH. A paymentType of REMAINDER will show a priority of 99 and can't be modified.This data field cannot be PATCHED.
    priority: typing.Optional[str] = Field(None, alias='priority')

    links: typing.Optional[typing.List[Link]] = Field(None, alias='links')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
