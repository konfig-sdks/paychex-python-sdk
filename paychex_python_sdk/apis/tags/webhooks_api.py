# coding: utf-8

"""
    External API

      # Developer Resources  Refer [Developer Resources](https://developer.paychex.com/resources/overview/) for more details on API specification 

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from paychex_python_sdk.paths.management_hooks.post import AddWebhook
from paychex_python_sdk.paths.management_hooks_hook_id.delete import DeleteById
from paychex_python_sdk.paths.management_domains.get import GetAvailableDomains
from paychex_python_sdk.paths.management_hooks_hook_id.get import GetSpecificHookById
from paychex_python_sdk.paths.management_hooks.get import List
from paychex_python_sdk.apis.tags.webhooks_api_raw import WebhooksApiRaw


class WebhooksApi(
    AddWebhook,
    DeleteById,
    GetAvailableDomains,
    GetSpecificHookById,
    List,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: WebhooksApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = WebhooksApiRaw(api_client)
