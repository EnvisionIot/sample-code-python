"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getAssetAIRawData_V2_0
 * Author:  Dylan Yeo
 * Date:    07/03/22
 * Description: Get the original AI data of specified measurement points of specified devices within a certain period
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/tsdb-data-api/en/2.3.0/v2.0/get_asset_ai_raw_data.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getAssetAIRawData_V2_0(accessKey, secretKey, orgId, url, assetIds, measurepoints, startTime, endTime, modelId=None):
    accessURL = url + '/tsdb-service/v2.0/ai'
    params = {"orgId": orgId,
              "assetIds": assetIds,
              "measurepoints": measurepoints,
              "startTime": startTime,
              "endTime": endTime,
              "modelId": modelId,
              "pageSize": 10,
              "accessKey": accessKey,
              "withQuality": False,
              "localTimeAccuracy": False
              }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)
    print(params)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


def getAssetAIRawData_V2_0_accessKey(accessKey, secretKey, orgId, url):
    accessURL = url + '/tsdb-service/v2.0/ai'
    params = {"orgId": orgId,
              "assetIds": "G5M8Ojhd,Re2qPON3",
              "measurepoints": "Int_Output,AI_Int_Power,AI_Double_Power",
              "startTime": "2022-01-01 00:00:00",
              "endTime": "2022-12-31 23:59:59",
              "accessKey": accessKey
              }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)
    print(params)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


def getAssetAIRawData_V2_0_withQuality(accessKey, secretKey, orgId, url, withQuality):
    accessURL = url + '/tsdb-service/v2.0/ai'
    params = {"orgId": orgId,
              "assetIds": "G5M8Ojhd,Re2qPON3",
              "measurepoints": "Int_Output,AI_Int_Power,AI_Double_Power",
              "startTime": "2022-01-01 00:00:00",
              "endTime": "2022-12-31 23:59:59",
              "withQuality": withQuality
              }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)
    print(params)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)