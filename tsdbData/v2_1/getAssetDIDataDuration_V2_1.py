"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getAssetDIDateDuration_V2_1
 * Author:  Dylan Yeo
 * Date:    02/03/22
 * Description: Get the duration of different status (DI) data of specified devices within a certain period
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/tsdb-data-api/en/2.3.0/v2.1/get_asset_di_data_durations.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getAssetDIDataDuration_V2_1(accessKey, secretKey, orgId, url, assetIds, pointIds, startTime, endTime, modelId=None):
    accessURL = url + '/tsdb-service/v2.1/di/duration'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"modelId": modelId,
            "assetIds": assetIds,
            "pointIds": pointIds,
            "startTime": startTime,
            "endTime": endTime,
            "status": None,
            "ifWithUnknown": True,
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def getAssetDIDataDuration_V2_1_Status(accessKey, secretKey, orgId, url, status):
    accessURL = url + '/tsdb-service/v2.1/di/duration'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"assetIds": "G5M8Ojhd",
            "pointIds": "DI_Int_Power",
            "startTime": "2022-01-01 00:00:00",
            "endTime": "2022-12-31 23:59:59",
            "status": status,
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def getAssetDIDataDuration_V2_1_Unknown(accessKey, secretKey, orgId, url, unknown):
    accessURL = url + '/tsdb-service/v2.1/di/duration'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"assetIds": "G5M8Ojhd,Re2qPON3",
            "pointIds": "DI_Int_Power,DIPower2",
            "startTime": "2022-01-01 00:00:00",
            "endTime": "2022-12-31 23:59:59",
            "ifWithUnknown": unknown,
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
