"""
 * Copyright (C), 2015-2021, Envision
 * FileName: getSessionInformation
 * Author:  Dylan Yeo
 * Date:    25/03/22
 * Description: Get the login session information after logging in to EnOS
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/iam-api/en/2.3.0/get_session_information.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def getSessionInformation(accessKey, secretKey, url, sessoinId):
    accessURL = url + "/enos-iam-service/v2.0/session/info"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    header ={"Authorization": sessoinId}
    print(header)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, headers=header, method="POST")
    print(response)