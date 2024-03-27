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


class RequiredAuthentication(TypedDict):
    pass

class OptionalAuthentication(TypedDict, total=False):
    # The token which will be used for making future calls.
    access_token: str

    # Number of seconds remaining before the token expires.
    expires_in: str

    # This will always return 'oob' (out of band) based on OAuth configuration.
    scope: str

    # This will always return 'Bearer' based on OAuth configuration.
    token_type: str

class Authentication(RequiredAuthentication, OptionalAuthentication):
    pass
