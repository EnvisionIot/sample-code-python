"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getAssetElectricPowerData_V2_1
 * Author:  Dylan Yeo
 * Date:    01/03/22
 * Description: Get the power consumption/production data of specified devices within a certain period
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/tsdb-data-api/en/2.3.0/v2.1/get_asset_electric_power_data.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getAssetElectricPowerData_V2_1(accessKey, secretKey, orgId, url, assetIds, pointIdsWithLogic, startTime, endTime, modelId=None):
    accessURL = url + '/tsdb-service/v2.1/electric-power'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"modelId": modelId,
            "assetIds": assetIds,
            "pointIdsWithLogic": pointIdsWithLogic,
            "startTime": startTime,
            "endTime": endTime,
            "interval": 10,
            "pageSize": 10,
            "localTimeAccuracy": False,
            "localTimeFormat": 1,
            "itemFormat": 0,
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

def getAssetElectricPowerData_V2_1_interval(accessKey, secretKey, orgId, url, pointIdsWithLogic, interval):
    accessURL = url + '/tsdb-service/v2.1/electric-power'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"assetIds": "G5M8Ojhd,Re2qPON3",
            "pointIdsWithLogic": pointIdsWithLogic,
            "startTime": "2022-01-01 00:00:00",
            "endTime": "2022-12-31 23:59:59",
            "interval": interval
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

def getAssetElectricPowerData_V2_1_itemFormat(accessKey, secretKey, orgId, url, itemFormat):
    accessURL = url + '/tsdb-service/v2.1/electric-power'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"assetIds": "G5M8Ojhd,Re2qPON3",
            "pointIdsWithLogic": "sum(PI_Double_Power),count(outputPower),avg(power2)",
            "startTime": "2022-01-01 00:00:00",
            "endTime": "2022-12-31 23:59:59",
            "interval": 10,
            "itemFormat": itemFormat
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)