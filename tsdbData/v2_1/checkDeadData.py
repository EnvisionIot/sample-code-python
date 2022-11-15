"""
 * Copyright (C), 2015-2021, Envision
 * FileName: checkDeadData
 * Author:  Dylan Yeo
 * Date:    03/03/22
 * Description: Check whether data of the specified measurement point of specified device is dead data and return the last changed data of the measurement point
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/tsdb-data-api/en/2.3.0/v2.1/check_dead_data.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def checkDeadData(accessKey, secretKey, orgId, url, assetId, pointId):
    accessURL = url + '/tsdb-service/v2.1/data/latest/check-dead'
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"payload": [{"assetId": assetId,
                        "pointId": pointId,
                        "interval": 100}]
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
