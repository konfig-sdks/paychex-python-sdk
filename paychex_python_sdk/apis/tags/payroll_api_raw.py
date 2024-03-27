# coding: utf-8

"""
    External API

      # Developer Resources  Refer [Developer Resources](https://developer.paychex.com/resources/overview/) for more details on API specification 

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from paychex_python_sdk.paths.companies_company_id_checks.post import AddCompanyChecksRaw
from paychex_python_sdk.paths.checks_check_id_checkcomponents.post import AddPayComponentToCheckRaw
from paychex_python_sdk.paths.workers_worker_id_checks.post import AddWorkerCheckRaw
from paychex_python_sdk.paths.checks.delete import DeleteChecksByPayPeriodAndUserRaw
from paychex_python_sdk.paths.companies_company_id_checks.get import GetCompanyChecksByPayPeriodRaw
from paychex_python_sdk.paths.companies_company_id_paycomponents_paycomponent_id.get import GetCompanyPayComponentRaw
from paychex_python_sdk.paths.companies_company_id_paycomponents.get import GetCompanyPayComponentsRaw
from paychex_python_sdk.paths.companies_company_id_payperiods.get import GetCompanyPayPeriodsRaw
from paychex_python_sdk.paths.companies_company_id_payperiods_payperiod_id.get import GetPayPeriodRaw
from paychex_python_sdk.paths.workers_worker_id_checks_external_check_id.get import GetWorkerCheckRaw
from paychex_python_sdk.paths.workers_worker_id_checks.get import GetWorkerChecksByPayPeriodRaw
from paychex_python_sdk.paths.checks_check_id_checkcomponents_check_component_id.delete import RemovePayComponentRaw
from paychex_python_sdk.paths.workers_worker_id_checks_external_check_id.delete import RemoveWorkerCheckRaw
from paychex_python_sdk.paths.checks_check_id_checkcomponents_check_component_id.patch import UpdatePayComponentRaw


class PayrollApiRaw(
    AddCompanyChecksRaw,
    AddPayComponentToCheckRaw,
    AddWorkerCheckRaw,
    DeleteChecksByPayPeriodAndUserRaw,
    GetCompanyChecksByPayPeriodRaw,
    GetCompanyPayComponentRaw,
    GetCompanyPayComponentsRaw,
    GetCompanyPayPeriodsRaw,
    GetPayPeriodRaw,
    GetWorkerCheckRaw,
    GetWorkerChecksByPayPeriodRaw,
    RemovePayComponentRaw,
    RemoveWorkerCheckRaw,
    UpdatePayComponentRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
