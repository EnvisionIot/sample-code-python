"""
 * Copyright (C), 2015-2021, Envision
 * FileName: chooseOrganization
 * Author:  Dylan Yeo
 * Date:    16/03/22
 * Description: Select the organization that the user needs to use after login
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/user_and_ou/choose_organization
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def chooseOrganization(accessKey, secretKey, orgId, url, accessToken):
    accessURL = url + "/app-portal-service/v2.2/session/set"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    headers = {"Authorization": "Bearer " + accessToken}
    print(headers)

    body = {"orgId": orgId}
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body, headers=headers)
    print(response)

    try:
        refreshToken = response["data"]["refreshToken"]
    except:
        refreshToken = None
    return refreshToken


