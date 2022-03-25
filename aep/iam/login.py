"""
 * Copyright (C), 2015-2021, Envision
 * FileName: login
 * Author:  Dylan Yeo
 * Date:    24/03/22
 * Description: Log in to EnOS
 * <author>          <time>          <version>          <desc>
 *
 * https://support.envisioniot.com/docs/iam-api/en/2.3.0/login
"""

import poseidon.poseidon
from requests.models import PreparedRequest

def login(accessKey, secretKey, url):
    accessURL = url + "/enos-iam-service/v2.0/login"
    params = {}
    req = PreparedRequest()
    req.prepare_url(accessURL, params)
    print(req.url)

    body = {"authType": 0,
            "principal": "dylan.yeo",
            "credentials": ""
            }
    # print(body)

    response = poseidon.poseidon.urlopen(accessKey, secretKey, req.url, body)
    print(response)

    try:
        sessionId = response["sessionId"]
    except:
        sessionId = None
    return sessionId
