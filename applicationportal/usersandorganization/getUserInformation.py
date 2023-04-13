"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getUserInformation
 * Author:  Dylan Yeo
 * Date:    17/03/22
 * Description: Get the information of the current user
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/user_and_ou/get_user_information.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def getUserInformation(accessKey, secretKey, url, accessToken):
    accessURL = url + "/app-portal-service/v2.2/user/info"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header = {"Authorization": "Bearer " + accessToken}
    print(header)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, headers=header)
    print(response)


