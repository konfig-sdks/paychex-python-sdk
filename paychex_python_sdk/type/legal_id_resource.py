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


class RequiredLegalIdResource(TypedDict):
    pass

class OptionalLegalIdResource(TypedDict, total=False):
    # A value that identifies the type of taxpayer identification number provided.   SSN: Social  Security Number - 9 digit number   , FEIN: Federal Employer Identification Number (EIN)
    legalIdType: str

    # The federal level taxpayer id number assigned to a business
    legalIdValue: str

class LegalIdResource(RequiredLegalIdResource, OptionalLegalIdResource):
    pass
