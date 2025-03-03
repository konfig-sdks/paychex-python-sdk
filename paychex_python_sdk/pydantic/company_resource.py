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

from paychex_python_sdk.pydantic.communication_resource import CommunicationResource
from paychex_python_sdk.pydantic.legal_id_resource import LegalIdResource
from paychex_python_sdk.pydantic.link import Link

class CompanyResource(BaseModel):
    # The unique identifier associated with this companies representation.
    company_id: typing.Optional[str] = Field(None, alias='companyId')

    # The client account number used for identification purposes. (no dash or spaces allowed, only the last 8 characters  of the ID)
    display_id: typing.Optional[str] = Field(None, alias='displayId')

    # The legal name of the company.
    legal_name: typing.Optional[str] = Field(None, alias='legalName')

    legal_id: typing.Optional[LegalIdResource] = Field(None, alias='legalId')

    communications: typing.Optional[typing.List[CommunicationResource]] = Field(None, alias='communications')

    links: typing.Optional[typing.List[Link]] = Field(None, alias='links')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
