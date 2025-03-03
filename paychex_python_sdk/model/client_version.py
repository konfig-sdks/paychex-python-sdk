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


class ClientVersion(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.Int64Schema
            taxPayerIdentificationNumber = schemas.StrSchema
            tinLastFour = schemas.StrSchema
            tinType = schemas.StrSchema
            tinValidStatusCode = schemas.StrSchema
            normalizedName = schemas.StrSchema
            normalizedCity = schemas.StrSchema
            normalizedCountryCode = schemas.StrSchema
            versionStatusCode = schemas.StrSchema
            beginEffectiveDate = schemas.DateTimeSchema
            endEffectiveDate = schemas.DateTimeSchema
            normalizedBuildingNumber = schemas.StrSchema
            normalizedSteetName = schemas.StrSchema
            normalizedUnitName = schemas.StrSchema
            normalizedPOBox = schemas.StrSchema
            normalizedStateProvince = schemas.StrSchema
            normalizedStateProvinceF = schemas.StrSchema
            normalizedPostalCode = schemas.StrSchema
            tinVersionStatusCode = schemas.StrSchema
            status = schemas.StrSchema
            statusDate = schemas.DateTimeSchema
            superceededBy = schemas.StrSchema
            modifiedDate = schemas.DateTimeSchema
            modifiedByApplicationName = schemas.StrSchema
            modifiedByApplicationSubProcessName = schemas.StrSchema
            modifiedByUserId = schemas.StrSchema
            modifiedReason = schemas.StrSchema
        
            @staticmethod
            def client() -> typing.Type['Client']:
                return Client
            __annotations__ = {
                "id": id,
                "taxPayerIdentificationNumber": taxPayerIdentificationNumber,
                "tinLastFour": tinLastFour,
                "tinType": tinType,
                "tinValidStatusCode": tinValidStatusCode,
                "normalizedName": normalizedName,
                "normalizedCity": normalizedCity,
                "normalizedCountryCode": normalizedCountryCode,
                "versionStatusCode": versionStatusCode,
                "beginEffectiveDate": beginEffectiveDate,
                "endEffectiveDate": endEffectiveDate,
                "normalizedBuildingNumber": normalizedBuildingNumber,
                "normalizedSteetName": normalizedSteetName,
                "normalizedUnitName": normalizedUnitName,
                "normalizedPOBox": normalizedPOBox,
                "normalizedStateProvince": normalizedStateProvince,
                "normalizedStateProvinceF": normalizedStateProvinceF,
                "normalizedPostalCode": normalizedPostalCode,
                "tinVersionStatusCode": tinVersionStatusCode,
                "status": status,
                "statusDate": statusDate,
                "superceededBy": superceededBy,
                "modifiedDate": modifiedDate,
                "modifiedByApplicationName": modifiedByApplicationName,
                "modifiedByApplicationSubProcessName": modifiedByApplicationSubProcessName,
                "modifiedByUserId": modifiedByUserId,
                "modifiedReason": modifiedReason,
                "client": client,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxPayerIdentificationNumber"]) -> MetaOapg.properties.taxPayerIdentificationNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tinLastFour"]) -> MetaOapg.properties.tinLastFour: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tinType"]) -> MetaOapg.properties.tinType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tinValidStatusCode"]) -> MetaOapg.properties.tinValidStatusCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normalizedName"]) -> MetaOapg.properties.normalizedName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normalizedCity"]) -> MetaOapg.properties.normalizedCity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normalizedCountryCode"]) -> MetaOapg.properties.normalizedCountryCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["versionStatusCode"]) -> MetaOapg.properties.versionStatusCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["beginEffectiveDate"]) -> MetaOapg.properties.beginEffectiveDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endEffectiveDate"]) -> MetaOapg.properties.endEffectiveDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normalizedBuildingNumber"]) -> MetaOapg.properties.normalizedBuildingNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normalizedSteetName"]) -> MetaOapg.properties.normalizedSteetName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normalizedUnitName"]) -> MetaOapg.properties.normalizedUnitName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normalizedPOBox"]) -> MetaOapg.properties.normalizedPOBox: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normalizedStateProvince"]) -> MetaOapg.properties.normalizedStateProvince: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normalizedStateProvinceF"]) -> MetaOapg.properties.normalizedStateProvinceF: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normalizedPostalCode"]) -> MetaOapg.properties.normalizedPostalCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tinVersionStatusCode"]) -> MetaOapg.properties.tinVersionStatusCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statusDate"]) -> MetaOapg.properties.statusDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["superceededBy"]) -> MetaOapg.properties.superceededBy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modifiedDate"]) -> MetaOapg.properties.modifiedDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modifiedByApplicationName"]) -> MetaOapg.properties.modifiedByApplicationName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modifiedByApplicationSubProcessName"]) -> MetaOapg.properties.modifiedByApplicationSubProcessName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modifiedByUserId"]) -> MetaOapg.properties.modifiedByUserId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modifiedReason"]) -> MetaOapg.properties.modifiedReason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client"]) -> 'Client': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "taxPayerIdentificationNumber", "tinLastFour", "tinType", "tinValidStatusCode", "normalizedName", "normalizedCity", "normalizedCountryCode", "versionStatusCode", "beginEffectiveDate", "endEffectiveDate", "normalizedBuildingNumber", "normalizedSteetName", "normalizedUnitName", "normalizedPOBox", "normalizedStateProvince", "normalizedStateProvinceF", "normalizedPostalCode", "tinVersionStatusCode", "status", "statusDate", "superceededBy", "modifiedDate", "modifiedByApplicationName", "modifiedByApplicationSubProcessName", "modifiedByUserId", "modifiedReason", "client", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxPayerIdentificationNumber"]) -> typing.Union[MetaOapg.properties.taxPayerIdentificationNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tinLastFour"]) -> typing.Union[MetaOapg.properties.tinLastFour, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tinType"]) -> typing.Union[MetaOapg.properties.tinType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tinValidStatusCode"]) -> typing.Union[MetaOapg.properties.tinValidStatusCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normalizedName"]) -> typing.Union[MetaOapg.properties.normalizedName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normalizedCity"]) -> typing.Union[MetaOapg.properties.normalizedCity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normalizedCountryCode"]) -> typing.Union[MetaOapg.properties.normalizedCountryCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["versionStatusCode"]) -> typing.Union[MetaOapg.properties.versionStatusCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["beginEffectiveDate"]) -> typing.Union[MetaOapg.properties.beginEffectiveDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endEffectiveDate"]) -> typing.Union[MetaOapg.properties.endEffectiveDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normalizedBuildingNumber"]) -> typing.Union[MetaOapg.properties.normalizedBuildingNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normalizedSteetName"]) -> typing.Union[MetaOapg.properties.normalizedSteetName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normalizedUnitName"]) -> typing.Union[MetaOapg.properties.normalizedUnitName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normalizedPOBox"]) -> typing.Union[MetaOapg.properties.normalizedPOBox, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normalizedStateProvince"]) -> typing.Union[MetaOapg.properties.normalizedStateProvince, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normalizedStateProvinceF"]) -> typing.Union[MetaOapg.properties.normalizedStateProvinceF, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normalizedPostalCode"]) -> typing.Union[MetaOapg.properties.normalizedPostalCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tinVersionStatusCode"]) -> typing.Union[MetaOapg.properties.tinVersionStatusCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statusDate"]) -> typing.Union[MetaOapg.properties.statusDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["superceededBy"]) -> typing.Union[MetaOapg.properties.superceededBy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modifiedDate"]) -> typing.Union[MetaOapg.properties.modifiedDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modifiedByApplicationName"]) -> typing.Union[MetaOapg.properties.modifiedByApplicationName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modifiedByApplicationSubProcessName"]) -> typing.Union[MetaOapg.properties.modifiedByApplicationSubProcessName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modifiedByUserId"]) -> typing.Union[MetaOapg.properties.modifiedByUserId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modifiedReason"]) -> typing.Union[MetaOapg.properties.modifiedReason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client"]) -> typing.Union['Client', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "taxPayerIdentificationNumber", "tinLastFour", "tinType", "tinValidStatusCode", "normalizedName", "normalizedCity", "normalizedCountryCode", "versionStatusCode", "beginEffectiveDate", "endEffectiveDate", "normalizedBuildingNumber", "normalizedSteetName", "normalizedUnitName", "normalizedPOBox", "normalizedStateProvince", "normalizedStateProvinceF", "normalizedPostalCode", "tinVersionStatusCode", "status", "statusDate", "superceededBy", "modifiedDate", "modifiedByApplicationName", "modifiedByApplicationSubProcessName", "modifiedByUserId", "modifiedReason", "client", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        taxPayerIdentificationNumber: typing.Union[MetaOapg.properties.taxPayerIdentificationNumber, str, schemas.Unset] = schemas.unset,
        tinLastFour: typing.Union[MetaOapg.properties.tinLastFour, str, schemas.Unset] = schemas.unset,
        tinType: typing.Union[MetaOapg.properties.tinType, str, schemas.Unset] = schemas.unset,
        tinValidStatusCode: typing.Union[MetaOapg.properties.tinValidStatusCode, str, schemas.Unset] = schemas.unset,
        normalizedName: typing.Union[MetaOapg.properties.normalizedName, str, schemas.Unset] = schemas.unset,
        normalizedCity: typing.Union[MetaOapg.properties.normalizedCity, str, schemas.Unset] = schemas.unset,
        normalizedCountryCode: typing.Union[MetaOapg.properties.normalizedCountryCode, str, schemas.Unset] = schemas.unset,
        versionStatusCode: typing.Union[MetaOapg.properties.versionStatusCode, str, schemas.Unset] = schemas.unset,
        beginEffectiveDate: typing.Union[MetaOapg.properties.beginEffectiveDate, str, datetime, schemas.Unset] = schemas.unset,
        endEffectiveDate: typing.Union[MetaOapg.properties.endEffectiveDate, str, datetime, schemas.Unset] = schemas.unset,
        normalizedBuildingNumber: typing.Union[MetaOapg.properties.normalizedBuildingNumber, str, schemas.Unset] = schemas.unset,
        normalizedSteetName: typing.Union[MetaOapg.properties.normalizedSteetName, str, schemas.Unset] = schemas.unset,
        normalizedUnitName: typing.Union[MetaOapg.properties.normalizedUnitName, str, schemas.Unset] = schemas.unset,
        normalizedPOBox: typing.Union[MetaOapg.properties.normalizedPOBox, str, schemas.Unset] = schemas.unset,
        normalizedStateProvince: typing.Union[MetaOapg.properties.normalizedStateProvince, str, schemas.Unset] = schemas.unset,
        normalizedStateProvinceF: typing.Union[MetaOapg.properties.normalizedStateProvinceF, str, schemas.Unset] = schemas.unset,
        normalizedPostalCode: typing.Union[MetaOapg.properties.normalizedPostalCode, str, schemas.Unset] = schemas.unset,
        tinVersionStatusCode: typing.Union[MetaOapg.properties.tinVersionStatusCode, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        statusDate: typing.Union[MetaOapg.properties.statusDate, str, datetime, schemas.Unset] = schemas.unset,
        superceededBy: typing.Union[MetaOapg.properties.superceededBy, str, schemas.Unset] = schemas.unset,
        modifiedDate: typing.Union[MetaOapg.properties.modifiedDate, str, datetime, schemas.Unset] = schemas.unset,
        modifiedByApplicationName: typing.Union[MetaOapg.properties.modifiedByApplicationName, str, schemas.Unset] = schemas.unset,
        modifiedByApplicationSubProcessName: typing.Union[MetaOapg.properties.modifiedByApplicationSubProcessName, str, schemas.Unset] = schemas.unset,
        modifiedByUserId: typing.Union[MetaOapg.properties.modifiedByUserId, str, schemas.Unset] = schemas.unset,
        modifiedReason: typing.Union[MetaOapg.properties.modifiedReason, str, schemas.Unset] = schemas.unset,
        client: typing.Union['Client', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ClientVersion':
        return super().__new__(
            cls,
            *args,
            id=id,
            taxPayerIdentificationNumber=taxPayerIdentificationNumber,
            tinLastFour=tinLastFour,
            tinType=tinType,
            tinValidStatusCode=tinValidStatusCode,
            normalizedName=normalizedName,
            normalizedCity=normalizedCity,
            normalizedCountryCode=normalizedCountryCode,
            versionStatusCode=versionStatusCode,
            beginEffectiveDate=beginEffectiveDate,
            endEffectiveDate=endEffectiveDate,
            normalizedBuildingNumber=normalizedBuildingNumber,
            normalizedSteetName=normalizedSteetName,
            normalizedUnitName=normalizedUnitName,
            normalizedPOBox=normalizedPOBox,
            normalizedStateProvince=normalizedStateProvince,
            normalizedStateProvinceF=normalizedStateProvinceF,
            normalizedPostalCode=normalizedPostalCode,
            tinVersionStatusCode=tinVersionStatusCode,
            status=status,
            statusDate=statusDate,
            superceededBy=superceededBy,
            modifiedDate=modifiedDate,
            modifiedByApplicationName=modifiedByApplicationName,
            modifiedByApplicationSubProcessName=modifiedByApplicationSubProcessName,
            modifiedByUserId=modifiedByUserId,
            modifiedReason=modifiedReason,
            client=client,
            _configuration=_configuration,
            **kwargs,
        )

from paychex_python_sdk.model.client import Client
