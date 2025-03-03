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


class ClientNameVersion(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            cnvId = schemas.Int64Schema
            cnvCltNm = schemas.StrSchema
            cnvVerStatCd = schemas.StrSchema
            cnvValStatCd = schemas.StrSchema
            cnvBegnEffDt = schemas.DateTimeSchema
            cnvEndEffDt = schemas.DateTimeSchema
            cnvModDt = schemas.DateTimeSchema
            cnvModByAppNm = schemas.StrSchema
            cnvModByAppUsrNm = schemas.StrSchema
            cnvModByAppSubNm = schemas.StrSchema
        
            @staticmethod
            def cltNmByCnId() -> typing.Type['ClientName']:
                return ClientName
            __annotations__ = {
                "cnvId": cnvId,
                "cnvCltNm": cnvCltNm,
                "cnvVerStatCd": cnvVerStatCd,
                "cnvValStatCd": cnvValStatCd,
                "cnvBegnEffDt": cnvBegnEffDt,
                "cnvEndEffDt": cnvEndEffDt,
                "cnvModDt": cnvModDt,
                "cnvModByAppNm": cnvModByAppNm,
                "cnvModByAppUsrNm": cnvModByAppUsrNm,
                "cnvModByAppSubNm": cnvModByAppSubNm,
                "cltNmByCnId": cltNmByCnId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cnvId"]) -> MetaOapg.properties.cnvId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cnvCltNm"]) -> MetaOapg.properties.cnvCltNm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cnvVerStatCd"]) -> MetaOapg.properties.cnvVerStatCd: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cnvValStatCd"]) -> MetaOapg.properties.cnvValStatCd: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cnvBegnEffDt"]) -> MetaOapg.properties.cnvBegnEffDt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cnvEndEffDt"]) -> MetaOapg.properties.cnvEndEffDt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cnvModDt"]) -> MetaOapg.properties.cnvModDt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cnvModByAppNm"]) -> MetaOapg.properties.cnvModByAppNm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cnvModByAppUsrNm"]) -> MetaOapg.properties.cnvModByAppUsrNm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cnvModByAppSubNm"]) -> MetaOapg.properties.cnvModByAppSubNm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cltNmByCnId"]) -> 'ClientName': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cnvId", "cnvCltNm", "cnvVerStatCd", "cnvValStatCd", "cnvBegnEffDt", "cnvEndEffDt", "cnvModDt", "cnvModByAppNm", "cnvModByAppUsrNm", "cnvModByAppSubNm", "cltNmByCnId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cnvId"]) -> typing.Union[MetaOapg.properties.cnvId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cnvCltNm"]) -> typing.Union[MetaOapg.properties.cnvCltNm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cnvVerStatCd"]) -> typing.Union[MetaOapg.properties.cnvVerStatCd, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cnvValStatCd"]) -> typing.Union[MetaOapg.properties.cnvValStatCd, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cnvBegnEffDt"]) -> typing.Union[MetaOapg.properties.cnvBegnEffDt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cnvEndEffDt"]) -> typing.Union[MetaOapg.properties.cnvEndEffDt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cnvModDt"]) -> typing.Union[MetaOapg.properties.cnvModDt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cnvModByAppNm"]) -> typing.Union[MetaOapg.properties.cnvModByAppNm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cnvModByAppUsrNm"]) -> typing.Union[MetaOapg.properties.cnvModByAppUsrNm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cnvModByAppSubNm"]) -> typing.Union[MetaOapg.properties.cnvModByAppSubNm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cltNmByCnId"]) -> typing.Union['ClientName', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cnvId", "cnvCltNm", "cnvVerStatCd", "cnvValStatCd", "cnvBegnEffDt", "cnvEndEffDt", "cnvModDt", "cnvModByAppNm", "cnvModByAppUsrNm", "cnvModByAppSubNm", "cltNmByCnId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        cnvId: typing.Union[MetaOapg.properties.cnvId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        cnvCltNm: typing.Union[MetaOapg.properties.cnvCltNm, str, schemas.Unset] = schemas.unset,
        cnvVerStatCd: typing.Union[MetaOapg.properties.cnvVerStatCd, str, schemas.Unset] = schemas.unset,
        cnvValStatCd: typing.Union[MetaOapg.properties.cnvValStatCd, str, schemas.Unset] = schemas.unset,
        cnvBegnEffDt: typing.Union[MetaOapg.properties.cnvBegnEffDt, str, datetime, schemas.Unset] = schemas.unset,
        cnvEndEffDt: typing.Union[MetaOapg.properties.cnvEndEffDt, str, datetime, schemas.Unset] = schemas.unset,
        cnvModDt: typing.Union[MetaOapg.properties.cnvModDt, str, datetime, schemas.Unset] = schemas.unset,
        cnvModByAppNm: typing.Union[MetaOapg.properties.cnvModByAppNm, str, schemas.Unset] = schemas.unset,
        cnvModByAppUsrNm: typing.Union[MetaOapg.properties.cnvModByAppUsrNm, str, schemas.Unset] = schemas.unset,
        cnvModByAppSubNm: typing.Union[MetaOapg.properties.cnvModByAppSubNm, str, schemas.Unset] = schemas.unset,
        cltNmByCnId: typing.Union['ClientName', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ClientNameVersion':
        return super().__new__(
            cls,
            *args,
            cnvId=cnvId,
            cnvCltNm=cnvCltNm,
            cnvVerStatCd=cnvVerStatCd,
            cnvValStatCd=cnvValStatCd,
            cnvBegnEffDt=cnvBegnEffDt,
            cnvEndEffDt=cnvEndEffDt,
            cnvModDt=cnvModDt,
            cnvModByAppNm=cnvModByAppNm,
            cnvModByAppUsrNm=cnvModByAppUsrNm,
            cnvModByAppSubNm=cnvModByAppSubNm,
            cltNmByCnId=cltNmByCnId,
            _configuration=_configuration,
            **kwargs,
        )

from paychex_python_sdk.model.client_name import ClientName
