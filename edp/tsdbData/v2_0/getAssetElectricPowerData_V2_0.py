"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getAssetElectricPowerData_V2_0
 * Author:  Dylan Yeo
 * Date:    07/03/22
 * Description: Get the power consumption/production data of specified devices within a certain period
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/tsdb-data-api/en/2.3.0/v2.0/get_asset_electric_power_data.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getAssetElectricPowerData_V2_0(accessKey, secretKey, orgId, url, assetIds, measurepointsWithLogic, startTime, endTime, modelId=None):
    accessURL = url + '/tsdb-service/v2.0/electric-power'
    params = {"orgId": orgId,
              "assetIds": assetIds,
              "measurepointsWithLogic": measurepointsWithLogic,
              "startTime": startTime,
              "endTime": endTime,
              "interval": 10,
              "modelId": modelId,
              "pageSize": 10,
              "accessKey": accessKey,
              "localTimeAccuracy": False,
              }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)
    print(params)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


def getAssetElectricPowerData_V2_0_interval(accessKey, secretKey, orgId, url, measurepointsWithLogic, interval):
    accessURL = url + '/tsdb-service/v2.0/electric-power'
    params = {"orgId": orgId,
              "assetIds": "G5M8Ojhd,Re2qPON3",
              "measurepointsWithLogic": measurepointsWithLogic,
              "interval": interval,
              "startTime": "2022-01-01 00:00:00",
              "endTime": "2022-12-31 23:59:59"
              }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)
    print(params)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


def getAssetElectricPowerData_V2_0_accessKey(accessKey, secretKey, orgId, url):
    accessURL = url + '/tsdb-service/v2.0/electric-power'
    params = {"orgId": orgId,
              "assetIds": "G5M8Ojhd,Re2qPON3",
              "measurepointsWithLogic": "sum(PI_Double_Power),count(outputPower),avg(power2)",
              "interval": 10,
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