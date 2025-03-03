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

from paychex_python_sdk.model.custom_fields_dropdown_resource import CustomFieldsDropdownResource as CustomFieldsDropdownResourceSchema
from paychex_python_sdk.model.custom_fields_resource import CustomFieldsResource as CustomFieldsResourceSchema
from paychex_python_sdk.model.error_resource import ErrorResource as ErrorResourceSchema
from paychex_python_sdk.model.link import Link as LinkSchema

from paychex_python_sdk.type.link import Link
from paychex_python_sdk.type.custom_fields_resource import CustomFieldsResource
from paychex_python_sdk.type.custom_fields_dropdown_resource import CustomFieldsDropdownResource
from paychex_python_sdk.type.error_resource import ErrorResource

from ...api_client import Dictionary
from paychex_python_sdk.pydantic.custom_fields_resource import CustomFieldsResource as CustomFieldsResourcePydantic
from paychex_python_sdk.pydantic.error_resource import ErrorResource as ErrorResourcePydantic
from paychex_python_sdk.pydantic.link import Link as LinkPydantic
from paychex_python_sdk.pydantic.custom_fields_dropdown_resource import CustomFieldsDropdownResource as CustomFieldsDropdownResourcePydantic

from . import path

# Path params
CompanyIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'companyId': typing.Union[CompanyIdSchema, str, ],
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


request_path_company_id = api_client.PathParameter(
    name="companyId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CompanyIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = CustomFieldsResourceSchema
SchemaForRequestBodyApplicationVndPaychexCompanyCustomfieldsV1json = CustomFieldsResourceSchema


request_body_custom_fields_resource = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'application/vnd.paychex.company.customfields.v1+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationVndPaychexCompanyCustomfieldsV1json),
    },
    required=True,
)
SchemaFor201ResponseBodyApplicationJson = CustomFieldsResourceSchema
SchemaFor201ResponseBodyApplicationVndPaychexCompanyCustomfieldsV1json = CustomFieldsResourceSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: CustomFieldsResource


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: CustomFieldsResource


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
        'application/vnd.paychex.company.customfields.v1+json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationVndPaychexCompanyCustomfieldsV1json),
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
    '201': _response_for_201,
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
    'application/vnd.paychex.company.customfields.v1+json',
)


class BaseApi(api_client.Api):

    def _create_custom_field_at_company_level_mapped_args(
        self,
        company_id: str,
        custom_field_id: typing.Optional[str] = None,
        custom_field_name: typing.Optional[str] = None,
        category_id: typing.Optional[str] = None,
        required: typing.Optional[bool] = None,
        check_stub: typing.Optional[bool] = None,
        employee_editable: typing.Optional[bool] = None,
        type: typing.Optional[str] = None,
        boolean_value: typing.Optional[bool] = None,
        links: typing.Optional[typing.List[Link]] = None,
        date_value: typing.Optional[datetime] = None,
        text_value: typing.Optional[str] = None,
        max_text_length: typing.Optional[typing.Union[int, float]] = None,
        numeric_value: typing.Optional[typing.Union[int, float]] = None,
        dropdown: typing.Optional[typing.List[CustomFieldsDropdownResource]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if custom_field_id is not None:
            _body["customFieldId"] = custom_field_id
        if custom_field_name is not None:
            _body["customFieldName"] = custom_field_name
        if category_id is not None:
            _body["categoryId"] = category_id
        if required is not None:
            _body["required"] = required
        if check_stub is not None:
            _body["checkStub"] = check_stub
        if employee_editable is not None:
            _body["employeeEditable"] = employee_editable
        if type is not None:
            _body["type"] = type
        if boolean_value is not None:
            _body["booleanValue"] = boolean_value
        if links is not None:
            _body["links"] = links
        if date_value is not None:
            _body["dateValue"] = date_value
        if text_value is not None:
            _body["textValue"] = text_value
        if max_text_length is not None:
            _body["maxTextLength"] = max_text_length
        if numeric_value is not None:
            _body["numericValue"] = numeric_value
        if dropdown is not None:
            _body["dropdown"] = dropdown
        args.body = _body
        if company_id is not None:
            _path_params["companyId"] = company_id
        args.path = _path_params
        return args

    async def _acreate_custom_field_at_company_level_oapg(
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
        Custom Field
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_id,
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
            path_template='/companies/{companyId}/customfields',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_custom_fields_resource.serialize(body, content_type)
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


    def _create_custom_field_at_company_level_oapg(
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
        Custom Field
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_id,
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
            path_template='/companies/{companyId}/customfields',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_custom_fields_resource.serialize(body, content_type)
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


class CreateCustomFieldAtCompanyLevelRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_custom_field_at_company_level(
        self,
        company_id: str,
        custom_field_id: typing.Optional[str] = None,
        custom_field_name: typing.Optional[str] = None,
        category_id: typing.Optional[str] = None,
        required: typing.Optional[bool] = None,
        check_stub: typing.Optional[bool] = None,
        employee_editable: typing.Optional[bool] = None,
        type: typing.Optional[str] = None,
        boolean_value: typing.Optional[bool] = None,
        links: typing.Optional[typing.List[Link]] = None,
        date_value: typing.Optional[datetime] = None,
        text_value: typing.Optional[str] = None,
        max_text_length: typing.Optional[typing.Union[int, float]] = None,
        numeric_value: typing.Optional[typing.Union[int, float]] = None,
        dropdown: typing.Optional[typing.List[CustomFieldsDropdownResource]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_custom_field_at_company_level_mapped_args(
            company_id=company_id,
            custom_field_id=custom_field_id,
            custom_field_name=custom_field_name,
            category_id=category_id,
            required=required,
            check_stub=check_stub,
            employee_editable=employee_editable,
            type=type,
            boolean_value=boolean_value,
            links=links,
            date_value=date_value,
            text_value=text_value,
            max_text_length=max_text_length,
            numeric_value=numeric_value,
            dropdown=dropdown,
        )
        return await self._acreate_custom_field_at_company_level_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def create_custom_field_at_company_level(
        self,
        company_id: str,
        custom_field_id: typing.Optional[str] = None,
        custom_field_name: typing.Optional[str] = None,
        category_id: typing.Optional[str] = None,
        required: typing.Optional[bool] = None,
        check_stub: typing.Optional[bool] = None,
        employee_editable: typing.Optional[bool] = None,
        type: typing.Optional[str] = None,
        boolean_value: typing.Optional[bool] = None,
        links: typing.Optional[typing.List[Link]] = None,
        date_value: typing.Optional[datetime] = None,
        text_value: typing.Optional[str] = None,
        max_text_length: typing.Optional[typing.Union[int, float]] = None,
        numeric_value: typing.Optional[typing.Union[int, float]] = None,
        dropdown: typing.Optional[typing.List[CustomFieldsDropdownResource]] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_custom_field_at_company_level_mapped_args(
            company_id=company_id,
            custom_field_id=custom_field_id,
            custom_field_name=custom_field_name,
            category_id=category_id,
            required=required,
            check_stub=check_stub,
            employee_editable=employee_editable,
            type=type,
            boolean_value=boolean_value,
            links=links,
            date_value=date_value,
            text_value=text_value,
            max_text_length=max_text_length,
            numeric_value=numeric_value,
            dropdown=dropdown,
        )
        return self._create_custom_field_at_company_level_oapg(
            body=args.body,
            path_params=args.path,
        )

class CreateCustomFieldAtCompanyLevel(BaseApi):

    async def acreate_custom_field_at_company_level(
        self,
        company_id: str,
        custom_field_id: typing.Optional[str] = None,
        custom_field_name: typing.Optional[str] = None,
        category_id: typing.Optional[str] = None,
        required: typing.Optional[bool] = None,
        check_stub: typing.Optional[bool] = None,
        employee_editable: typing.Optional[bool] = None,
        type: typing.Optional[str] = None,
        boolean_value: typing.Optional[bool] = None,
        links: typing.Optional[typing.List[Link]] = None,
        date_value: typing.Optional[datetime] = None,
        text_value: typing.Optional[str] = None,
        max_text_length: typing.Optional[typing.Union[int, float]] = None,
        numeric_value: typing.Optional[typing.Union[int, float]] = None,
        dropdown: typing.Optional[typing.List[CustomFieldsDropdownResource]] = None,
        validate: bool = False,
        **kwargs,
    ) -> CustomFieldsResourcePydantic:
        raw_response = await self.raw.acreate_custom_field_at_company_level(
            company_id=company_id,
            custom_field_id=custom_field_id,
            custom_field_name=custom_field_name,
            category_id=category_id,
            required=required,
            check_stub=check_stub,
            employee_editable=employee_editable,
            type=type,
            boolean_value=boolean_value,
            links=links,
            date_value=date_value,
            text_value=text_value,
            max_text_length=max_text_length,
            numeric_value=numeric_value,
            dropdown=dropdown,
            **kwargs,
        )
        if validate:
            return CustomFieldsResourcePydantic(**raw_response.body)
        return api_client.construct_model_instance(CustomFieldsResourcePydantic, raw_response.body)
    
    
    def create_custom_field_at_company_level(
        self,
        company_id: str,
        custom_field_id: typing.Optional[str] = None,
        custom_field_name: typing.Optional[str] = None,
        category_id: typing.Optional[str] = None,
        required: typing.Optional[bool] = None,
        check_stub: typing.Optional[bool] = None,
        employee_editable: typing.Optional[bool] = None,
        type: typing.Optional[str] = None,
        boolean_value: typing.Optional[bool] = None,
        links: typing.Optional[typing.List[Link]] = None,
        date_value: typing.Optional[datetime] = None,
        text_value: typing.Optional[str] = None,
        max_text_length: typing.Optional[typing.Union[int, float]] = None,
        numeric_value: typing.Optional[typing.Union[int, float]] = None,
        dropdown: typing.Optional[typing.List[CustomFieldsDropdownResource]] = None,
        validate: bool = False,
    ) -> CustomFieldsResourcePydantic:
        raw_response = self.raw.create_custom_field_at_company_level(
            company_id=company_id,
            custom_field_id=custom_field_id,
            custom_field_name=custom_field_name,
            category_id=category_id,
            required=required,
            check_stub=check_stub,
            employee_editable=employee_editable,
            type=type,
            boolean_value=boolean_value,
            links=links,
            date_value=date_value,
            text_value=text_value,
            max_text_length=max_text_length,
            numeric_value=numeric_value,
            dropdown=dropdown,
        )
        if validate:
            return CustomFieldsResourcePydantic(**raw_response.body)
        return api_client.construct_model_instance(CustomFieldsResourcePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        company_id: str,
        custom_field_id: typing.Optional[str] = None,
        custom_field_name: typing.Optional[str] = None,
        category_id: typing.Optional[str] = None,
        required: typing.Optional[bool] = None,
        check_stub: typing.Optional[bool] = None,
        employee_editable: typing.Optional[bool] = None,
        type: typing.Optional[str] = None,
        boolean_value: typing.Optional[bool] = None,
        links: typing.Optional[typing.List[Link]] = None,
        date_value: typing.Optional[datetime] = None,
        text_value: typing.Optional[str] = None,
        max_text_length: typing.Optional[typing.Union[int, float]] = None,
        numeric_value: typing.Optional[typing.Union[int, float]] = None,
        dropdown: typing.Optional[typing.List[CustomFieldsDropdownResource]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_custom_field_at_company_level_mapped_args(
            company_id=company_id,
            custom_field_id=custom_field_id,
            custom_field_name=custom_field_name,
            category_id=category_id,
            required=required,
            check_stub=check_stub,
            employee_editable=employee_editable,
            type=type,
            boolean_value=boolean_value,
            links=links,
            date_value=date_value,
            text_value=text_value,
            max_text_length=max_text_length,
            numeric_value=numeric_value,
            dropdown=dropdown,
        )
        return await self._acreate_custom_field_at_company_level_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        company_id: str,
        custom_field_id: typing.Optional[str] = None,
        custom_field_name: typing.Optional[str] = None,
        category_id: typing.Optional[str] = None,
        required: typing.Optional[bool] = None,
        check_stub: typing.Optional[bool] = None,
        employee_editable: typing.Optional[bool] = None,
        type: typing.Optional[str] = None,
        boolean_value: typing.Optional[bool] = None,
        links: typing.Optional[typing.List[Link]] = None,
        date_value: typing.Optional[datetime] = None,
        text_value: typing.Optional[str] = None,
        max_text_length: typing.Optional[typing.Union[int, float]] = None,
        numeric_value: typing.Optional[typing.Union[int, float]] = None,
        dropdown: typing.Optional[typing.List[CustomFieldsDropdownResource]] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_custom_field_at_company_level_mapped_args(
            company_id=company_id,
            custom_field_id=custom_field_id,
            custom_field_name=custom_field_name,
            category_id=category_id,
            required=required,
            check_stub=check_stub,
            employee_editable=employee_editable,
            type=type,
            boolean_value=boolean_value,
            links=links,
            date_value=date_value,
            text_value=text_value,
            max_text_length=max_text_length,
            numeric_value=numeric_value,
            dropdown=dropdown,
        )
        return self._create_custom_field_at_company_level_oapg(
            body=args.body,
            path_params=args.path,
        )

