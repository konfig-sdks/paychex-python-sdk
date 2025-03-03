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

from paychex_python_sdk.type.link import Link

class RequiredPurchaseResource(TypedDict):
    pass

class OptionalPurchaseResource(TypedDict, total=False):
    transactionId: str

    type: str

    count: str

    price: typing.Union[int, float]

    links: typing.List[Link]

class PurchaseResource(RequiredPurchaseResource, OptionalPurchaseResource):
    pass
