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


class ClientPayComponentOptions(BaseModel):
    opt_value_id: typing.Optional[int] = Field(None, alias='optValueId')

    opt_value_name: typing.Optional[str] = Field(None, alias='optValueName')

    opt_value_type_id: typing.Optional[int] = Field(None, alias='optValueTypeId')

    opt_value: typing.Optional[str] = Field(None, alias='optValue')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
