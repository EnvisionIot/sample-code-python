"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getUserApplications
 * Author:  Dylan Yeo
 * Date:    21/03/22
 * Description: Get a list of applications that the current user has permission to access through the access token
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/application/get_user_apps.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest


def getUserApplications(accessKey, secretKey, url, accessToken):
    accessURL = url + "/app-portal-service/v2.2/user/app/list"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"Authorization": "Bearer " + accessToken}
    print(header)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, headers=header)
    print(response)
