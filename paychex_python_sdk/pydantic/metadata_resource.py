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

from paychex_python_sdk.pydantic.pagination_metadata_resource import PaginationMetadataResource

class MetadataResource(BaseModel):
    content_item_count: typing.Optional[int] = Field(None, alias='contentItemCount')

    pagination: typing.Optional[PaginationMetadataResource] = Field(None, alias='pagination')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
