"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getTokenInformation
 * Author:  Dylan Yeo
 * Date:    16/03/22
 * Description: Get information about the user who is currently logged-in through the access token.
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/authentication/get_token_information.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def getTokenInformation(accessKey, secretKey, url, accessToken):
    accessURL = url + "/app-portal-service/v2.2/session/info"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"Authorization": "Bearer " + accessToken}
    print(header)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, headers=header)
    print(response)

