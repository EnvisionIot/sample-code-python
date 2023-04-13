"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getOrganizationList
 * Author:  Dylan Yeo
 * Date:    17/03/22
 * Description: List the organizations which the current user belongs to according to the access token
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/user_and_ou/get_organization_list.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def getOrganizationList(accessKey, secretKey, url, accessToken):
    accessURL = url + "/app-portal-service/v2.2/user/organization/list"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"Authorization": "Bearer " + accessToken}
    print(header)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, headers=header)
    print(response)


