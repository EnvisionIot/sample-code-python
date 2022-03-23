"""
 * Copyright (C), 2015-2021, Envision
 * FileName: checkAssetPermission
 * Author:  Dylan Yeo
 * Date:    18/03/22
 * Description: When a new asset on the EnOS platform is synchronized to the Application Portal, use this API to authorize the new asset to the asset creator
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/asset/authorize_asset.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def checkAssetPermission(accessKey, secretKey, url, accessToken):
    accessURL = url + "/app-portal-service/v2.2/user/authorization/asset/check"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"Authorization": "Bearer " + accessToken}
    print(header)

    body = { "assetIds": ["G5M8Ojhd", "OPVD7NPz", "Nmw9npSq"]}
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body, header)
    print(response)
