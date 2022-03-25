"""
 * Copyright (C), 2015-2021, Envision
 * FileName: listUserOrganization
 * Author:  Dylan Yeo
 * Date:    25/03/22
 * Description: List the organization to which a user belongs
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/iam-api/en/2.3.0/list_user_organization.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def listUserOrganization(accessKey, secretKey, url, sessoinId):
    accessURL = url + "/enos-iam-service/v2.0/user/organization/list"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header ={"Authorization": sessoinId}
    print(header)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, headers=header, method="POST")
    print(response)