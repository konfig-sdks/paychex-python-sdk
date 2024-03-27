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
from pydantic import BaseModel, Field, RootModel, ConfigDict


class Authentication(BaseModel):
    # The token which will be used for making future calls.
    access_token: typing.Optional[str] = Field(None, alias='access_token')

    # Number of seconds remaining before the token expires.
    expires_in: typing.Optional[str] = Field(None, alias='expires_in')

    # This will always return 'oob' (out of band) based on OAuth configuration.
    scope: typing.Optional[str] = Field(None, alias='scope')

    # This will always return 'Bearer' based on OAuth configuration.
    token_type: typing.Optional[str] = Field(None, alias='token_type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
