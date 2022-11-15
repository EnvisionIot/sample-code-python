"""
 * Copyright (C), 2015-2021, Envision
 * FileName: removeUserRoles
 * Author:  Dylan Yeo
 * Date:    18/03/22
 * Description: Assign a role to the user without logging in to Application Portal
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/user_and_ou/assign_user_roles.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def removeUserRoles(accessKey, secretKey, orgId, url):
    accessURL = url + "/app-portal-service/v2.2/role/removeRoles"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"organizationId": orgId,
            "userId": "u16473063753681521",
            "roleIds": ["ro16059397494401", "ro16113096236511727"]}
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
