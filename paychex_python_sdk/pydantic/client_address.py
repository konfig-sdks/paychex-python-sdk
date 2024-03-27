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

if TYPE_CHECKING:
    from paychex_python_sdk.pydantic.client import Client
if TYPE_CHECKING:
    from paychex_python_sdk.pydantic.client_address_version import ClientAddressVersion

class ClientAddress(BaseModel):
    id: typing.Optional[int] = Field(None, alias='id')

    address_usage_type: typing.Optional[str] = Field(None, alias='addressUsageType')

    created_date: typing.Optional[datetime] = Field(None, alias='createdDate')

    created_by_application_name: typing.Optional[str] = Field(None, alias='createdByApplicationName')

    created_by_user_id: typing.Optional[str] = Field(None, alias='createdByUserId')

    created_by_application_sub_process_name: typing.Optional[str] = Field(None, alias='createdByApplicationSubProcessName')

    client: typing.Optional['Client'] = Field(None, alias='client')

    client_address_versions: typing.Optional['typing.List[ClientAddressVersion]'] = Field(None, alias='clientAddressVersions')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
