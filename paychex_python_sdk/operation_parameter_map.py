operation_parameter_map = {
    '/auth/oauth/v2/token-POST': {
        'parameters': [
            {
                'name': 'grant_type'
            },
            {
                'name': 'client_id'
            },
            {
                'name': 'client_secret'
            },
        ]
    },
    '/companies/{companyId}/workers-POST': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'workerId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'workerType'
            },
            {
                'name': 'employmentType'
            },
            {
                'name': 'exemptionType'
            },
            {
                'name': 'birthDate'
            },
            {
                'name': 'sex'
            },
            {
                'name': 'ethnicityCode'
            },
            {
                'name': 'hireDate'
            },
            {
                'name': 'clockId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'legalId'
            },
            {
                'name': 'laborAssignmentId'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'locationId'
            },
            {
                'name': 'job'
            },
            {
                'name': 'organization'
            },
            {
                'name': 'supervisor'
            },
            {
                'name': 'currentStatus'
            },
            {
                'name': 'communications'
            },
            {
                'name': 'workerCorrelationId'
            },
        ]
    },
    '/companies/{companyId}/jobs-POST': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'jobCorrelationId'
            },
            {
                'name': 'jobName'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'links'
            },
            {
                'name': 'jobNumber'
            },
        ]
    },
    '/companies/{companyId}/customfields-POST': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'customFieldId'
            },
            {
                'name': 'customFieldName'
            },
            {
                'name': 'categoryId'
            },
            {
                'name': 'required'
            },
            {
                'name': 'checkStub'
            },
            {
                'name': 'employeeEditable'
            },
            {
                'name': 'type'
            },
            {
                'name': 'booleanValue'
            },
            {
                'name': 'links'
            },
            {
                'name': 'dateValue'
            },
            {
                'name': 'textValue'
            },
            {
                'name': 'maxTextLength'
            },
            {
                'name': 'numericValue'
            },
            {
                'name': 'dropdown'
            },
        ]
    },
    '/companies/{companyId}/customfieldscategories-POST': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'categoryId'
            },
            {
                'name': 'categoryName'
            },
            {
                'name': 'links'
            },
        ]
    },
    '/companies/{companyId}/customfields/{customfieldid}-DELETE': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'customfieldid'
            },
        ]
    },
    '/companies/{companyId}/customfieldscategories/{categoryid}-DELETE': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'categoryid'
            },
        ]
    },
    '/companies/{companyId}/calculationbases-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
        ]
    },
    '/companies/{companyId}/contacttypes-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
        ]
    },
    '/companies/{companyId}/customfields/{customFieldId}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'customFieldId'
            },
        ]
    },
    '/companies/{companyId}/customfieldscategories-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
        ]
    },
    '/companies/{companyId}/customfields-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
        ]
    },
    '/companies/{companyId}/customfieldscategories/{categoryId}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'categoryId'
            },
        ]
    },
    '/companies/{companyId}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
        ]
    },
    '/companies/{companyId}/jobs/{jobId}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'asof'
            },
        ]
    },
    '/companies/{companyId}/jobsegments-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
        ]
    },
    '/companies/{companyId}/jobtitles/{jobTitleId}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'workerJobTitleId'
            },
        ]
    },
    '/companies/{companyId}/jobs-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'asof'
            },
        ]
    },
    '/companies/{companyId}/laborassignments/{laborAssignmentId}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'laborAssignmentId'
            },
            {
                'name': 'asof'
            },
        ]
    },
    '/companies/{companyId}/locations/{locationId}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'locationId'
            },
            {
                'name': 'asof'
            },
        ]
    },
    '/companies/{companyId}/locations-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'asof'
            },
        ]
    },
    '/companies/{companyId}/organizations/{orgId}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'organizationId'
            },
        ]
    },
    '/companies/{companyId}/organizations-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
        ]
    },
    '/companies/{companyId}/payfrequencies-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'payfrequency'
            },
        ]
    },
    '/companies/{companyId}/workerstatuses/{statusId}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'workerStatusId'
            },
        ]
    },
    '/companies/{companyId}/workers-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'givenname'
            },
            {
                'name': 'familyname'
            },
            {
                'name': 'legallastfour'
            },
            {
                'name': 'employeeid'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'locationid'
            },
        ]
    },
    '/companies-GET': {
        'parameters': [
            {
                'name': 'displayid'
            },
        ]
    },
    '/companies/{companyId}/jobtitles-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
        ]
    },
    '/companies/{companyId}/laborassignments-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'asof'
            },
        ]
    },
    '/companies/{companyId}/workerstatuses-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
        ]
    },
    '/companies/{companyId}/customfields/{customfieldid}-PATCH': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'customfieldid'
            },
            {
                'name': 'customFieldId'
            },
            {
                'name': 'customFieldName'
            },
            {
                'name': 'categoryId'
            },
            {
                'name': 'required'
            },
            {
                'name': 'checkStub'
            },
            {
                'name': 'employeeEditable'
            },
            {
                'name': 'type'
            },
            {
                'name': 'booleanValue'
            },
            {
                'name': 'links'
            },
            {
                'name': 'dateValue'
            },
            {
                'name': 'textValue'
            },
            {
                'name': 'maxTextLength'
            },
            {
                'name': 'numericValue'
            },
            {
                'name': 'dropdown'
            },
        ]
    },
    '/companies/{companyId}/customfieldscategories/{categoryid}-PATCH': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'categoryid'
            },
            {
                'name': 'categoryId'
            },
            {
                'name': 'categoryName'
            },
            {
                'name': 'links'
            },
        ]
    },
    '/companies/{companyId}/jobs/{jobId}-PATCH': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'jobCorrelationId'
            },
            {
                'name': 'jobName'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'links'
            },
            {
                'name': 'jobNumber'
            },
        ]
    },
    '/management/requestclientaccess-POST': {
        'parameters': [
            {
                'name': 'displayId'
            },
        ]
    },
    '/companies/{companyId}/checks-POST': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'workerId'
            },
            {
                'name': 'paycheckId'
            },
            {
                'name': 'payPeriodId'
            },
            {
                'name': 'checkCorrelationId'
            },
            {
                'name': 'blockAutoDistribution'
            },
            {
                'name': 'earnings'
            },
            {
                'name': 'deductions'
            },
            {
                'name': 'checkDate'
            },
            {
                'name': 'informational'
            },
            {
                'name': 'taxes'
            },
            {
                'name': 'links'
            },
        ]
    },
    '/checks/{checkId}/checkcomponents-POST': {
        'parameters': [
            {
                'name': 'checkId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'componentId'
            },
            {
                'name': 'checkComponentId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'classificationType'
            },
            {
                'name': 'effectOnPay'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'appliesToWorkerTypes'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'laborAssignmentId'
            },
            {
                'name': 'payRateId'
            },
            {
                'name': 'payRate'
            },
            {
                'name': 'payHours'
            },
            {
                'name': 'payUnits'
            },
            {
                'name': 'payAmount'
            },
            {
                'name': 'memoed'
            },
            {
                'name': 'lineDate'
            },
        ]
    },
    '/workers/{workerId}/checks-POST': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'workerId'
            },
            {
                'name': 'paycheckId'
            },
            {
                'name': 'payPeriodId'
            },
            {
                'name': 'checkCorrelationId'
            },
            {
                'name': 'blockAutoDistribution'
            },
            {
                'name': 'earnings'
            },
            {
                'name': 'deductions'
            },
            {
                'name': 'informational'
            },
            {
                'name': 'taxes'
            },
        ]
    },
    '/checks-DELETE': {
        'parameters': [
            {
                'name': 'payperiodid'
            },
            {
                'name': 'deletebyuserid'
            },
        ]
    },
    '/companies/{companyId}/checks-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'payperiodid'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'filterbyuserid'
            },
        ]
    },
    '/companies/{companyId}/paycomponents/{paycomponentId}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'paycomponentId'
            },
            {
                'name': 'asof'
            },
        ]
    },
    '/companies/{companyId}/paycomponents-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'effectonpay'
            },
            {
                'name': 'asof'
            },
            {
                'name': 'classificationtype'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/companies/{companyId}/payperiods-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'status'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
        ]
    },
    '/companies/{companyId}/payperiods/{payperiodId}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'payperiodId'
            },
        ]
    },
    '/workers/{workerId}/checks/{externalCheckId}-GET': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'paycheckId'
            },
        ]
    },
    '/workers/{workerId}/checks-GET': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'payperiodid'
            },
            {
                'name': 'filterbyuserid'
            },
        ]
    },
    '/checks/{checkId}/checkcomponents/{checkComponentId}-DELETE': {
        'parameters': [
            {
                'name': 'checkId'
            },
            {
                'name': 'checkComponentId'
            },
        ]
    },
    '/workers/{workerId}/checks/{externalCheckId}-DELETE': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'paycheckId'
            },
        ]
    },
    '/checks/{checkId}/checkcomponents/{checkComponentId}-PATCH': {
        'parameters': [
            {
                'name': 'checkId'
            },
            {
                'name': 'checkComponentId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'componentId'
            },
            {
                'name': 'checkComponentId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'classificationType'
            },
            {
                'name': 'effectOnPay'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'appliesToWorkerTypes'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'laborAssignmentId'
            },
            {
                'name': 'payRateId'
            },
            {
                'name': 'payRate'
            },
            {
                'name': 'payHours'
            },
            {
                'name': 'payUnits'
            },
            {
                'name': 'payAmount'
            },
            {
                'name': 'memoed'
            },
            {
                'name': 'lineDate'
            },
        ]
    },
    '/management/hooks-POST': {
        'parameters': [
            {
                'name': 'uri'
            },
            {
                'name': 'authentication'
            },
            {
                'name': 'domains'
            },
            {
                'name': 'hookId'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'links'
            },
        ]
    },
    '/management/hooks/{hookId}-DELETE': {
        'parameters': [
            {
                'name': 'hookId'
            },
        ]
    },
    '/management/domains-GET': {
        'parameters': [
        ]
    },
    '/management/hooks/{hookId}-GET': {
        'parameters': [
            {
                'name': 'hookId'
            },
        ]
    },
    '/management/hooks-GET': {
        'parameters': [
        ]
    },
    '/workers/{workerId}/communications-POST': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'communicationId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'usageType'
            },
            {
                'name': 'dialCountry'
            },
            {
                'name': 'dialArea'
            },
            {
                'name': 'dialNumber'
            },
            {
                'name': 'dialExtension'
            },
            {
                'name': 'uri'
            },
            {
                'name': 'streetLineOne'
            },
            {
                'name': 'streetLineTwo'
            },
            {
                'name': 'postOfficeBox'
            },
            {
                'name': 'city'
            },
            {
                'name': 'postalCode'
            },
            {
                'name': 'postalCodeExtension'
            },
            {
                'name': 'countrySubdivisionCode'
            },
            {
                'name': 'countryCode'
            },
            {
                'name': 'links'
            },
        ]
    },
    '/workers/{workerId}/directdeposits-POST': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'directDepositId'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'paymentType'
            },
            {
                'name': 'accountType'
            },
            {
                'name': 'value'
            },
            {
                'name': 'routingNumber'
            },
            {
                'name': 'accountNumber'
            },
            {
                'name': 'priority'
            },
            {
                'name': 'links'
            },
        ]
    },
    '/workers/{workerId}/federaltax-POST': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'taxId'
            },
            {
                'name': 'filingStatus'
            },
            {
                'name': 'multipleJobs'
            },
            {
                'name': 'dependentsAmount'
            },
            {
                'name': 'otherIncome'
            },
            {
                'name': 'deductionsAmount'
            },
            {
                'name': 'extraWithholdingAmount'
            },
            {
                'name': 'taxesWithheld'
            },
        ]
    },
    '/workers/{workerId}/paycomponents-POST': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'workerComponentId'
            },
            {
                'name': 'componentId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'calculationType'
            },
            {
                'name': 'calculationBaseId'
            },
            {
                'name': 'value'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'effectOnPay'
            },
            {
                'name': 'classificationType'
            },
            {
                'name': 'frequency'
            },
            {
                'name': 'links'
            },
        ]
    },
    '/workers/{workerId}/compensation/payrates-POST': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'rateId'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'rateNumber'
            },
            {
                'name': 'rateType'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'standardHours'
            },
            {
                'name': 'standardOvertime'
            },
            {
                'name': 'default'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'links'
            },
        ]
    },
    '/workers/{workerId}/contacts-POST': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'contactId'
            },
            {
                'name': 'contactType'
            },
            {
                'name': 'relationship'
            },
        ]
    },
    '/workers/{workerId}/customfields-POST': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'workerCustomFieldId'
            },
            {
                'name': 'customFieldId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'booleanValue'
            },
            {
                'name': 'textValue'
            },
            {
                'name': 'numericValue'
            },
            {
                'name': 'dateValue'
            },
            {
                'name': 'dropdownId'
            },
            {
                'name': 'dropdownValue'
            },
            {
                'name': 'customFieldName'
            },
            {
                'name': 'required'
            },
            {
                'name': 'checkStub'
            },
            {
                'name': 'employeeEditable'
            },
        ]
    },
    '/workers/{workerId}/contacts/{contactId}-DELETE': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'contactId'
            },
        ]
    },
    '/workers/{workerId}/customfields/{workerCustomFieldId}-DELETE': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'workerCustomFieldId'
            },
        ]
    },
    '/workers/{workerId}-DELETE': {
        'parameters': [
            {
                'name': 'workerId'
            },
        ]
    },
    '/workers/{workerId}/communications/{communicationId}-GET': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'communicationId'
            },
        ]
    },
    '/workers/{workerId}/communications-GET': {
        'parameters': [
            {
                'name': 'workerId'
            },
        ]
    },
    '/workers/{workerId}/compensation-GET': {
        'parameters': [
            {
                'name': 'workerId'
            },
        ]
    },
    '/workers/{workerId}/contacts/{contactId}-GET': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'contactId'
            },
        ]
    },
    '/workers/{workerId}/contacts-GET': {
        'parameters': [
            {
                'name': 'workerId'
            },
        ]
    },
    '/workers/{workerId}/customfields/{workerCustomFieldId}-GET': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'workerCustomFieldId'
            },
            {
                'name': 'asof'
            },
        ]
    },
    '/workers/{workerId}/customfields-GET': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'asof'
            },
        ]
    },
    '/workers/{workerId}/directdeposits/{directDepositId}-GET': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'directDepositId'
            },
            {
                'name': 'effectivitydate'
            },
        ]
    },
    '/workers/{workerId}/federaltax-GET': {
        'parameters': [
            {
                'name': 'workerId'
            },
        ]
    },
    '/workers/{workerId}-GET': {
        'parameters': [
            {
                'name': 'workerId'
            },
        ]
    },
    '/workers/{workerId}/paycomponents/{workerComponentId}-GET': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'workerComponentId'
            },
            {
                'name': 'asof'
            },
        ]
    },
    '/workers/{workerId}/paycomponents-GET': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'effectonpay'
            },
            {
                'name': 'asof'
            },
            {
                'name': 'name'
            },
            {
                'name': 'componentid'
            },
            {
                'name': 'classificationtype'
            },
        ]
    },
    '/workers/{workerId}/compensation/payrates/{rateId}-GET': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'rateId'
            },
            {
                'name': 'asof'
            },
        ]
    },
    '/workers/{workerId}/compensation/payrates-GET': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'asof'
            },
        ]
    },
    '/workers/{workerId}/compensation/paystandards-GET': {
        'parameters': [
            {
                'name': 'workerId'
            },
        ]
    },
    '/workers/{workerId}/timeoff-GET': {
        'parameters': [
            {
                'name': 'workerId'
            },
        ]
    },
    '/workers/{workerId}/status-GET': {
        'parameters': [
            {
                'name': 'workerId'
            },
        ]
    },
    '/workers/{workerId}/assignmentdistributions-GET': {
        'parameters': [
            {
                'name': 'workerId'
            },
        ]
    },
    '/workers/{workerId}/directdeposits-GET': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'effectivitydate'
            },
            {
                'name': 'asof'
            },
        ]
    },
    '/workers/{workerId}/communications/{communicationId}-DELETE': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'communicationId'
            },
        ]
    },
    '/workers/{workerId}/directdeposits/{directDepositId}-DELETE': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'directDepositId'
            },
            {
                'name': 'effectivitydate'
            },
        ]
    },
    '/workers/{workerId}/federaltax-DELETE': {
        'parameters': [
            {
                'name': 'workerId'
            },
        ]
    },
    '/workers/{workerId}/paycomponents/{workerComponentId}-DELETE': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'workerComponentId'
            },
        ]
    },
    '/workers/{workerId}/compensation/payrates/{rateId}-DELETE': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'rateId'
            },
        ]
    },
    '/workers/{workerId}/communications/{communicationId}-PATCH': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'communicationId'
            },
            {
                'name': 'communicationId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'usageType'
            },
            {
                'name': 'dialCountry'
            },
            {
                'name': 'dialArea'
            },
            {
                'name': 'dialNumber'
            },
            {
                'name': 'dialExtension'
            },
            {
                'name': 'uri'
            },
            {
                'name': 'streetLineOne'
            },
            {
                'name': 'streetLineTwo'
            },
            {
                'name': 'postOfficeBox'
            },
            {
                'name': 'city'
            },
            {
                'name': 'postalCode'
            },
            {
                'name': 'postalCodeExtension'
            },
            {
                'name': 'countrySubdivisionCode'
            },
            {
                'name': 'countryCode'
            },
            {
                'name': 'links'
            },
        ]
    },
    '/workers/{workerId}/compensation/payrates/{rateId}-PATCH': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'rateId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'rateId'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'rateNumber'
            },
            {
                'name': 'rateType'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'standardHours'
            },
            {
                'name': 'standardOvertime'
            },
            {
                'name': 'default'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'links'
            },
        ]
    },
    '/workers/{workerId}/contacts/{contactId}-PATCH': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'contactId'
            },
            {
                'name': 'contactId'
            },
            {
                'name': 'contactType'
            },
            {
                'name': 'relationship'
            },
        ]
    },
    '/workers/{workerId}/customfields/{workerCustomFieldId}-PATCH': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'workerCustomFieldId'
            },
            {
                'name': 'workerCustomFieldId'
            },
            {
                'name': 'customFieldId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'booleanValue'
            },
            {
                'name': 'textValue'
            },
            {
                'name': 'numericValue'
            },
            {
                'name': 'dateValue'
            },
            {
                'name': 'dropdownId'
            },
            {
                'name': 'dropdownValue'
            },
            {
                'name': 'customFieldName'
            },
            {
                'name': 'required'
            },
            {
                'name': 'checkStub'
            },
            {
                'name': 'employeeEditable'
            },
        ]
    },
    '/workers/{workerId}/directdeposits/{directDepositId}-PATCH': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'directDepositId'
            },
            {
                'name': 'directDepositId'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'paymentType'
            },
            {
                'name': 'accountType'
            },
            {
                'name': 'value'
            },
            {
                'name': 'routingNumber'
            },
            {
                'name': 'accountNumber'
            },
            {
                'name': 'priority'
            },
            {
                'name': 'links'
            },
            {
                'name': 'effectivitydate'
            },
        ]
    },
    '/workers/{workerId}/directdeposits-PATCH': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'directDepositId'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'paymentType'
            },
            {
                'name': 'accountType'
            },
            {
                'name': 'value'
            },
            {
                'name': 'routingNumber'
            },
            {
                'name': 'accountNumber'
            },
            {
                'name': 'priority'
            },
            {
                'name': 'links'
            },
            {
                'name': 'effectivitydate'
            },
        ]
    },
    '/workers/{workerId}/federaltax-PATCH': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'taxId'
            },
            {
                'name': 'filingStatus'
            },
            {
                'name': 'multipleJobs'
            },
            {
                'name': 'dependentsAmount'
            },
            {
                'name': 'otherIncome'
            },
            {
                'name': 'deductionsAmount'
            },
            {
                'name': 'extraWithholdingAmount'
            },
            {
                'name': 'taxesWithheld'
            },
        ]
    },
    '/workers/{workerId}/paycomponents/{workerComponentId}-PATCH': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'workerComponentId'
            },
            {
                'name': 'workerComponentId'
            },
            {
                'name': 'componentId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'calculationType'
            },
            {
                'name': 'calculationBaseId'
            },
            {
                'name': 'value'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'effectOnPay'
            },
            {
                'name': 'classificationType'
            },
            {
                'name': 'frequency'
            },
            {
                'name': 'links'
            },
        ]
    },
    '/workers/{workerId}/paycomponents-PATCH': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'workerComponentId'
            },
            {
                'name': 'componentId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'calculationType'
            },
            {
                'name': 'calculationBaseId'
            },
            {
                'name': 'value'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'effectOnPay'
            },
            {
                'name': 'classificationType'
            },
            {
                'name': 'frequency'
            },
            {
                'name': 'links'
            },
        ]
    },
    '/workers/{workerId}-PATCH': {
        'parameters': [
            {
                'name': 'workerId'
            },
            {
                'name': 'workerId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'workerType'
            },
            {
                'name': 'employmentType'
            },
            {
                'name': 'exemptionType'
            },
            {
                'name': 'birthDate'
            },
            {
                'name': 'sex'
            },
            {
                'name': 'ethnicityCode'
            },
            {
                'name': 'hireDate'
            },
            {
                'name': 'clockId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'legalId'
            },
            {
                'name': 'laborAssignmentId'
            },
            {
                'name': 'locationId'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'job'
            },
            {
                'name': 'organization'
            },
            {
                'name': 'supervisor'
            },
            {
                'name': 'currentStatus'
            },
            {
                'name': 'communications'
            },
            {
                'name': 'links'
            },
            {
                'name': 'workerCorrelationId'
            },
        ]
    },
};