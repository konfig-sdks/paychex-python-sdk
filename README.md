<div align="left">

[![Visit Paychex](./header.png)](https://paychex.com)

# Paychex<a id="paychex"></a>



# Developer Resources<a id="developer-resources"></a>
 Refer
[Developer Resources](https://developer.paychex.com/resources/overview/) for more details on API specification 


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`paychex.authentication.create_bearer_token`](#paychexauthenticationcreate_bearer_token)
  * [`paychex.company.add_in_progress_workers`](#paychexcompanyadd_in_progress_workers)
  * [`paychex.company.add_job`](#paychexcompanyadd_job)
  * [`paychex.company.create_custom_field_at_company_level`](#paychexcompanycreate_custom_field_at_company_level)
  * [`paychex.company.create_custom_field_category`](#paychexcompanycreate_custom_field_category)
  * [`paychex.company.delete_custom_field`](#paychexcompanydelete_custom_field)
  * [`paychex.company.delete_custom_fields_category`](#paychexcompanydelete_custom_fields_category)
  * [`paychex.company.get_calculation_bases`](#paychexcompanyget_calculation_bases)
  * [`paychex.company.get_contact_types`](#paychexcompanyget_contact_types)
  * [`paychex.company.get_custom_field`](#paychexcompanyget_custom_field)
  * [`paychex.company.get_custom_field_categories`](#paychexcompanyget_custom_field_categories)
  * [`paychex.company.get_custom_fields`](#paychexcompanyget_custom_fields)
  * [`paychex.company.get_custom_fields_category`](#paychexcompanyget_custom_fields_category)
  * [`paychex.company.get_information`](#paychexcompanyget_information)
  * [`paychex.company.get_job_information`](#paychexcompanyget_job_information)
  * [`paychex.company.get_job_segment_structure_setup`](#paychexcompanyget_job_segment_structure_setup)
  * [`paychex.company.get_job_title`](#paychexcompanyget_job_title)
  * [`paychex.company.get_jobs`](#paychexcompanyget_jobs)
  * [`paychex.company.get_labor_assignment`](#paychexcompanyget_labor_assignment)
  * [`paychex.company.get_location`](#paychexcompanyget_location)
  * [`paychex.company.get_locations`](#paychexcompanyget_locations)
  * [`paychex.company.get_organization`](#paychexcompanyget_organization)
  * [`paychex.company.get_organizations`](#paychexcompanyget_organizations)
  * [`paychex.company.get_pay_frequencies`](#paychexcompanyget_pay_frequencies)
  * [`paychex.company.get_status`](#paychexcompanyget_status)
  * [`paychex.company.get_workers`](#paychexcompanyget_workers)
  * [`paychex.company.list`](#paychexcompanylist)
  * [`paychex.company.list_job_titles`](#paychexcompanylist_job_titles)
  * [`paychex.company.list_labor_assignments`](#paychexcompanylist_labor_assignments)
  * [`paychex.company.list_worker_statuses`](#paychexcompanylist_worker_statuses)
  * [`paychex.company.update_custom_field`](#paychexcompanyupdate_custom_field)
  * [`paychex.company.update_custom_fields_category`](#paychexcompanyupdate_custom_fields_category)
  * [`paychex.company.update_job`](#paychexcompanyupdate_job)
  * [`paychex.management.link_paychex_clients`](#paychexmanagementlink_paychex_clients)
  * [`paychex.payroll.add_company_checks`](#paychexpayrolladd_company_checks)
  * [`paychex.payroll.add_pay_component_to_check`](#paychexpayrolladd_pay_component_to_check)
  * [`paychex.payroll.add_worker_check`](#paychexpayrolladd_worker_check)
  * [`paychex.payroll.delete_checks_by_pay_period_and_user`](#paychexpayrolldelete_checks_by_pay_period_and_user)
  * [`paychex.payroll.get_company_checks_by_pay_period`](#paychexpayrollget_company_checks_by_pay_period)
  * [`paychex.payroll.get_company_pay_component`](#paychexpayrollget_company_pay_component)
  * [`paychex.payroll.get_company_pay_components`](#paychexpayrollget_company_pay_components)
  * [`paychex.payroll.get_company_pay_periods`](#paychexpayrollget_company_pay_periods)
  * [`paychex.payroll.get_pay_period`](#paychexpayrollget_pay_period)
  * [`paychex.payroll.get_worker_check`](#paychexpayrollget_worker_check)
  * [`paychex.payroll.get_worker_checks_by_pay_period`](#paychexpayrollget_worker_checks_by_pay_period)
  * [`paychex.payroll.remove_pay_component`](#paychexpayrollremove_pay_component)
  * [`paychex.payroll.remove_worker_check`](#paychexpayrollremove_worker_check)
  * [`paychex.payroll.update_pay_component`](#paychexpayrollupdate_pay_component)
  * [`paychex.webhooks.add_webhook`](#paychexwebhooksadd_webhook)
  * [`paychex.webhooks.delete_by_id`](#paychexwebhooksdelete_by_id)
  * [`paychex.webhooks.get_available_domains`](#paychexwebhooksget_available_domains)
  * [`paychex.webhooks.get_specific_hook_by_id`](#paychexwebhooksget_specific_hook_by_id)
  * [`paychex.webhooks.list`](#paychexwebhookslist)
  * [`paychex.worker.add_communication`](#paychexworkeradd_communication)
  * [`paychex.worker.add_direct_deposit`](#paychexworkeradd_direct_deposit)
  * [`paychex.worker.add_federal_tax_setup`](#paychexworkeradd_federal_tax_setup)
  * [`paychex.worker.add_pay_component`](#paychexworkeradd_pay_component)
  * [`paychex.worker.add_pay_rate`](#paychexworkeradd_pay_rate)
  * [`paychex.worker.add_worker_contacts`](#paychexworkeradd_worker_contacts)
  * [`paychex.worker.create_custom_field`](#paychexworkercreate_custom_field)
  * [`paychex.worker.delete_contact_by_contact_id`](#paychexworkerdelete_contact_by_contact_id)
  * [`paychex.worker.delete_custom_field`](#paychexworkerdelete_custom_field)
  * [`paychex.worker.delete_in_progress`](#paychexworkerdelete_in_progress)
  * [`paychex.worker.get_communication_item`](#paychexworkerget_communication_item)
  * [`paychex.worker.get_communications`](#paychexworkerget_communications)
  * [`paychex.worker.get_compensation_information`](#paychexworkerget_compensation_information)
  * [`paychex.worker.get_contact_by_contact_id`](#paychexworkerget_contact_by_contact_id)
  * [`paychex.worker.get_contacts`](#paychexworkerget_contacts)
  * [`paychex.worker.get_custom_field`](#paychexworkerget_custom_field)
  * [`paychex.worker.get_custom_fields`](#paychexworkerget_custom_fields)
  * [`paychex.worker.get_direct_deposit`](#paychexworkerget_direct_deposit)
  * [`paychex.worker.get_federal_tax_setup`](#paychexworkerget_federal_tax_setup)
  * [`paychex.worker.get_information`](#paychexworkerget_information)
  * [`paychex.worker.get_pay_component`](#paychexworkerget_pay_component)
  * [`paychex.worker.get_pay_components`](#paychexworkerget_pay_components)
  * [`paychex.worker.get_pay_rate`](#paychexworkerget_pay_rate)
  * [`paychex.worker.get_pay_rates_by_worker_id`](#paychexworkerget_pay_rates_by_worker_id)
  * [`paychex.worker.get_pay_standards`](#paychexworkerget_pay_standards)
  * [`paychex.worker.get_time_off_balance`](#paychexworkerget_time_off_balance)
  * [`paychex.worker.get_worker_status_list`](#paychexworkerget_worker_status_list)
  * [`paychex.worker.list_assignment_distributions`](#paychexworkerlist_assignment_distributions)
  * [`paychex.worker.list_direct_deposits`](#paychexworkerlist_direct_deposits)
  * [`paychex.worker.remove_communication`](#paychexworkerremove_communication)
  * [`paychex.worker.remove_direct_deposit`](#paychexworkerremove_direct_deposit)
  * [`paychex.worker.remove_federal_tax`](#paychexworkerremove_federal_tax)
  * [`paychex.worker.remove_pay_component`](#paychexworkerremove_pay_component)
  * [`paychex.worker.remove_pay_rate`](#paychexworkerremove_pay_rate)
  * [`paychex.worker.update_communication_item`](#paychexworkerupdate_communication_item)
  * [`paychex.worker.update_compensation_rate`](#paychexworkerupdate_compensation_rate)
  * [`paychex.worker.update_contact`](#paychexworkerupdate_contact)
  * [`paychex.worker.update_custom_field`](#paychexworkerupdate_custom_field)
  * [`paychex.worker.update_direct_deposit`](#paychexworkerupdate_direct_deposit)
  * [`paychex.worker.update_direct_deposits`](#paychexworkerupdate_direct_deposits)
  * [`paychex.worker.update_federal_tax_setup`](#paychexworkerupdate_federal_tax_setup)
  * [`paychex.worker.update_pay_component`](#paychexworkerupdate_pay_component)
  * [`paychex.worker.update_pay_components`](#paychexworkerupdate_pay_components)
  * [`paychex.worker.update_unique_worker`](#paychexworkerupdate_unique_worker)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Paychex&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from paychex_python_sdk import Paychex, ApiException

paychex = Paychex(
)

try:
    # Create Bearer token
    create_bearer_token_response = paychex.authentication.create_bearer_token(
        grant_type="string_example",
        client_id="string_example",
        client_secret="string_example",
    )
    print(create_bearer_token_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi.create_bearer_token: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from paychex_python_sdk import Paychex, ApiException

paychex = Paychex(
)

async def main():
    try:
        # Create Bearer token
        create_bearer_token_response = await paychex.authentication.acreate_bearer_token(
            grant_type="string_example",
            client_id="string_example",
            client_secret="string_example",
        )
        print(create_bearer_token_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi.create_bearer_token: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from paychex_python_sdk import Paychex, ApiException

paychex = Paychex(
)

try:
    # Create Bearer token
    create_bearer_token_response = paychex.authentication.raw.create_bearer_token(
        grant_type="string_example",
        client_id="string_example",
        client_secret="string_example",
    )
    pprint(create_bearer_token_response.body)
    pprint(create_bearer_token_response.body["access_token"])
    pprint(create_bearer_token_response.body["expires_in"])
    pprint(create_bearer_token_response.body["scope"])
    pprint(create_bearer_token_response.body["token_type"])
    pprint(create_bearer_token_response.headers)
    pprint(create_bearer_token_response.status)
    pprint(create_bearer_token_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AuthenticationApi.create_bearer_token: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `paychex.authentication.create_bearer_token`<a id="paychexauthenticationcreate_bearer_token"></a>

Request a Bearer token that will be used as an access token when making calls to resources.  The credentials need to be sent within the body of the request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_bearer_token_response = paychex.authentication.create_bearer_token(
    grant_type="string_example",
    client_id="string_example",
    client_secret="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### grant_type: `str`<a id="grant_type-str"></a>

Send \\\"client_credentials\\\".

##### client_id: `str`<a id="client_id-str"></a>

The applications API key.

##### client_secret: `str`<a id="client_secret-str"></a>

The applications corresponding secret.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AuthenticationCreateBearerTokenRequest`](./paychex_python_sdk/type/authentication_create_bearer_token_request.py)
user info to be filled

#### 🔄 Return<a id="🔄-return"></a>

[`Authentication`](./paychex_python_sdk/pydantic/authentication.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/auth/oauth/v2/token` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.add_in_progress_workers`<a id="paychexcompanyadd_in_progress_workers"></a>

Add one or more workers to a specific company that your application has been granted access to. These workers will be added with an IN_PROGRESS status assigned to them.  In_Progress workers will pre-populated within Paychex Flex and will require someone to complete them to be fully available with the Flex platform.  Paychex Flex UI will hold a majority of validation, rules, and enforced required fields based on the clients configuration.  Required fields are givenName, familyName, & workerType (when adding multiple workers at a time you will need to also include a "workerCorrelationId" data element on each worker, that will be used as an identifier in our responses). Optionally you can include a workers communications object within the worker.  Once generated the IN_PROGRESS worker can have their communications, Compensation and Federal Taxes POSTed and PATCHed using the generated workerId.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_in_progress_workers_response = paychex.company.add_in_progress_workers(
    company_id="companyId_example",
    worker_id="00Z5V9BTIHRQF2CF7BTH",
    employee_id="3052",
    worker_type="EMPLOYEE",
    employment_type="NON_EXEMPT",
    exemption_type="EXEMPT",
    birth_date="1970-01-01T00:00:00.00Z",
    sex="MALE",
    ethnicity_code="(blank)",
    hire_date="2015-06-15T00:00:00Z",
    clock_id="4321",
    name={
        "family_name": "JONES",
        "middle_name": "H",
        "given_name": "INDIANA",
        "preferred_name": "Indi",
        "qualification_affix_code": "Jr",
        "title_affix_code": "Dr.",
    },
    legal_id={
        "legal_id_type": "SSN",
        "legal_id_value": "995886885",
    },
    labor_assignment_id="970001557863345",
    job_id="970001557916904",
    location_id="970001701620675",
    job={
        "title": "Archaeologist",
        "job_title_id": "00DWS906IMW2JSH8AQJ8",
        "start_date": "2010-01-01T00:00:00Z",
        "end_date": "2016-12-31T00:00:00Z",
    },
    organization={
        "organization_id": "970000055981384",
        "name": "2 Division B",
        "number": "2",
        "level": "Level 2",
    },
    supervisor={
        "worker_id": "00H2A1IUJ4IPERJ589YE",
    },
    current_status={
        "worker_status_id": "00DWS906IMW2JSH8AQJ9",
        "status_type": "ACTIVE",
        "status_reason": "HIRED",
    },
    communications=[
        {
            "communication_id": "00Z5V9BTINBT97UMERCA",
            "type": "STREET_ADDRESS",
            "usage_type": "BUSINESS",
            "street_line_one": "Mike St",
            "street_line_two": "Sulley Ln",
            "city": "ANAHEIM",
            "postal_code": "92802",
            "country_subdivision_code": "CA",
            "country_code": "US",
        }
    ],
    worker_correlation_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The id assigned to the company that workers are being requested for.

##### worker_id: `str`<a id="worker_id-str"></a>

The unique identifier associated with this worker representation.

##### employee_id: `str`<a id="employee_id-str"></a>

The workers employee identification information.

##### worker_type: `str`<a id="worker_type-str"></a>

The type of worker. This data field cannot be PATCHED.

##### employment_type: `str`<a id="employment_type-str"></a>

The type of employment for the worker.

##### exemption_type: `str`<a id="exemption_type-str"></a>

The Overtime classification of the worker.This data field cannot be PATCHED for ACTIVE workers.

##### birth_date: `datetime`<a id="birth_date-datetime"></a>

The workers date of birth. It cannot be greater than today's date.

##### sex: `str`<a id="sex-str"></a>

##### ethnicity_code: `str`<a id="ethnicity_code-str"></a>

Disclaimer:This parameter is not visible in Flex for the client. This data field cannot be PATCHED for ACTIVE workers.

##### hire_date: `datetime`<a id="hire_date-datetime"></a>

The date which the worker was hired. It cannot be PATCHED for ACTIVE workers.

##### clock_id: `str`<a id="clock_id-str"></a>

The clock ID of the worker that can be an identification for other systems.

##### name: [`NameResource`](./paychex_python_sdk/type/name_resource.py)<a id="name-nameresourcepaychex_python_sdktypename_resourcepy"></a>


##### legal_id: [`LegalIdResource`](./paychex_python_sdk/type/legal_id_resource.py)<a id="legal_id-legalidresourcepaychex_python_sdktypelegal_id_resourcepy"></a>


##### labor_assignment_id: `str`<a id="labor_assignment_id-str"></a>

The workers home labor assignment. This data field cannot be POSTED or PATCHED

##### job_id: `str`<a id="job_id-str"></a>

The workers home job. This data field cannot be POSTED or PATCHED.

##### location_id: `str`<a id="location_id-str"></a>

The workers location. This data field cannot be POSTED or PATCHED.

##### job: [`JobTitleResource`](./paychex_python_sdk/type/job_title_resource.py)<a id="job-jobtitleresourcepaychex_python_sdktypejob_title_resourcepy"></a>


##### organization: [`OrganizationResource`](./paychex_python_sdk/type/organization_resource.py)<a id="organization-organizationresourcepaychex_python_sdktypeorganization_resourcepy"></a>


##### supervisor: [`SupervisorResource`](./paychex_python_sdk/type/supervisor_resource.py)<a id="supervisor-supervisorresourcepaychex_python_sdktypesupervisor_resourcepy"></a>


##### current_status: [`Status`](./paychex_python_sdk/type/status.py)<a id="current_status-statuspaychex_python_sdktypestatuspy"></a>


##### communications: List[`CommunicationResource`]<a id="communications-listcommunicationresource"></a>

Worker Communications. This data field cannot be updated for worker endpoint.

##### worker_correlation_id: `str`<a id="worker_correlation_id-str"></a>

Id that you define which is used for error handling/responses.This data field is used while POSTING multiple IN_PROGRESS workers

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WorkerResource`](./paychex_python_sdk/type/worker_resource.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WorkerResource`](./paychex_python_sdk/pydantic/worker_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/workers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.add_job`<a id="paychexcompanyadd_job"></a>

Add a company level job. If a client has their job numbering structured in 2-3 separate 'segments', you may need to first do a GET on the jobsegements endpoint, so you can see how many segments and the character length of each segment, as well as the name of those segments, which you will need to have before you POST.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_job_response = paychex.company.add_job(
    company_id="companyId_example",
    job_id="970001557916902",
    job_correlation_id="string_example",
    job_name="My job A",
    start_date="2018-12-20T00:00:00Z",
    end_date="2025-12-20T00:00:00Z",
    links=[
        {
        }
    ],
    job_number={
        "segment1": "A1",
        "segment2": "A2",
        "segment3": "A3",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The ID of the company.

##### job_id: `str`<a id="job_id-str"></a>

The unique identifier associated with this job.

##### job_correlation_id: `str`<a id="job_correlation_id-str"></a>

Id that you define which is used for error handling/responses.

##### job_name: `str`<a id="job_name-str"></a>

The name of the job.

##### start_date: `datetime`<a id="start_date-datetime"></a>

The start date associated with this job.

##### end_date: `datetime`<a id="end_date-datetime"></a>

The end date associated with this job.

##### links: List[`Link`]<a id="links-listlink"></a>

##### job_number: [`JobSegmentsResource`](./paychex_python_sdk/type/job_segments_resource.py)<a id="job_number-jobsegmentsresourcepaychex_python_sdktypejob_segments_resourcepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`JobResource`](./paychex_python_sdk/type/job_resource.py)
#### 🔄 Return<a id="🔄-return"></a>

[`JobResource`](./paychex_python_sdk/pydantic/job_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/jobs` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.create_custom_field_at_company_level`<a id="paychexcompanycreate_custom_field_at_company_level"></a>

Create CustomFields at the company level which a company could be assigned.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_custom_field_at_company_level_response = paychex.company.create_custom_field_at_company_level(
    company_id="companyId_example",
    custom_field_id="1040014203417589",
    custom_field_name="Hobbies",
    category_id="1040014179116276",
    required=False,
    check_stub=False,
    employee_editable=False,
    type="DROPDOWN",
    boolean_value=True,
    links=[
        {
        }
    ],
    date_value="1970-01-01T00:00:00.00Z",
    text_value="string_example",
    max_text_length=3.14,
    numeric_value=3.14,
    dropdown=[
        {
            "dropdown_id": "1040014203453303",
            "dropdown_value": "Basketball",
            "dropdown_default": True,
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

ID associated with desired company.

##### custom_field_id: `str`<a id="custom_field_id-str"></a>

The unique identifier that is autogenerated when a custom field is created

##### custom_field_name: `str`<a id="custom_field_name-str"></a>

The name of the custom field

##### category_id: `str`<a id="category_id-str"></a>

The unique identifier that is autogenerated when creating a category

##### required: `bool`<a id="required-bool"></a>

Where to indicate if the custom field is required on the worker where true = required and false = not required

##### check_stub: `bool`<a id="check_stub-bool"></a>

Where to indicate if the custom field is required on the worker's pay stub, where true = required and false = not required

##### employee_editable: `bool`<a id="employee_editable-bool"></a>

Where to indicate if the custom field is able to be edited by the employee, where true = required and false = not required

##### type: `str`<a id="type-str"></a>

The type of field the custom field is.

##### boolean_value: `bool`<a id="boolean_value-bool"></a>

The value for BOOLEAN type (true / false)

##### links: List[`Link`]<a id="links-listlink"></a>

##### date_value: `datetime`<a id="date_value-datetime"></a>

The value for DATE type , example : 2012-02-01T05:00:00Z

##### text_value: `str`<a id="text_value-str"></a>

The value for TEXT type (any text, alphanumeric, special characters allowed)

##### max_text_length: `Union[int, float]`<a id="max_text_length-unionint-float"></a>

The maximum allowed value for textValue

##### numeric_value: `Union[int, float]`<a id="numeric_value-unionint-float"></a>

Numeric data type can have three formats namely - whole number, second decimal place and fourth decimal place, example: 12 , 12.34 or 12.3456

##### dropdown: List[`CustomFieldsDropdownResource`]<a id="dropdown-listcustomfieldsdropdownresource"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CustomFieldsResource`](./paychex_python_sdk/type/custom_fields_resource.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsResource`](./paychex_python_sdk/pydantic/custom_fields_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/customfields` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.create_custom_field_category`<a id="paychexcompanycreate_custom_field_category"></a>

Create CustomFieldsCategory at the company level which a company could be assigned.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_custom_field_category_response = paychex.company.create_custom_field_category(
    company_id="companyId_example",
    category_id="970003868555304",
    category_name="Social",
    links=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

ID associated with desired company.

##### category_id: `str`<a id="category_id-str"></a>

The unique identifier that is autogenerated when creating a category

##### category_name: `str`<a id="category_name-str"></a>

The name of the Category

##### links: List[`Link`]<a id="links-listlink"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CustomFieldsCategoryResource`](./paychex_python_sdk/type/custom_fields_category_resource.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsCategoryResource`](./paychex_python_sdk/pydantic/custom_fields_category_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/customfieldscategories` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.delete_custom_field`<a id="paychexcompanydelete_custom_field"></a>

Delete CustomField at the company level.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paychex.company.delete_custom_field(
    company_id="companyId_example",
    customfieldid="customfieldid_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

ID associated with desired company.

##### customfieldid: `str`<a id="customfieldid-str"></a>

ID associated with desired custom field.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/customfields/{customfieldid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.delete_custom_fields_category`<a id="paychexcompanydelete_custom_fields_category"></a>

Delete CustomFieldsCategory at the company level.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paychex.company.delete_custom_fields_category(
    company_id="companyId_example",
    categoryid="categoryid_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

ID associated with desired company.

##### categoryid: `str`<a id="categoryid-str"></a>

ID associated with desired category.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/customfieldscategories/{categoryid}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.get_calculation_bases`<a id="paychexcompanyget_calculation_bases"></a>

Array of calculation bases that are used with a worker pay components that are not FLAT_DOLLAR_AMOUNT allow you to determine what to apply the calculation against when determining the amount during the pay run.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_calculation_bases_response = paychex.company.get_calculation_bases(
    company_id="companyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The ID of the company.

#### 🔄 Return<a id="🔄-return"></a>

[`CalculationBase`](./paychex_python_sdk/pydantic/calculation_base.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/calculationbases` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.get_contact_types`<a id="paychexcompanyget_contact_types"></a>

Information about contact types that your application has been granted access to.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_contact_types_response = paychex.company.get_contact_types(
    company_id="companyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

ID associated with desired company.

#### 🔄 Return<a id="🔄-return"></a>

[`ContactTypeResource`](./paychex_python_sdk/pydantic/contact_type_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/contacttypes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.get_custom_field`<a id="paychexcompanyget_custom_field"></a>

Information about a single CustomField.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_custom_field_response = paychex.company.get_custom_field(
    company_id="companyId_example",
    custom_field_id="customFieldId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

ID associated with desired company.

##### custom_field_id: `str`<a id="custom_field_id-str"></a>

ID associated with desired custom field.

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsResource`](./paychex_python_sdk/pydantic/custom_fields_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/customfields/{customFieldId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.get_custom_field_categories`<a id="paychexcompanyget_custom_field_categories"></a>

Array of CustomFieldsCategories Configured at the company level 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_custom_field_categories_response = paychex.company.get_custom_field_categories(
    company_id="companyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

ID associated with desired company.

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsCategoryResource`](./paychex_python_sdk/pydantic/custom_fields_category_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/customfieldscategories` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.get_custom_fields`<a id="paychexcompanyget_custom_fields"></a>

Array of customFields Configured at the company level 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_custom_fields_response = paychex.company.get_custom_fields(
    company_id="companyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

ID associated with desired company.

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsResource`](./paychex_python_sdk/pydantic/custom_fields_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/customfields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.get_custom_fields_category`<a id="paychexcompanyget_custom_fields_category"></a>

Information about a single CustomFieldsCategory.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_custom_fields_category_response = paychex.company.get_custom_fields_category(
    company_id="companyId_example",
    category_id="categoryId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

ID associated with desired company.

##### category_id: `str`<a id="category_id-str"></a>

ID associated with desired category.

#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsCategoryResource`](./paychex_python_sdk/pydantic/custom_fields_category_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/customfieldscategories/{categoryId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.get_information`<a id="paychexcompanyget_information"></a>

Information about a single company that your application has access to.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_information_response = paychex.company.get_information(
    company_id="companyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The ID of the company.

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyResource`](./paychex_python_sdk/pydantic/company_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.get_job_information`<a id="paychexcompanyget_job_information"></a>

Information about a single Job.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_job_information_response = paychex.company.get_job_information(
    company_id="companyId_example",
    job_id="jobId_example",
    asof="2020-01-04T00:00:00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The ID of the company.

##### job_id: `str`<a id="job_id-str"></a>

The ID of the job.

##### asof: `str`<a id="asof-str"></a>

Returns job as of the date used in the request.

#### 🔄 Return<a id="🔄-return"></a>

[`JobResource`](./paychex_python_sdk/pydantic/job_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/jobs/{jobId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.get_job_segment_structure_setup`<a id="paychexcompanyget_job_segment_structure_setup"></a>

Retrieve job segment structure setup for this client. This endpoint is only available if the client has their job numbering set up in '2-3 separate 'segments'.  The response will give you back the exact character lengths and the segment names so you are able to POST.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_job_segment_structure_setup_response = paychex.company.get_job_segment_structure_setup(
    company_id="companyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The ID of the company.

#### 🔄 Return<a id="🔄-return"></a>

[`JobSegmentsConfigResource`](./paychex_python_sdk/pydantic/job_segments_config_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/jobsegments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.get_job_title`<a id="paychexcompanyget_job_title"></a>

Information about a single Job Title.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_job_title_response = paychex.company.get_job_title(
    company_id="companyId_example",
    worker_job_title_id="workerJobTitleId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The ID of the company.

##### worker_job_title_id: `str`<a id="worker_job_title_id-str"></a>

The ID of the worker job title.

#### 🔄 Return<a id="🔄-return"></a>

[`JobTitleResource`](./paychex_python_sdk/pydantic/job_title_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/jobtitles/{jobTitleId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.get_jobs`<a id="paychexcompanyget_jobs"></a>

Array of jobs set at the company level.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_jobs_response = paychex.company.get_jobs(
    company_id="companyId_example",
    asof="2020-01-04T00:00:00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The ID of the company.

##### asof: `str`<a id="asof-str"></a>

Returns all jobs as of the date used in the request.

#### 🔄 Return<a id="🔄-return"></a>

[`JobResource`](./paychex_python_sdk/pydantic/job_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/jobs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.get_labor_assignment`<a id="paychexcompanyget_labor_assignment"></a>

Information about a single Labor Assignment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_labor_assignment_response = paychex.company.get_labor_assignment(
    company_id="companyId_example",
    labor_assignment_id="laborAssignmentId_example",
    asof="2020-01-04T00:00:00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The ID of the company.

##### labor_assignment_id: `str`<a id="labor_assignment_id-str"></a>

The ID of the labor assignment.

##### asof: `str`<a id="asof-str"></a>

Returns labour assignment as of the date used in the request.

#### 🔄 Return<a id="🔄-return"></a>

[`LaborAssignmentResource`](./paychex_python_sdk/pydantic/labor_assignment_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/laborassignments/{laborAssignmentId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.get_location`<a id="paychexcompanyget_location"></a>

Information about a single Location.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_location_response = paychex.company.get_location(
    company_id="companyId_example",
    location_id="locationId_example",
    asof="2020-01-04T00:00:00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

ID associated with desired company.

##### location_id: `str`<a id="location_id-str"></a>

The ID of the location.

##### asof: `str`<a id="asof-str"></a>

Returns location as of the date used in the request.

#### 🔄 Return<a id="🔄-return"></a>

[`LocationResource`](./paychex_python_sdk/pydantic/location_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/locations/{locationId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.get_locations`<a id="paychexcompanyget_locations"></a>

Array of locations set at the company level.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_locations_response = paychex.company.get_locations(
    company_id="companyId_example",
    asof="2020-01-04T00:00:00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The ID of the company.

##### asof: `str`<a id="asof-str"></a>

Returns all locations as of the date used in the request.

#### 🔄 Return<a id="🔄-return"></a>

[`LocationResource`](./paychex_python_sdk/pydantic/location_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/locations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.get_organization`<a id="paychexcompanyget_organization"></a>

Information about a single Organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_organization_response = paychex.company.get_organization(
    company_id="companyId_example",
    organization_id="organizationId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The ID of the company.

##### organization_id: `str`<a id="organization_id-str"></a>

The ID of the organization.

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationResource`](./paychex_python_sdk/pydantic/organization_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/organizations/{orgId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.get_organizations`<a id="paychexcompanyget_organizations"></a>

Array of organizations set at the company level.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_organizations_response = paychex.company.get_organizations(
    company_id="companyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The ID of the company.

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationResource`](./paychex_python_sdk/pydantic/organization_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/organizations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.get_pay_frequencies`<a id="paychexcompanyget_pay_frequencies"></a>

Array of pay frequencies that workers maybe paid on. This is a generic array that is currently not specific to the companies pay frequency. This is to be used with the workers pay components to determine what the frequency, occurrence, and intervals are allowed.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_pay_frequencies_response = paychex.company.get_pay_frequencies(
    company_id="companyId_example",
    payfrequency="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The ID of the company.

##### payfrequency: `str`<a id="payfrequency-str"></a>

The frequency that you would like to search for.

#### 🔄 Return<a id="🔄-return"></a>

[`FrequencyCombinationUnitResource`](./paychex_python_sdk/pydantic/frequency_combination_unit_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/payfrequencies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.get_status`<a id="paychexcompanyget_status"></a>

Information about a single status.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_status_response = paychex.company.get_status(
    company_id="companyId_example",
    worker_status_id="workerStatusId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The ID of the company.

##### worker_status_id: `str`<a id="worker_status_id-str"></a>

The ID of the worker status.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkerStatus`](./paychex_python_sdk/pydantic/worker_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/workerstatuses/{statusId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.get_workers`<a id="paychexcompanyget_workers"></a>

Array of workers (employee and contractor) for all of the companies who are associated with a specific company that your application has been granted access to. The combination of query parameters to be used with this endpoint are as follows:  1. givenname, familyname, legallastfour  2. from, to (start date, end date)  3. employeeid  4. locationid  5. offset, limit (paging).  Note: Paging and filtering attributes cannot be applied together. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_workers_response = paychex.company.get_workers(
    company_id="companyId_example",
    givenname="string_example",
    familyname="string_example",
    legallastfour="string_example",
    employeeid="string_example",
    _from="string_example",
    to="string_example",
    locationid="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The id assigned to the company that workers are being requested for.

##### givenname: `str`<a id="givenname-str"></a>

The given or first name of the workers to search for.

##### familyname: `str`<a id="familyname-str"></a>

The family or last name of the workers to search for.

##### legallastfour: `str`<a id="legallastfour-str"></a>

The last 4 digits of the workers federal level taxpayer id number of the worker to search for.

##### employeeid: `str`<a id="employeeid-str"></a>

The assigned workers employee ID.

##### _from: `str`<a id="_from-str"></a>

The beginning of the search date range using for when the worker was created.

##### to: `str`<a id="to-str"></a>

The ending of the search date range using for then the worker was created.

##### locationid: `str`<a id="locationid-str"></a>

The location Id.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkerResource`](./paychex_python_sdk/pydantic/worker_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/workers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.list`<a id="paychexcompanylist"></a>

Array of companies that your application has been granted with some level of access. Your Application (API Key) can be granted access to one or more companies (clients) accounts that are associated with one or more product lines within Paychex.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = paychex.company.list(
    displayid="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### displayid: `str`<a id="displayid-str"></a>

The client account number used for identification purposes. (no dash or spaces allowed, only the last 8 characters  of the ID)

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyResource`](./paychex_python_sdk/pydantic/company_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.list_job_titles`<a id="paychexcompanylist_job_titles"></a>

Array of job titles set at the company level which a worker could be assigned.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_job_titles_response = paychex.company.list_job_titles(
    company_id="companyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The ID of the company.

#### 🔄 Return<a id="🔄-return"></a>

[`JobTitleResource`](./paychex_python_sdk/pydantic/job_title_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/jobtitles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.list_labor_assignments`<a id="paychexcompanylist_labor_assignments"></a>

Array of labor assignments set at the company level.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_labor_assignments_response = paychex.company.list_labor_assignments(
    company_id="companyId_example",
    asof="2020-01-04T00:00:00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The ID of the company.

##### asof: `str`<a id="asof-str"></a>

Returns all labour assignments as of the date used in the request.

#### 🔄 Return<a id="🔄-return"></a>

[`LaborAssignmentResource`](./paychex_python_sdk/pydantic/labor_assignment_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/laborassignments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.list_worker_statuses`<a id="paychexcompanylist_worker_statuses"></a>

Array of statuses set at the company level which a worker could be assigned.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_worker_statuses_response = paychex.company.list_worker_statuses(
    company_id="companyId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The ID of the company.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkerStatus`](./paychex_python_sdk/pydantic/worker_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/workerstatuses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.update_custom_field`<a id="paychexcompanyupdate_custom_field"></a>

Update CustomFields at the company level which a company could be assigned.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_custom_field_response = paychex.company.update_custom_field(
    company_id="companyId_example",
    customfieldid="customfieldid_example",
    custom_field_id="1040014203417589",
    custom_field_name="Hobbies",
    category_id="1040014179116276",
    required=False,
    check_stub=False,
    employee_editable=False,
    type="DROPDOWN",
    boolean_value=True,
    links=[
        {
        }
    ],
    date_value="1970-01-01T00:00:00.00Z",
    text_value="string_example",
    max_text_length=3.14,
    numeric_value=3.14,
    dropdown=[
        {
            "dropdown_id": "1040014203453303",
            "dropdown_value": "Basketball",
            "dropdown_default": True,
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

ID associated with desired company.

##### customfieldid: `str`<a id="customfieldid-str"></a>

ID associated with desired custom field.

##### custom_field_id: `str`<a id="custom_field_id-str"></a>

The unique identifier that is autogenerated when a custom field is created

##### custom_field_name: `str`<a id="custom_field_name-str"></a>

The name of the custom field

##### category_id: `str`<a id="category_id-str"></a>

The unique identifier that is autogenerated when creating a category

##### required: `bool`<a id="required-bool"></a>

Where to indicate if the custom field is required on the worker where true = required and false = not required

##### check_stub: `bool`<a id="check_stub-bool"></a>

Where to indicate if the custom field is required on the worker's pay stub, where true = required and false = not required

##### employee_editable: `bool`<a id="employee_editable-bool"></a>

Where to indicate if the custom field is able to be edited by the employee, where true = required and false = not required

##### type: `str`<a id="type-str"></a>

The type of field the custom field is.

##### boolean_value: `bool`<a id="boolean_value-bool"></a>

The value for BOOLEAN type (true / false)

##### links: List[`Link`]<a id="links-listlink"></a>

##### date_value: `datetime`<a id="date_value-datetime"></a>

The value for DATE type , example : 2012-02-01T05:00:00Z

##### text_value: `str`<a id="text_value-str"></a>

The value for TEXT type (any text, alphanumeric, special characters allowed)

##### max_text_length: `Union[int, float]`<a id="max_text_length-unionint-float"></a>

The maximum allowed value for textValue

##### numeric_value: `Union[int, float]`<a id="numeric_value-unionint-float"></a>

Numeric data type can have three formats namely - whole number, second decimal place and fourth decimal place, example: 12 , 12.34 or 12.3456

##### dropdown: List[`CustomFieldsDropdownResource`]<a id="dropdown-listcustomfieldsdropdownresource"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CustomFieldsResource`](./paychex_python_sdk/type/custom_fields_resource.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsResource`](./paychex_python_sdk/pydantic/custom_fields_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/customfields/{customfieldid}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.update_custom_fields_category`<a id="paychexcompanyupdate_custom_fields_category"></a>

Update  CustomFieldsCategory at the company level.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_custom_fields_category_response = paychex.company.update_custom_fields_category(
    company_id="companyId_example",
    categoryid="categoryid_example",
    category_id="970003868555304",
    category_name="Social",
    links=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

ID associated with desired company.

##### categoryid: `str`<a id="categoryid-str"></a>

ID associated with desired custom field.

##### category_id: `str`<a id="category_id-str"></a>

The unique identifier that is autogenerated when creating a category

##### category_name: `str`<a id="category_name-str"></a>

The name of the Category

##### links: List[`Link`]<a id="links-listlink"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CustomFieldsCategoryResource`](./paychex_python_sdk/type/custom_fields_category_resource.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CustomFieldsCategoryResource`](./paychex_python_sdk/pydantic/custom_fields_category_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/customfieldscategories/{categoryid}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.company.update_job`<a id="paychexcompanyupdate_job"></a>

Update a single Job.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_job_response = paychex.company.update_job(
    company_id="companyId_example",
    job_id="jobId_example",
    job_id="970001557916902",
    job_correlation_id="string_example",
    job_name="My job A",
    start_date="2018-12-20T00:00:00Z",
    end_date="2025-12-20T00:00:00Z",
    links=[
        {
        }
    ],
    job_number={
        "segment1": "A1",
        "segment2": "A2",
        "segment3": "A3",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The ID of the company.

##### job_id: `str`<a id="job_id-str"></a>

The ID of the job.

##### requestBody: [`JobResource`](./paychex_python_sdk/type/job_resource.py)<a id="requestbody-jobresourcepaychex_python_sdktypejob_resourcepy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`JobResource`](./paychex_python_sdk/pydantic/job_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/jobs/{jobId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.management.link_paychex_clients`<a id="paychexmanagementlink_paychex_clients"></a>

(For partnerships only) Link Paychex clients to a 3rd party partner application

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
link_paychex_clients_response = paychex.management.link_paychex_clients(
    display_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### display_id: `str`<a id="display_id-str"></a>

The client account number used for identification purposes. (no dash or spaces allowed, only the last 8 characters of the ID)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PartnerLinkRequestResource`](./paychex_python_sdk/type/partner_link_request_resource.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DeepUrlResponseResource`](./paychex_python_sdk/pydantic/deep_url_response_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/management/requestclientaccess` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.payroll.add_company_checks`<a id="paychexpayrolladd_company_checks"></a>

Add a check for one or more worker within a company for an available pay period.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_company_checks_response = paychex.payroll.add_company_checks(
    company_id="companyId_example",
    worker_id="004UWBZQJ7GEB9TVWFR9",
    paycheck_id="1020026552555444",
    pay_period_id="1020026427391732",
    check_correlation_id="string_example",
    block_auto_distribution=False,
    earnings=[
        {
            "description": "Use for regular pay.",
            "component_id": "970000076689381",
            "code": "1",
            "name": "Hourly",
            "classification_type": "Regular",
            "effect_on_pay": "ADDITION",
            "start_date": "2016-01-01T00:00:00Z",
            "pay_rate": "7.25",
            "pay_hours": "4",
            "memoed": False,
        }
    ],
    deductions=[
        {
            "description": "Use for regular pay.",
            "component_id": "970000076689381",
            "code": "1",
            "name": "Hourly",
            "classification_type": "Regular",
            "effect_on_pay": "ADDITION",
            "start_date": "2016-01-01T00:00:00Z",
            "pay_rate": "7.25",
            "pay_hours": "4",
            "memoed": False,
        }
    ],
    check_date="2019-05-12T20:00:00Z",
    informational=[
        {
            "description": "Use for regular pay.",
            "component_id": "970000076689381",
            "code": "1",
            "name": "Hourly",
            "classification_type": "Regular",
            "effect_on_pay": "ADDITION",
            "start_date": "2016-01-01T00:00:00Z",
            "pay_rate": "7.25",
            "pay_hours": "4",
            "memoed": False,
        }
    ],
    taxes=[
        {
            "description": "Use for regular pay.",
            "component_id": "970000076689381",
            "code": "1",
            "name": "Hourly",
            "classification_type": "Regular",
            "effect_on_pay": "ADDITION",
            "start_date": "2016-01-01T00:00:00Z",
            "pay_rate": "7.25",
            "pay_hours": "4",
            "memoed": False,
        }
    ],
    links=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

ID associated with desired company.

##### worker_id: `str`<a id="worker_id-str"></a>

The id assigned to the worker.

##### paycheck_id: `str`<a id="paycheck_id-str"></a>

The id of a single check that a workers has.

##### pay_period_id: `str`<a id="pay_period_id-str"></a>

The id for the unprocessed payperiod. 

##### check_correlation_id: `str`<a id="check_correlation_id-str"></a>

Id that you define which is used for error handling/responses. This is not required when sending a single check.

##### block_auto_distribution: `bool`<a id="block_auto_distribution-bool"></a>

This is used optionally for blocking the auto distribution of the earnings on the workers if they are setup for auto distribution.

##### earnings: List[`PayComponentResource`]<a id="earnings-listpaycomponentresource"></a>

The earnings to apply to the check.Each earning needs to define as one of the following:1 .payHours: Will use the default hourly rate defined on the worker to apply the hours against. 2. payHours and payRate: Will allow you to define the monetary rate that the hours will be applied against. 3. payHours and payRateId: Will allow you to define which workers predefined pay rate the hours will be applied against. 4. payUnits: Will use the default hourly rate defined on the worker to apply the units against. 5. payUnits and payRate: Will allow you to define the monetary rate that the units will be applied against. 6. payUnits and payRateId: Will allow you to define which workers predefined pay rate the units will be applied against. 7. payAmount: Will allow you to define straight monetary amount.

##### deductions: List[`PayComponentResource`]<a id="deductions-listpaycomponentresource"></a>

Deduction pay components on the check.

##### check_date: `str`<a id="check_date-str"></a>

The check date 

##### informational: List[`PayComponentResource`]<a id="informational-listpaycomponentresource"></a>

Informational pay components on the check.

##### taxes: List[`PayComponentResource`]<a id="taxes-listpaycomponentresource"></a>

Tax pay components on the check.

##### links: List[`Link`]<a id="links-listlink"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CheckResource`](./paychex_python_sdk/type/check_resource.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CheckResource`](./paychex_python_sdk/pydantic/check_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/checks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.payroll.add_pay_component_to_check`<a id="paychexpayrolladd_pay_component_to_check"></a>

Add a new pay component on an individual unprocessed check.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_pay_component_to_check_response = paychex.payroll.add_pay_component_to_check(
    check_id="checkId_example",
    description="string_example",
    component_id="970000053577899",
    check_component_id="1020026552555441",
    name="string_example",
    classification_type="string_example",
    effect_on_pay="ADDITION",
    start_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
    applies_to_worker_types=[
        "string_example"
    ],
    job_id="string_example",
    labor_assignment_id="string_example",
    pay_rate_id="string_example",
    pay_rate="string_example",
    pay_hours="string_example",
    pay_units="string_example",
    pay_amount="string_example",
    memoed=True,
    line_date="1970-01-01T00:00:00.00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### check_id: `str`<a id="check_id-str"></a>

ID associated with desired check.

##### description: `str`<a id="description-str"></a>

Description

##### component_id: `str`<a id="component_id-str"></a>

The identifier of the pay component to add to the check. An overtime pay component can't be placed on a worker that is OT exempt.

##### check_component_id: `str`<a id="check_component_id-str"></a>

The unique identifier associated for the pay component on this check.

##### name: `str`<a id="name-str"></a>

The name given to the pay component

##### classification_type: `str`<a id="classification_type-str"></a>

The category that this component falls into.

##### effect_on_pay: `str`<a id="effect_on_pay-str"></a>

The effect that the pay component will have on the check amount.

##### start_date: `datetime`<a id="start_date-datetime"></a>

The date that the pay component is able to be applied on a check.

##### end_date: `datetime`<a id="end_date-datetime"></a>

The date that the pay component is not available to be applied on a check moving forward.

##### applies_to_worker_types: [`PayComponentResource2AppliesToWorkerTypes`](./paychex_python_sdk/type/pay_component_resource2_applies_to_worker_types.py)<a id="applies_to_worker_types-paycomponentresource2appliestoworkertypespaychex_python_sdktypepay_component_resource2_applies_to_worker_typespy"></a>

##### job_id: `str`<a id="job_id-str"></a>

This is used optionally for overriding a job when it needs to be different then the workers default. This option is only available when the client has job costing.

##### labor_assignment_id: `str`<a id="labor_assignment_id-str"></a>

This is used optionally for overriding a labor assignment when it needs to be different then the workers assignment distribution. This option is only available when the client has labor assignment.

##### pay_rate_id: `str`<a id="pay_rate_id-str"></a>

The rate identifier for the workers compensation

##### pay_rate: `str`<a id="pay_rate-str"></a>

The rate amount that will be applied for this component. Used in conjunction with Hours or Units.

##### pay_hours: `str`<a id="pay_hours-str"></a>

The number of hours that will be applied for this component. Used in conjunction with rate.

##### pay_units: `str`<a id="pay_units-str"></a>

The number of units that will be applied for this component. Used in conjunction with rate.

##### pay_amount: `str`<a id="pay_amount-str"></a>

The flat amount to be applied for this component. Not used with Rate, Hours, or Units.

##### memoed: `bool`<a id="memoed-bool"></a>

This is used optionally for memoing the payHours or payUnits so that they are informational when using a payAmount.

##### line_date: `datetime`<a id="line_date-datetime"></a>

This is used optionally for specifying a date that the pay component was generated on.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayComponentResource2`](./paychex_python_sdk/type/pay_component_resource2.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CheckResource2`](./paychex_python_sdk/pydantic/check_resource2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checks/{checkId}/checkcomponents` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.payroll.add_worker_check`<a id="paychexpayrolladd_worker_check"></a>

Add a check to a worker for an unprocessed pay period.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_worker_check_response = paychex.payroll.add_worker_check(
    worker_id="workerId_example",
    worker_id="004UWBZQJ7GEB9TVWFR9",
    paycheck_id="1020026552555444",
    pay_period_id="1020026427391732",
    check_correlation_id="yourID_1",
    block_auto_distribution=False,
    earnings=[
        {
            "check_component_id": "1020026552555441",
            "name": "Hourly",
            "classification_type": "REGULAR",
            "effect_on_pay": "ADDITION",
            "pay_rate": "40.2",
            "pay_units": "4",
        }
    ],
    deductions=[
        {
            "check_component_id": "1020026552555441",
            "name": "Hourly",
            "classification_type": "REGULAR",
            "effect_on_pay": "ADDITION",
            "pay_rate": "40.2",
            "pay_units": "4",
        }
    ],
    informational=[
        {
            "check_component_id": "1020026552555441",
            "name": "Hourly",
            "classification_type": "REGULAR",
            "effect_on_pay": "ADDITION",
            "pay_rate": "40.2",
            "pay_units": "4",
        }
    ],
    taxes=[
        {
            "check_component_id": "1020026552555441",
            "name": "Hourly",
            "classification_type": "REGULAR",
            "effect_on_pay": "ADDITION",
            "pay_rate": "40.2",
            "pay_units": "4",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### requestBody: [`CheckResource1`](./paychex_python_sdk/type/check_resource1.py)<a id="requestbody-checkresource1paychex_python_sdktypecheck_resource1py"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CheckResource1`](./paychex_python_sdk/pydantic/check_resource1.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/checks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.payroll.delete_checks_by_pay_period_and_user`<a id="paychexpayrolldelete_checks_by_pay_period_and_user"></a>

Delete checks by pay period Id and user Id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paychex.payroll.delete_checks_by_pay_period_and_user(
    payperiodid="payperiodid_example",
    deletebyuserid=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payperiodid: `str`<a id="payperiodid-str"></a>

ID associated with desired pay period.

##### deletebyuserid: `bool`<a id="deletebyuserid-bool"></a>

Value for deletebyuserid parameter should be \"true\" 

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checks` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.payroll.get_company_checks_by_pay_period`<a id="paychexpayrollget_company_checks_by_pay_period"></a>

Get check(s) that are for a specific company within a processed or unprocessed pay period.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_company_checks_by_pay_period_response = paychex.payroll.get_company_checks_by_pay_period(
    company_id="companyId_example",
    payperiodid="payperiodid_example",
    offset=0,
    limit=0,
    filterbyuserid=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

ID associated with desired company.

##### payperiodid: `str`<a id="payperiodid-str"></a>

The id assigned to the pay period that the check will be within.

##### offset: `int`<a id="offset-int"></a>

The zero based offset of the next page of data to be presented.

##### limit: `int`<a id="limit-int"></a>

The maximum number of elements to be returned in a page transition.

##### filterbyuserid: `bool`<a id="filterbyuserid-bool"></a>

Filter by User Id.

#### 🔄 Return<a id="🔄-return"></a>

[`CheckResource`](./paychex_python_sdk/pydantic/check_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/checks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.payroll.get_company_pay_component`<a id="paychexpayrollget_company_pay_component"></a>

Pay component associated with the company.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_company_pay_component_response = paychex.payroll.get_company_pay_component(
    company_id="companyId_example",
    paycomponent_id="paycomponentId_example",
    asof="2020-01-04T00:00:00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The id assigned to the company that is being requested for.

##### paycomponent_id: `str`<a id="paycomponent_id-str"></a>

The unique identifier used to identify a pay component.

##### asof: `str`<a id="asof-str"></a>

Returns PayComponent as of the date used in the request.

#### 🔄 Return<a id="🔄-return"></a>

[`PayComponentResource`](./paychex_python_sdk/pydantic/pay_component_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/paycomponents/{paycomponentId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.payroll.get_company_pay_components`<a id="paychexpayrollget_company_pay_components"></a>

Array of pay components that are configured for a company. Pay components are earnings and deductions which are used for payroll.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_company_pay_components_response = paychex.payroll.get_company_pay_components(
    company_id="companyId_example",
    effectonpay="string_example",
    asof="2020-01-04T00:00:00Z",
    classificationtype="string_example",
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The id assigned to the company that is being requested for.

##### effectonpay: `str`<a id="effectonpay-str"></a>

The type of effect on pay that you are requested for.

##### asof: `str`<a id="asof-str"></a>

Returns all PayComponent's as of the date used in the request.

##### classificationtype: `str`<a id="classificationtype-str"></a>

The category that this component falls into. (such as  EARNINGS  or   SICK_PAY )

##### name: `str`<a id="name-str"></a>

The name of a pay component that a company has.

#### 🔄 Return<a id="🔄-return"></a>

[`PayComponentResource`](./paychex_python_sdk/pydantic/pay_component_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/paycomponents` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.payroll.get_company_pay_periods`<a id="paychexpayrollget_company_pay_periods"></a>

Array of pay periods associated with the company.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_company_pay_periods_response = paychex.payroll.get_company_pay_periods(
    company_id="companyId_example",
    status=[
        "string_example"
    ],
    _from="string_example",
    to="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The id assigned to the company that is being requested for.

##### status: List[`str`]<a id="status-liststr"></a>

Get PayPeriods that are in List of specific status.

##### _from: `str`<a id="_from-str"></a>

The beginning of the search date range using the Payperiod start date.

##### to: `str`<a id="to-str"></a>

The ending of the search date range using the Payperiod end date.

#### 🔄 Return<a id="🔄-return"></a>

[`PayPeriodResource`](./paychex_python_sdk/pydantic/pay_period_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/payperiods` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.payroll.get_pay_period`<a id="paychexpayrollget_pay_period"></a>

A single pay period.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_pay_period_response = paychex.payroll.get_pay_period(
    company_id="companyId_example",
    payperiod_id="payperiodId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The id assigned to the company that is being requested for.

##### payperiod_id: `str`<a id="payperiod_id-str"></a>

The id assigned to the PayPeriod you are looking for.

#### 🔄 Return<a id="🔄-return"></a>

[`PayPeriodResource`](./paychex_python_sdk/pydantic/pay_period_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companies/{companyId}/payperiods/{payperiodId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.payroll.get_worker_check`<a id="paychexpayrollget_worker_check"></a>

Retrieve a specific unprocessed or processed check that a worker has.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_worker_check_response = paychex.payroll.get_worker_check(
    worker_id="workerId_example",
    paycheck_id="paycheckId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### paycheck_id: `str`<a id="paycheck_id-str"></a>

The id of a single check that a workers has.

#### 🔄 Return<a id="🔄-return"></a>

[`CheckResource1`](./paychex_python_sdk/pydantic/check_resource1.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/checks/{externalCheckId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.payroll.get_worker_checks_by_pay_period`<a id="paychexpayrollget_worker_checks_by_pay_period"></a>

Get check(s) that are for a specific worker   within a processed or unprocessed pay period.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_worker_checks_by_pay_period_response = paychex.payroll.get_worker_checks_by_pay_period(
    worker_id="workerId_example",
    payperiodid="payperiodid_example",
    filterbyuserid=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### payperiodid: `str`<a id="payperiodid-str"></a>

The id assigned to the pay period that the  check will be within.

##### filterbyuserid: `bool`<a id="filterbyuserid-bool"></a>

Filter by User Id.

#### 🔄 Return<a id="🔄-return"></a>

[`CheckResource1`](./paychex_python_sdk/pydantic/check_resource1.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/checks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.payroll.remove_pay_component`<a id="paychexpayrollremove_pay_component"></a>

Remove a single pay component on an individual unprocessed check.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paychex.payroll.remove_pay_component(
    check_id="checkId_example",
    check_component_id="checkComponentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### check_id: `str`<a id="check_id-str"></a>

ID associated with desired check.

##### check_component_id: `str`<a id="check_component_id-str"></a>

ID associated with an Earning of this check

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checks/{checkId}/checkcomponents/{checkComponentId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.payroll.remove_worker_check`<a id="paychexpayrollremove_worker_check"></a>

Remove a specific unprocessed check that a worker has.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_worker_check_response = paychex.payroll.remove_worker_check(
    worker_id="workerId_example",
    paycheck_id="paycheckId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### paycheck_id: `str`<a id="paycheck_id-str"></a>

The id of a single check that a workers has.

#### 🔄 Return<a id="🔄-return"></a>

[`CheckResource1`](./paychex_python_sdk/pydantic/check_resource1.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/checks/{externalCheckId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.payroll.update_pay_component`<a id="paychexpayrollupdate_pay_component"></a>

 Update a single pay component on an individual unprocessed check.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_pay_component_response = paychex.payroll.update_pay_component(
    check_id="checkId_example",
    check_component_id="checkComponentId_example",
    description="string_example",
    component_id="970000053577899",
    check_component_id="1020026552555441",
    name="string_example",
    classification_type="string_example",
    effect_on_pay="ADDITION",
    start_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
    applies_to_worker_types=[
        "string_example"
    ],
    job_id="string_example",
    labor_assignment_id="string_example",
    pay_rate_id="string_example",
    pay_rate="string_example",
    pay_hours="string_example",
    pay_units="string_example",
    pay_amount="string_example",
    memoed=True,
    line_date="1970-01-01T00:00:00.00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### check_id: `str`<a id="check_id-str"></a>

ID associated with desired check.

##### check_component_id: `str`<a id="check_component_id-str"></a>

ID associated with an Earning of this check

##### requestBody: [`PayComponentResource2`](./paychex_python_sdk/type/pay_component_resource2.py)<a id="requestbody-paycomponentresource2paychex_python_sdktypepay_component_resource2py"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PayComponentResource2`](./paychex_python_sdk/pydantic/pay_component_resource2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checks/{checkId}/checkcomponents/{checkComponentId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.webhooks.add_webhook`<a id="paychexwebhooksadd_webhook"></a>

<h3>Add a webhook for the calling application.</h3><p>When registering a webhook, you will need to provide your own URI in the request body (see our <a href='https://developer.paychex.com/resources/webhooks'>full webhook documention here</a> on how to configure your URI). The newly registered webhook will send notifications to this endpoint as JSON payloads which vary by domain. Please configure your endpoint to accept the relevant payloads. To see an example payload for each domain, please refer to the "Callbacks" tab.</p>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_webhook_response = paychex.webhooks.add_webhook(
    uri="string_example",
    authentication={
        "auth_type": "NO_AUTH",
    },
    domains=[
        "string_example"
    ],
    hook_id="string_example",
    company_id="string_example",
    links=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### uri: `str`<a id="uri-str"></a>

Enter a valid URL for the webhook to receive events.

##### authentication: [`Authentication1`](./paychex_python_sdk/type/authentication1.py)<a id="authentication-authentication1paychex_python_sdktypeauthentication1py"></a>


##### domains: [`WebhookRequestDomains`](./paychex_python_sdk/type/webhook_request_domains.py)<a id="domains-webhookrequestdomainspaychex_python_sdktypewebhook_request_domainspy"></a>

##### hook_id: `str`<a id="hook_id-str"></a>

The unique identifier associated with this webhook. Not required for Posting.

##### company_id: `str`<a id="company_id-str"></a>

ID associated with desired company that will receive the webhook notifications. NOTE: If no Company ID is provided in the POST, then all companies linked to the app will receive notifications.

##### links: List[`Link`]<a id="links-listlink"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhookRequest`](./paychex_python_sdk/type/webhook_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebhookResponse`](./paychex_python_sdk/pydantic/webhook_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/management/hooks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.webhooks.delete_by_id`<a id="paychexwebhooksdelete_by_id"></a>

Delete a specific hook for the calling application by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_by_id_response = paychex.webhooks.delete_by_id(
    hook_id="hookId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### hook_id: `str`<a id="hook_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/management/hooks/{hookId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.webhooks.get_available_domains`<a id="paychexwebhooksget_available_domains"></a>

Will return a list of available domains depending on application type.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_available_domains_response = paychex.webhooks.get_available_domains()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/management/domains` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.webhooks.get_specific_hook_by_id`<a id="paychexwebhooksget_specific_hook_by_id"></a>

Get a specific hook for the calling application by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_hook_by_id_response = paychex.webhooks.get_specific_hook_by_id(
    hook_id="hookId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### hook_id: `str`<a id="hook_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksGetSpecificHookByIdResponse`](./paychex_python_sdk/pydantic/webhooks_get_specific_hook_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/management/hooks/{hookId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.webhooks.list`<a id="paychexwebhookslist"></a>

List all the webhooks setup for the calling application

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = paychex.webhooks.list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksListResponse`](./paychex_python_sdk/pydantic/webhooks_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/management/hooks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.add_communication`<a id="paychexworkeradd_communication"></a>

Add a single communication to the "Active" or "In-progress" worker.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_communication_response = paychex.worker.add_communication(
    worker_id="workerId_example",
    communication_id="string_example",
    type="STREET_ADDRESS",
    usage_type="PERSONAL",
    dial_country="string_example",
    dial_area="string_example",
    dial_number="string_example",
    dial_extension="string_example",
    uri="string_example",
    street_line_one="string_example",
    street_line_two="string_example",
    post_office_box="string_example",
    city="string_example",
    postal_code="string_example",
    postal_code_extension="string_example",
    country_subdivision_code="string_example",
    country_code="string_example",
    links=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

The id assigned to the worker that workers are being requested for.

##### communication_id: `str`<a id="communication_id-str"></a>

The ID for the workers specific communication item.

##### type: `str`<a id="type-str"></a>

A set of communication types classifying an instruction that the customer, requester, or subject must comply with in order for the screening to go forward. NOTE: PHONE and EMAIL type supports BUSINESS and PERSONAL usage type only.MOBILE_PHONE, FAX and PAGER supports BUSINESS usage type only.This data field cannot be PATCHED.

##### usage_type: `str`<a id="usage_type-str"></a>

A code classifying a designated use associated with a contact method. For example, whether a telephone or email address is one for business communications or one primarily for personal use.This data field cannot be PATCHED.

##### dial_country: `str`<a id="dial_country-str"></a>

The country dialing code for a communication number

##### dial_area: `str`<a id="dial_area-str"></a>

The area dialing code for a communication number

##### dial_number: `str`<a id="dial_number-str"></a>

The communication number, not including country dialing or area dialing codes

##### dial_extension: `str`<a id="dial_extension-str"></a>

The extension of the associated communication number

##### uri: `str`<a id="uri-str"></a>

The mailto address as specified in RFC2368

##### street_line_one: `str`<a id="street_line_one-str"></a>

The street address line one

##### street_line_two: `str`<a id="street_line_two-str"></a>

The street address line two

##### post_office_box: `str`<a id="post_office_box-str"></a>

The postal office box. This data field cannot be PATCHED

##### city: `str`<a id="city-str"></a>

The city name

##### postal_code: `str`<a id="postal_code-str"></a>

The zip-code

##### postal_code_extension: `str`<a id="postal_code_extension-str"></a>

The zip-code extension

##### country_subdivision_code: `str`<a id="country_subdivision_code-str"></a>

The state code (ISO 3166 subdivision code). This data field cannot be PATCHED for ACTIVE worker

##### country_code: `str`<a id="country_code-str"></a>

The country code (ISO 3166 alpha-2)

##### links: List[`Link`]<a id="links-listlink"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CommunicationResource1`](./paychex_python_sdk/type/communication_resource1.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CommunicationResource1`](./paychex_python_sdk/pydantic/communication_resource1.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/communications` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.add_direct_deposit`<a id="paychexworkeradd_direct_deposit"></a>

Add a direct deposit to an "Active" worker.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_direct_deposit_response = paychex.worker.add_direct_deposit(
    worker_id="workerId_example",
    direct_deposit_id="1020026420675252",
    start_date="2017-09-11T00:00:00Z",
    payment_type="PERCENTAGE",
    account_type="CHECKING",
    value=75,
    routing_number="222371863",
    account_number="123456",
    priority="1",
    links=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### direct_deposit_id: `str`<a id="direct_deposit_id-str"></a>

The ID for the direct deposit item.

##### start_date: `datetime`<a id="start_date-datetime"></a>

The date that this direct deposit will be applied to future pay periods. This data field cannot be PATCHED.

##### payment_type: `str`<a id="payment_type-str"></a>

A type of payment for the direct deposit.

##### account_type: `str`<a id="account_type-str"></a>

Financial institutions account type. This data field cannot be PATCHED.

##### value: `Union[int, float]`<a id="value-unionint-float"></a>

The amount to be applied to this direct deposit.

##### routing_number: `str`<a id="routing_number-str"></a>

The financial institutions routing number.This data field cannot be PATCHED.

##### account_number: `str`<a id="account_number-str"></a>

The financial institutions account number.This data field cannot be PATCHED.

##### priority: `str`<a id="priority-str"></a>

The priority order for which the direct deposits will be performed in. When a new direct deposit is added the priority will be assigned. The priority can be modified only by swapping with a different direct deposit using the bulk PATCH. A paymentType of REMAINDER will show a priority of 99 and can't be modified.This data field cannot be PATCHED.

##### links: List[`Link`]<a id="links-listlink"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DirectDepositResource`](./paychex_python_sdk/type/direct_deposit_resource.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DirectDepositResource`](./paychex_python_sdk/pydantic/direct_deposit_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/directdeposits` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.add_federal_tax_setup`<a id="paychexworkeradd_federal_tax_setup"></a>

Add federal tax setup for a "Active" or "In-progress" worker.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_federal_tax_setup_response = paychex.worker.add_federal_tax_setup(
    worker_id="workerId_example",
    tax_id="3520000118851387",
    filing_status="MARRIED_FILING_JOINTLY",
    multiple_jobs="false",
    dependents_amount="123.45",
    other_income="23.45",
    deductions_amount="2.45",
    extra_withholding_amount="3.45",
    taxes_withheld="true",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### tax_id: `str`<a id="tax_id-str"></a>

The ID for the federal tax item.

##### filing_status: `str`<a id="filing_status-str"></a>

Filing status.

##### multiple_jobs: `str`<a id="multiple_jobs-str"></a>

See federal W-4 instructions.

##### dependents_amount: `str`<a id="dependents_amount-str"></a>

See federal W-4 instructions.

##### other_income: `str`<a id="other_income-str"></a>

See federal W-4 instructions.

##### deductions_amount: `str`<a id="deductions_amount-str"></a>

See federal W-4 instructions.

##### extra_withholding_amount: `str`<a id="extra_withholding_amount-str"></a>

Additional tax you want withheld each pay period.

##### taxes_withheld: `str`<a id="taxes_withheld-str"></a>

Should federal taxes be withheld.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WorkerFederalTaxResource`](./paychex_python_sdk/type/worker_federal_tax_resource.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WorkerFederalTaxResource`](./paychex_python_sdk/pydantic/worker_federal_tax_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/federaltax` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.add_pay_component`<a id="paychexworkeradd_pay_component"></a>

Add a single pay component to the "Active" worker. This pay component will be used for apply recurring pay components on a workers check based on the frequency specified. supports the ability to POST both Addition and Reduction type pay components.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_pay_component_response = paychex.worker.add_pay_component(
    worker_id="workerId_example",
    worker_component_id="970000223656831",
    component_id="970000180599325",
    name="Deduction - 1",
    calculation_type="00H2A1IUJE7MXV6TQ37U",
    calculation_base_id="00H2A1IUJE7MXV6TQ37U",
    value=5,
    start_date="2018-03-01T00:00:00Z",
    effective_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
    effect_on_pay="REDUCTION",
    classification_type="string_example",
    frequency={
        "applied": "BY_PAY_PERIOD",
        "occurrence": "QUARTERLY",
        "effected_checks": "EVERY_CHECK",
    },
    links=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### worker_component_id: `str`<a id="worker_component_id-str"></a>

The id of a single pay component that a workers has.

##### component_id: `str`<a id="component_id-str"></a>

The unique identifier of the pay component. This data field cannot be PATCHED.

##### name: `str`<a id="name-str"></a>

Name of the pay component. This data field will be populated automatically based on componentId.

##### calculation_type: `str`<a id="calculation_type-str"></a>

The type of calculation that will be applied for the pay component .

##### calculation_base_id: `str`<a id="calculation_base_id-str"></a>

This is required if you are not using a FLAT_DOLLAR_AMOUNT Calculation Type.

##### value: `Union[int, float]`<a id="value-unionint-float"></a>

This is used to specify the value that is used against the calculationType.

##### start_date: `datetime`<a id="start_date-datetime"></a>

Date which this pay component will start to be applied during the payruns. This is an optional field that default to current datetime if not provided. This cannot be backdated but can be added to start in the future.

##### effective_date: `datetime`<a id="effective_date-datetime"></a>

Date which this pay component has started for the worker.

##### end_date: `datetime`<a id="end_date-datetime"></a>

Date which this pay component has ended for the worker.

##### effect_on_pay: `str`<a id="effect_on_pay-str"></a>

What the effect on pay will be (REDUCTION OR ADDITION), currently only reductions are available. This data field will be populated automatically based on componentId. This data field cannot be PATCHED

##### classification_type: `str`<a id="classification_type-str"></a>

The category that this component falls into.

##### frequency: [`PayComponentFrequencyTypeResource1`](./paychex_python_sdk/type/pay_component_frequency_type_resource1.py)<a id="frequency-paycomponentfrequencytyperesource1paychex_python_sdktypepay_component_frequency_type_resource1py"></a>


##### links: List[`Link`]<a id="links-listlink"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RecurringResource`](./paychex_python_sdk/type/recurring_resource.py)
#### 🔄 Return<a id="🔄-return"></a>

[`RecurringResource`](./paychex_python_sdk/pydantic/recurring_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/paycomponents` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.add_pay_rate`<a id="paychexworkeradd_pay_rate"></a>

Add a single compensation rate to the "Active" or "In-progress" worker.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_pay_rate_response = paychex.worker.add_pay_rate(
    worker_id="workerId_example",
    description="Security2",
    rate_id="970000054610137",
    start_date="1970-01-01T00:00:00.00Z",
    rate_number="RATE_1",
    rate_type="RATE_1",
    amount="40.2",
    standard_hours="25.25",
    standard_overtime="3.25",
    default=True,
    effective_date="string_example",
    links=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### description: `str`<a id="description-str"></a>

Describes the rate for the worker.

##### rate_id: `str`<a id="rate_id-str"></a>

Unique identifier for this workers pay rate. **This ID will change if this is created for an IN_PROGRESS worker that is later completed within Flex**

##### start_date: `datetime`<a id="start_date-datetime"></a>

The date when the pay rate is going to begin.

##### rate_number: `str`<a id="rate_number-str"></a>

The number of the rate. A worker can have up to 5 different rates.

##### rate_type: `str`<a id="rate_type-str"></a>

Type of rate.

##### amount: `str`<a id="amount-str"></a>

The currency amount which this rate is applied.

##### standard_hours: `str`<a id="standard_hours-str"></a>

Default standard hours that this rate is used with a pay frequency.

##### standard_overtime: `str`<a id="standard_overtime-str"></a>

Default over time hours that this rate is used with a pay frequency.

##### default: `bool`<a id="default-bool"></a>

If this rate is the default one to apply on the worker.

##### effective_date: `str`<a id="effective_date-str"></a>

The date when the pay rate becomes effective for the worker.(can be used only in POST/PATCH for an active worker)

##### links: List[`Link`]<a id="links-listlink"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayRateResource`](./paychex_python_sdk/type/pay_rate_resource.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PayRateResource`](./paychex_python_sdk/pydantic/pay_rate_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/compensation/payrates` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.add_worker_contacts`<a id="paychexworkeradd_worker_contacts"></a>

Add one or more contacts to a worker. A contact may represent a person or entity (organization) but not both. A contact must have at least one communication (telecom, postal, or email). Person contacts can have multiple communications for each communication type (telecom, postal, or email) to support BUSINESS and PERSONAL. Exactly one contact must be marked as primary for each contact type. If one or more contacts are posted for the same contact type, and there are currently no contacts of that type for the worker, the first contact in the list will be made primary unless another in the list is expressly marked as primary. When a new contact is made primary the previous primary contact will be marked as not primary. Use the GET /companies/{companyId}/contacttypes endpoint to get a full list of available contact types and relationship types (used for person contacts).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_worker_contacts_response = paychex.worker.add_worker_contacts(
    worker_id="workerId_example",
    contact_id="string_example",
    contact_type={
    },
    relationship={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### contact_id: `str`<a id="contact_id-str"></a>

The ID for the workers specific contact.

##### contact_type: [`ContactTypeResource1`](./paychex_python_sdk/type/contact_type_resource1.py)<a id="contact_type-contacttyperesource1paychex_python_sdktypecontact_type_resource1py"></a>


##### relationship: [`RelationshipResource`](./paychex_python_sdk/type/relationship_resource.py)<a id="relationship-relationshipresourcepaychex_python_sdktyperelationship_resourcepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WorkerContactResource`](./paychex_python_sdk/type/worker_contact_resource.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WorkerContactResource`](./paychex_python_sdk/pydantic/worker_contact_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/contacts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.create_custom_field`<a id="paychexworkercreate_custom_field"></a>

Create CustomField at the worker level

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_custom_field_response = paychex.worker.create_custom_field(
    worker_id="workerId_example",
    worker_custom_field_id="string_example",
    custom_field_id="string_example",
    type="DROPDOWN",
    boolean_value=True,
    text_value="string_example",
    numeric_value=3.14,
    date_value="1970-01-01T00:00:00.00Z",
    dropdown_id="string_example",
    dropdown_value="string_example",
    custom_field_name="string_example",
    required=True,
    check_stub=True,
    employee_editable=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### worker_custom_field_id: `str`<a id="worker_custom_field_id-str"></a>

The unique identifier that is autogenerated when a custom field is created

##### custom_field_id: `str`<a id="custom_field_id-str"></a>

client Custom Field Id

##### type: `str`<a id="type-str"></a>

The type of field the custom field is

##### boolean_value: `bool`<a id="boolean_value-bool"></a>

The value for BOOLEAN type (true/false)

##### text_value: `str`<a id="text_value-str"></a>

The value for TEXT type (any text, alphanumeric, special characters allowed)

##### numeric_value: `Union[int, float]`<a id="numeric_value-unionint-float"></a>

Numeric data type can have three formats namely - whole number, second decimal place and fourth decimal place, example: 12 , 12.34 or 12.3456

##### date_value: `datetime`<a id="date_value-datetime"></a>

The value for DATE type , example : 2012-02-01T05:00:00Z

##### dropdown_id: `str`<a id="dropdown_id-str"></a>

The unique identifier that is autogenerated when dropdown list is created

##### dropdown_value: `str`<a id="dropdown_value-str"></a>

The value for dropdown list

##### custom_field_name: `str`<a id="custom_field_name-str"></a>

The name of the custom field. Such as: \\\"Hobbies\\\"

##### required: `bool`<a id="required-bool"></a>

Where to indicate if the custom field is required on the worker where true = required and false = not required

##### check_stub: `bool`<a id="check_stub-bool"></a>

Where to indicate if the custom field is required on the workers pay stub, where true = required and false = not required.

##### employee_editable: `bool`<a id="employee_editable-bool"></a>

Where to indicate if the custom field is able to be edited by the employee, where true = required and false = not required.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WorkerCustomFieldsResource`](./paychex_python_sdk/type/worker_custom_fields_resource.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WorkerCustomFieldsResource`](./paychex_python_sdk/pydantic/worker_custom_fields_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/customfields` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.delete_contact_by_contact_id`<a id="paychexworkerdelete_contact_by_contact_id"></a>

Delete a worker contact by contactId.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paychex.worker.delete_contact_by_contact_id(
    worker_id="workerId_example",
    contact_id="contactId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### contact_id: `str`<a id="contact_id-str"></a>

ID associated with desired worker contact.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/contacts/{contactId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.delete_custom_field`<a id="paychexworkerdelete_custom_field"></a>

Delete CustomField at the worker level

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paychex.worker.delete_custom_field(
    worker_id="workerId_example",
    worker_custom_field_id="workerCustomFieldId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### worker_custom_field_id: `str`<a id="worker_custom_field_id-str"></a>

ID associated with desired worker custom field.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/customfields/{workerCustomFieldId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.delete_in_progress`<a id="paychexworkerdelete_in_progress"></a>

Delete in progress Worker

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paychex.worker.delete_in_progress(
    worker_id="workerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.get_communication_item`<a id="paychexworkerget_communication_item"></a>

A "Active" or "In-progress" workers single communication item.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_communication_item_response = paychex.worker.get_communication_item(
    worker_id="workerId_example",
    communication_id="communicationId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

The id assigned to the worker that workers are being requested for.

##### communication_id: `str`<a id="communication_id-str"></a>

The id of a single workers communication.

#### 🔄 Return<a id="🔄-return"></a>

[`CommunicationResource1`](./paychex_python_sdk/pydantic/communication_resource1.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/communications/{communicationId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.get_communications`<a id="paychexworkerget_communications"></a>

Information about "Active" or "In-progress"  workers communications.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_communications_response = paychex.worker.get_communications(
    worker_id="workerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

The id assigned to the worker that workers are being requested for.

#### 🔄 Return<a id="🔄-return"></a>

[`CommunicationResource1`](./paychex_python_sdk/pydantic/communication_resource1.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/communications` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.get_compensation_information`<a id="paychexworkerget_compensation_information"></a>

Information about a workers compensation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_compensation_information_response = paychex.worker.get_compensation_information(
    worker_id="workerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

#### 🔄 Return<a id="🔄-return"></a>

[`CollectionResource`](./paychex_python_sdk/pydantic/collection_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/compensation` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.get_contact_by_contact_id`<a id="paychexworkerget_contact_by_contact_id"></a>

Get a worker contact by contactId.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_contact_by_contact_id_response = paychex.worker.get_contact_by_contact_id(
    worker_id="workerId_example",
    contact_id="contactId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### contact_id: `str`<a id="contact_id-str"></a>

The id of a single Contact.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkerContactResource`](./paychex_python_sdk/pydantic/worker_contact_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/contacts/{contactId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.get_contacts`<a id="paychexworkerget_contacts"></a>

Get all contacts for the specified worker.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_contacts_response = paychex.worker.get_contacts(
    worker_id="workerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkerContactResource`](./paychex_python_sdk/pydantic/worker_contact_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/contacts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.get_custom_field`<a id="paychexworkerget_custom_field"></a>

Get the worker's customFields by workerCustomFieldId

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_custom_field_response = paychex.worker.get_custom_field(
    worker_id="workerId_example",
    worker_custom_field_id="workerCustomFieldId_example",
    asof="2020-01-04T00:00:00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### worker_custom_field_id: `str`<a id="worker_custom_field_id-str"></a>

ID associated with desired worker custom field.

##### asof: `str`<a id="asof-str"></a>

Returns custom field as of the date used in the request

#### 🔄 Return<a id="🔄-return"></a>

[`WorkerCustomFieldsResource`](./paychex_python_sdk/pydantic/worker_custom_fields_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/customfields/{workerCustomFieldId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.get_custom_fields`<a id="paychexworkerget_custom_fields"></a>

Get the worker's customFields

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_custom_fields_response = paychex.worker.get_custom_fields(
    worker_id="workerId_example",
    asof="2020-01-04T00:00:00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### asof: `str`<a id="asof-str"></a>

Returns all custom fields as of the date used in the request

#### 🔄 Return<a id="🔄-return"></a>

[`WorkerCustomFieldsResource`](./paychex_python_sdk/pydantic/worker_custom_fields_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/customfields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.get_direct_deposit`<a id="paychexworkerget_direct_deposit"></a>

Single direct deposit for an "Active" worker.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_direct_deposit_response = paychex.worker.get_direct_deposit(
    worker_id="workerId_example",
    direct_deposit_id="directDepositId_example",
    effectivitydate="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### direct_deposit_id: `str`<a id="direct_deposit_id-str"></a>

The id assigned to the direct deposit for this worker.

##### effectivitydate: `str`<a id="effectivitydate-str"></a>

The effectivity date.

#### 🔄 Return<a id="🔄-return"></a>

[`DirectDepositResource`](./paychex_python_sdk/pydantic/direct_deposit_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/directdeposits/{directDepositId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.get_federal_tax_setup`<a id="paychexworkerget_federal_tax_setup"></a>

Federal tax setup for "Active" or "In-progress"  worker.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_federal_tax_setup_response = paychex.worker.get_federal_tax_setup(
    worker_id="workerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkerFederalTaxResource`](./paychex_python_sdk/pydantic/worker_federal_tax_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/federaltax` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.get_information`<a id="paychexworkerget_information"></a>

Information about a unique worker (employee and contractor) that your application has been granted access to. Currently workers that exist within Paychex Flex payroll will be available, future enhancements will make workers from other Paychex systems available.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_information_response = paychex.worker.get_information(
    worker_id="workerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkerResource1`](./paychex_python_sdk/pydantic/worker_resource1.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.get_pay_component`<a id="paychexworkerget_pay_component"></a>

Retrieve a specific pay component that a "Active" worker has.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_pay_component_response = paychex.worker.get_pay_component(
    worker_id="workerId_example",
    worker_component_id="workerComponentId_example",
    asof="2020-01-04T00:00:00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### worker_component_id: `str`<a id="worker_component_id-str"></a>

The id of a single pay component that a  \"Active\" worker has.

##### asof: `str`<a id="asof-str"></a>

Returns pay component as of the date used in the request

#### 🔄 Return<a id="🔄-return"></a>

[`RecurringResource`](./paychex_python_sdk/pydantic/recurring_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/paycomponents/{workerComponentId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.get_pay_components`<a id="paychexworkerget_pay_components"></a>

Get all the the pay components for a specific "Active" worker.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_pay_components_response = paychex.worker.get_pay_components(
    worker_id="workerId_example",
    effectonpay="string_example",
    asof="2020-01-04T00:00:00Z",
    name="string_example",
    componentid="string_example",
    classificationtype="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### effectonpay: `str`<a id="effectonpay-str"></a>

What the effect on pay will be (REDUCTION OR ADDITION), currently only reductions are available.

##### asof: `str`<a id="asof-str"></a>

Returns all pay components as of the date used in the request

##### name: `str`<a id="name-str"></a>

The name of a pay component that a workers has.

##### componentid: `str`<a id="componentid-str"></a>

The unique identifier of the pay component.

##### classificationtype: `str`<a id="classificationtype-str"></a>

The classification type of a pay component that a worker has. (such as \"DEDUCTION\", or \"REGULAR\",)

#### 🔄 Return<a id="🔄-return"></a>

[`RecurringResource`](./paychex_python_sdk/pydantic/recurring_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/paycomponents` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.get_pay_rate`<a id="paychexworkerget_pay_rate"></a>

A workers single compensation rate.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_pay_rate_response = paychex.worker.get_pay_rate(
    worker_id="workerId_example",
    rate_id="rateId_example",
    asof="2020-01-04T00:00:00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### rate_id: `str`<a id="rate_id-str"></a>

The id of a single workers compensation rate.

##### asof: `str`<a id="asof-str"></a>

Returns compensation as of the date used in the request

#### 🔄 Return<a id="🔄-return"></a>

[`PayRateResource`](./paychex_python_sdk/pydantic/pay_rate_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/compensation/payrates/{rateId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.get_pay_rates_by_worker_id`<a id="paychexworkerget_pay_rates_by_worker_id"></a>

Information about a workers compensation rates. Rate one is only one available if the worker is In-Progress. The multiple rates is available for workers that have been completed within Flex. It’s not required for a worker to have a rate in the system.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_pay_rates_by_worker_id_response = paychex.worker.get_pay_rates_by_worker_id(
    worker_id="workerId_example",
    asof="2020-01-04T00:00:00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### asof: `str`<a id="asof-str"></a>

Returns all pay rates as of the date used in the request

#### 🔄 Return<a id="🔄-return"></a>

[`PayRateResource`](./paychex_python_sdk/pydantic/pay_rate_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/compensation/payrates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.get_pay_standards`<a id="paychexworkerget_pay_standards"></a>

Information about a workers compensation pay standards.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_pay_standards_response = paychex.worker.get_pay_standards(
    worker_id="workerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

#### 🔄 Return<a id="🔄-return"></a>

[`PayStandardResource`](./paychex_python_sdk/pydantic/pay_standard_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/compensation/paystandards` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.get_time_off_balance`<a id="paychexworkerget_time_off_balance"></a>

Array of time off balance(s) a worker has for each policy type of time off, for that worker. NOTE: This data is only available if the client has the Time Off Accrual product (This is not related to the Flex Time product which has it is own dev portal for those APIs).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_time_off_balance_response = paychex.worker.get_time_off_balance(
    worker_id="workerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

The ID of the worker.

#### 🔄 Return<a id="🔄-return"></a>

[`TimeOffResource`](./paychex_python_sdk/pydantic/time_off_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/timeoff` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.get_worker_status_list`<a id="paychexworkerget_worker_status_list"></a>

Retrieve the full list of worker statuses (past, present, and future). For each status the workerStatusId is the value of the corresponding company worker status ID. If no company worker status with a matching type/reason exists then workerStatusId is omitted. If multiple statuses share an effective date the order field will indicate the order in which they were posted.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_worker_status_list_response = paychex.worker.get_worker_status_list(
    worker_id="workerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

#### 🔄 Return<a id="🔄-return"></a>

[`Status1`](./paychex_python_sdk/pydantic/status1.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/status` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.list_assignment_distributions`<a id="paychexworkerlist_assignment_distributions"></a>

Array of assignments that will be used for auto distribution assigned to the worker.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_assignment_distributions_response = paychex.worker.list_assignment_distributions(
    worker_id="workerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

The ID of the worker.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkerAssignmentDistributionsResource`](./paychex_python_sdk/pydantic/worker_assignment_distributions_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/assignmentdistributions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.list_direct_deposits`<a id="paychexworkerlist_direct_deposits"></a>

Array of direct deposits on the "Active" worker.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_direct_deposits_response = paychex.worker.list_direct_deposits(
    worker_id="workerId_example",
    effectivitydate="string_example",
    asof="2020-01-04T00:00:00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### effectivitydate: `str`<a id="effectivitydate-str"></a>

The effectivity date

##### asof: `str`<a id="asof-str"></a>

Returns all direct deposits as of the date used in the request

#### 🔄 Return<a id="🔄-return"></a>

[`DirectDepositResource`](./paychex_python_sdk/pydantic/direct_deposit_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/directdeposits` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.remove_communication`<a id="paychexworkerremove_communication"></a>

Remove a communication item from a "Active" or "In-progress" worker.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_communication_response = paychex.worker.remove_communication(
    worker_id="workerId_example",
    communication_id="communicationId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

The id assigned to the worker that workers are being requested for.

##### communication_id: `str`<a id="communication_id-str"></a>

The id of a single workers communication.

#### 🔄 Return<a id="🔄-return"></a>

[`CommunicationResource1`](./paychex_python_sdk/pydantic/communication_resource1.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/communications/{communicationId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.remove_direct_deposit`<a id="paychexworkerremove_direct_deposit"></a>

Remove a single direct deposit for a "Active" worker.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paychex.worker.remove_direct_deposit(
    worker_id="workerId_example",
    direct_deposit_id="directDepositId_example",
    effectivitydate="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### direct_deposit_id: `str`<a id="direct_deposit_id-str"></a>

The id assigned to the direct deposit for this worker.

##### effectivitydate: `str`<a id="effectivitydate-str"></a>

The effectivity date.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/directdeposits/{directDepositId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.remove_federal_tax`<a id="paychexworkerremove_federal_tax"></a>

Remove the federal tax setup for an "In-progress" worker.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paychex.worker.remove_federal_tax(
    worker_id="workerId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/federaltax` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.remove_pay_component`<a id="paychexworkerremove_pay_component"></a>

Remove a specific pay component that a "Active" worker has.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paychex.worker.remove_pay_component(
    worker_id="workerId_example",
    worker_component_id="workerComponentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### worker_component_id: `str`<a id="worker_component_id-str"></a>

The id of a single pay component that a workers has.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/paycomponents/{workerComponentId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.remove_pay_rate`<a id="paychexworkerremove_pay_rate"></a>

Remove a compensation rate from a worker.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paychex.worker.remove_pay_rate(
    worker_id="workerId_example",
    rate_id="rateId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### rate_id: `str`<a id="rate_id-str"></a>

The id of a single workers compensation rate.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/compensation/payrates/{rateId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.update_communication_item`<a id="paychexworkerupdate_communication_item"></a>

Update a "Active" or "In-progress" workers specific communication item.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_communication_item_response = paychex.worker.update_communication_item(
    worker_id="workerId_example",
    communication_id="communicationId_example",
    communication_id="string_example",
    type="STREET_ADDRESS",
    usage_type="PERSONAL",
    dial_country="string_example",
    dial_area="string_example",
    dial_number="string_example",
    dial_extension="string_example",
    uri="string_example",
    street_line_one="string_example",
    street_line_two="string_example",
    post_office_box="string_example",
    city="string_example",
    postal_code="string_example",
    postal_code_extension="string_example",
    country_subdivision_code="string_example",
    country_code="string_example",
    links=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

The id assigned to the worker that workers are being requested for.

##### communication_id: `str`<a id="communication_id-str"></a>

The id of a single workers communication.

##### requestBody: [`CommunicationResource1`](./paychex_python_sdk/type/communication_resource1.py)<a id="requestbody-communicationresource1paychex_python_sdktypecommunication_resource1py"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CommunicationResource1`](./paychex_python_sdk/pydantic/communication_resource1.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/communications/{communicationId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.update_compensation_rate`<a id="paychexworkerupdate_compensation_rate"></a>

Update a workers specific compensation rate.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_compensation_rate_response = paychex.worker.update_compensation_rate(
    worker_id="workerId_example",
    rate_id="rateId_example",
    description="Security2",
    rate_id="970000054610137",
    start_date="1970-01-01T00:00:00.00Z",
    rate_number="RATE_1",
    rate_type="RATE_1",
    amount="40.2",
    standard_hours="25.25",
    standard_overtime="3.25",
    default=True,
    effective_date="string_example",
    links=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### rate_id: `str`<a id="rate_id-str"></a>

The id of a single workers compensation rate.

##### requestBody: [`PayRateResource`](./paychex_python_sdk/type/pay_rate_resource.py)<a id="requestbody-payrateresourcepaychex_python_sdktypepay_rate_resourcepy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PayRateResource`](./paychex_python_sdk/pydantic/pay_rate_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/compensation/payrates/{rateId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.update_contact`<a id="paychexworkerupdate_contact"></a>

Update a worker contact. A contact may represent a person or entity (organization) but not both. A contact must have at least one communication (telecom, postal, or email). Person contacts can have multiple communications for each communication type (telecom, postal, or email) to support BUSINESS and PERSONAL. Exactly one contact must be marked as primary for each contact type. When a new contact is made primary the previous primary contact will be marked as not primary. A postal contact can be switched from a street address to a PO box and vice versa. This is done by setting either streetLineOne or postOfficeBox (a postal communication may not have both). Use the GET /companies/{companyId}/contacttypes endpoint to get a full list of available contact types and relationship types (used for person contacts).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_contact_response = paychex.worker.update_contact(
    worker_id="workerId_example",
    contact_id="contactId_example",
    contact_id="string_example",
    contact_type={
    },
    relationship={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### contact_id: `str`<a id="contact_id-str"></a>

ID associated with desired worker contact.

##### requestBody: [`WorkerContactResource`](./paychex_python_sdk/type/worker_contact_resource.py)<a id="requestbody-workercontactresourcepaychex_python_sdktypeworker_contact_resourcepy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`WorkerContactResource`](./paychex_python_sdk/pydantic/worker_contact_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/contacts/{contactId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.update_custom_field`<a id="paychexworkerupdate_custom_field"></a>

Update CustomField at the worker level

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_custom_field_response = paychex.worker.update_custom_field(
    worker_id="workerId_example",
    worker_custom_field_id="workerCustomFieldId_example",
    worker_custom_field_id="string_example",
    custom_field_id="string_example",
    type="DROPDOWN",
    boolean_value=True,
    text_value="string_example",
    numeric_value=3.14,
    date_value="1970-01-01T00:00:00.00Z",
    dropdown_id="string_example",
    dropdown_value="string_example",
    custom_field_name="string_example",
    required=True,
    check_stub=True,
    employee_editable=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### worker_custom_field_id: `str`<a id="worker_custom_field_id-str"></a>

ID associated with desired worker custom field.

##### requestBody: [`WorkerCustomFieldsResource`](./paychex_python_sdk/type/worker_custom_fields_resource.py)<a id="requestbody-workercustomfieldsresourcepaychex_python_sdktypeworker_custom_fields_resourcepy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`WorkerCustomFieldsResource`](./paychex_python_sdk/pydantic/worker_custom_fields_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/customfields/{workerCustomFieldId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.update_direct_deposit`<a id="paychexworkerupdate_direct_deposit"></a>

Update a single direct deposit for a an "Active" worker.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_direct_deposit_response = paychex.worker.update_direct_deposit(
    worker_id="workerId_example",
    direct_deposit_id="directDepositId_example",
    direct_deposit_id="1020026420675252",
    start_date="2017-09-11T00:00:00Z",
    payment_type="PERCENTAGE",
    account_type="CHECKING",
    value=75,
    routing_number="222371863",
    account_number="123456",
    priority="1",
    links=[
        {
        }
    ],
    effectivitydate="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### direct_deposit_id: `str`<a id="direct_deposit_id-str"></a>

The id assigned to the direct deposit for this worker.

##### effectivitydate: `str`<a id="effectivitydate-str"></a>

The effectivity date.

##### requestBody: [`DirectDepositResource`](./paychex_python_sdk/type/direct_deposit_resource.py)<a id="requestbody-directdepositresourcepaychex_python_sdktypedirect_deposit_resourcepy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DirectDepositResource`](./paychex_python_sdk/pydantic/direct_deposit_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/directdeposits/{directDepositId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.update_direct_deposits`<a id="paychexworkerupdate_direct_deposits"></a>

Update multiple direct deposits of an "Active" Worker at a time.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_direct_deposits_response = paychex.worker.update_direct_deposits(
    worker_id="workerId_example",
    direct_deposit_id="1020026420675252",
    start_date="2017-09-11T00:00:00Z",
    payment_type="PERCENTAGE",
    account_type="CHECKING",
    value=75,
    routing_number="222371863",
    account_number="123456",
    priority="1",
    links=[
        {
        }
    ],
    effectivitydate="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### direct_deposit_id: `str`<a id="direct_deposit_id-str"></a>

The ID for the direct deposit item.

##### start_date: `datetime`<a id="start_date-datetime"></a>

The date that this direct deposit will be applied to future pay periods. This data field cannot be PATCHED.

##### payment_type: `str`<a id="payment_type-str"></a>

A type of payment for the direct deposit.

##### account_type: `str`<a id="account_type-str"></a>

Financial institutions account type. This data field cannot be PATCHED.

##### value: `Union[int, float]`<a id="value-unionint-float"></a>

The amount to be applied to this direct deposit.

##### routing_number: `str`<a id="routing_number-str"></a>

The financial institutions routing number.This data field cannot be PATCHED.

##### account_number: `str`<a id="account_number-str"></a>

The financial institutions account number.This data field cannot be PATCHED.

##### priority: `str`<a id="priority-str"></a>

The priority order for which the direct deposits will be performed in. When a new direct deposit is added the priority will be assigned. The priority can be modified only by swapping with a different direct deposit using the bulk PATCH. A paymentType of REMAINDER will show a priority of 99 and can't be modified.This data field cannot be PATCHED.

##### links: List[`Link`]<a id="links-listlink"></a>

##### effectivitydate: `str`<a id="effectivitydate-str"></a>

The effectivity date.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DirectDepositResource`](./paychex_python_sdk/type/direct_deposit_resource.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DirectDepositResource`](./paychex_python_sdk/pydantic/direct_deposit_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/directdeposits` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.update_federal_tax_setup`<a id="paychexworkerupdate_federal_tax_setup"></a>

Update the federal tax setup for a "Active" or "In-progress" worker.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_federal_tax_setup_response = paychex.worker.update_federal_tax_setup(
    worker_id="workerId_example",
    tax_id="3520000118851387",
    filing_status="MARRIED_FILING_JOINTLY",
    multiple_jobs="false",
    dependents_amount="123.45",
    other_income="23.45",
    deductions_amount="2.45",
    extra_withholding_amount="3.45",
    taxes_withheld="true",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### tax_id: `str`<a id="tax_id-str"></a>

The ID for the federal tax item.

##### filing_status: `str`<a id="filing_status-str"></a>

Filing status.

##### multiple_jobs: `str`<a id="multiple_jobs-str"></a>

See federal W-4 instructions.

##### dependents_amount: `str`<a id="dependents_amount-str"></a>

See federal W-4 instructions.

##### other_income: `str`<a id="other_income-str"></a>

See federal W-4 instructions.

##### deductions_amount: `str`<a id="deductions_amount-str"></a>

See federal W-4 instructions.

##### extra_withholding_amount: `str`<a id="extra_withholding_amount-str"></a>

Additional tax you want withheld each pay period.

##### taxes_withheld: `str`<a id="taxes_withheld-str"></a>

Should federal taxes be withheld.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WorkerFederalTaxResource`](./paychex_python_sdk/type/worker_federal_tax_resource.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WorkerFederalTaxResource`](./paychex_python_sdk/pydantic/worker_federal_tax_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/federaltax` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.update_pay_component`<a id="paychexworkerupdate_pay_component"></a>

 Update a single pay component associated to the "Active" worker.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_pay_component_response = paychex.worker.update_pay_component(
    worker_id="workerId_example",
    worker_component_id="workerComponentId_example",
    worker_component_id="970000223656831",
    component_id="970000180599325",
    name="Deduction - 1",
    calculation_type="00H2A1IUJE7MXV6TQ37U",
    calculation_base_id="00H2A1IUJE7MXV6TQ37U",
    value=5,
    start_date="2018-03-01T00:00:00Z",
    effective_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
    effect_on_pay="REDUCTION",
    classification_type="string_example",
    frequency={
        "applied": "BY_PAY_PERIOD",
        "occurrence": "QUARTERLY",
        "effected_checks": "EVERY_CHECK",
    },
    links=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### worker_component_id: `str`<a id="worker_component_id-str"></a>

The id of a single pay component that a workers has.

##### requestBody: [`RecurringResource`](./paychex_python_sdk/type/recurring_resource.py)<a id="requestbody-recurringresourcepaychex_python_sdktyperecurring_resourcepy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`RecurringResource`](./paychex_python_sdk/pydantic/recurring_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/paycomponents/{workerComponentId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.update_pay_components`<a id="paychexworkerupdate_pay_components"></a>

Batch update pay components associated to the "Active" worker.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_pay_components_response = paychex.worker.update_pay_components(
    worker_id="workerId_example",
    worker_component_id="970000223656831",
    component_id="970000180599325",
    name="Deduction - 1",
    calculation_type="00H2A1IUJE7MXV6TQ37U",
    calculation_base_id="00H2A1IUJE7MXV6TQ37U",
    value=5,
    start_date="2018-03-01T00:00:00Z",
    effective_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
    effect_on_pay="REDUCTION",
    classification_type="string_example",
    frequency={
        "applied": "BY_PAY_PERIOD",
        "occurrence": "QUARTERLY",
        "effected_checks": "EVERY_CHECK",
    },
    links=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### worker_component_id: `str`<a id="worker_component_id-str"></a>

The id of a single pay component that a workers has.

##### component_id: `str`<a id="component_id-str"></a>

The unique identifier of the pay component. This data field cannot be PATCHED.

##### name: `str`<a id="name-str"></a>

Name of the pay component. This data field will be populated automatically based on componentId.

##### calculation_type: `str`<a id="calculation_type-str"></a>

The type of calculation that will be applied for the pay component .

##### calculation_base_id: `str`<a id="calculation_base_id-str"></a>

This is required if you are not using a FLAT_DOLLAR_AMOUNT Calculation Type.

##### value: `Union[int, float]`<a id="value-unionint-float"></a>

This is used to specify the value that is used against the calculationType.

##### start_date: `datetime`<a id="start_date-datetime"></a>

Date which this pay component will start to be applied during the payruns. This is an optional field that default to current datetime if not provided. This cannot be backdated but can be added to start in the future.

##### effective_date: `datetime`<a id="effective_date-datetime"></a>

Date which this pay component has started for the worker.

##### end_date: `datetime`<a id="end_date-datetime"></a>

Date which this pay component has ended for the worker.

##### effect_on_pay: `str`<a id="effect_on_pay-str"></a>

What the effect on pay will be (REDUCTION OR ADDITION), currently only reductions are available. This data field will be populated automatically based on componentId. This data field cannot be PATCHED

##### classification_type: `str`<a id="classification_type-str"></a>

The category that this component falls into.

##### frequency: [`PayComponentFrequencyTypeResource1`](./paychex_python_sdk/type/pay_component_frequency_type_resource1.py)<a id="frequency-paycomponentfrequencytyperesource1paychex_python_sdktypepay_component_frequency_type_resource1py"></a>


##### links: List[`Link`]<a id="links-listlink"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RecurringResource`](./paychex_python_sdk/type/recurring_resource.py)
#### 🔄 Return<a id="🔄-return"></a>

[`RecurringResource`](./paychex_python_sdk/pydantic/recurring_resource.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}/paycomponents` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paychex.worker.update_unique_worker`<a id="paychexworkerupdate_unique_worker"></a>

Update a unique worker (employee and contractor) that your application has been granted access to modify.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_unique_worker_response = paychex.worker.update_unique_worker(
    worker_id="workerId_example",
    worker_id="00Z5V9BTIHRQF2CF7BTH",
    employee_id="3052",
    worker_type="EMPLOYEE",
    employment_type="FULL_TIME",
    exemption_type="NON_EXEMPT",
    birth_date="1988-07-01T00:00:00Z",
    sex="MALE",
    ethnicity_code="string_example",
    hire_date="2015-06-15T00:00:00Z",
    clock_id="4321",
    name={
        "family_name": "JONES",
        "middle_name": "H",
        "given_name": "INDIANA",
        "preferred_name": "Indi",
        "qualification_affix_code": "Jr",
        "title_affix_code": "Dr",
    },
    legal_id={
        "legal_id_type": "SSN",
        "legal_id_value": "333221111",
    },
    labor_assignment_id="970001557863345",
    location_id="970001701620675",
    job_id="970001557916904",
    job={
        "title": "Archaeologist",
        "job_title_id": "00DWS906IMW2JSH8AQJ8",
    },
    organization={
        "organization_id": "1020022951957523",
        "name": "2 Division B",
        "number": "1",
    },
    supervisor={
        "worker_id": "00H2A1IUJ4IPERJ589YE",
    },
    current_status={
        "worker_status_id": "00DWS906IMW2JSH8AQJ9",
        "status_type": "ACTIVE",
        "status_reason": "HIRED",
        "effective_date": "2015-06-15T00:00:00Z",
    },
    communications=[
        {
            "type": "STREET_ADDRESS",
            "usage_type": "PERSONAL",
        }
    ],
    links=[
        {
        }
    ],
    worker_correlation_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### worker_id: `str`<a id="worker_id-str"></a>

ID associated with desired worker.

##### requestBody: [`WorkerResource1`](./paychex_python_sdk/type/worker_resource1.py)<a id="requestbody-workerresource1paychex_python_sdktypeworker_resource1py"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`WorkerResource1`](./paychex_python_sdk/pydantic/worker_resource1.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workers/{workerId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
