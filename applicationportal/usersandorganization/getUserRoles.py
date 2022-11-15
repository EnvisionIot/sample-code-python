"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getUserRoles
 * Author:  Dylan Yeo
 * Date:    17/03/22
 * Description: Get all roles that are assigned to a user
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/user_and_ou/get_user_roles.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def getUserRoles(accessKey, secretKey, orgId, url):
    accessURL = url + "/app-portal-service/v2.2/user/role/assignedList"
    params = {"orgId": orgId, "userId": "u16473063753681521"}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"locale": "en_US"}

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, headers=header)
    print(response)


