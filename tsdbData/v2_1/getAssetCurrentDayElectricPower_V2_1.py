"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getAssetAIDataWithAggregationLogic_V2_1
 * Author:  Dylan Yeo
 * Date:    01/03/22
 * Description: Get the accumulated power consumption/production data of specified devices from 00:00 (local time) of the current day
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/tsdb-data-api/en/2.3.0/v2.1/get_asset_current_day_electric_power.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getAssetCurrentDayElectricPower_V2_1(accessKey, secretKey, orgId, url, assetIds, pointIds, modelId=None):
    accessURL = url + '/tsdb-service/v2.1/electric-power/current-day'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"modelId": modelId,
            "assetIds": assetIds,
            "pointIds": pointIds,
            "localTimeAccuracy": False,
            "localTimeFormat": 1,
            "itemFormat": 0
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def getAssetCurrentDayElectricPower_V2_1_itemFormat(accessKey, secretKey, orgId, url, itemFormat):
    accessURL = url + '/tsdb-service/v2.1/electric-power/current-day'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"assetIds": "G5M8Ojhd,Re2qPON3",
            "pointIds": "PI_Double_Power,outputPower,power2",
            "itemFormat": itemFormat
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)