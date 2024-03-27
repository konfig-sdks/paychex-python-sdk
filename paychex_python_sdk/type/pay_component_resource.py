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

from paychex_python_sdk.type.link import Link
from paychex_python_sdk.type.pay_component_resource_applies_to_worker_types import PayComponentResourceAppliesToWorkerTypes

class RequiredPayComponentResource(TypedDict):
    pass

class OptionalPayComponentResource(TypedDict, total=False):
    # The description of the Pay Component.
    description: str

    # The unique identifier used to identify a pay component.
    componentId: str

    # The unique identifier associated for the pay component on this check.
    checkComponentId: str

    # The Paychex standard code number for the Pay Component, can be two digit.
    code: str

    # Name given to the pay component.
    name: str

    # The category that this component falls into.
    classificationType: str

    # The effect that the pay component will have on the check amount.
    effectOnPay: str

    # The date that the pay component is able to be applied on a check.
    startDate: datetime

    # The date that the pay component is not available to be applied on a check moving forward.
    endDate: datetime

    appliesToWorkerTypes: PayComponentResourceAppliesToWorkerTypes

    # This is used optionally for overriding a job when it needs to be different than the workers default. This option is only available when the client has job costing.
    jobId: str

    # This is used optionally for overriding a labor assignment when it needs to be different than the workers assignment distribution. This option is only available when the client has labor assignment.
    laborAssignmentId: str

    # Unique identifier for this workers pay rate **This ID will change if this is created for an IN_PROGRESS worker that is later completed within Flex**
    payRateId: str

    # The rate amount that will be applied for this component. Used in conjunction with Hours or Units.
    payRate: str

    # The number of hours that will be applied for this component. Used in conjunction with rate.
    payHours: str

    # The number of units that will be applied for this component. Used in conjunction with rate.
    payUnits: str

    # The flat amount to be applied for this component. Not used with Rate, Hours, or Units.
    payAmount: str

    # This is used optionally for specifying a date that the pay component was generated on.
    lineDate: datetime

    # This is used optionally for memoing the payHours or payUnits so that they are informational when using a payAmount.
    memoed: bool

    links: typing.List[Link]

class PayComponentResource(RequiredPayComponentResource, OptionalPayComponentResource):
    pass
