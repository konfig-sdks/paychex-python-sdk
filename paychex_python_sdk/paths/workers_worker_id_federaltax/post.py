# coding: utf-8

"""
    External API

      # Developer Resources  Refer [Developer Resources](https://developer.paychex.com/resources/overview/) for more details on API specification 

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from paychex_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from paychex_python_sdk.api_response import AsyncGeneratorResponse
from paychex_python_sdk import api_client, exceptions
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

from paychex_python_sdk.model.worker_federal_tax_resource import WorkerFederalTaxResource as WorkerFederalTaxResourceSchema
from paychex_python_sdk.model.error_resource import ErrorResource as ErrorResourceSchema

from paychex_python_sdk.type.worker_federal_tax_resource import WorkerFederalTaxResource
from paychex_python_sdk.type.error_resource import ErrorResource

from ...api_client import Dictionary
from paychex_python_sdk.pydantic.error_resource import ErrorResource as ErrorResourcePydantic
from paychex_python_sdk.pydantic.worker_federal_tax_resource import WorkerFederalTaxResource as WorkerFederalTaxResourcePydantic

from . import path

# Path params
WorkerIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'workerId': typing.Union[WorkerIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_worker_id = api_client.PathParameter(
    name="workerId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=WorkerIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = WorkerFederalTaxResourceSchema
SchemaForRequestBodyApplicationVndPaychexWorkerFederaltax2020V1json = WorkerFederalTaxResourceSchema


request_body_worker_federal_tax_resource = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'application/vnd.paychex.worker.federaltax2020.v1+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationVndPaychexWorkerFederaltax2020V1json),
    },
    required=True,
)
SchemaFor201ResponseBodyApplicationVndPaychexWorkerFederaltax2020V1json = WorkerFederalTaxResourceSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: WorkerFederalTaxResource


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: WorkerFederalTaxResource


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/vnd.paychex.worker.federaltax2020.v1+json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationVndPaychexWorkerFederaltax2020V1json),
    },
)
SchemaFor400ResponseBodyApplicationJson = ErrorResourceSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: ErrorResource


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: ErrorResource


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = ErrorResourceSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: ErrorResource


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: ErrorResource


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = ErrorResourceSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: ErrorResource


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: ErrorResource


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '201': _response_for_201,
    '400': _response_for_400,
    '404': _response_for_404,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/vnd.paychex.worker.federaltax2020.v1+json',
    'application/json',
)


class BaseApi(api_client.Api):

    def _add_federal_tax_setup_mapped_args(
        self,
        worker_id: str,
        tax_id: typing.Optional[str] = None,
        filing_status: typing.Optional[str] = None,
        multiple_jobs: typing.Optional[str] = None,
        dependents_amount: typing.Optional[str] = None,
        other_income: typing.Optional[str] = None,
        deductions_amount: typing.Optional[str] = None,
        extra_withholding_amount: typing.Optional[str] = None,
        taxes_withheld: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if tax_id is not None:
            _body["taxId"] = tax_id
        if filing_status is not None:
            _body["filingStatus"] = filing_status
        if multiple_jobs is not None:
            _body["multipleJobs"] = multiple_jobs
        if dependents_amount is not None:
            _body["dependentsAmount"] = dependents_amount
        if other_income is not None:
            _body["otherIncome"] = other_income
        if deductions_amount is not None:
            _body["deductionsAmount"] = deductions_amount
        if extra_withholding_amount is not None:
            _body["extraWithholdingAmount"] = extra_withholding_amount
        if taxes_withheld is not None:
            _body["taxesWithheld"] = taxes_withheld
        args.body = _body
        if worker_id is not None:
            _path_params["workerId"] = worker_id
        args.path = _path_params
        return args

    async def _aadd_federal_tax_setup_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Worker Federal Tax
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_worker_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/workers/{workerId}/federaltax',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_worker_federal_tax_resource.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _add_federal_tax_setup_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Worker Federal Tax
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_worker_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/workers/{workerId}/federaltax',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_worker_federal_tax_resource.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class AddFederalTaxSetupRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aadd_federal_tax_setup(
        self,
        worker_id: str,
        tax_id: typing.Optional[str] = None,
        filing_status: typing.Optional[str] = None,
        multiple_jobs: typing.Optional[str] = None,
        dependents_amount: typing.Optional[str] = None,
        other_income: typing.Optional[str] = None,
        deductions_amount: typing.Optional[str] = None,
        extra_withholding_amount: typing.Optional[str] = None,
        taxes_withheld: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_federal_tax_setup_mapped_args(
            worker_id=worker_id,
            tax_id=tax_id,
            filing_status=filing_status,
            multiple_jobs=multiple_jobs,
            dependents_amount=dependents_amount,
            other_income=other_income,
            deductions_amount=deductions_amount,
            extra_withholding_amount=extra_withholding_amount,
            taxes_withheld=taxes_withheld,
        )
        return await self._aadd_federal_tax_setup_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def add_federal_tax_setup(
        self,
        worker_id: str,
        tax_id: typing.Optional[str] = None,
        filing_status: typing.Optional[str] = None,
        multiple_jobs: typing.Optional[str] = None,
        dependents_amount: typing.Optional[str] = None,
        other_income: typing.Optional[str] = None,
        deductions_amount: typing.Optional[str] = None,
        extra_withholding_amount: typing.Optional[str] = None,
        taxes_withheld: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_federal_tax_setup_mapped_args(
            worker_id=worker_id,
            tax_id=tax_id,
            filing_status=filing_status,
            multiple_jobs=multiple_jobs,
            dependents_amount=dependents_amount,
            other_income=other_income,
            deductions_amount=deductions_amount,
            extra_withholding_amount=extra_withholding_amount,
            taxes_withheld=taxes_withheld,
        )
        return self._add_federal_tax_setup_oapg(
            body=args.body,
            path_params=args.path,
        )

class AddFederalTaxSetup(BaseApi):

    async def aadd_federal_tax_setup(
        self,
        worker_id: str,
        tax_id: typing.Optional[str] = None,
        filing_status: typing.Optional[str] = None,
        multiple_jobs: typing.Optional[str] = None,
        dependents_amount: typing.Optional[str] = None,
        other_income: typing.Optional[str] = None,
        deductions_amount: typing.Optional[str] = None,
        extra_withholding_amount: typing.Optional[str] = None,
        taxes_withheld: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> WorkerFederalTaxResourcePydantic:
        raw_response = await self.raw.aadd_federal_tax_setup(
            worker_id=worker_id,
            tax_id=tax_id,
            filing_status=filing_status,
            multiple_jobs=multiple_jobs,
            dependents_amount=dependents_amount,
            other_income=other_income,
            deductions_amount=deductions_amount,
            extra_withholding_amount=extra_withholding_amount,
            taxes_withheld=taxes_withheld,
            **kwargs,
        )
        if validate:
            return WorkerFederalTaxResourcePydantic(**raw_response.body)
        return api_client.construct_model_instance(WorkerFederalTaxResourcePydantic, raw_response.body)
    
    
    def add_federal_tax_setup(
        self,
        worker_id: str,
        tax_id: typing.Optional[str] = None,
        filing_status: typing.Optional[str] = None,
        multiple_jobs: typing.Optional[str] = None,
        dependents_amount: typing.Optional[str] = None,
        other_income: typing.Optional[str] = None,
        deductions_amount: typing.Optional[str] = None,
        extra_withholding_amount: typing.Optional[str] = None,
        taxes_withheld: typing.Optional[str] = None,
        validate: bool = False,
    ) -> WorkerFederalTaxResourcePydantic:
        raw_response = self.raw.add_federal_tax_setup(
            worker_id=worker_id,
            tax_id=tax_id,
            filing_status=filing_status,
            multiple_jobs=multiple_jobs,
            dependents_amount=dependents_amount,
            other_income=other_income,
            deductions_amount=deductions_amount,
            extra_withholding_amount=extra_withholding_amount,
            taxes_withheld=taxes_withheld,
        )
        if validate:
            return WorkerFederalTaxResourcePydantic(**raw_response.body)
        return api_client.construct_model_instance(WorkerFederalTaxResourcePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        worker_id: str,
        tax_id: typing.Optional[str] = None,
        filing_status: typing.Optional[str] = None,
        multiple_jobs: typing.Optional[str] = None,
        dependents_amount: typing.Optional[str] = None,
        other_income: typing.Optional[str] = None,
        deductions_amount: typing.Optional[str] = None,
        extra_withholding_amount: typing.Optional[str] = None,
        taxes_withheld: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_federal_tax_setup_mapped_args(
            worker_id=worker_id,
            tax_id=tax_id,
            filing_status=filing_status,
            multiple_jobs=multiple_jobs,
            dependents_amount=dependents_amount,
            other_income=other_income,
            deductions_amount=deductions_amount,
            extra_withholding_amount=extra_withholding_amount,
            taxes_withheld=taxes_withheld,
        )
        return await self._aadd_federal_tax_setup_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        worker_id: str,
        tax_id: typing.Optional[str] = None,
        filing_status: typing.Optional[str] = None,
        multiple_jobs: typing.Optional[str] = None,
        dependents_amount: typing.Optional[str] = None,
        other_income: typing.Optional[str] = None,
        deductions_amount: typing.Optional[str] = None,
        extra_withholding_amount: typing.Optional[str] = None,
        taxes_withheld: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_federal_tax_setup_mapped_args(
            worker_id=worker_id,
            tax_id=tax_id,
            filing_status=filing_status,
            multiple_jobs=multiple_jobs,
            dependents_amount=dependents_amount,
            other_income=other_income,
            deductions_amount=deductions_amount,
            extra_withholding_amount=extra_withholding_amount,
            taxes_withheld=taxes_withheld,
        )
        return self._add_federal_tax_setup_oapg(
            body=args.body,
            path_params=args.path,
        )

