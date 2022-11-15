"""
 * Copyright (C), 2015-2021, Envision
 * FileName: createAndJoinUser
 * Author:  Dylan Yeo
 * Date:    17/03/22
 * Description: Create a user and assign an OU to the user without logging in to Application Portal
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/app-portal-api/en/2.3.0/user_and_ou/create_and_join_user.html
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def createAndJoinUser(accessKey, secretKey, orgId, url):
    accessURL = url + "/app-portal-service/v2.2/user/createAndJoin"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"name": "songxibin2013",
            "domain": "iotsoft",
            "email": "songxibin2013@gmail.com",
            "organizationId": orgId,
            "locale": "zh_CN",
            "nickName": "songxibin2021"
            }
    print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)


