import typing_extensions

from paychex_python_sdk.paths import PathValues
from paychex_python_sdk.apis.paths.auth_oauth_v2_token import AuthOauthV2Token
from paychex_python_sdk.apis.paths.companies import Companies
from paychex_python_sdk.apis.paths.companies_company_id import CompaniesCompanyId
from paychex_python_sdk.apis.paths.companies_company_id_calculationbases import CompaniesCompanyIdCalculationbases
from paychex_python_sdk.apis.paths.companies_company_id_checks import CompaniesCompanyIdChecks
from paychex_python_sdk.apis.paths.companies_company_id_contacttypes import CompaniesCompanyIdContacttypes
from paychex_python_sdk.apis.paths.companies_company_id_customfields import CompaniesCompanyIdCustomfields
from paychex_python_sdk.apis.paths.companies_company_id_customfields_custom_field_id import CompaniesCompanyIdCustomfieldsCustomFieldId
from paychex_python_sdk.apis.paths.companies_company_id_customfields_customfieldid import CompaniesCompanyIdCustomfieldsCustomfieldid
from paychex_python_sdk.apis.paths.companies_company_id_customfieldscategories import CompaniesCompanyIdCustomfieldscategories
from paychex_python_sdk.apis.paths.companies_company_id_customfieldscategories_category_id import CompaniesCompanyIdCustomfieldscategoriesCategoryId
from paychex_python_sdk.apis.paths.companies_company_id_customfieldscategories_categoryid import CompaniesCompanyIdCustomfieldscategoriesCategoryid
from paychex_python_sdk.apis.paths.companies_company_id_jobs import CompaniesCompanyIdJobs
from paychex_python_sdk.apis.paths.companies_company_id_jobs_job_id import CompaniesCompanyIdJobsJobId
from paychex_python_sdk.apis.paths.companies_company_id_jobsegments import CompaniesCompanyIdJobsegments
from paychex_python_sdk.apis.paths.companies_company_id_jobtitles import CompaniesCompanyIdJobtitles
from paychex_python_sdk.apis.paths.companies_company_id_jobtitles_job_title_id import CompaniesCompanyIdJobtitlesJobTitleId
from paychex_python_sdk.apis.paths.companies_company_id_laborassignments import CompaniesCompanyIdLaborassignments
from paychex_python_sdk.apis.paths.companies_company_id_laborassignments_labor_assignment_id import CompaniesCompanyIdLaborassignmentsLaborAssignmentId
from paychex_python_sdk.apis.paths.companies_company_id_locations import CompaniesCompanyIdLocations
from paychex_python_sdk.apis.paths.companies_company_id_locations_location_id import CompaniesCompanyIdLocationsLocationId
from paychex_python_sdk.apis.paths.companies_company_id_organizations import CompaniesCompanyIdOrganizations
from paychex_python_sdk.apis.paths.companies_company_id_organizations_org_id import CompaniesCompanyIdOrganizationsOrgId
from paychex_python_sdk.apis.paths.companies_company_id_paycomponents import CompaniesCompanyIdPaycomponents
from paychex_python_sdk.apis.paths.companies_company_id_paycomponents_paycomponent_id import CompaniesCompanyIdPaycomponentsPaycomponentId
from paychex_python_sdk.apis.paths.companies_company_id_payfrequencies import CompaniesCompanyIdPayfrequencies
from paychex_python_sdk.apis.paths.companies_company_id_payperiods import CompaniesCompanyIdPayperiods
from paychex_python_sdk.apis.paths.companies_company_id_payperiods_payperiod_id import CompaniesCompanyIdPayperiodsPayperiodId
from paychex_python_sdk.apis.paths.companies_company_id_workers import CompaniesCompanyIdWorkers
from paychex_python_sdk.apis.paths.companies_company_id_workerstatuses import CompaniesCompanyIdWorkerstatuses
from paychex_python_sdk.apis.paths.companies_company_id_workerstatuses_status_id import CompaniesCompanyIdWorkerstatusesStatusId
from paychex_python_sdk.apis.paths.workers_worker_id import WorkersWorkerId
from paychex_python_sdk.apis.paths.workers_worker_id_assignmentdistributions import WorkersWorkerIdAssignmentdistributions
from paychex_python_sdk.apis.paths.workers_worker_id_checks import WorkersWorkerIdChecks
from paychex_python_sdk.apis.paths.workers_worker_id_checks_external_check_id import WorkersWorkerIdChecksExternalCheckId
from paychex_python_sdk.apis.paths.workers_worker_id_communications import WorkersWorkerIdCommunications
from paychex_python_sdk.apis.paths.workers_worker_id_communications_communication_id import WorkersWorkerIdCommunicationsCommunicationId
from paychex_python_sdk.apis.paths.workers_worker_id_compensation import WorkersWorkerIdCompensation
from paychex_python_sdk.apis.paths.workers_worker_id_compensation_payrates import WorkersWorkerIdCompensationPayrates
from paychex_python_sdk.apis.paths.workers_worker_id_compensation_payrates_rate_id import WorkersWorkerIdCompensationPayratesRateId
from paychex_python_sdk.apis.paths.workers_worker_id_compensation_paystandards import WorkersWorkerIdCompensationPaystandards
from paychex_python_sdk.apis.paths.workers_worker_id_contacts import WorkersWorkerIdContacts
from paychex_python_sdk.apis.paths.workers_worker_id_contacts_contact_id import WorkersWorkerIdContactsContactId
from paychex_python_sdk.apis.paths.workers_worker_id_customfields import WorkersWorkerIdCustomfields
from paychex_python_sdk.apis.paths.workers_worker_id_customfields_worker_custom_field_id import WorkersWorkerIdCustomfieldsWorkerCustomFieldId
from paychex_python_sdk.apis.paths.workers_worker_id_directdeposits import WorkersWorkerIdDirectdeposits
from paychex_python_sdk.apis.paths.workers_worker_id_directdeposits_direct_deposit_id import WorkersWorkerIdDirectdepositsDirectDepositId
from paychex_python_sdk.apis.paths.workers_worker_id_federaltax import WorkersWorkerIdFederaltax
from paychex_python_sdk.apis.paths.workers_worker_id_paycomponents import WorkersWorkerIdPaycomponents
from paychex_python_sdk.apis.paths.workers_worker_id_paycomponents_worker_component_id import WorkersWorkerIdPaycomponentsWorkerComponentId
from paychex_python_sdk.apis.paths.workers_worker_id_status import WorkersWorkerIdStatus
from paychex_python_sdk.apis.paths.workers_worker_id_timeoff import WorkersWorkerIdTimeoff
from paychex_python_sdk.apis.paths.checks import Checks
from paychex_python_sdk.apis.paths.checks_check_id_checkcomponents import ChecksCheckIdCheckcomponents
from paychex_python_sdk.apis.paths.checks_check_id_checkcomponents_check_component_id import ChecksCheckIdCheckcomponentsCheckComponentId
from paychex_python_sdk.apis.paths.management_domains import ManagementDomains
from paychex_python_sdk.apis.paths.management_hooks import ManagementHooks
from paychex_python_sdk.apis.paths.management_hooks_hook_id import ManagementHooksHookId
from paychex_python_sdk.apis.paths.management_requestclientaccess import ManagementRequestclientaccess

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.AUTH_OAUTH_V2_TOKEN: AuthOauthV2Token,
        PathValues.COMPANIES: Companies,
        PathValues.COMPANIES_COMPANY_ID: CompaniesCompanyId,
        PathValues.COMPANIES_COMPANY_ID_CALCULATIONBASES: CompaniesCompanyIdCalculationbases,
        PathValues.COMPANIES_COMPANY_ID_CHECKS: CompaniesCompanyIdChecks,
        PathValues.COMPANIES_COMPANY_ID_CONTACTTYPES: CompaniesCompanyIdContacttypes,
        PathValues.COMPANIES_COMPANY_ID_CUSTOMFIELDS: CompaniesCompanyIdCustomfields,
        PathValues.COMPANIES_COMPANY_ID_CUSTOMFIELDS_CUSTOM_FIELD_ID: CompaniesCompanyIdCustomfieldsCustomFieldId,
        PathValues.COMPANIES_COMPANY_ID_CUSTOMFIELDS_CUSTOMFIELDID: CompaniesCompanyIdCustomfieldsCustomfieldid,
        PathValues.COMPANIES_COMPANY_ID_CUSTOMFIELDSCATEGORIES: CompaniesCompanyIdCustomfieldscategories,
        PathValues.COMPANIES_COMPANY_ID_CUSTOMFIELDSCATEGORIES_CATEGORY_ID: CompaniesCompanyIdCustomfieldscategoriesCategoryId,
        PathValues.COMPANIES_COMPANY_ID_CUSTOMFIELDSCATEGORIES_CATEGORYID: CompaniesCompanyIdCustomfieldscategoriesCategoryid,
        PathValues.COMPANIES_COMPANY_ID_JOBS: CompaniesCompanyIdJobs,
        PathValues.COMPANIES_COMPANY_ID_JOBS_JOB_ID: CompaniesCompanyIdJobsJobId,
        PathValues.COMPANIES_COMPANY_ID_JOBSEGMENTS: CompaniesCompanyIdJobsegments,
        PathValues.COMPANIES_COMPANY_ID_JOBTITLES: CompaniesCompanyIdJobtitles,
        PathValues.COMPANIES_COMPANY_ID_JOBTITLES_JOB_TITLE_ID: CompaniesCompanyIdJobtitlesJobTitleId,
        PathValues.COMPANIES_COMPANY_ID_LABORASSIGNMENTS: CompaniesCompanyIdLaborassignments,
        PathValues.COMPANIES_COMPANY_ID_LABORASSIGNMENTS_LABOR_ASSIGNMENT_ID: CompaniesCompanyIdLaborassignmentsLaborAssignmentId,
        PathValues.COMPANIES_COMPANY_ID_LOCATIONS: CompaniesCompanyIdLocations,
        PathValues.COMPANIES_COMPANY_ID_LOCATIONS_LOCATION_ID: CompaniesCompanyIdLocationsLocationId,
        PathValues.COMPANIES_COMPANY_ID_ORGANIZATIONS: CompaniesCompanyIdOrganizations,
        PathValues.COMPANIES_COMPANY_ID_ORGANIZATIONS_ORG_ID: CompaniesCompanyIdOrganizationsOrgId,
        PathValues.COMPANIES_COMPANY_ID_PAYCOMPONENTS: CompaniesCompanyIdPaycomponents,
        PathValues.COMPANIES_COMPANY_ID_PAYCOMPONENTS_PAYCOMPONENT_ID: CompaniesCompanyIdPaycomponentsPaycomponentId,
        PathValues.COMPANIES_COMPANY_ID_PAYFREQUENCIES: CompaniesCompanyIdPayfrequencies,
        PathValues.COMPANIES_COMPANY_ID_PAYPERIODS: CompaniesCompanyIdPayperiods,
        PathValues.COMPANIES_COMPANY_ID_PAYPERIODS_PAYPERIOD_ID: CompaniesCompanyIdPayperiodsPayperiodId,
        PathValues.COMPANIES_COMPANY_ID_WORKERS: CompaniesCompanyIdWorkers,
        PathValues.COMPANIES_COMPANY_ID_WORKERSTATUSES: CompaniesCompanyIdWorkerstatuses,
        PathValues.COMPANIES_COMPANY_ID_WORKERSTATUSES_STATUS_ID: CompaniesCompanyIdWorkerstatusesStatusId,
        PathValues.WORKERS_WORKER_ID: WorkersWorkerId,
        PathValues.WORKERS_WORKER_ID_ASSIGNMENTDISTRIBUTIONS: WorkersWorkerIdAssignmentdistributions,
        PathValues.WORKERS_WORKER_ID_CHECKS: WorkersWorkerIdChecks,
        PathValues.WORKERS_WORKER_ID_CHECKS_EXTERNAL_CHECK_ID: WorkersWorkerIdChecksExternalCheckId,
        PathValues.WORKERS_WORKER_ID_COMMUNICATIONS: WorkersWorkerIdCommunications,
        PathValues.WORKERS_WORKER_ID_COMMUNICATIONS_COMMUNICATION_ID: WorkersWorkerIdCommunicationsCommunicationId,
        PathValues.WORKERS_WORKER_ID_COMPENSATION: WorkersWorkerIdCompensation,
        PathValues.WORKERS_WORKER_ID_COMPENSATION_PAYRATES: WorkersWorkerIdCompensationPayrates,
        PathValues.WORKERS_WORKER_ID_COMPENSATION_PAYRATES_RATE_ID: WorkersWorkerIdCompensationPayratesRateId,
        PathValues.WORKERS_WORKER_ID_COMPENSATION_PAYSTANDARDS: WorkersWorkerIdCompensationPaystandards,
        PathValues.WORKERS_WORKER_ID_CONTACTS: WorkersWorkerIdContacts,
        PathValues.WORKERS_WORKER_ID_CONTACTS_CONTACT_ID: WorkersWorkerIdContactsContactId,
        PathValues.WORKERS_WORKER_ID_CUSTOMFIELDS: WorkersWorkerIdCustomfields,
        PathValues.WORKERS_WORKER_ID_CUSTOMFIELDS_WORKER_CUSTOM_FIELD_ID: WorkersWorkerIdCustomfieldsWorkerCustomFieldId,
        PathValues.WORKERS_WORKER_ID_DIRECTDEPOSITS: WorkersWorkerIdDirectdeposits,
        PathValues.WORKERS_WORKER_ID_DIRECTDEPOSITS_DIRECT_DEPOSIT_ID: WorkersWorkerIdDirectdepositsDirectDepositId,
        PathValues.WORKERS_WORKER_ID_FEDERALTAX: WorkersWorkerIdFederaltax,
        PathValues.WORKERS_WORKER_ID_PAYCOMPONENTS: WorkersWorkerIdPaycomponents,
        PathValues.WORKERS_WORKER_ID_PAYCOMPONENTS_WORKER_COMPONENT_ID: WorkersWorkerIdPaycomponentsWorkerComponentId,
        PathValues.WORKERS_WORKER_ID_STATUS: WorkersWorkerIdStatus,
        PathValues.WORKERS_WORKER_ID_TIMEOFF: WorkersWorkerIdTimeoff,
        PathValues.CHECKS: Checks,
        PathValues.CHECKS_CHECK_ID_CHECKCOMPONENTS: ChecksCheckIdCheckcomponents,
        PathValues.CHECKS_CHECK_ID_CHECKCOMPONENTS_CHECK_COMPONENT_ID: ChecksCheckIdCheckcomponentsCheckComponentId,
        PathValues.MANAGEMENT_DOMAINS: ManagementDomains,
        PathValues.MANAGEMENT_HOOKS: ManagementHooks,
        PathValues.MANAGEMENT_HOOKS_HOOK_ID: ManagementHooksHookId,
        PathValues.MANAGEMENT_REQUESTCLIENTACCESS: ManagementRequestclientaccess,
    }
)

path_to_api = PathToApi(
    {
        PathValues.AUTH_OAUTH_V2_TOKEN: AuthOauthV2Token,
        PathValues.COMPANIES: Companies,
        PathValues.COMPANIES_COMPANY_ID: CompaniesCompanyId,
        PathValues.COMPANIES_COMPANY_ID_CALCULATIONBASES: CompaniesCompanyIdCalculationbases,
        PathValues.COMPANIES_COMPANY_ID_CHECKS: CompaniesCompanyIdChecks,
        PathValues.COMPANIES_COMPANY_ID_CONTACTTYPES: CompaniesCompanyIdContacttypes,
        PathValues.COMPANIES_COMPANY_ID_CUSTOMFIELDS: CompaniesCompanyIdCustomfields,
        PathValues.COMPANIES_COMPANY_ID_CUSTOMFIELDS_CUSTOM_FIELD_ID: CompaniesCompanyIdCustomfieldsCustomFieldId,
        PathValues.COMPANIES_COMPANY_ID_CUSTOMFIELDS_CUSTOMFIELDID: CompaniesCompanyIdCustomfieldsCustomfieldid,
        PathValues.COMPANIES_COMPANY_ID_CUSTOMFIELDSCATEGORIES: CompaniesCompanyIdCustomfieldscategories,
        PathValues.COMPANIES_COMPANY_ID_CUSTOMFIELDSCATEGORIES_CATEGORY_ID: CompaniesCompanyIdCustomfieldscategoriesCategoryId,
        PathValues.COMPANIES_COMPANY_ID_CUSTOMFIELDSCATEGORIES_CATEGORYID: CompaniesCompanyIdCustomfieldscategoriesCategoryid,
        PathValues.COMPANIES_COMPANY_ID_JOBS: CompaniesCompanyIdJobs,
        PathValues.COMPANIES_COMPANY_ID_JOBS_JOB_ID: CompaniesCompanyIdJobsJobId,
        PathValues.COMPANIES_COMPANY_ID_JOBSEGMENTS: CompaniesCompanyIdJobsegments,
        PathValues.COMPANIES_COMPANY_ID_JOBTITLES: CompaniesCompanyIdJobtitles,
        PathValues.COMPANIES_COMPANY_ID_JOBTITLES_JOB_TITLE_ID: CompaniesCompanyIdJobtitlesJobTitleId,
        PathValues.COMPANIES_COMPANY_ID_LABORASSIGNMENTS: CompaniesCompanyIdLaborassignments,
        PathValues.COMPANIES_COMPANY_ID_LABORASSIGNMENTS_LABOR_ASSIGNMENT_ID: CompaniesCompanyIdLaborassignmentsLaborAssignmentId,
        PathValues.COMPANIES_COMPANY_ID_LOCATIONS: CompaniesCompanyIdLocations,
        PathValues.COMPANIES_COMPANY_ID_LOCATIONS_LOCATION_ID: CompaniesCompanyIdLocationsLocationId,
        PathValues.COMPANIES_COMPANY_ID_ORGANIZATIONS: CompaniesCompanyIdOrganizations,
        PathValues.COMPANIES_COMPANY_ID_ORGANIZATIONS_ORG_ID: CompaniesCompanyIdOrganizationsOrgId,
        PathValues.COMPANIES_COMPANY_ID_PAYCOMPONENTS: CompaniesCompanyIdPaycomponents,
        PathValues.COMPANIES_COMPANY_ID_PAYCOMPONENTS_PAYCOMPONENT_ID: CompaniesCompanyIdPaycomponentsPaycomponentId,
        PathValues.COMPANIES_COMPANY_ID_PAYFREQUENCIES: CompaniesCompanyIdPayfrequencies,
        PathValues.COMPANIES_COMPANY_ID_PAYPERIODS: CompaniesCompanyIdPayperiods,
        PathValues.COMPANIES_COMPANY_ID_PAYPERIODS_PAYPERIOD_ID: CompaniesCompanyIdPayperiodsPayperiodId,
        PathValues.COMPANIES_COMPANY_ID_WORKERS: CompaniesCompanyIdWorkers,
        PathValues.COMPANIES_COMPANY_ID_WORKERSTATUSES: CompaniesCompanyIdWorkerstatuses,
        PathValues.COMPANIES_COMPANY_ID_WORKERSTATUSES_STATUS_ID: CompaniesCompanyIdWorkerstatusesStatusId,
        PathValues.WORKERS_WORKER_ID: WorkersWorkerId,
        PathValues.WORKERS_WORKER_ID_ASSIGNMENTDISTRIBUTIONS: WorkersWorkerIdAssignmentdistributions,
        PathValues.WORKERS_WORKER_ID_CHECKS: WorkersWorkerIdChecks,
        PathValues.WORKERS_WORKER_ID_CHECKS_EXTERNAL_CHECK_ID: WorkersWorkerIdChecksExternalCheckId,
        PathValues.WORKERS_WORKER_ID_COMMUNICATIONS: WorkersWorkerIdCommunications,
        PathValues.WORKERS_WORKER_ID_COMMUNICATIONS_COMMUNICATION_ID: WorkersWorkerIdCommunicationsCommunicationId,
        PathValues.WORKERS_WORKER_ID_COMPENSATION: WorkersWorkerIdCompensation,
        PathValues.WORKERS_WORKER_ID_COMPENSATION_PAYRATES: WorkersWorkerIdCompensationPayrates,
        PathValues.WORKERS_WORKER_ID_COMPENSATION_PAYRATES_RATE_ID: WorkersWorkerIdCompensationPayratesRateId,
        PathValues.WORKERS_WORKER_ID_COMPENSATION_PAYSTANDARDS: WorkersWorkerIdCompensationPaystandards,
        PathValues.WORKERS_WORKER_ID_CONTACTS: WorkersWorkerIdContacts,
        PathValues.WORKERS_WORKER_ID_CONTACTS_CONTACT_ID: WorkersWorkerIdContactsContactId,
        PathValues.WORKERS_WORKER_ID_CUSTOMFIELDS: WorkersWorkerIdCustomfields,
        PathValues.WORKERS_WORKER_ID_CUSTOMFIELDS_WORKER_CUSTOM_FIELD_ID: WorkersWorkerIdCustomfieldsWorkerCustomFieldId,
        PathValues.WORKERS_WORKER_ID_DIRECTDEPOSITS: WorkersWorkerIdDirectdeposits,
        PathValues.WORKERS_WORKER_ID_DIRECTDEPOSITS_DIRECT_DEPOSIT_ID: WorkersWorkerIdDirectdepositsDirectDepositId,
        PathValues.WORKERS_WORKER_ID_FEDERALTAX: WorkersWorkerIdFederaltax,
        PathValues.WORKERS_WORKER_ID_PAYCOMPONENTS: WorkersWorkerIdPaycomponents,
        PathValues.WORKERS_WORKER_ID_PAYCOMPONENTS_WORKER_COMPONENT_ID: WorkersWorkerIdPaycomponentsWorkerComponentId,
        PathValues.WORKERS_WORKER_ID_STATUS: WorkersWorkerIdStatus,
        PathValues.WORKERS_WORKER_ID_TIMEOFF: WorkersWorkerIdTimeoff,
        PathValues.CHECKS: Checks,
        PathValues.CHECKS_CHECK_ID_CHECKCOMPONENTS: ChecksCheckIdCheckcomponents,
        PathValues.CHECKS_CHECK_ID_CHECKCOMPONENTS_CHECK_COMPONENT_ID: ChecksCheckIdCheckcomponentsCheckComponentId,
        PathValues.MANAGEMENT_DOMAINS: ManagementDomains,
        PathValues.MANAGEMENT_HOOKS: ManagementHooks,
        PathValues.MANAGEMENT_HOOKS_HOOK_ID: ManagementHooksHookId,
        PathValues.MANAGEMENT_REQUESTCLIENTACCESS: ManagementRequestclientaccess,
    }
)
