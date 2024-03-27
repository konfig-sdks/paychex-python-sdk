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

from paychex_python_sdk.pydantic.report_resource_document_content import ReportResourceDocumentContent

class ReportResource(BaseModel):
    document_name: typing.Optional[str] = Field(None, alias='documentName')

    document_content: typing.Optional[ReportResourceDocumentContent] = Field(None, alias='documentContent')

    file_name: typing.Optional[str] = Field(None, alias='fileName')

    type: typing.Optional[str] = Field(None, alias='type')

    size: typing.Optional[int] = Field(None, alias='size')

    success_indicator: typing.Optional[bool] = Field(None, alias='successIndicator')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
