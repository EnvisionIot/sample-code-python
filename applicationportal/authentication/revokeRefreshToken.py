"""
 * Copyright (C), 2015-2021, Envision
 * FileName: revokeRefreshToken
 * Author:  Dylan Yeo
 * Date:    16/03/22
 * Description: Revoke a user’s refresh token
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/authentication/revoke_refresh_token.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def revokeRefreshToken(accessKey, secretKey, url, accessToken, refreshToken):
    accessURL = url + "/app-portal-service/v2.2/refreshToken/revokeAll"
    params = {"refreshToken": refreshToken}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"Authorization": "Bearer " + accessToken,
              "Content-Type": "application/x-www-form-urlencoded"}
    print(header)

    body = {}
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body, headers=header, method='POST')
    print(response)


