"""
 * Copyright (C), 2015-2021, Envision
 * FileName: filterAssetLatestData_V2_0
 * Author:  Dylan Yeo
 * Date:    07/03/22
 * Description: Filter and query the latest data of a single measurement point for multiple devices
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/tsdb-data-api/en/2.3.0/v2.0/filter_asset_latest_data.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def filterAssetLatestData_V2_0(accessKey, secretKey, orgId, url, modelId, assetIds, measurepoint, operator, valueFilter):
    accessURL = url + '/tsdb-service/v2.0/latest/filter'
    params = {"orgId": orgId,
              "modelId": modelId,
              "assetIds": assetIds,
              "measurepoint": measurepoint,
              "operator": operator,
              "valueFilter": valueFilter,
              "timeWindow": None,
              "accessKey": accessKey,
              "ifWithLocalTime": True,
              "localTimeAccuracy": False
              }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)
    print(params)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


def filterAssetLatestData_V2_0_timeWindow(accessKey, secretKey, orgId, url, timeWindow):
    accessURL = url + '/tsdb-service/v2.0/latest/filter'
    params = {"orgId": orgId,
              "modelId": "Python_Demo_Model",
              "assetIds": "Re2qPON3",
              "measurepoint": "Generic_Int_Power",
              "operator": "eq",
              "valueFilter": 999,
              "timeWindow": timeWindow}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)
    print(params)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


def filterAssetLatestData_V2_0_accessKey(accessKey, secretKey, orgId, url):
    accessURL = url + '/tsdb-service/v2.0/latest/filter'
    params = {"orgId": orgId,
              "modelId": "Python_Demo_Model",
              "assetIds": "Re2qPON3",
              "measurepoint": "Generic_Int_Power",
              "operator": "eq",
              "valueFilter": 999,
              "accessKey": accessKey}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)
    print(params)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)