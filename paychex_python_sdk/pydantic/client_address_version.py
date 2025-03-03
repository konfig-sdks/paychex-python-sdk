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
    from paychex_python_sdk.pydantic.client_address import ClientAddress

class ClientAddressVersion(BaseModel):
    id: typing.Optional[int] = Field(None, alias='id')

    city: typing.Optional[str] = Field(None, alias='city')

    val_state_code: typing.Optional[str] = Field(None, alias='valStateCode')

    ver_state_code: typing.Optional[str] = Field(None, alias='verStateCode')

    begin_effective_date: typing.Optional[datetime] = Field(None, alias='beginEffectiveDate')

    end_effective_date: typing.Optional[datetime] = Field(None, alias='endEffectiveDate')

    modified_date: typing.Optional[datetime] = Field(None, alias='modifiedDate')

    state_province: typing.Optional[str] = Field(None, alias='stateProvince')

    state_province_f: typing.Optional[str] = Field(None, alias='stateProvinceF')

    portal_code: typing.Optional[str] = Field(None, alias='portalCode')

    country_code: typing.Optional[str] = Field(None, alias='countryCode')

    building_number: typing.Optional[str] = Field(None, alias='buildingNumber')

    unit_name: typing.Optional[str] = Field(None, alias='unitName')

    street_name: typing.Optional[str] = Field(None, alias='streetName')

    po_box: typing.Optional[str] = Field(None, alias='poBox')

    street_address_one: typing.Optional[str] = Field(None, alias='streetAddressOne')

    street_address_two: typing.Optional[str] = Field(None, alias='streetAddressTwo')

    modifed_by_application_name: typing.Optional[str] = Field(None, alias='modifedByApplicationName')

    modified_by_application_sub_process_name: typing.Optional[str] = Field(None, alias='modifiedByApplicationSubProcessName')

    modified_by_user_id: typing.Optional[str] = Field(None, alias='modifiedByUserId')

    client_address: typing.Optional['ClientAddress'] = Field(None, alias='clientAddress')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
