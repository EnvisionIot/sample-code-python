"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getAssetStructure
 * Author:  Dylan Yeo
 * Date:    21/03/22
 * Description: Get the upstream organizational structure where the asset is located
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/asset/get_asset_structure.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getAssetStructure(accessKey, secretKey, url, accessToken):
    accessURL = url + "/app-portal-service/v2.2/asset/structure"
    params = {"assetId": "0x19kHPY"}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"Authorization": "Bearer " + accessToken}
    print(header)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, headers=header)
    print(response)
