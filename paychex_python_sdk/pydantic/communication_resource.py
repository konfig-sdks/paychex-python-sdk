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


class CommunicationResource(BaseModel):
    # The unique ID associated with communication 
    communication_id: typing.Optional[str] = Field(None, alias='communicationId')

    # A set of communication types classifying an instruction that the customer, requester, or subject must comply with in order for the screening to go forward. NOTE: PHONE and EMAIL type supports BUSINESS and PERSONAL usage type only.MOBILE_PHONE, FAX and PAGER supports BUSINESS usage type only.This data field cannot be PATCHED.
    type: typing.Optional[Literal["STREET_ADDRESS", "PO_BOX_ADDRESS", "PHONE", "MOBILE_PHONE", "FAX", "EMAIL", "PAGER"]] = Field(None, alias='type')

    # A code classifying a designated use associated with a contact method. For example, whether a telephone or email address is one for business communications or one primarily for personal use.This data field cannot be PATCHED.
    usage_type: typing.Optional[Literal["PERSONAL", "BUSINESS", "HOME", "WORK", "LOCATION_STREET_ADDRESS", "MAILING_ADDRESS"]] = Field(None, alias='usageType')

    # The country dialing code for a communication number.
    dial_country: typing.Optional[str] = Field(None, alias='dialCountry')

    # The area dialing code for a communication number.
    dial_area: typing.Optional[str] = Field(None, alias='dialArea')

    # The communication number, not including country dialing or area dialing codes.
    dial_number: typing.Optional[str] = Field(None, alias='dialNumber')

    # The extension of the associated communication number.
    dial_extension: typing.Optional[str] = Field(None, alias='dialExtension')

    # The mailto address as specified in RFC2368 .
    uri: typing.Optional[str] = Field(None, alias='uri')

    # The street address line one
    street_line_one: typing.Optional[str] = Field(None, alias='streetLineOne')

    # The street address line two
    street_line_two: typing.Optional[str] = Field(None, alias='streetLineTwo')

    # The postal office box. This data field cannot be PATCHED.
    post_office_box: typing.Optional[str] = Field(None, alias='postOfficeBox')

    # The city name
    city: typing.Optional[str] = Field(None, alias='city')

    # The zip-code
    postal_code: typing.Optional[str] = Field(None, alias='postalCode')

    # The zip-code extension
    postal_code_extension: typing.Optional[str] = Field(None, alias='postalCodeExtension')

    # The state code (ISO 3166 subdivision code). This data field cannot be PATCHED for ACTIVE worker.
    country_subdivision_code: typing.Optional[str] = Field(None, alias='countrySubdivisionCode')

    # The country code (ISO 3166 alpha-2)
    country_code: typing.Optional[str] = Field(None, alias='countryCode')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
