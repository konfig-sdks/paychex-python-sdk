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

from paychex_python_sdk.pydantic.link import Link

class OrganizationResource1(BaseModel):
    # The unique identifier associated with this organizations representation.
    organization_id: typing.Optional[str] = Field(None, alias='organizationId')

    # The name of the organization.
    name: typing.Optional[str] = Field(None, alias='name')

    # The number assigned to the organization.
    number: typing.Optional[str] = Field(None, alias='number')

    # The level number within the organizational structures hierarchy.
    level: typing.Optional[str] = Field(None, alias='level')

    children: typing.Optional['typing.List["OrganizationResource1"]'] = Field(None, alias='children')

    links: typing.Optional[typing.List[Link]] = Field(None, alias='links')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
