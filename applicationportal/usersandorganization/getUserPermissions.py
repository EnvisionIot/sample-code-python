"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getUserPermissions
 * Author:  Dylan Yeo
 * Date:    18/03/22
 * Description: Get the permissions that are assigned to a user for the current application
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/user_and_ou/get_user_permissions.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def getUserPermissions(accessKey, secretKey, orgId, url):
    accessURL = url + "/app-portal-service/v2.2/user/permissions"
    params = {"orgId": orgId, "userId": "u16473063753681521", "locale": "en_US"}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)


