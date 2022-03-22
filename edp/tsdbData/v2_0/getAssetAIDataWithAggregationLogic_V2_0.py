"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getAssetAIDataWithAggregationLogic_V2_0
 * Author:  Dylan Yeo
 * Date:    04/03/22
 * Description: Get the AI normalized data of specified measurement points of specified devices within a certain period. The queried data can also be aggregated by the specified logic
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/tsdb-data-api/en/2.3.0/v2.0/get_asset_ai_data_with_aggregation_logic.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getAssetAIDataWithAggregationLogic_V2_0(accessKey, secretKey, orgId, url, assetIds, measurepointsWithLogic, startTime, endTime, modelId=None):
    accessURL = url + '/tsdb-service/v2.0/ai-normalized'
    params = {"orgId": orgId,
              "assetIds": assetIds,
              "measurepointsWithLogic": measurepointsWithLogic,
              "interval": 10,
              "startTime": startTime,
              "endTime": endTime,
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


def getAssetAIDataWithAggregationLogic_V2_0_interval(accessKey, secretKey, orgId, url, measurepointsWithLogic, interval):
    accessURL = url + '/tsdb-service/v2.0/ai-normalized'
    params = {"orgId": orgId,
              "assetIds": "G5M8Ojhd,Re2qPON3",
              "measurepointsWithLogic": measurepointsWithLogic,
              "startTime": "2022-01-01 00:00:00",
              "endTime": "2022-12-31 23:59:59",
              "interval": interval
              }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)
    print(params)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


def getAssetAIDataWithAggregationLogic_V2_0_accessKey(accessKey, secretKey, orgId, url):
    accessURL = url + '/tsdb-service/v2.0/ai-normalized'
    params = {"orgId": orgId,
              "assetIds": "G5M8Ojhd,Re2qPON3",
              "measurepointsWithLogic": "count(AI_Int_Power)",
              "interval": 10,
              "startTime": "2022-01-01 00:00:00",
              "endTime": "2022-12-31 23:59:59",
              "accessKey": accessKey,
              }
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)
    print(params)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)