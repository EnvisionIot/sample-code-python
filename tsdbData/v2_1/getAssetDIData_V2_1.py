"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getAssetDIDate_V2_1
 * Author:  Dylan Yeo
 * Date:    01/03/22
 * Description: Get the status change (DI) data of specified devices within a certain period
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/tsdb-data-api/en/2.3.0/v2.1/get_asset_di_data.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getAssetDIData_V2_1(accessKey, secretKey, orgId, url, assetIds, pointIds, startTime, endTime, modelId=None):
    accessURL = url + '/tsdb-service/v2.1/di'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"modelId": modelId,
            "assetIds": assetIds,
            "pointIds": pointIds,
            "startTime": startTime,
            "endTime": endTime,
            "interval": 10,
            "pageSize": 10,
            "localTimeAccuracy": False,
            "autoInterpolate": False,
            "localTimeFormat": 1,
            "itemFormat": 0
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def getAssetDIData_V2_1_itemFormat(accessKey, secretKey, orgId, url, itemFormat):
    accessURL = url + '/tsdb-service/v2.1/di'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"assetIds": "G5M8Ojhd,Re2qPON3",
            "pointIds": "DI_Int_Power,DIPower2",
            "startTime": "2022-01-01 00:00:00",
            "endTime": "2022-12-31 23:59:59",
            "interval": 10,
            "pageSize": 10,
            "localTimeAccuracy": False,
            "autoInterpolate": False,
            "localTimeFormat": 1,
            "itemFormat": itemFormat
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def getAssetDIData_V2_1_autoInterpolate(accessKey, secretKey, orgId, url, autoInterpolate):
    accessURL = url + '/tsdb-service/v2.1/di'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"assetIds": "G5M8Ojhd,Re2qPON3",
            "pointIds": "DI_Int_Power,DIPower2",
            "startTime": "2022-01-01 00:00:00",
            "endTime": "2022-12-31 23:59:59",
            "autoInterpolate": autoInterpolate,
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)