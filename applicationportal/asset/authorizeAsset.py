"""
 * Copyright (C), 2015-2021, Envision
 * FileName: authorizeAsset
 * Author:  Dylan Yeo
 * Date:    18/03/22
 * Description: When a new asset on the EnOS platform is synchronized to the Application Portal, use this API to authorize the new asset to the asset creator
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/asset/authorize_asset.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def authorizeAsset(accessKey, secretKey, orgId, url):
    accessURL = url + "/app-portal-service/v2.2/user/asset/append"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"orgId": orgId,
            "userId": "u16473063753681521",
            "assetIds": ["G5M8Ojhd", "OPVD7NPz", "Nmw9npSq"]}
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
