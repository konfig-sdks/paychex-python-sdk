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

from paychex_python_sdk.type.pay_rate_resource import PayRateResource
from paychex_python_sdk.type.pay_standard_resource import PayStandardResource

class RequiredPayRatesStandardResource(TypedDict):
    pass

class OptionalPayRatesStandardResource(TypedDict, total=False):
    payStandards: PayStandardResource

    payRates: typing.List[PayRateResource]

class PayRatesStandardResource(RequiredPayRatesStandardResource, OptionalPayRatesStandardResource):
    pass
