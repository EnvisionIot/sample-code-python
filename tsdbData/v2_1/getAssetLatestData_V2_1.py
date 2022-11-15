"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getAssetLatestData_V2_1
 * Author:  Dylan Yeo
 * Date:    02/03/22
 * Description: Get the latest data of the specified measurement points of specified devices
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/tsdb-data-api/en/2.3.0/v2.1/get_asset_latest_data.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getAssetLatestData_V2_1(accessKey, secretKey, orgId, url, assetIds, pointIds, timeWindow, modelId=None):
    accessURL = url + '/tsdb-service/v2.1/latest'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"assetIds": assetIds,
            "pointIds": pointIds,
            "modelId": modelId,
            "timeWindow": timeWindow,
            "ifWithLocalTime": False,
            "localTimeAccuracy": False,
            "localTimeFormat": 1,
            "itemFormat": 0,
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def getAssetLatestData_V2_1_itemFormat(accessKey, secretKey, orgId, url, itemFormat):
    accessURL = url + '/tsdb-service/v2.1/latest'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"assetIds": "G5M8Ojhd,Re2qPON3",
            "pointIds": "Generic_Int_Power,Generic_Double_Power,AI_Int_Power,AI_Double_Power,PI_Double_Power,DI_Int_Power",
            "itemFormat": itemFormat,
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def getAssetLatestData_V2_1_withLocalTime(accessKey, secretKey, orgId, url, LocalTime):
    accessURL = url + '/tsdb-service/v2.1/latest'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"assetIds": "G5M8Ojhd,Re2qPON3",
            "pointIds": "Generic_Int_Power,Generic_Double_Power,AI_Int_Power,AI_Double_Power,PI_Double_Power,DI_Int_Power",
            "ifWithLocalTime": LocalTime,
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)