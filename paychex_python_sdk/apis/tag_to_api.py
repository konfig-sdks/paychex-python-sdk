import typing_extensions

from paychex_python_sdk.apis.tags import TagValues
from paychex_python_sdk.apis.tags.worker_api import WorkerApi
from paychex_python_sdk.apis.tags.company_api import CompanyApi
from paychex_python_sdk.apis.tags.payroll_api import PayrollApi
from paychex_python_sdk.apis.tags.webhooks_api import WebhooksApi
from paychex_python_sdk.apis.tags.authentication_api import AuthenticationApi
from paychex_python_sdk.apis.tags.management_api import ManagementApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.WORKER: WorkerApi,
        TagValues.COMPANY: CompanyApi,
        TagValues.PAYROLL: PayrollApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.MANAGEMENT: ManagementApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.WORKER: WorkerApi,
        TagValues.COMPANY: CompanyApi,
        TagValues.PAYROLL: PayrollApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.MANAGEMENT: ManagementApi,
    }
)
