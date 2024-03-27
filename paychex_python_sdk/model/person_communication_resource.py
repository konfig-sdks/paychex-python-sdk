# coding: utf-8

"""
    External API

      # Developer Resources  Refer [Developer Resources](https://developer.paychex.com/resources/overview/) for more details on API specification 

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

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


class PersonCommunicationResource(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The set of communications for this contact. Required for POST contacts.
    """


    class MetaOapg:
        
        class properties:
            
            
            class telecom(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TelecomResource']:
                        return TelecomResource
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['TelecomResource'], typing.List['TelecomResource']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'telecom':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TelecomResource':
                    return super().__getitem__(i)
            
            
            class postal(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PostalResource']:
                        return PostalResource
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['PostalResource'], typing.List['PostalResource']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'postal':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PostalResource':
                    return super().__getitem__(i)
            
            
            class email(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['EmailResource']:
                        return EmailResource
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['EmailResource'], typing.List['EmailResource']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'email':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'EmailResource':
                    return super().__getitem__(i)
            __annotations__ = {
                "telecom": telecom,
                "postal": postal,
                "email": email,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["telecom"]) -> MetaOapg.properties.telecom: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["postal"]) -> MetaOapg.properties.postal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["telecom", "postal", "email", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["telecom"]) -> typing.Union[MetaOapg.properties.telecom, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["postal"]) -> typing.Union[MetaOapg.properties.postal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["telecom", "postal", "email", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        telecom: typing.Union[MetaOapg.properties.telecom, list, tuple, schemas.Unset] = schemas.unset,
        postal: typing.Union[MetaOapg.properties.postal, list, tuple, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PersonCommunicationResource':
        return super().__new__(
            cls,
            *args,
            telecom=telecom,
            postal=postal,
            email=email,
            _configuration=_configuration,
            **kwargs,
        )

from paychex_python_sdk.model.email_resource import EmailResource
from paychex_python_sdk.model.postal_resource import PostalResource
from paychex_python_sdk.model.telecom_resource import TelecomResource
