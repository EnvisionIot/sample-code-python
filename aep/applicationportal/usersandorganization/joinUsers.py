"""
 * Copyright (C), 2015-2021, Envision
 * FileName: joinUsers
 * Author:  Dylan Yeo
 * Date:    17/03/22
 * Description: Assign users to an organization without logging in to Application Portal
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/user_and_ou/join_users.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def joinUsers(accessKey, secretKey, orgId, url):
    accessURL = url + "/app-portal-service/v2.2/user/users/join"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"organizationId": orgId,
            "userIds": ["u16473063753681521"]}
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


