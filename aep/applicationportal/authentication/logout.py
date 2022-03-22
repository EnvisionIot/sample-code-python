"""
 * Copyright (C), 2015-2021, Envision
 * FileName: logout
 * Author:  Dylan Yeo
 * Date:    16/03/22
 * Description: Log out of the account
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/authentication/logout.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def logout(accessKey, secretKey, url, accessToken):
    accessURL = url + "/app-portal-service/v2.0/logout"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header= {"Authorization": accessToken}

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, headers=header)
    print(response)
