"""
 * Copyright (C), 2015-2021, Envision
 * FileName: syncAsset
 * Author:  Dylan Yeo
 * Date:    21/03/22
 * Description: Synchronize assets on the EnOS to the Application Portal
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/asset/sync_asset.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def syncAsset(accessKey, secretKey, orgId, url):
    accessURL = url + "/app-portal-service/v2.2/asset/sync"
    params = {"orgId": orgId}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)


    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)
