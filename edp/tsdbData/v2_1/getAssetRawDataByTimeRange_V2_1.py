"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getAssetRawDataByTimeRange_V2_1
 * Author:  Dylan Yeo
 * Date:    02/03/22
 * Description: Get the original data of specified measurement points of specified devices within a certain period (covering AI, AI Normalized, DI, PI, and Generic data types) and perform application development
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/tsdb-data-api/en/2.3.0/v2.1/get_asset_raw_data_by_time_range.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getAssetRawDataByTimeRange_V2_1(accessKey, secretKey, orgId, url, assetIds, pointIds, startTime, endTime, modelId=None):
    accessURL = url + '/tsdb-service/v2.1/raw'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"modelId": modelId,
            "assetIds": assetIds,
            "pointIds": pointIds,
            "startTime": startTime,
            "endTime": endTime,
            "pageSize": 10,
            "orderBy": "timestamp asc",
            "withQuality": False,
            "localTimeAccuracy": False,
            "localTimeFormat": 1,
            "itemFormat": 0,
            "boundaryType": None,
            "interval": None,
            "interpolation": None,
            "type": None
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def getAssetRawDataByTimeRange_V2_1_itemFormat(accessKey, secretKey, orgId, url, itemFormat):
    accessURL = url + '/tsdb-service/v2.1/raw'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"assetIds": "G5M8Ojhd,Re2qPON3",
            "pointIds": "Generic_Int_Power,Generic_Double_Power,AI_Int_Power,AI_Double_Power,PI_Double_Power,DI_Int_Power",
            "startTime": "2022-01-01 00:00:00",
            "endTime": "2022-12-31 23:59:59",
            "itemFormat": itemFormat,
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def getAssetRawDataByTimeRange_V2_1_order(accessKey, secretKey, orgId, url, orderBy):
    accessURL = url + '/tsdb-service/v2.1/raw'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"assetIds": "G5M8Ojhd,Re2qPON3",
            "pointIds": "Generic_Int_Power,Generic_Double_Power,AI_Int_Power,AI_Double_Power,PI_Double_Power,DI_Int_Power",
            "startTime": "2022-01-01 00:00:00",
            "endTime": "2022-12-31 23:59:59",
            "orderBy": orderBy,
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def getAssetRawDataByTimeRange_V2_1_withQuality(accessKey, secretKey, orgId, url, withQuality):
    accessURL = url + '/tsdb-service/v2.1/raw'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"assetIds": "G5M8Ojhd,Re2qPON3",
            "pointIds": "Generic_Int_Power,Generic_Double_Power,AI_Int_Power,AI_Double_Power,PI_Double_Power,DI_Int_Power",
            "startTime": "2022-01-01 00:00:00",
            "endTime": "2022-12-31 23:59:59",
            "withQuality": withQuality,
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def getAssetRawDataByTimeRange_V2_1_type(accessKey, secretKey, orgId, url, storage_type):
    accessURL = url + '/tsdb-service/v2.1/raw'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"assetIds": "G5M8Ojhd,Re2qPON3",
            "pointIds": "Generic_Int_Power,Generic_Double_Power,AI_Int_Power,AI_Double_Power,PI_Double_Power,DI_Int_Power",
            "startTime": "2022-01-01 00:00:00",
            "endTime": "2022-12-31 23:59:59",
            "type": storage_type,
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def getAssetRawDataByTimeRange_V2_1_boundaryType(accessKey, secretKey, orgId, url, boundaryType, interval=None, interpolation=None):
    accessURL = url + '/tsdb-service/v2.1/raw'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"assetIds": "G5M8Ojhd",
            "pointIds": "Generic_Int_Power",
            "startTime": "2022-01-01 00:00:00",
            "endTime": "2022-12-31 23:59:59",
            "boundaryType": boundaryType,
            "interval": interval,
            "interpolation": interpolation,
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)