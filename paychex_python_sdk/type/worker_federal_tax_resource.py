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


class RequiredWorkerFederalTaxResource(TypedDict):
    pass

class OptionalWorkerFederalTaxResource(TypedDict, total=False):
    # The ID for the federal tax item.
    taxId: str

    # Filing status.
    filingStatus: str

    # See federal W-4 instructions.
    multipleJobs: str

    # See federal W-4 instructions.
    dependentsAmount: str

    # See federal W-4 instructions.
    otherIncome: str

    # See federal W-4 instructions.
    deductionsAmount: str

    # Additional tax you want withheld each pay period.
    extraWithholdingAmount: str

    # Should federal taxes be withheld.
    taxesWithheld: str

class WorkerFederalTaxResource(RequiredWorkerFederalTaxResource, OptionalWorkerFederalTaxResource):
    pass
