"""
 * Copyright (C), 2015-2021, Envision
 * FileName: filterAssetLatestData_V2_1
 * Author:  Dylan Yeo
 * Date:    04/03/22
 * Description: Filter and query the latest data of a single measurement point for multiple devices
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/tsdb-data-api/en/2.3.0/v2.1/filter_asset_latest_data.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def filterAssetLatestData_V2_1(accessKey, secretKey, orgId, url, modelId, assetIds, pointId, operator, valueFilter):
    accessURL = url + '/tsdb-service/v2.1/latest/filter'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"modelId": modelId,
            "assetIds": assetIds,
            "pointId": pointId,
            "operator": operator,
            "valueFilter": valueFilter,
            "timeWindow": None,
            "ifWithLocalTime": True,
            "localTimeAccuracy": False,
            "localTimeFormat": 1,
            "itemFormat": 0
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def filterAssetLatestData_V2_1_timeWindow(accessKey, secretKey, orgId, url, timeWindow):
    accessURL = url + '/tsdb-service/v2.1/latest/filter'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"modelId": "Python_Demo_Model",
            "assetIds": "Re2qPON3",
            "pointId": "Generic_Int_Power",
            "operator": "eq",
            "valueFilter": 999,
            "timeWindow": timeWindow,
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def filterAssetLatestData_V2_1_itemFormat(accessKey, secretKey, orgId, url, itemFormat):
    accessURL = url + '/tsdb-service/v2.1/latest/filter'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"modelId": "Python_Demo_Model",
            "assetIds": "G5M8Ojhd,Re2qPON3",
            "pointId": "Generic_Int_Power",
            "operator": "eq",
            "valueFilter": 999,
            "itemFormat": itemFormat,
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)