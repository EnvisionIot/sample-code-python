"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getAssetDIDateDuration_V2_0
 * Author:  Dylan Yeo
 * Date:    07/03/22
 * Description: Get the duration of different status (DI) data of specified devices within a certain period
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/tsdb-data-api/en/2.3.0/v2.0/get_asset_di_data_durations.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getAssetDIDataDuration_V2_0(accessKey, secretKey, orgId, url, assetIds, measurepoints, startTime, endTime, modelId=None):
    accessURL = url + '/tsdb-service/v2.0/di/duration'
    params = {"orgId": orgId,
              "assetIds": assetIds,
              "measurepoints": measurepoints,
              "startTime": startTime,
              "endTime": endTime,
              "modelId": modelId,
              "status": None,
              "ifWithUnknown": True}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)
    print(params)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


def getAssetDIDataDuration_V2_0_status(accessKey, secretKey, orgId, url, status):
    accessURL = url + '/tsdb-service/v2.0/di/duration'
    params = {"orgId": orgId,
              "assetIds": "G5M8Ojhd",
              "measurepoints": "DI_Int_Power",
              "startTime": "2022-01-01 00:00:00",
              "endTime": "2022-12-31 23:59:59",
              "status": status}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)
    print(params)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


def getAssetDIDataDuration_V2_0_Unknown(accessKey, secretKey, orgId, url, unknown):
    accessURL = url + '/tsdb-service/v2.0/di/duration'
    params = {"orgId": orgId,
              "assetIds": "G5M8Ojhd,Re2qPON3",
              "measurepoints": "DI_Int_Power,DIPower2",
              "startTime": "2022-01-01 00:00:00",
              "endTime": "2022-12-31 23:59:59",
              "ifWithUnknown": unknown}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)
    print(params)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)
