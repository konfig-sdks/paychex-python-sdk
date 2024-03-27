# coding: utf-8

"""
    External API

      # Developer Resources  Refer [Developer Resources](https://developer.paychex.com/resources/overview/) for more details on API specification 

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from paychex_python_sdk import schemas  # noqa: F401


class WebhooksListResponse(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['WebhooksListResponseItem']:
            return WebhooksListResponseItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['WebhooksListResponseItem'], typing.List['WebhooksListResponseItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'WebhooksListResponse':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'WebhooksListResponseItem':
        return super().__getitem__(i)

from paychex_python_sdk.model.webhooks_list_response_item import WebhooksListResponseItem
