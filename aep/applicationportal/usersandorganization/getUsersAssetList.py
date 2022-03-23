"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getUsersAssetList
 * Author:  Dylan Yeo
 * Date:    18/03/22
 * Description: Get the asset permissions of users without logging in to Application Portal
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/user_and_ou/get_users_asset_list.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getUsersAssetList(accessKey, secretKey, orgId, url):
    accessURL = url + "/app-portal-service/v2.2/user/users/assetList"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"organizationId": orgId,
            "userIds": ["u15839808375371", "u16238383442701531", "u16050768760791", "u16473063753681521"]}
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)