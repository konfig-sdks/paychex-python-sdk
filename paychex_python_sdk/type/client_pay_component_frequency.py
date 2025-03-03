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


class RequiredClientPayComponentFrequency(TypedDict):
    pass

class OptionalClientPayComponentFrequency(TypedDict, total=False):
    cfId: int

    frequencyOptionId: int

    freqTypeId: int

    frequencyType: str

    freqType: str

    payFreqId: int

    payFrequency: str

    payFreq: str

    firstPeriodOccurrenceId: int

    firstPeriodOccurrenceType: str

    firstFrequencyPeriod: str

    firstPeriodOccurrence: str

    secondPeriodOccurrenceId: int

    secondPeriodOccurrenceType: str

    secondFrequencyPeriod: str

    secondPeriodOccurrence: str

    intervalValue: int

    firstCheckRuleId: int

    firstCheckRuleType: str

    firstCheckRule: str

    firstCheckOnly: bool

class ClientPayComponentFrequency(RequiredClientPayComponentFrequency, OptionalClientPayComponentFrequency):
    pass
