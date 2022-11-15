"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getAssetsByOrganization
 * Author:  Dylan Yeo
 * Date:    21/03/22
 * Description: Get all the assets that a specified user can access under a specified organization
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/asset/get_assets_by_ou.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getAssetsByOrganization(accessKey, secretKey, orgId, url):
    accessURL = url + "/app-portal-service/v2.2/user/asset/list"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"orgId": orgId,
            "userId": "u16473063753681521",
            "pagination": {"pageNo": 0,
                           "pageSize": 5}
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
