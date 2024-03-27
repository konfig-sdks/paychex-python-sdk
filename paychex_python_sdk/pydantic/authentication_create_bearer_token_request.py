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


class AuthenticationCreateBearerTokenRequest(BaseModel):
    # Send \"client_credentials\".
    grant_type: str = Field(alias='grant_type')

    # The applications API key.
    client_id: str = Field(alias='client_id')

    # The applications corresponding secret.
    client_secret: str = Field(alias='client_secret')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
