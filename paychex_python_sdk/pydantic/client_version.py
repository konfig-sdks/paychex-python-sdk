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

class ClientVersion(BaseModel):
    id: typing.Optional[int] = Field(None, alias='id')

    tax_payer_identification_number: typing.Optional[str] = Field(None, alias='taxPayerIdentificationNumber')

    tin_last_four: typing.Optional[str] = Field(None, alias='tinLastFour')

    tin_type: typing.Optional[str] = Field(None, alias='tinType')

    tin_valid_status_code: typing.Optional[str] = Field(None, alias='tinValidStatusCode')

    normalized_name: typing.Optional[str] = Field(None, alias='normalizedName')

    normalized_city: typing.Optional[str] = Field(None, alias='normalizedCity')

    normalized_country_code: typing.Optional[str] = Field(None, alias='normalizedCountryCode')

    version_status_code: typing.Optional[str] = Field(None, alias='versionStatusCode')

    begin_effective_date: typing.Optional[datetime] = Field(None, alias='beginEffectiveDate')

    end_effective_date: typing.Optional[datetime] = Field(None, alias='endEffectiveDate')

    normalized_building_number: typing.Optional[str] = Field(None, alias='normalizedBuildingNumber')

    normalized_steet_name: typing.Optional[str] = Field(None, alias='normalizedSteetName')

    normalized_unit_name: typing.Optional[str] = Field(None, alias='normalizedUnitName')

    normalized_p_o_box: typing.Optional[str] = Field(None, alias='normalizedPOBox')

    normalized_state_province: typing.Optional[str] = Field(None, alias='normalizedStateProvince')

    normalized_state_province_f: typing.Optional[str] = Field(None, alias='normalizedStateProvinceF')

    normalized_postal_code: typing.Optional[str] = Field(None, alias='normalizedPostalCode')

    tin_version_status_code: typing.Optional[str] = Field(None, alias='tinVersionStatusCode')

    status: typing.Optional[str] = Field(None, alias='status')

    status_date: typing.Optional[datetime] = Field(None, alias='statusDate')

    superceeded_by: typing.Optional[str] = Field(None, alias='superceededBy')

    modified_date: typing.Optional[datetime] = Field(None, alias='modifiedDate')

    modified_by_application_name: typing.Optional[str] = Field(None, alias='modifiedByApplicationName')

    modified_by_application_sub_process_name: typing.Optional[str] = Field(None, alias='modifiedByApplicationSubProcessName')

    modified_by_user_id: typing.Optional[str] = Field(None, alias='modifiedByUserId')

    modified_reason: typing.Optional[str] = Field(None, alias='modifiedReason')

    client: typing.Optional['Client'] = Field(None, alias='client')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
