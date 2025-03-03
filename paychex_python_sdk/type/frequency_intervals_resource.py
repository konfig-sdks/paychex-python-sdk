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


class RequiredFrequencyIntervalsResource(TypedDict):
    pass

class OptionalFrequencyIntervalsResource(TypedDict, total=False):
    # Interval 1 
    interval1: str

    # Interval 2
    interval2: str

class FrequencyIntervalsResource(RequiredFrequencyIntervalsResource, OptionalFrequencyIntervalsResource):
    pass
