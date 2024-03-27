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

from paychex_python_sdk.model.pay_component_frequency_type_resource1 import PayComponentFrequencyTypeResource1 as PayComponentFrequencyTypeResource1Schema
from paychex_python_sdk.model.recurring_resource import RecurringResource as RecurringResourceSchema
from paychex_python_sdk.model.error_resource import ErrorResource as ErrorResourceSchema
from paychex_python_sdk.model.link import Link as LinkSchema

from paychex_python_sdk.type.link import Link
from paychex_python_sdk.type.recurring_resource import RecurringResource
from paychex_python_sdk.type.pay_component_frequency_type_resource1 import PayComponentFrequencyTypeResource1
from paychex_python_sdk.type.error_resource import ErrorResource

from ...api_client import Dictionary
from paychex_python_sdk.pydantic.error_resource import ErrorResource as ErrorResourcePydantic
from paychex_python_sdk.pydantic.link import Link as LinkPydantic
from paychex_python_sdk.pydantic.recurring_resource import RecurringResource as RecurringResourcePydantic
from paychex_python_sdk.pydantic.pay_component_frequency_type_resource1 import PayComponentFrequencyTypeResource1 as PayComponentFrequencyTypeResource1Pydantic

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
SchemaForRequestBodyApplicationJson = RecurringResourceSchema
SchemaForRequestBodyApplicationVndPaychexPayrollPaycomponentsV1json = RecurringResourceSchema


request_body_recurring_resource = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'application/vnd.paychex.payroll.paycomponents.v1+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationVndPaychexPayrollPaycomponentsV1json),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = RecurringResourceSchema
SchemaFor200ResponseBodyApplicationVndPaychexPayrollPaycomponentsV1json = RecurringResourceSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: RecurringResource


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: RecurringResource


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
        'application/vnd.paychex.payroll.paycomponents.v1+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndPaychexPayrollPaycomponentsV1json),
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
SchemaFor415ResponseBodyApplicationJson = ErrorResourceSchema


@dataclass
class ApiResponseFor415(api_client.ApiResponse):
    body: ErrorResource


@dataclass
class ApiResponseFor415Async(api_client.AsyncApiResponse):
    body: ErrorResource


_response_for_415 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor415,
    response_cls_async=ApiResponseFor415Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor415ResponseBodyApplicationJson),
    },
)
SchemaFor423ResponseBodyApplicationJson = ErrorResourceSchema


@dataclass
class ApiResponseFor423(api_client.ApiResponse):
    body: ErrorResource


@dataclass
class ApiResponseFor423Async(api_client.AsyncApiResponse):
    body: ErrorResource


_response_for_423 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor423,
    response_cls_async=ApiResponseFor423Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor423ResponseBodyApplicationJson),
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
_all_accept_content_types = (
    'application/json',
    'application/vnd.paychex.payroll.paycomponents.v1+json',
)


class BaseApi(api_client.Api):

    def _update_pay_components_mapped_args(
        self,
        worker_id: str,
        worker_component_id: typing.Optional[str] = None,
        component_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        calculation_type: typing.Optional[str] = None,
        calculation_base_id: typing.Optional[str] = None,
        value: typing.Optional[typing.Union[int, float]] = None,
        start_date: typing.Optional[datetime] = None,
        effective_date: typing.Optional[datetime] = None,
        end_date: typing.Optional[datetime] = None,
        effect_on_pay: typing.Optional[str] = None,
        classification_type: typing.Optional[str] = None,
        frequency: typing.Optional[PayComponentFrequencyTypeResource1] = None,
        links: typing.Optional[typing.List[Link]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if worker_component_id is not None:
            _body["workerComponentId"] = worker_component_id
        if component_id is not None:
            _body["componentId"] = component_id
        if name is not None:
            _body["name"] = name
        if calculation_type is not None:
            _body["calculationType"] = calculation_type
        if calculation_base_id is not None:
            _body["calculationBaseId"] = calculation_base_id
        if value is not None:
            _body["value"] = value
        if start_date is not None:
            _body["startDate"] = start_date
        if effective_date is not None:
            _body["effectiveDate"] = effective_date
        if end_date is not None:
            _body["endDate"] = end_date
        if effect_on_pay is not None:
            _body["effectOnPay"] = effect_on_pay
        if classification_type is not None:
            _body["classificationType"] = classification_type
        if frequency is not None:
            _body["frequency"] = frequency
        if links is not None:
            _body["links"] = links
        args.body = _body
        if worker_id is not None:
            _path_params["workerId"] = worker_id
        args.path = _path_params
        return args

    async def _aupdate_pay_components_oapg(
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
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Worker Pay Components
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
        method = 'patch'.upper()
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
            path_template='/workers/{workerId}/paycomponents',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_recurring_resource.serialize(body, content_type)
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


    def _update_pay_components_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Worker Pay Components
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
        method = 'patch'.upper()
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
            path_template='/workers/{workerId}/paycomponents',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_recurring_resource.serialize(body, content_type)
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


class UpdatePayComponentsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_pay_components(
        self,
        worker_id: str,
        worker_component_id: typing.Optional[str] = None,
        component_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        calculation_type: typing.Optional[str] = None,
        calculation_base_id: typing.Optional[str] = None,
        value: typing.Optional[typing.Union[int, float]] = None,
        start_date: typing.Optional[datetime] = None,
        effective_date: typing.Optional[datetime] = None,
        end_date: typing.Optional[datetime] = None,
        effect_on_pay: typing.Optional[str] = None,
        classification_type: typing.Optional[str] = None,
        frequency: typing.Optional[PayComponentFrequencyTypeResource1] = None,
        links: typing.Optional[typing.List[Link]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_pay_components_mapped_args(
            worker_id=worker_id,
            worker_component_id=worker_component_id,
            component_id=component_id,
            name=name,
            calculation_type=calculation_type,
            calculation_base_id=calculation_base_id,
            value=value,
            start_date=start_date,
            effective_date=effective_date,
            end_date=end_date,
            effect_on_pay=effect_on_pay,
            classification_type=classification_type,
            frequency=frequency,
            links=links,
        )
        return await self._aupdate_pay_components_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_pay_components(
        self,
        worker_id: str,
        worker_component_id: typing.Optional[str] = None,
        component_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        calculation_type: typing.Optional[str] = None,
        calculation_base_id: typing.Optional[str] = None,
        value: typing.Optional[typing.Union[int, float]] = None,
        start_date: typing.Optional[datetime] = None,
        effective_date: typing.Optional[datetime] = None,
        end_date: typing.Optional[datetime] = None,
        effect_on_pay: typing.Optional[str] = None,
        classification_type: typing.Optional[str] = None,
        frequency: typing.Optional[PayComponentFrequencyTypeResource1] = None,
        links: typing.Optional[typing.List[Link]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_pay_components_mapped_args(
            worker_id=worker_id,
            worker_component_id=worker_component_id,
            component_id=component_id,
            name=name,
            calculation_type=calculation_type,
            calculation_base_id=calculation_base_id,
            value=value,
            start_date=start_date,
            effective_date=effective_date,
            end_date=end_date,
            effect_on_pay=effect_on_pay,
            classification_type=classification_type,
            frequency=frequency,
            links=links,
        )
        return self._update_pay_components_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdatePayComponents(BaseApi):

    async def aupdate_pay_components(
        self,
        worker_id: str,
        worker_component_id: typing.Optional[str] = None,
        component_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        calculation_type: typing.Optional[str] = None,
        calculation_base_id: typing.Optional[str] = None,
        value: typing.Optional[typing.Union[int, float]] = None,
        start_date: typing.Optional[datetime] = None,
        effective_date: typing.Optional[datetime] = None,
        end_date: typing.Optional[datetime] = None,
        effect_on_pay: typing.Optional[str] = None,
        classification_type: typing.Optional[str] = None,
        frequency: typing.Optional[PayComponentFrequencyTypeResource1] = None,
        links: typing.Optional[typing.List[Link]] = None,
        validate: bool = False,
        **kwargs,
    ) -> RecurringResourcePydantic:
        raw_response = await self.raw.aupdate_pay_components(
            worker_id=worker_id,
            worker_component_id=worker_component_id,
            component_id=component_id,
            name=name,
            calculation_type=calculation_type,
            calculation_base_id=calculation_base_id,
            value=value,
            start_date=start_date,
            effective_date=effective_date,
            end_date=end_date,
            effect_on_pay=effect_on_pay,
            classification_type=classification_type,
            frequency=frequency,
            links=links,
            **kwargs,
        )
        if validate:
            return RecurringResourcePydantic(**raw_response.body)
        return api_client.construct_model_instance(RecurringResourcePydantic, raw_response.body)
    
    
    def update_pay_components(
        self,
        worker_id: str,
        worker_component_id: typing.Optional[str] = None,
        component_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        calculation_type: typing.Optional[str] = None,
        calculation_base_id: typing.Optional[str] = None,
        value: typing.Optional[typing.Union[int, float]] = None,
        start_date: typing.Optional[datetime] = None,
        effective_date: typing.Optional[datetime] = None,
        end_date: typing.Optional[datetime] = None,
        effect_on_pay: typing.Optional[str] = None,
        classification_type: typing.Optional[str] = None,
        frequency: typing.Optional[PayComponentFrequencyTypeResource1] = None,
        links: typing.Optional[typing.List[Link]] = None,
        validate: bool = False,
    ) -> RecurringResourcePydantic:
        raw_response = self.raw.update_pay_components(
            worker_id=worker_id,
            worker_component_id=worker_component_id,
            component_id=component_id,
            name=name,
            calculation_type=calculation_type,
            calculation_base_id=calculation_base_id,
            value=value,
            start_date=start_date,
            effective_date=effective_date,
            end_date=end_date,
            effect_on_pay=effect_on_pay,
            classification_type=classification_type,
            frequency=frequency,
            links=links,
        )
        if validate:
            return RecurringResourcePydantic(**raw_response.body)
        return api_client.construct_model_instance(RecurringResourcePydantic, raw_response.body)


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        worker_id: str,
        worker_component_id: typing.Optional[str] = None,
        component_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        calculation_type: typing.Optional[str] = None,
        calculation_base_id: typing.Optional[str] = None,
        value: typing.Optional[typing.Union[int, float]] = None,
        start_date: typing.Optional[datetime] = None,
        effective_date: typing.Optional[datetime] = None,
        end_date: typing.Optional[datetime] = None,
        effect_on_pay: typing.Optional[str] = None,
        classification_type: typing.Optional[str] = None,
        frequency: typing.Optional[PayComponentFrequencyTypeResource1] = None,
        links: typing.Optional[typing.List[Link]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_pay_components_mapped_args(
            worker_id=worker_id,
            worker_component_id=worker_component_id,
            component_id=component_id,
            name=name,
            calculation_type=calculation_type,
            calculation_base_id=calculation_base_id,
            value=value,
            start_date=start_date,
            effective_date=effective_date,
            end_date=end_date,
            effect_on_pay=effect_on_pay,
            classification_type=classification_type,
            frequency=frequency,
            links=links,
        )
        return await self._aupdate_pay_components_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        worker_id: str,
        worker_component_id: typing.Optional[str] = None,
        component_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        calculation_type: typing.Optional[str] = None,
        calculation_base_id: typing.Optional[str] = None,
        value: typing.Optional[typing.Union[int, float]] = None,
        start_date: typing.Optional[datetime] = None,
        effective_date: typing.Optional[datetime] = None,
        end_date: typing.Optional[datetime] = None,
        effect_on_pay: typing.Optional[str] = None,
        classification_type: typing.Optional[str] = None,
        frequency: typing.Optional[PayComponentFrequencyTypeResource1] = None,
        links: typing.Optional[typing.List[Link]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_pay_components_mapped_args(
            worker_id=worker_id,
            worker_component_id=worker_component_id,
            component_id=component_id,
            name=name,
            calculation_type=calculation_type,
            calculation_base_id=calculation_base_id,
            value=value,
            start_date=start_date,
            effective_date=effective_date,
            end_date=end_date,
            effect_on_pay=effect_on_pay,
            classification_type=classification_type,
            frequency=frequency,
            links=links,
        )
        return self._update_pay_components_oapg(
            body=args.body,
            path_params=args.path,
        )

