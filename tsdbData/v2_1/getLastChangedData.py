"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getLastChangedData
 * Author:  Dylan Yeo
 * Date:    03/03/22
 * Description: Get the last changed data of the specified measurement points of specified devices
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/tsdb-data-api/en/2.3.0/v2.1/get_last_changed_data.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getLastChangedData(accessKey, secretKey, orgId, url, assetIds, pointIds):
    accessURL = url + '/tsdb-service/v2.1/data/last-changed'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"assetIds": assetIds,
            "pointIds": pointIds,
            "ifWithLocalTime": False,
            "localTimeAccuracy": False,
            "localTimeFormat": 1,
            "itemFormat": 0
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def getLastChangedData_withLocalTime(accessKey, secretKey, orgId, url, localTime):
    accessURL = url + '/tsdb-service/v2.1/data/last-changed'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"assetIds": "G5M8Ojhd,Re2qPON3",
            "pointIds": "AI_Int_Power,AI_Double_Power,PI_Double_Power,DI_Int_Power",
            "ifWithLocalTime": localTime,
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


def getLastChangedData_itemFormat(accessKey, secretKey, orgId, url, itemFormat):
    accessURL = url + '/tsdb-service/v2.1/data/last-changed'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"assetIds": "G5M8Ojhd,Re2qPON3",
            "pointIds": "AI_Int_Power,AI_Double_Power,PI_Double_Power,DI_Int_Power",
            "itemFormat": itemFormat,
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)