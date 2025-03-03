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


class EmailResource(BaseModel):
    # The ID for this email communication.
    communication_id: typing.Optional[str] = Field(None, alias='communicationId')

    # The mailto address as specified in RFC2368. Required for POST contacts.
    uri: typing.Optional[str] = Field(None, alias='uri')

    # Enum: \"PERSONAL\", \"BUSINESS\"  A code classifying a designated use associated with a contact method. For example, whether a telephone or email address is one for work communications or one primarily for personal use. This data field cannot be PATCHED. Required for POST contacts.
    usage_type: typing.Optional[str] = Field(None, alias='usageType')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
