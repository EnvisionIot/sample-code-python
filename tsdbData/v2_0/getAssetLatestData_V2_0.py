"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getAssetLatestData_V2_0
 * Author:  Dylan Yeo
 * Date:    07/03/22
 * Description: Get the latest data of the specified measurement points of specified devices
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/tsdb-data-api/en/2.3.0/v2.0/get_asset_latest_data.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getAssetLatestData_V2_0(accessKey, secretKey, orgId, url, assetIds, measurepoints, timeWindow, modelId=None):
    accessURL = url + '/tsdb-service/v2.0/latest'
    params = {"orgId": orgId,
              "assetIds": assetIds,
              "measurepoints": measurepoints,
              "modelId": modelId,
              "timeWindow": timeWindow,
              "accessKey": accessKey,
              "ifWithLocalTime": False,
              "localTimeAccuracy": False,
              }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)
    print(params)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


def getAssetLatestData_V2_0_withLocalTime(accessKey, secretKey, orgId, url, LocalTime):
    accessURL = url + '/tsdb-service/v2.0/latest'
    params = {"orgId": orgId,
              "assetIds": "G5M8Ojhd,Re2qPON3",
              "measurepoints": "Generic_Int_Power,Generic_Double_Power,AI_Int_Power,AI_Double_Power,PI_Double_Power,DI_Int_Power",
              "ifWithLocalTime": LocalTime,
              }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)
    print(params)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


def getAssetLatestData_V2_0_accessKey(accessKey, secretKey, orgId, url):
    accessURL = url + '/tsdb-service/v2.0/latest'
    params = {"orgId": orgId,
              "assetIds": "G5M8Ojhd,Re2qPON3",
              "measurepoints": "Generic_Int_Power,Generic_Double_Power,AI_Int_Power,AI_Double_Power,PI_Double_Power,DI_Int_Power",
              "accessKey": accessKey,
              }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)
    print(params)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)