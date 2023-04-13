"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getAssetAIRawData_V2_1
 * Author:  Dylan Yeo
 * Date:    01/03/22
 * Description: Get the original AI data of specified measurement points of specified devices within a certain period
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/tsdb-data-api/en/2.3.0/v2.1/get_asset_ai_raw_data.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getAssetAIRawData_V2_1(accessKey, secretKey, orgId, url, assetIds, pointIds, startTime, endTime, modelId=None):
    accessURL = url + '/tsdb-service/v2.1/ai'
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
            "withQuality": False,
            "localTimeAccuracy": False,
            "localTimeFormat": 1,
            "itemFormat": 0,
            "boundaryType": None,
            "interval": None,
            "interpolation": None
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def getAssetAIRawData_V2_1_itemFormat(accessKey, secretKey, orgId, url, itemFormat):
    accessURL = url + '/tsdb-service/v2.1/ai'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"assetIds": "G5M8Ojhd,Re2qPON3",
            "pointIds": "Int_Output,AI_Int_Power,AI_Double_Power",
            "startTime": "2022-01-01 00:00:00",
            "endTime": "2022-12-31 23:59:59",
            "itemFormat": itemFormat,
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def getAssetAIRawData_V2_1_withQuality(accessKey, secretKey, orgId, url, withQuality):
    accessURL = url + '/tsdb-service/v2.1/ai'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"assetIds": "G5M8Ojhd,Re2qPON3",
            "pointIds": "Int_Output,AI_Int_Power,AI_Double_Power",
            "startTime": "2022-01-01 00:00:00",
            "endTime": "2022-12-31 23:59:59",
            "withQuality": withQuality,
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def getAssetAIRawData_V2_1_boundaryType(accessKey, secretKey, orgId, url, boundaryType, interval=None, interpolation=None):
    accessURL = url + '/tsdb-service/v2.1/ai'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"assetIds": "G5M8Ojhd",
            "pointIds": "AI_Int_Power",
            "startTime": "2022-01-01 00:00:00",
            "endTime": "2022-12-31 23:59:59",
            "boundaryType": boundaryType,
            "interval": interval,
            "interpolation": interpolation
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)