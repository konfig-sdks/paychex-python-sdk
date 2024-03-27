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


class RequiredCustomFieldsDropdownResource(TypedDict):
    pass

class OptionalCustomFieldsDropdownResource(TypedDict, total=False):
    # The unique identifier that is autogenerated when dropdown list is created
    dropdownId: str

    # The value for dropdown list
    dropdownValue: str

    # The default value for dropdown list
    dropdownDefault: bool

class CustomFieldsDropdownResource(RequiredCustomFieldsDropdownResource, OptionalCustomFieldsDropdownResource):
    pass
