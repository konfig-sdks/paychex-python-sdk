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


class RequiredContactTypeResource1(TypedDict):
    pass

class OptionalContactTypeResource1(TypedDict, total=False):
    # The ID for specific type of contact. Required for POST contacts.
    contactTypeId: str

    # Enum:  \"EMERGENCY_CONTACT\"  The name for specific type of contact.
    contactTypeName: str

class ContactTypeResource1(RequiredContactTypeResource1, OptionalContactTypeResource1):
    pass
