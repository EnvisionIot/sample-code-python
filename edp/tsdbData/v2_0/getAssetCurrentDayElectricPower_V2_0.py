"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getAssetAIDataWithAggregationLogic_V2_0
 * Author:  Dylan Yeo
 * Date:    07/03/22
 * Description: Get the accumulated power consumption/production data of specified devices from 00:00 (local time) of the current day
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/tsdb-data-api/en/2.3.0/v2.0/get_asset_current_day_electric_power.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getAssetCurrentDayElectricPower_V2_0(accessKey, secretKey, orgId, url, assetIds, measurepoints, modelId=None):
    accessURL = url + '/tsdb-service/v2.0/electric-power/current-day'
    params = {"orgId": orgId,
              "assetIds": assetIds,
              "measurepoints": measurepoints,
              "modelId": modelId,
              "accessKey": accessKey,
              "localTimeAccuracy": False,
              }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)
    print(params)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


def getAssetCurrentDayElectricPower_V2_0_accessKey(accessKey, secretKey, orgId, url):
    accessURL = url + '/tsdb-service/v2.0/electric-power/current-day'
    params = {"orgId": orgId,
              "assetIds": "G5M8Ojhd,Re2qPON3",
              "measurepoints": "PI_Double_Power,outputPower,power2",
              "accessKey": accessKey,

              }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)
    print(params)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)