"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getAssetsByApplication
 * Author:  Dylan Yeo
 * Date:    21/03/22
 * Description: Get all the assets that the current user can access under a specified application
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/asset/get_assets_by_app.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getAssetsByApplication(accessKey, secretKey, url, accessToken):
    accessURL = url + "/app-portal-service/v2.2/user/app/asset/tree"
    params = {"accessKey": accessKey}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"Authorization": "Bearer " + accessToken}
    print(header)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, headers=header)
    print(response)
