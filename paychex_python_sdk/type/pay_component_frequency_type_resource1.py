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

from paychex_python_sdk.type.frequency_intervals_resource1 import FrequencyIntervalsResource1

class RequiredPayComponentFrequencyTypeResource1(TypedDict):
    pass

class OptionalPayComponentFrequencyTypeResource1(TypedDict, total=False):
    # Currently we only support a BY_PAY_PERIOD value for the API.
    applied: str

    # This is how often the pay component will be applied on the pay run. The available values for this will depend on the payFrequency that a worker is paid which can be found on the worker compensations pay standards.
    occurrence: str

    occurrenceIntervals: FrequencyIntervalsResource1

    # Which check(s) within the payrun that the paycomponent will be applied to.FIRST_CHECK: The Pay Component will be applied to the first check for the worker within the pay run. This is used for a pay component that only should be applied once like a health insurance deduction.EVERY_CHECK: The Pay Component will be applied to all of the checks for the worker within the pay run. This is used for a pay component that is applied on all check like a retirement deduction.
    effectedChecks: str

class PayComponentFrequencyTypeResource1(RequiredPayComponentFrequencyTypeResource1, OptionalPayComponentFrequencyTypeResource1):
    pass
