"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getUsersWithAssetAccess
 * Author:  Dylan Yeo
 * Date:    21/03/22
 * Description: Get the list of users who have access permission to a specific asset
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/asset/get_assets_by_ou.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getUsersWithAssetAccess(accessKey, secretKey, orgId, url):
    accessURL = url + "/app-portal-service/v2.2/asset/authorize/user/list"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"orgId": orgId,
            "assetId": "G5M8Ojhd"
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)