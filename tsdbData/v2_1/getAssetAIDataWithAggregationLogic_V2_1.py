"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getAssetAIDataWithAggregationLogic_V2_1
 * Author:  Dylan Yeo
 * Date:    01/03/22
 * Description: Get the AI normalized data of specified measurement points of specified devices within a certain period. The queried data can also be aggregated by the specified logic
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/tsdb-data-api/en/2.3.0/v2.1/get_asset_ai_data_with_aggregation_logic.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getAssetAIDataWithAggregationLogic_V2_1(accessKey, secretKey, orgId, url, assetIds, pointsIdsWithLogic, startTime, endTime, modelId=None):
    accessURL = url + '/tsdb-service/v2.1/ai-normalized'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"modelId": modelId,
            "assetIds": assetIds,
            "pointIdsWithLogic": pointsIdsWithLogic,
            "startTime": startTime,
            "endTime": endTime,
            "interval": 10,
            "pageSize": 10,
            "localTimeAccuracy": False,
            "localTimeFormat": 1,
            "itemFormat": 0
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def getAssetAIDataWithAggregationLogic_V2_1_interval(accessKey, secretKey, orgId, url, pointIdsWithLogic, interval):
    accessURL = url + '/tsdb-service/v2.1/ai-normalized'
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


def getAssetAIDataWithAggregationLogic_V2_1_itemFormat(accessKey, secretKey, orgId, url, itemFormat):
    accessURL = url + '/tsdb-service/v2.1/ai-normalized'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"assetIds": "G5M8Ojhd,Re2qPON3",
            "pointIdsWithLogic": "count(Int_Output),avg(AI_Int_Power)",
            "startTime": "2022-01-01 00:00:00",
            "endTime": "2022-12-31 23:59:59",
            "interval": 10,
            "itemFormat": itemFormat
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)