"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getStructureAsset
 * Author:  Dylan Yeo
 * Date:    21/03/22
 * Description: Get all the assets that the user can access under an organization structure
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/asset/get_structure_asset.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getStructureAsset(accessKey, secretKey, url, accessToken):
    accessURL = url + "/app-portal-service/v2.2/structure/asset/list"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"Authorization": "Bearer " + accessToken}
    print(header)

    body = {"structureIds": ["sg16256613934031600", "sg15780327471491"],
            "locale": "en_US"
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body, header)
    print(response)
