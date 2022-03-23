"""
 * Copyright (C), 2015-2021, Envision
 * FileName: refreshAccessToken
 * Author:  Dylan Yeo
 * Date:    16/03/22
 * Description: Request a new access token using the refresh token
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/authentication/refresh_access_token.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def refreshAccessToken(accessKey, secretKey, url, refreshToken):
    accessURL = url + "/app-portal-service/v2.2/token/refresh"
    params = {"refreshToken": refreshToken}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url)
    print(response)

    try:
        newAccessToken = response["data"]["accessToken"]
    except:
        newAccessToken = None
    return newAccessToken


