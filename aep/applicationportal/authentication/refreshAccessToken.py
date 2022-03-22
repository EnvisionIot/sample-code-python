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

def refreshAccessToken(accessKey, secretKey, url):
    accessURL = url + "/app-portal-service/v2.0/login"
    params = {"refreshToken": ""}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body={"account": "songxibin2013",
          "password": "Password1"
          }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    try:
        accessToken = response["data"]["accessToken"]
    except:
        accessToken = None
    return accessToken

