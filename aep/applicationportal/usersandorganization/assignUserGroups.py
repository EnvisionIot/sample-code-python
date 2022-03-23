"""
 * Copyright (C), 2015-2021, Envision
 * FileName: assignUserGroups
 * Author:  Dylan Yeo
 * Date:    18/03/22
 * Description: Assign a user group to the user without logging in to Application Portal
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/user_and_ou/assign_usergroups.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def assignUserGroups(accessKey, secretKey, orgId, url):
    accessURL = url + "/app-portal-service/v2.2/userGroup/appendUserGroups"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"organizationId": orgId,
            "userId": "u16473063753681521",
            "userGroupIds": ["ug16110406799521691", "ug16124463904521679"]}
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
