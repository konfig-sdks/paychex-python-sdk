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

from paychex_python_sdk.model.direct_deposit_resource import DirectDepositResource as DirectDepositResourceSchema
from paychex_python_sdk.model.error_resource import ErrorResource as ErrorResourceSchema

from paychex_python_sdk.type.direct_deposit_resource import DirectDepositResource
from paychex_python_sdk.type.error_resource import ErrorResource

from ...api_client import Dictionary
from paychex_python_sdk.pydantic.error_resource import ErrorResource as ErrorResourcePydantic
from paychex_python_sdk.pydantic.direct_deposit_resource import DirectDepositResource as DirectDepositResourcePydantic

from . import path

# Query params
EffectivitydateSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'effectivitydate': typing.Union[EffectivitydateSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_effectivitydate = api_client.QueryParameter(
    name="effectivitydate",
    style=api_client.ParameterStyle.FORM,
    schema=EffectivitydateSchema,
    explode=True,
)
# Path params
WorkerIdSchema = schemas.StrSchema
DirectDepositIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'workerId': typing.Union[WorkerIdSchema, str, ],
        'directDepositId': typing.Union[DirectDepositIdSchema, str, ],
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
request_path_direct_deposit_id = api_client.PathParameter(
    name="directDepositId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=DirectDepositIdSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = DirectDepositResourceSchema
SchemaFor200ResponseBodyApplicationVndPaychexPayrollDirectdepositV1json = DirectDepositResourceSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: DirectDepositResource


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: DirectDepositResource


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
        'application/vnd.paychex.payroll.directdeposit.v1+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndPaychexPayrollDirectdepositV1json),
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
SchemaFor401ResponseBodyApplicationJson = ErrorResourceSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: ErrorResource


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: ErrorResource


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = ErrorResourceSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: ErrorResource


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: ErrorResource


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
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
SchemaFor405ResponseBodyApplicationJson = ErrorResourceSchema


@dataclass
class ApiResponseFor405(api_client.ApiResponse):
    body: ErrorResource


@dataclass
class ApiResponseFor405Async(api_client.AsyncApiResponse):
    body: ErrorResource


_response_for_405 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor405,
    response_cls_async=ApiResponseFor405Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor405ResponseBodyApplicationJson),
    },
)
SchemaFor406ResponseBodyApplicationJson = ErrorResourceSchema


@dataclass
class ApiResponseFor406(api_client.ApiResponse):
    body: ErrorResource


@dataclass
class ApiResponseFor406Async(api_client.AsyncApiResponse):
    body: ErrorResource


_response_for_406 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor406,
    response_cls_async=ApiResponseFor406Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor406ResponseBodyApplicationJson),
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
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '404': _response_for_404,
    '405': _response_for_405,
    '406': _response_for_406,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
    'application/vnd.paychex.payroll.directdeposit.v1+json',
)


class BaseApi(api_client.Api):

    def _get_direct_deposit_mapped_args(
        self,
        worker_id: str,
        direct_deposit_id: str,
        effectivitydate: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if effectivitydate is not None:
            _query_params["effectivitydate"] = effectivitydate
        if worker_id is not None:
            _path_params["workerId"] = worker_id
        if direct_deposit_id is not None:
            _path_params["directDepositId"] = direct_deposit_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_direct_deposit_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Worker Direct Deposit
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_worker_id,
            request_path_direct_deposit_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_effectivitydate,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/workers/{workerId}/directdeposits/{directDepositId}',
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _get_direct_deposit_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Worker Direct Deposit
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_worker_id,
            request_path_direct_deposit_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_effectivitydate,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/workers/{workerId}/directdeposits/{directDepositId}',
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            prefix_separator_iterator=prefix_separator_iterator,
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


class GetDirectDepositRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_direct_deposit(
        self,
        worker_id: str,
        direct_deposit_id: str,
        effectivitydate: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_direct_deposit_mapped_args(
            worker_id=worker_id,
            direct_deposit_id=direct_deposit_id,
            effectivitydate=effectivitydate,
        )
        return await self._aget_direct_deposit_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_direct_deposit(
        self,
        worker_id: str,
        direct_deposit_id: str,
        effectivitydate: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_direct_deposit_mapped_args(
            worker_id=worker_id,
            direct_deposit_id=direct_deposit_id,
            effectivitydate=effectivitydate,
        )
        return self._get_direct_deposit_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetDirectDeposit(BaseApi):

    async def aget_direct_deposit(
        self,
        worker_id: str,
        direct_deposit_id: str,
        effectivitydate: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> DirectDepositResourcePydantic:
        raw_response = await self.raw.aget_direct_deposit(
            worker_id=worker_id,
            direct_deposit_id=direct_deposit_id,
            effectivitydate=effectivitydate,
            **kwargs,
        )
        if validate:
            return DirectDepositResourcePydantic(**raw_response.body)
        return api_client.construct_model_instance(DirectDepositResourcePydantic, raw_response.body)
    
    
    def get_direct_deposit(
        self,
        worker_id: str,
        direct_deposit_id: str,
        effectivitydate: typing.Optional[str] = None,
        validate: bool = False,
    ) -> DirectDepositResourcePydantic:
        raw_response = self.raw.get_direct_deposit(
            worker_id=worker_id,
            direct_deposit_id=direct_deposit_id,
            effectivitydate=effectivitydate,
        )
        if validate:
            return DirectDepositResourcePydantic(**raw_response.body)
        return api_client.construct_model_instance(DirectDepositResourcePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        worker_id: str,
        direct_deposit_id: str,
        effectivitydate: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_direct_deposit_mapped_args(
            worker_id=worker_id,
            direct_deposit_id=direct_deposit_id,
            effectivitydate=effectivitydate,
        )
        return await self._aget_direct_deposit_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        worker_id: str,
        direct_deposit_id: str,
        effectivitydate: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_direct_deposit_mapped_args(
            worker_id=worker_id,
            direct_deposit_id=direct_deposit_id,
            effectivitydate=effectivitydate,
        )
        return self._get_direct_deposit_oapg(
            query_params=args.query,
            path_params=args.path,
        )

