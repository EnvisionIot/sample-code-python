"""
 * Copyright (C), 2015-2021, Envision
 * FileName: removeUser
 * Author:  Dylan Yeo
 * Date:    18/03/22
 * Description: Remove a user from an OU without logging in to Application Portal. If the user only belongs to one OU, the user and the associated user data (including the username and the registered email address) will be permanently deleted
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/user_and_ou/remove_user.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def removeUser(accessKey, secretKey, orgId, url):
    accessURL = url + "/app-portal-service/v2.2/user/remove"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"organizationId": orgId,
            "userId": "u16475072968221401"}
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)
