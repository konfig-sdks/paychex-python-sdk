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

from paychex_python_sdk.type.name_resource1 import NameResource1
from paychex_python_sdk.type.person_communication_resource import PersonCommunicationResource

class RequiredPersonResource(TypedDict):
    pass

class OptionalPersonResource(TypedDict, total=False):
    name: NameResource1

    communication: PersonCommunicationResource

class PersonResource(RequiredPersonResource, OptionalPersonResource):
    pass
