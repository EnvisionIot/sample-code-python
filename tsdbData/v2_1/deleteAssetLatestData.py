"""
 * Copyright (C), 2015-2021, Envision
 * FileName: deleteAssetLatestData
 * Author:  Dylan Yeo
 * Date:    03/03/22
 * Description: Delete the latest data of the specified measurement points of specified devices
 * History:
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/tsdb-data-api/en/2.3.0/v2.1/delete_asset_latest_data.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def deleteAssetLatestData(accessKey, secretKey, orgId, url, assetIds, pointIds):
    accessURL = url + '/tsdb-service/v2.1/latest'
    params = {"orgId": orgId, "action": "delete"}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"Content-Type": "application/json"}

    body = {"assetIds": assetIds,
            "pointIds": pointIds,
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body, header)
    print(response)