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


class RequiredPostalResource(TypedDict):
    pass

class OptionalPostalResource(TypedDict, total=False):
    # The ID for the workers relationship to contact.
    communicationId: str

    # The street address line one. Required for street address. Required for POST contacts.
    streetLineOne: str

    # The street address line two.
    streetLineTwo: str

    # The postal office box. Required for PO Box with POST contacts.
    postOfficeBox: str

    # The city name. Required for POST contacts.
    city: str

    # The zip-code. Required for POST contacts.
    postalCode: str

    # The state code (ISO 3166 subdivision code). Required for POST contacts.
    countrySubdivisionCode: str

    # The country code (ISO 3166 alpha-2). Required for POST contacts.
    countryCode: str

class PostalResource(RequiredPostalResource, OptionalPostalResource):
    pass
